import math

def findAreaAndCircumference(r):
    pi_value = math.pi 
    c = 2*pi_value*r
    a=pi_value*(r**2)

    return print(f"Area of the circle:{a}", f"Circumfrence of the circle is:{c}")



findAreaAndCircumference(16)