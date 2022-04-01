# This file focuses on how to parse and store the input equation

from string import ascii_letters as letters


class Term:
    def __init__(self, term:str) -> None:
        assert term != "", "What is '' supposed to mean?"
        """
        The Parsing Algorithm:
        1. Loop through each element of the term
        2. Add it to its respective group
          * sign
          * numerical coefficient
          * literal coefficient
        3. Store each variable as an attribute of the class instance
        """
        charge = ""
        lit_coef = ""
        num_coef = ""
        for i in term:
            if i in letters:
                lit_coef += i
            elif i == "+" or i == "-":
                charge += i
            elif i in "1234567890.":
                num_coef += i
        if num_coef == "":
            num_coef = "1"
        # if there are even number of -, then the total charge is actually positive
        # as then the - signs cancel. Otherwise, it is truly negative.
        self.charge = "-" if charge.count("-") % 2 == 1 else "+"
        self.lit_coef = lit_coef
        self.num_coef = float(self.charge+num_coef)
        self.term = str(self.num_coef)+self.lit_coef
    def __str__(self) -> str:
        return self.term
    def getCharge(self):
        return self.charge
    def getLitCoef(self):
        return self.lit_coef
    def getNumCoef(self):
        return self.num_coef
    def getMagnitude(self):
        return str(self.num_coef)+self.lit_coef
    def add(self, term):
        if term.getLitCoef() == self.getLitCoef():
            pass
    def inverse(self):
        return Term(str(-self.getNumCoef())+self.getLitCoef())



class Expression:
    def __init__(self, terms:str) -> None:
        """assumes terms is a str of terms"""
        terms_copy = [i for i in terms.split()]
        # get everything which has a sign in front
        terms_with_charge = terms_copy[1:]
        # print(repr(terms_with_charge))
        # print(terms)
        # pair the signs with the terms
        paired = [terms_copy[0]]
        for i in range(int(len(terms_with_charge)/2)):
            paired.append("".join(terms_with_charge[i*2:i*2+2]))
        # print(paired)
        # finally, make each term an instance of the Term class
        self.terms = [Term(i) for i in paired]
    def getTerms(self):
        return self.terms
    def setTerms(self, terms):
        self.terms = terms
    def __str__(self) -> str:
        result = ""
        first = True
        for i in self.terms:
            # if this is the first term, make the sign of the term close to it.
            if first:
                result += i.getMagnitude() #+" " if i.getCharge() == "+" else "-"+i.getMagnitude()+" "
                first = False
            # otherwise make the sign an operator instead
            else:
                result += i.getCharge()+" "+i.getMagnitude()+" "
        # finally, return the str but remove the trailing " " (space)
        return result[:-1]


class Equation:
    def __init__(self, equa:str) -> None:
        """Assumes equa is a string"""
        equa_split = equa.partition("=")
        # equa_split = equa.split()
        # print(equa_split)
        # expr1 = " ".join(equa_split[:equa_split.index("=")])
        # expr2 = " ".join(equa_split[equa_split.index("=")+1:])
        expr1 = equa_split[0]
        expr2 = equa_split[2]
        # print(repr(expr1), repr(expr2))
        self.expr1 = Expression(expr1)
        self.expr2 = Expression(expr2)
    def getExpr1(self):
        return self.expr1
    def getExpr2(self):
        return self.expr2
    def setExpr1(self, expr1):
        self.expr1 = expr1
    def setExpr2(self, expr2):
        self.expr2 = expr2
    def __str__(self) -> str:
        return str(self.expr1) + " = " + str(self.expr2)


# eq1 = Equation("5x - 6c + 8 = -r + 3e")
# t = Term("5g")
# print(t.inverse())
