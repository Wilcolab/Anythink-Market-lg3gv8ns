# extract_names.sh
# grep -i "@amazon.com" ./Users\ list\ -\ MOCK_DATA.csv | cut -d ',' -f 2,3 > data.txt
# grep -i "@amazon.com" ./$1 | cut -d ',' -f 2,3 > $1.txt
# grep -i "@amazon.com" ./$1 | cut -d ',' -f 2,3 > output_names_$1.txt
grep -i "@amazon.com" ./$1 | cut -d ',' -f 2,3 > output_names.txt
