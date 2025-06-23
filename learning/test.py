#definition of classes to be used in OOP
class TV:
    def __init__(self,brand,model,year):
        self.brand = brand
        self.model = model
        self.year = year

    def quality(self):
        return "The quality TV in the market"
    
#object creation
tv1 = TV("Hisense" , "S500tx" , "2019")
tv2 = TV("Samsung" , "HD78349" , "2024")
tv3 = TV("LG", "TJGS89" , "2025")

#Accessing the contents of the object class can be done through the following command
print(f"This is a {tv1.brand} of model number {tv1.model} and was manufactured in the year {tv1.year} ")
print(f"This is a {tv2.brand} of model number {tv2.model} and was manufactured in the year {tv2.year} ")
print(f"This is a {tv3.brand} of model number {tv3.model} and was manufactured in the year {tv3.year} ")