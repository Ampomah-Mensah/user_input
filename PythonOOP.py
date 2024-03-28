class Person:
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender
        
    def showName(self):
        # print('Persons Name:',self.name ', Your age:',self.age)
        print(f"Your name is {self.name}. You're {self.age} years old and a {self.gender}. ")

# for getting name of the user
naming = input('Enter your Name: ')
# for getting age of the user
your_Age = input('Enter your Age: ')
# for getting gender of the user
sex = input('Enter your Gender: ')

# object and instance of the class Person 
Details = Person(naming,your_Age,sex)  
Details.showName()     