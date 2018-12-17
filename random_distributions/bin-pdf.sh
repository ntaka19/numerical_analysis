awk 'BEGIN{i = 0}{
  bin = 0.5 #size of bin
  a[int($1/bin)*bin][count[int($1/bin)*bin]]=$2;
  count[int($1/bin)*bin]+=1;
  }
  END{
    for (level in a){
      for (i in a[level]){
	sum[level]+=a[level][i]
      }
    }
    for (level in a){
	print "level:",level,"avg:",sum[level]/length(a[level]);
      } #level, average within bin
  }' sampledata.dat | sort -k2g  
  
