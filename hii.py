file = open("bucketlist.html","w")
file.write("1.Travel the world!\n")
file.write("2.Attend a concert!!\n")
file.write("3.Visit Disneyland!\n")
file.close()

n = int(input("How many characters to review?"))
file = open("bucketlist.txt","r")
print(file.read(n))
file.close()
print()

file = open("bucketlist.html","r")
lines = file.readlines()
file.close()
print("Total lines:",len(lines))
for i in range(len(lines)):
    print(i + 1,"->",lines[i].strip())
print()

word = input("Skip lines starting with: ")
file = open("bucketlist.html","r")
for line in file:
    if line.startswith(word):
        print("Skip -->",line.strip())
    else:
        print("Keep -->",line.strip())
file.close()
print()

file = open("bucketlist.html","r")
lines = file.readlines()
out = open("odd-lines.txt","w")
for i in range(0,len(lines), 2):
    out.write(lines[i])
out.close()
print("Odd lines saves to Odd-lines.txt")    
