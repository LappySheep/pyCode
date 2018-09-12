a,b="helloworld",0
exec("print(a[b]+a[b+1]);b+=1;"*(int(len(a))-1))
