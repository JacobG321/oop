from ninja_class import Ninja
from pet_class import Pet



Roger = Ninja("Roger", "NinjaMan", Pet("Rufus", "dog", "sit, speak, laydown", "bark, bark, bark"), "bacon", "puppy chow")
# Rufus = Pet("Rufus", "dog", "sit, speak, laydown", "bark, bark, bark")

# print(Roger.pet.name)
# Rufus.sleep()

Roger.feed().bathe().walk()