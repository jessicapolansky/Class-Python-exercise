#Exercise 1. Basics
class Person:
    def __init__(self, name, email, phone):
        self.friends = []
        self.name = name
        self.email = email
        self.phone = phone        
        self.friends = []
        self.count = 0
        self.ucount = 0
        self.greeted_by = []
    def __str__(self):
        return 'Person: {} {} {}'.format(self.name, self.email, self.phone)
#Add a friend method
    def add_friend(self, person):
        self.friends.append(person)
    def greet(self, other_person):
        print('Hello {}, I am {}!'.format(other_person.name, self.name))
        self.count += 1
#Bonus: Unique greeting
        if other_person not in self.greeted_by:
            self.ucount += 1            
            self.greeted_by.append(other_person)
#Add a method 2 or Exercise 2    
    def print_contact_info(self):
        print("{}'s email: {}, {}'s phone number: {}.".format(sonny.name, sonny.email, sonny.name, sonny.phone))
#Add a number of friends method
    def num_friends(self):
        return len(self.friends)
#Count number of greetings
    def greeting_count(self):
        return self.count
sonny = Person('Sonny', 'sonny@hotmail.com', '483-485-4948')
jordan = Person('Jordan', 'jordan@aol.com', '495-586-3456')
sonny.greet(jordan)
jordan.greet(sonny)
#Add the print_contact_info method
print("Sonny's contact info: Email = {} Phone= {}.".format(sonny.email, sonny.phone))
print("Jordan's contact info: Email = {} Phone= {}.".format(jordan.email, jordan.phone))
#Add the friends attribute
sonny.friends.append(jordan) 
jordan.friends.append(sonny)
len(jordan.friends)
#OR add_friend method
sonny.add_friend(jordan)

# #Exercise 2. Make your own class
# class Vehicle:
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#     def print_info(self):
#         print(self.make, self.model, self.year)
# #Add a method
# car = Vehicle('Toyota', 'Camry', 2005)
# print(car.year, car.make, car.model)