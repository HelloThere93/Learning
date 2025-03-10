studenttuple = ("John", "17", "LA, CA 1104TM", "+1031230217987") #Packing
'''
name, age, add, mn = studenttuple #unpacking
num = 0
print(name, age, add, mn)

Details = input("Enter details seperated by spaces: ").split()

studenttuplenew = tuple(Details)


print(studenttuplenew)
a = input("What Do you want to find: ")
for i in studenttuplenew:
    print(i)
    if i == a:
        print("found")
        break
'''
#print(studenttuplenew[3:5])

t1 = ("a", "b", "c","e","f","g")

print(t1[1:3])

print(t1[1:6:2])

print(t1[::2])