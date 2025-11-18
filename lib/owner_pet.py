class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all =[]
    def __init__(self,name,pet_type, owner=None):
        self.owner =owner
        self._pet_type =None
        self.name =name
        self.pet_type =pet_type
        

        # storing all instancess inside the all class atr
        Pet.all.append(self)
    @property
    def pet_type(self):
        return self._pet_type
    
    @pet_type.setter
    def pet_type(self, pet_type):
        if pet_type not in Pet.PET_TYPES:
            raise Exception("Sorry the pet_type is not in PET_TYPES")
        else:
            self._pet_type =pet_type
    

        
        

class Owner:
    def __init__(self,name): 
        self.name =name

    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]

    def get_sorted_pets(self):
        return sorted(self.pets(), key=lambda pet: pet.name)
            
    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception("pet must be an instance of Pet")
        pet.owner = self

