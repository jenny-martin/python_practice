# exercise-04 What kind of Triangle?

# Write the code that:
# 1. Prompts the user to enter the three lengths of a triangle (one at a time):
#      Enter the lengths of three side of a triangle:
#      a: 
#      b:
#      c:
# 2. Write the code that determines if the triangle is:
#      equalateral - all three sides are equal in length
#      scalene - all three sides are unequal in length
#      isosceles - two sides are the same length
# 3. Print a message such as:
#      - A triangle with sides of <a>, <b> & <c> is a <type of triangle> triangle


l_triA = int(input('Please enter the length of a side of a triangle, one at a time. First side: '))
l_triB = int(input('Second side: '))
l_triC = int(input('Third side: '))
if l_triA == l_triB and l_triB == l_triC:
    print(f'A triangle with sides of the same length like {l_triA}, {l_triB}, and {l_triC} is an equilateral triangle')
elif l_triA != l_triB and l_triA != l_triC and l_triB == l_triC:
    print(f'A triangle with 2 sides of the 3 that are the same like {l_triA}, {l_triB}, and {l_triC} is scalene triangle')
else: print(f'A triangle with no sides that are equal like {l_triA}, {l_triB}, and {l_triC} is an isosceles triangle')