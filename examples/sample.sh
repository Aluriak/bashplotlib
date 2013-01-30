#plotting coordinates
../bin/scatter.py -f ../data/texas.txt

#with x and y coords
../bin/scatter.py -x ../data/x_test.txt -y ../data/y_test.txt

#plotting a histogram
../bin/hist.py -f ../data/exp.txt

#with colors
../bin/hist.py -f ../data/exp.txt -c blue

#changing the shape of the point
../bin/hist.py -f ../data/exp.txt -p .

#using stdin
curl https://dl.dropbox.com/u/49171662/example.txt | ../bin/hist.py

#getting data from a webpage
curl http://www.baseball-reference.com/ \
| grep  -o -E "[$]([0-9]+)" | grep -o -E "[0-9]+" \
| ../bin/hist.py -b 20 -t "Baseball Payrolls" --height 20 --pch "*"


