f=open("bank.txt","w")
list=["Kotak", "HDFC", "RBL", "SBI", "Bank of Baroda"]
i=0
while i<len(list):
    f.write(list[i])
    f.write("\n")
    i=i+1
f.close()