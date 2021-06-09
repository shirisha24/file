b=open("chinni.txt","r")

print(b.readlines())


# another model
f=open("chinni.txt","r")
c=0
for i in (f):
    c=c+1
print("total lines",c)
f.close()