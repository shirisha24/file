t=open("doggy.txt","w")
list=["animals,birds"]
i=0
while i<len(list):
    t.write(list[i])
    i=i+1
t.close()
    