class Requirements:
	def __init__(self,cal,prot,carbs,fat,satfat,sugar,salt,fibre):
		self.cal = cal
		self.prot = prot
		self.carbs = carbs
		self.fat = fat
		self.satfat = satfat
		self.sugar = sugar
		self.salt = salt
		self.fibre = fibre
	
	def __init__(self,cal,prot,carbs,fat):
		self.cal = cal
		self.prot = prot
		self.carbs = carbs
		self.fat = fat
		self.satfat = None
		self.sugar = None
		self.salt = None
		self.fibre = None

	def __str__(self):
		output = "Requirements:\n"
		output += " Calories: " + str(self.cal) + "\n"
		output += " Protein: " + str(self.prot) + "\n"
		output += " Total Carbohydrates: " + str(self.carbs) + "\n"
		output += " Fat: " + str(self.fat) + "\n"
		output += " Saturated Fat: " + str(self.satfat) + "\n"
		output += " Sugar: " + str(self.sugar) + "\n"
		output += " Salt: " + str(self.salt) + "\n"
		output += " Fibre: " + str(self.salt) + "\n"
		return output

	def number_of_requirements(self):
		return 8
	    
	def to_array(self):
	    return [self.cal,self.prot,self.carbs,self.fat,self,self.satfat,self.sugar,self.salt,self.fibre]
	    
    
class NutrientRequirement:
    def __init__(self,val,restriction,error):
        self.val = val
        self.restriction = restriction
        self.error_margin = error

    def __str__(self):
        return "Value: " + str(self.val) + " Error Margin: " + str(self.error_margin) + "%"
        
class Ingredient:
	def __init__(self,name,cal,prot,carbs,fat,satfat,sugar,salt,fibre,restriction,quantity):
		self.name = name
		self.cal = cal
		self.prot = prot
		self.carbs = carbs
		self.fat = fat
		self.satfat = satfat
		self.sugar = sugar
		self.salt = salt
		self.fibre = fibre
		self.restriction = restriction
		self.quantity = quantity

        
def testClasses():
    calories = NutrientRequirement(2000,"=",5)
    protein = NutrientRequirement(100,"=",5)
    carb = NutrientRequirement(200,"=",5)
    fat = NutrientRequirement(50,"=",5)


    requirementsObject = Requirements(calories,protein,carb,fat)
    print requirementsObject

testClasses()
