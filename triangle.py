import math

def detect_triangle(a, b, c):
    e=10**-10
    if (a<0 or b<0 or c<0
        or a>2**32-1 or b>2**32-1 or c>2**32-1 
        or type(a) not in [float, long, int]
        or type(b) not in [float, long, int]
        or type(c) not in [float, long, int]):
        return 'data not valid.'
    elif (a+b<c) or (a+c<b) or (b+c<a):
        return 'not triangle.'
    else:
        if a == b == c :
            return 'equilateral triangle.'
        elif (b==c and math.fabs(a*a - b*b - c*c) < e) or (a==c and math.fabs(b*b - c*c - a*a )< e) or (a==b and math.fabs(c*c - a*a - b*b )< e):
            return 'isoceles square triangle.'
        elif (a==b) or (b==c) or (c==a) :
            return 'isoceles triangle.'
        elif a*a==b*b+c*c or b*b==a*a+c*c or c*c==a*a+b*b :
            return 'square triangle.'
        else:
            return 'scalene triangle.'

            