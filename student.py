with open("student.txt","r") as file :
    a=file.readlines()
    for line in a:
        word=line.split()
        print(word)