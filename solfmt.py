import re
import os
import argparse
import difflib

version = "0.1.8"

class Transformer(object):
    def __init__(self, *arg):
        super(Transformer, self).__init__()
        self.arg = arg

    @classmethod
    def new(cls):
        return cls().inspect

    def inspect(self, line):
        raise NotImplementedError

    def explain(self, old, new):
        if old == new:
            return
        name = self.__class__.__name__
        print("{}:\n- {}\n+".format(name, old, new))


class AddCol(Transformer):

    def inspect(self, line):
        sline = line.strip(' \t')
        last_char = sline[-1] if sline else ''
        if '/' in sline:
            return line
        if not sline:
            return line
        good_ending = '}{;/'
        if last_char not in good_ending:
            line = line + ';'
        return line


class SpacesEqOp(Transformer):

    def inspect(self, line):
        line = re.sub(r'([^\s^\-^\+\=\>\!\<])=', r'\1 =', line)
        line = re.sub(r'=([^\s^\>\=])', r'= \1', line)
        return line


class SpacesCommaOp(Transformer):

    def inspect(self, line):
        line = re.sub(r',([^\s])', r', \1', line)
        line = re.sub(r'\s+\,', r',', line)
        line = re.sub(r'\s+\;', r';', line)
        return line


class SpacesSignsOp(Transformer):

    def inspect(self, line):
        line = re.sub(r'([^\s\+])\+', r'\1 +', line)
        line = re.sub(r'([^\s\-])\-', r'\1 -', line)
        line = re.sub(r'\+([^\s^\=\+])', r'+ \1', line)
        line = re.sub(r'\-([^\s^\=\-])', r'- \1', line)
        return line


class CurlyBrackets(Transformer):

    def inspect(self, line):
        line = re.sub(r'\s\)', r')', line)
        line = re.sub(r'\)([^\s^;^,])', r') \1', line)
        line = re.sub(r'\)\s*\;', r');', line)
        return line


class TabsIdent(Transformer):

    def inspect(self, line):
        return line.replace('\t', ' ' * 4)


class CommentsFmt(Transformer):

    def inspect(self, line):
        return re.sub(r'^\/\/([^\s])', r'// \1', line)


class Parentesis(Transformer):

    def inspect(self, line):
        line = re.sub(r'\n\s*{', ' {\n', line)
        line = re.sub(r'([^\s]){', r'\1 {', line)
        return line


def fix_parentesis(line):
    line = re.sub(r'\n\s*{', ' {\n', line)
    line = re.sub(r'([^\s]){', r'\1 {', line)
    return line


def fix_indent(lines):
    open_brackets = 0
    closed_brackets = 0
    indent = 0
    tranformed_lines = []
    for line in lines:
        line = line.strip(' \t')
        if not line:
            tranformed_lines.append('')
            continue
        if '}' in line and '{' not in line:
            indent -= 1
        line = '    ' * indent + line if indent else line
        tranformed_lines.append(line)
        open_brackets += 1 if '{' in line else 0
        closed_brackets += 1 if '}' in line else 0
        indent = open_brackets - closed_brackets
    return tranformed_lines


tranforms = [
    SpacesEqOp.new(),
    SpacesSignsOp.new(),
    SpacesCommaOp.new(),
    CommentsFmt.new(),
    TabsIdent.new(),
    CurlyBrackets.new(),
    AddCol.new()
]


def fmt(source):
    data = source.replace('\n\n\n', '\n\n')
    data = fix_parentesis(data)
    lines = data.split('\n')
    filtered = []
    for line in data.split('\n'):
        for t in tranforms:
            line = t(line)
        filtered.append(line)
    filtered = fix_indent(filtered)
    return '\n'.join(filtered)


def discover_sol_files(path):
    sols = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if not file.endswith(".sol"):
                continue
            sols.append('{}/{}'.format(root, file))
    return sols


class Fmt:
    def run(self, inplace, root, **opts):
        pathes = discover_sol_files(root)
        changed = [self._format_one(v, inplace) for v in pathes]

    def _format_one(self, source, inplace=False):
        with open(source, "r") as fp:
            data = fp.read()

        cleared_source = fmt(data)
        if cleared_source == data:
            return ''
        if not inplace:
            print(cleared_source)
        else:
            print(self._diff(data, cleared_source, source))
            with open(source, "w") as fp:
                fp.write(cleared_source)
        return source

    def _diff(self, before, after, source_name):
        return "\n".join(
            difflib.unified_diff(
                before.splitlines(),
                after.splitlines(),
                fromfile=source_name,
                tofile=source_name))

    run.__doc__ = """
    Solidity fmt

    Version {}
    """.format(version)


def entrypoint():
    parser = argparse.ArgumentParser(description='Solidity formatter.')
    parser.add_argument('root', help='Path')
    parser.add_argument(
        '-i',
        '--inplace',
        default=False,
        action="store_true",
        help='Write in place')
    args = parser.parse_args()
    Fmt().run(**vars(args))


if __name__ == "__main__":
    entrypoint()
