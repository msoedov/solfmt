### Solfmt

Solfmt is an autoformatting source code tool for solidity.


## Instalation

```shell
pip install solfmt --upgrade

pip install solfmt --user --upgrade
```

## Usage

```shell
solfmt . -i
```


## Notes

- It has a dead simple implementation based on reg exp rules.
- There is no solidity AST parsing involved for now.
- It only supports a minimalistic set of transformation
  - It fixes missing semicolum
  - Fixes mix tabs and spaces
  - Fixes trailing spaces after/before `,=(){}><`
  - Fixes indentation


 It still under heavy development and can break your code.
