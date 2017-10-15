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


--- Contract.sol

+++ Contract.sol

@@ -112,7 +112,7 @@

     }

     function TotalAmount() returns(uint) {
-        return Amount + Fee ;
+        return Amount + Fee;
     }

     function refund() private {
```


## Notes
- Feel free to fill a bug/issue.
- It has a dead simple implementation based on reg exp rules.
- There is no solidity AST parsing involved for now.
- It only supports a minimalistic set of transformation
  - It fixes missing semicolum
  - Fixes mix tabs and spaces
  - Fixes trailing spaces after/before `,=(){}><`
  - Fixes indentation


 It still under heavy development and can break your code.
