set -e

for f in contracts/*.sol; do
  python app.py $f >$f.new
  solcjs $f.new --bin
done
rm *.bin
