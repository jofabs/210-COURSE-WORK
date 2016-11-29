"""Question 3
Write the pseudocode for a function which returns the highest perfect square
which is less or equal to its parameter (a positive integer).
Implement this in a programming language of your choice."""

import math

"""Using math
#square root of the number and round it to the largest integer
#value less than or equal to x: math.floor(x)"""

paraNO = input("Give parametre: ")
def perfectsquare(paraNO):
    #Code below returns the floor of paraNO, largest integer < or = to paraNO
    # and returns square root of parametre
    paraN1 = math.floor(math.sqrt(int(paraNO)))
    squarPARA = paraN1 * paraN1
    print (squarPARA)

perfectsquare(paraNO)


"""
PSEUDOCODE

COLLECT USER INPUT ELEMENT AS paraNO

PERFECTSQUARE(paraNO)
    paraN1 ROUNDING DOWN THE SQUARE OF paraNO
    squarPARA MULTIPLIPLY paraN1 BY ITSELF
    PRINT squarPARA

CALL PERFECTSQUARE(paraNO)
"""

#""" Fuction which returns true if the parametre is a perfect square"""
#n = int(input("Give parametre: "))
#def perfectsquare(n):
#    print (n % n**0.5 == 0)

#perfectsquare(n)
