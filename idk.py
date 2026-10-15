file = open("Movies.list.html", "w")
file.write("1.Laapata Ladies!\n")
file.write("2.Three Idiots\n")
file.write("3.Animal\n")
file.close()
print("Movie list saved to Movies.list.html!!")

file = open("Movies.list.html", "r")
content = file.read()
print("---My Movie List---\n")
print(content)
file.close()

# file = open("Bucket.list.txt", "r")
# lines = file.readlines()
# print(f"There are {len(lines)} items in your bucket list" )
# file.close()

# file = open("Bucket.list.txt", "a")
# file.write("4.Go on a trip with my best friends!!!\n")
# file.write("5.Learn a new skill!!\n")
# file.close()

# file = open("Bucket.list.txt","r")
# print("===Updated Bucket List===")
# print(file.read())
# file.close()

