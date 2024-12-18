# Define a class


class Pet:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def introduce(self):
        {print(f"Hello, my name is {self.name} and I am a {self.species}.")}


# Create an instance of the class
dog = Pet(name="Buddy", species="Dog")
cat = Pet("Whiskers", "Cat")

dog.name
dog.species
cat.name
cat.species

dog.introduce()
cat.introduce()
