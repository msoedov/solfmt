### Solfmt

Solfmt is an autoformatting source code tool for solidity.


## Instalation

```shell
pip install solfmt --upgrade

pip install solfmt --user --upgrade
```

## Usage

```shell
solfmt contract.sol -i
```


## Notes

- It has a dead simple implementation based on regexp rules.
- There is no solidity AST parsing involved for now.
- It only supports a minimalistic set of tranformation
  - It fixes missing semicolumn
  - Fixes mix tabs and spaces
  - Fixes trailing spaces after/before `,=(){}><`
  - Fixes indentation
