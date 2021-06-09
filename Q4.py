f=open("Q4.txt","r")
sum=f.readlines()
for a in sum:
    if "delhi" in a:
        b=open("delhi.txt","a")
        b.write(a)
        print(b)
    elif "shimla" in a:
        c=open("shimla.txt","a")
        c.write(a)
        print(c)
    else:
        pass
f.close()


