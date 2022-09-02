dog = []
dog = {'name':"tommy", 'color':"white", 'breed':"bulldog", 'legs':"short", 'age':"2"}
student={'first_name':"Sindhu", 'last_name':"Rajanala", 'gender':"Female", 'age':"22", 'marital status':"single" ,
'skills':['java','python','perl','shell'], 'country':"USA", 'city':"Overland park"}
print("lenght of the student dictonary")
print(len(student))
print("skills known:")
print((student['skills']))
b=(student['skills'])
for i in b :
 print(i + " datatype is "+str(type(i)))
 print("skilled updated:")
student["skills"] = ['c','java','python','perl','shell','c++']
print(student)
print(student.keys())
print(list(student.values()))