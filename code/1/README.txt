example

>>> a,b=input(),0;exec("print(a[b]+a[b+1]);b+=1;"*(int(len(a))-1))
abcdef
ab
bc
cd
de
ef
