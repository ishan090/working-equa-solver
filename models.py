# This file is a file that contains all the classes and models for the main.py file
# This file is very important so please dont delete it


# Imports
from string import ascii_letters as letters

# Authors: Snehashish Laskar and Ishan Kashyap
# Date: 1st August 2021
# Contact: organizationpythonprogramming.gmail.com

class Term:
    def __init__(self, term:str) -> None:
        # Raising error if term is empty
        assert term != "", "What is '' supposed to mean?"
        # Creating basic variables
        charge = ""
        lit_coef = ""
        num_coef = ""

        # iterating over each item in the term
        for item in term:
            # Checking of the item is a variable
            if item in letters:
                # and if yes, joining it to the lit_coef
                lit_coef += item
            # Checking if the item is a sign
            elif item == "+" or item == "-":
                # And if it is a sign then declaring it as the sign
                charge += item
            # Checking if the item is a numerical coefficient
            elif item in "1234567890.":
                # If yes then joining it to the num_coef variable3
                num_coef += item
        # If the numerical coefficient is nothing then declaring it as 1
        if num_coef == "":
            num_coef = 1.0
        # if there are even number of -, then the total charge is actually positive
        # as then the - signs cancel. Otherwise, it is truly negative.
        # Adding all the values to the class
        self.charge = "-" if charge.count("-") % 2 == 1 else "+"
        self.lit_coef = lit_coef
        self.num_coef = float(num_coef)
        self.term = self.charge+str(self.num_coef)+self.lit_coef

    # Functions to retun the stored Value
    def __str__(self) -> str:
        return self.term
    # returning charge
    def getCharge(self):
        return self.charge
    # returning the literal coefficient
    def getLitCoef(self):
        return self.lit_coef
    # returning the numerical coefficient
    def getNumCoef(self):
        return self.num_coef
    # returning the magnitude
    def getMagnitude(self):
        return str(self.num_coef)+self.lit_coef


class Expression:
    def __init__(self, terms:str) -> None:
        "assumes terms is a list of terms"
        terms_copy = [i for i in terms.split()]
        terms_with_charge = terms_copy[1:]
        # print(repr(terms_with_charge))
        # print(terms)
        paired = [terms_copy[0]]
        for i in range(int(len(terms_with_charge)/2)):
            paired.append("".join(terms_with_charge[i*2:i*2+2]))
        # print(paired)
        self.terms = [Term(i) for i in paired]
    def getTerms(self):
        return self.terms
    def __str__(self) -> str:
        result = ""
        first = True
        for i in self.terms:
            if first:
                result += i.getMagnitude()+" " if i.getCharge() == "+" else "-"+i.getMagnitude()+" "
                first = False
            else:
                result += i.getCharge()+" "+i.getMagnitude()+" "
        return result[:-1]


class Equation:
    def __init__(self, equa:str) -> None:
        """Assumes equa is a string"""
        equa_split = equa.partition("=")
        # equa_split = equa.split()
        # print(equa_split)
        LHS = " ".join(equa_split[:equa_split.index("=")])
        RHS = " ".join(equa_split[equa_split.index("=")+1:])
        expr1 = equa_split[0]
        expr2 = equa_split[2]
        # print(repr(expr1), repr(expr2))
        self.expr1 = Expression(LHS)
        self.expr2 = Expression(RHS)
        self.rhs = self.expr2
        self.lhs = self.expr1
    def getExpr1(self):
        return self.expr1
    def getExpr2(self):
        return self.expr2
    def __str__(self) -> str:
        return str(self.expr1) + " = " + str(self.expr2)