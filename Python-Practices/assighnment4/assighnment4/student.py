from introduce import person

class Student(person):
    
    def __init__(self,name="mohsen",age=25,birth_country="iran",university_name="university         of bolzano",graduation_year="2023"):
        super().__init__(name,age,birth_country)
        self.university_name=university_name
        self.graduation_year=graduation_year
person1 = person()
print(person1.introduce)        