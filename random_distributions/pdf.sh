#!/bin/bash

#uniqは基本的にしなくてもいいが、多少は計算を減らせる
#$2は基本的に1。つまり範囲に含まれる個数のことを言っている
#data は確率分布に従う数値

data=$1

sort -n $1.dat| 
uniq -c | 
awk '{print $2,$1}' | 
awk 'BEGIN{
  i = -10
  n = 0
}{
  if($1<i){
    n=n+$2
  }
  else{
    print i-0.05,n
    i=i+0.1
    n=$2 
  }
}END{print i-0.05,n}' > $data\_pdf.dat

#n=$2 passes the next row which is 1. 
#pretty much corresponds with initialization


gnuplot<<EOF
set terminal png 
set output "$data\_pdf.png"
p "$data\_pdf.dat" u 1:2 w boxes
set output
EOF
