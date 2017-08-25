#!/bin/sh

python HISTORY_splice.py HISTORY_PIMD.01
./append-msite.pl 288 > msite_288.dat
for i in {1..20}; do
  python HISTORYtoCONFIG.py history.$i
  cat config.$i msite_288.dat > CONFIG.$i
done
