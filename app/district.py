#read file from hello.txt
file1 = open("hello.txt", "r").read()
# save each line in a list
lines = file1.split()
list1 = []
# print(lines)
for i in range(len(lines)):
    #index posion of i
    if i % 2 == 0:
        # print(lines[i])
        list1.append(lines[i])
    
print(len(lines))
        
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def __str__(self):
#         return f'{self.name} is {self.age} years old'
    

# saurab = Person('Saurab', 25)
# print(saurab)