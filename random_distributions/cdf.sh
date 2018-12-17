#!/bin/bash
data=$1
sum=`awk 'BEGIN{sum=0}{sum+=$1}END{print sum}' $1.dat`
sort -k1gr $1.dat > $1.dat
awk '{print $1,NR/'${sum}'}' $1.dat > $1\_cdf.dat

