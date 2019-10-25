class Dog:

    # CLASS OBJECT Attribute - these apply to all instances of the class.
    family = "mammal"

    def __init__(self, breed, name):
        self.breed = breed
        self.name = name


my_dog = Dog("Huskie", "fred")
her_dog = Dog("Lab", "Labby")
print(my_dog.name)
print(her_dog.family)
