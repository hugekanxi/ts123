#-*- coding: UTF-8 -*-
class Student(object):
    def __init__(self,name,score):
        self.name=name
        self.score=score
    def get_grade(self):
        if self.score>=90:
            return 'A'
        elif self.score>=60:
            return 'B'
        else:
            return 'C'

bart1=Student('chenhu',90)
bart2=Student('J' ,60)
bart3=Student('C',59)

print bart1.score
print bart1.get_grade()
bart1.name