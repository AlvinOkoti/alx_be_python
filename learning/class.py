class student:
    def __init__(self,name,age,stage):
        self.name = name
        self.age = age
        self.stage = stage

    def learner(self):
        return "This is a learner in our class and has the best of grades"
    
#defining an object
sdt1 = student("Alex" , "12" , "Grade 2")
sdt2 = student("James" , "12" , "Grade 2")
sdt3 = student("Sasha" , "9" , "Grade 1")

#print out of the same output expected
print(f"Our first student is {sdt1.name} , in {sdt1.stage} and is {sdt1.age} years old")
print(f"Our second student is {sdt2.name} , in {sdt2.stage} and is {sdt2.age} years old")
print(f"Our first student is {sdt3.name} , in {sdt3.stage} and is {sdt3.age} years old")