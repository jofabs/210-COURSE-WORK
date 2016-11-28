"""QUESTION 8
#Write a recursive function that removes all vocals from a given string s.
#Input:"beautiful" Output: "btfl"."""


print ("please enter a word for vowel revomal:" )#Print message giving instructions to the user
a = input() #variable storing user input 
def vowlElliminator(a):#Recursive function definition
    if not a: # empty string
        return a
    elif a[0] in "aeiou": #determining if user inputs vowels in lower case
        return vowlElliminator(a[1:])
    elif a[0] in "AEIOU": #determining if user inputs vowels in upper case
        return vowlElliminator(a[1:])
    return a[0] + vowlElliminator(a[1:])#original word with eliminated vowel return

print ("When the vowles are removed, your word is:", vowlElliminator(a), ".")#Prints, and calls
#the funtion,and presents it in a sentence nicely


"""PSEUDOCODE

#DEF VOWL-ELLIMINATOR(A):
#    if not A: 
#        return A
#    elif A[0] in "aeiou":
#        return VOWL-ELLIMINATOR(A[1:])
#    elif A[0] in "AEIOU": 
#        return VOWL-ELLIMINATOR(A[1:])
#    return A[0] + VOWL-ELLIMINATOR(A[1:])
"""
