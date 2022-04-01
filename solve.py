# File that does the actual solving part of the program

from parse import Equation, Expression, Term


def sumTerm(t1, t2):
    if t1.getLitCoef() == t2.getLitCoef():
        return Term(str(t1.getNumCoef()+t2.getNumCoef())+t1.getLitCoef())
    raise ValueError("terms without common literal coefficients cannot be added")
def subTerm(t1, t2):
    if t1.getLitCoef() == t2.getLitCoef():
        return Term(str(t1.getNumCoef-t2.getNumCoef()))
    raise ValueError("terms without common literal coefficients cannot be subtracted")
def multiply(t1, t2):
    """can only multiply constants (to keep things simple)"""
    return t1.getNumCoef*t2.getNumCoef()
def divide(t1, t2):
    """can only divide constants (to keep things simple)"""
    return t1.getNumCoef()/t2.getNumCoef()

def addToSide(side, term):
    terms = side.getTerms()
    for i in range(len(terms)):
        if terms[i].getLitCoef() == term.getLitCoef():
            terms[i] = sumTerm(terms[i], term)
        break
    side.setTerms(terms)
    return side

def addToEqua(equa, term):
    expr1 = equa.getExpr1()
    expr2 = equa.getExpr2()
    expr1 = addToSide(expr1, term)
    expr2 = addToSide(expr2, term)
    equa.setExpr1(expr1)
    equa.setExpr2(expr2)
    return equa


def addLikeTerms(expr1):
    # litCoefs = []
    terms = expr1.getTerms()
    for i, t in enumerate(terms):
        while t.getLitCoef() in [i.getLitCoef() for i in terms[i+1:]]:
            for j in range(len(terms[i+1:])):
                if terms[i+1:][j].getLitCoef() == t.getLitCoef():
                    indx = j
            t = sumTerm(t, terms[indx+i+1])
            terms[i] = t
            del terms[indx+i+1]
    expr1.setTerms(terms)
    return expr1

# expr = Expression("3x + 5 + x - 5x + 8")
# print(addLikeTerms(expr))

def simplifySides(equa):
    equa.setExpr1(addLikeTerms(equa.getExpr1))
    equa.setExpr2(addLikeTerms(equa.getExpr2))
    return equa


def sendToSides(equa):
    expr1 = equa.getExpr1()
    expr2 = equa.getExpr2()
    for j in expr1.getTerms():
        if j.getLitCoef() == "":
            equa = addToEqua(equa, j.inverse())
            expr1, expr2 = equa.getExpr1(), equa.getExpr2()
    for k in expr2.getTerms():
        if k.getLitCoef() != "":
            equa = addToEqua(equa, k.inverse())
            expr1, expr2 = equa.getExpr1(), equa.getExpr2()
    return equa

eq = Equation("5x - 6 = 3x + 4")
print(sendToSides(eq))


def solve(equa):
    """
    Assumes equation is in one variable of order 1 (Linear Equation)
    example equation: 5x - 7 = 3
    """
    # Step 1: Adding the like terms on each side
    equa = simplifySides(equa)
    # Step 2: Taking contant terms and variable terms to opposite sides
    # This step doesn't work currently. A lto of debugging issues have arised,
    # which will take some time to solve
