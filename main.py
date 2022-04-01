# This is the main file of this project
# You should not use delete this!

# Imports

# Authors: Snehashish Laskar and Ishan Kashyap
# Date: 1st August 2021
# Contact: organizationpythonprogramming.gmail.com

from models import *


myEqua = Equation("9x - 8y  =90")

for i in myEqua.rhs.terms:
	print(i.term)


# Algorithm to shift an element from LHS to RHS

# def Move_term(term:str) -> None :

