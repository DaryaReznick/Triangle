"""
This is a program to calculate the area of a triangle.
"""

A = int(input())
B = int(input())
C = int(input())
if A == 0 or B == 0 or C == 0:
    print('Impossible: the side of triangle may not be equal to 0.')
elif A > B+C or B > A+C or C > A+B:
    print('Impossible: the side of the triangle is too long.')
else:
    P = float((A)+(B)+(C))/2
    D = float((P)*((P)-(A))*((P)-(B))*((P)-(C)))
    ITOG = float(D**(1/2.0))
    print(ITOG)
