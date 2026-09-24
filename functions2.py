fruits = ["Mango","Guava","Grapes","Strawberry","Apple"]
print("Fruit List:",fruits)
print("Total Number Of Fruits:",len(fruits))
print("First fruit:",fruits[0])
print("Last fruit:",fruits[-1])
print("First Four Fruits:",fruits[:4])

fruits.append("Banana")
print("\nAfter adding Banana:",fruits)
fruits.remove("Mango")
print("After Removing Mango:",fruits)
fruits.sort()
print("Sorted Alphabetically:",fruits)
fruits.reverse()
print("Reversed:",fruits)

me = {"name" : "Watermelon","colour" : "Red", "Size" : "Big"}
print("\nTeacher profile:", me)

print("Colour:", me["colour"])
print("Size:",me.get("Size"))
me["Size"] = 5
me["E-mail"] = "me@gmail"
me.pop("Size")
print("Updated:",me)

roll_numbers = [1,2,3,4,5]
names = ["Sam","Cam","Tam","Pam","Jam"]
student_directory = dict(zip(roll_numbers,names))
print("\nStudent Directory:", student_directory)
print("Student At Roll Number 5:",student_directory[5])