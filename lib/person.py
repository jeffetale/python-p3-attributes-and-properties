#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    def __init__(self, name='Guido', job='Sales'):
        self.name = name
        self.job = job

    def get_name(self):
        print("Getting name")
        if hasattr(self, '_name'):
            return self._name.title()
        else:
            return None
    
    def set_name(self, name):
        if isinstance(name, str) and 1 <= len(name) <= 25:
            print(f"Setting name to {name}")
            self._name = name
        else:
            print("Name must be string between 1 and 25 characters.")
    
    name = property(get_name, set_name)

    @property
    def job(self):
        print("Getting job")
        return self._job
    
    @job.setter
    def job(self, job):
        if isinstance(job, str) and job in APPROVED_JOBS:
            self._job = job
        else:
            print("Job must be in list of approved jobs.")





guido = Person("guido halland")
print(guido.name)

guido.job = "Sales"
print(guido.job)



'''
class Human:
    species = "Homo sapiens"
    def __init__(self, name):
        self.name = name
        self._age = 0
    
    def get_age(self):
        print("Retrieving age")
        return self._age
    
    def set_age(self, age):
        if (type(age) in (int, float)) and (0 <= age <= 120):
            print(f"Setting age to {age}")
            self._age = age
        else:
            print("Age must be a number between 0 and 120")

    age = property(get_age, set_age)


guido = Human("Guido")
#print(guido.species)
#print(guido)
print(guido.age)

guido.age = False
guido.age = 56
print(guido.age)
guido.age

guido.species = "Python programmer"
guido.name = "Guido van Rossum"

#print(guido.species)
#print(guido.name)

#guido.nationality= "Dutch"
#print(guido.nationality)

my_attr = "is_a_friend"
#print(getattr(guido, my_attr, False))

setattr(guido, my_attr, True)
#print(getattr(guido, my_attr, False))
'''