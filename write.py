g=open("colours.txt","w")
list=["black,green,white,yellow,blue"]
i=0
while i<len(list):
    g.write(list[i])
    i=i+1
g.close()
