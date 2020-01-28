"""
Exercise
Consider a quadratic function f(x; a, b, c) =  ax^2 + bx + c. Make a class Quadratic for representing f , where a, b, and c are data attributes, and the methods are :
__init__for storing the attributes a, b, and c
value for computing a value of f at a point x
table for writing out a table of x and f values for n x-values in the interval [L;R]
roots for computing the two roots
Also equip the ﬁle with a test function for verifying the implementation of valueand roots.
"""


class Quadratic(object):
    def __init__(self, a, b, c):
        self.a, self.b, self.c = a, b, c

    def value(self, x):
        return self.a*x**2 + self.b*x + self.c

    def table(self, L, R, n):
        xcolumn = []
        ycolumn = []
        table = []
        import numpy as np
        for x in np.linspace(L, R, n):
            xcolumn.append(x)
            y = self.value(x)
            ycolumn.append(y)
        for i, j in zip(xcolumn, ycolumn):
            table = [xcolumn, ycolumn]
        return table

    def roots(self):
        from math import sqrt
        roots = []
        x1 = ((-self.b + sqrt(self.b**2 - 4*self.a*self.c))/(2*self.a))
        x2 = ((-self.b - sqrt(self.b**2 - 4*self.a*self.c))/(2*self.a))
        roots.append(x1)
        roots.append(x2)
        return roots


def test_Quadratic_value():
    from numpy.random import randint
    a, b, c = 1, 1, -6
    x1 = randint(0, 10)
    x2 = randint(0, 10)
    x3 = randint(0, 10)
    expected = [
        a*x1**2+b*x1+c,
        a*x2**2+b*x2+c,
        a*x3**2+b*x3+c
    ]
    calculated = [
        Quadratic(a, b, c).value(x1),
        Quadratic(a, b, c).value(x2),
        Quadratic(a, b, c).value(x3)
    ]
    msg = "NOT WORKING"
    for i, j in zip(expected, calculated):
        success = i == j
        assert success, msg

test_Quadratic_value()

def test_Quadratic_roots():
    from math import sqrt
    a1, b1, c1 = 1, 1, -6
    a2, b2, c2 = 1, -1, -2
    expected = [
        [((-b1 + (sqrt(b1**2-4*a1*c1)))/(2*a1)),
        ((-b1 - (sqrt(b1**2-4*a1*c1)))/(2*a1))],
        [((-b2 + (sqrt(b2**2-4*a2*c2)))/(2*a2)),
        ((-b2 - (sqrt(b2**2-4*a2*c2)))/(2*a2))]
    ]
    calculated = [
        Quadratic(a1, b1, c1).roots(),
        Quadratic(a2, b2, c2).roots()
        ]
    msg = "NOT WORKING"
    for i, j in zip(expected, calculated):
        success = i == j
    assert success, msg
test_Quadratic_roots()

"""
kjøreeksempel

Process finished with exit code 0
"""