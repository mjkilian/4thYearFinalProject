#Module containing representations of key components in meal generation


"""Holds a users nutritional requirements for a meal/day."""
from Website.meals import UnitConversions


class Requirements(object):
    def __init__(self):
       """Base constructor. Initialise an empty requirements map"""
       self.requirements = {}

    def add(self,name,nutrient_requirement):
        """Add a NutrientRequirement to the requirements set
           Returns True if requirement is addedd successfully
           False if parameter not of type NutrientRequirement
        """
        if isinstance(nutrient_requirement,NutrientRequirement):
            self.requirements[name.lower()] = nutrient_requirement
            return True
        return False

    def get_requirement(self,nutrient_name):
        """looks in the set of requirements for a requirement on the named nutrient
           returns the requirement if it exists, returns None otherwise.
        """
        return self.requirements.get(nutrient_name.lower())

    def __str__(self):
        output = ""
        for requirement in self.requirements.items():
            output += str(requirement[0]) + ": " +  str(requirement[1]) + "\n"
        return output

    def number_of_requirements(self):
        return len(self.requirements)

    def to_array(self):
        return self.requirements.values()

    def items(self):
        return self.requirements.items()
    
    def nutrients(self):
        return self.requirements.keys()


"""Holds the requirements for a specific nutrient as a required value"""
class NutrientRequirement(object):
    def __init__(self,val):
        self.val = val

    def __str__(self):
        return str(" Value: " + str(self.val))

"""Holds a definite requirement. That is a requirement where we wish to acheive a specific value or be within an acceptable range of values"""
class DefiniteNutrientRequirement(NutrientRequirement):
    def __init__(self,val,error):
        super(DefiniteNutrientRequirement,self).__init__(val)
        self.error_margin = error

    def __str__(self):
        output = super(DefiniteNutrientRequirement,self).__str__()
        return output + " Error: " + str(self.error_margin)

"""Holds a restricted requirement. That is a requirement which is specified only in terms of having at least or at most a certain value"""
class RestrictedNutrientRequirement(NutrientRequirement):
    def __init__(self,threshold,restriction):
        super(RestrictedNutrientRequirement,self).__init__(threshold)
        self.restriction = restriction

    def threshold(self):
        return self.val

    def __str__(self):
        return "Restriction: " + str(self.restriction) + " " + str(self.val)

"""Class for an ingredient and its nutritional content.
"""

class Ingredient(object):
    def __init__(self,name,nutrient_values,quantity,unit,fixed):
        self.name = name.lower()
        self.nutrient_values = nutrient_values
        self.quantity = quantity
        self.unit = unit
        self.fixed = fixed
        if not fixed: #if the ingredient is not fixed, we can convert its values to grams
           if unit.lower() == "oz":
               q = quantity * UnitConversions.OZ_TO_G
               for key in nutrient_values:
                    nutrient_values[key] = float(nutrient_values[key]) / q
           elif unit.lower() == "g":
               for key in nutrient_values:
                    nutrient_values[key] = float(nutrient_values[key]) / quantity

    
    def get_val(self,nutrient_name):
        return self.nutrient_values.get(nutrient_name,0) #default to 0 if no entry for nutrient

    def __str__(self):
        output = ""
        output += (self.name + ":\n")
        output += str(self.nutrient_values) + "\n"
        output += ("Amount: " + str(self.quantity) + " " + str(self.unit)) + "\n"
        return output

"""A restricted ingredient is one where we wish to limit the amount so we use no more than or at least a certain quantity"""
class RestrictedIngredient(Ingredient):
    def __init__(self,name,nutrient_values,quantity,unit,fixed,restriction,threshold):
        super(RestrictedIngredient,self).__init__(name,nutrient_values,quantity,unit,fixed)
        self.restriction = restriction
        self.threshold = threshold

    def __str__(self):
       output = super(RestrictedIngredient,self).__str__()
       return output + str("Restriction: " + str(self.restriction) + " " + str(self.threshold))

class Quantity(object):
    def __init__(self,name,quantity,unit):
        self.name = name.lower()
        self.quantity = quantity
        self.unit = unit


def testClasses():
    calories = DefiniteNutrientRequirement(2000,5)
    protein = DefiniteNutrientRequirement(100,5)
    carb = DefiniteNutrientRequirement(200,5)
    fat = DefiniteNutrientRequirement(50,5)
    requirementsObject = Requirements()
    requirementsObject.add("calories",calories)
    print requirementsObject

#testClasses()
