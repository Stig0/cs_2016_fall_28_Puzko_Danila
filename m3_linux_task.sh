wget 2700chess.com
cat index.html | grep -o 'players/[a-z\+\-]\+">[A-Z][a-z]\+' > rating.txt
sed -e 's/players[/][a-z\+\-]\+">//g' rating.txt > rating1.txt
cat -n rating1.txt; rm index.html
