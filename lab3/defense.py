"""
student
name and grade
щценка из 100 баллов
4 студента
вывести у кого больше 70++
"""
class Student:
    def __init__(self, stud, grade):
        self.stud = stud
        self.grade = grade
      
    def goodStud(self):
        if self.grade >= 70:
            return True

listik = []
for x in range(4):
    name = input("What is your name? :")
    grade = int(input("What grade do you have? :"))
    stud1 = Student(name, grade)
    if stud1.goodStud() == True:
        listik.append(name)
        
print(listik)