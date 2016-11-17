wget 2700chess.com
cat index.html | grep -o 'players/[a-z\+\-]\+">[A-Z][a-z]\+' > rating.txt
sed -e 's/players[/][a-z\+\-]\+">//g' rating > rating1
cat -n rating1; rm index.html
