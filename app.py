import re
import fire

version = "0.0.1"

def add_separator(line):
    last_char = line[-1] if line else ''
    sline = line.strip(' \t')
    if last_char != '}' and last_char != '{' and last_char != ';' and sline and line[0] != '/':
        line = line + ';'
    return line


def blank_spaces_eq(line):
    line = re.sub(r'([^\s^\-^\+\=\>])=', r'\1 =', line)
    line = re.sub(r'=([^\s^\>\=])', r'= \1', line)
    return line


def blank_spaces_coma(line):
    line = re.sub(r',([^\s])', r', \1', line)
    line = re.sub(r'\s+\,', r',', line)
    return line


def clear_brackets(line):
    line = re.sub(r'\s\)', r')', line)
    line = re.sub(r'\)([^\s^;^,])', r') \1', line)
    line = re.sub(r'\)\s*\;', r');', line)
    return line


def blank_spaces_plus(line):
    line = re.sub(r'([^\s])\+', r'\1 +', line)
    line = re.sub(r'([^\s])\-', r'\1 -', line)
    line = re.sub(r'\+([^\s^\=])', r'+ \1', line)
    line = re.sub(r'\-([^\s^\=])', r'- \1', line)
    return line


def tabs_to_spaces(line):
    return line.replace('\t', ' ' * 4)


def fix_parentesis(line):
    return re.sub(r'\n\s*{', ' {\n', line)


def clear_comment(line):
    return re.sub(r'^\/\/([^\s])', r'// \1', line)


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
    blank_spaces_eq,
    blank_spaces_plus,
    blank_spaces_coma,
    clear_comment,
    tabs_to_spaces,
    clear_brackets,
    add_separator,
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



class Fmt:

    def run(self, source, i=''):
        with open(source, "r") as fp:
            data = fp.read()

        cleared_source = fmt(data)
        if not i:
            print(cleared_source)
        else:
            with open(source, "w") as fp:
                fp.write(cleared_source)

    run.__doc__ = """
    Solidity fmt

    Version {}
    """.format(version)


def entrypoint():
    fire.Fire(Fmt().run)


if __name__ == "__main__":
    entrypoint()
