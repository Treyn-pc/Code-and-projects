"""
Exercise:
The equation u' = -au is a relevant model for radioactive decay, where u(t) is the fraction of particles that remains in the radioactive substance at time t. The parameter a is the inverse of the so-called mean lifetime of the substance. The initial condition is u(0)= 1.
a) Introduce a class Decay to hold information about the physical problem: the parameter a and a __call__method for computing the right-hand side -au of the ODE.
b) Initialize an instance of class Decay with a = ln(2)/5600 1/y. The unit 1/y means one divided by year, so time is here measured in years, and the particular value of a corresponds to the Carbon-14radioactive isotope whose decay is used extensively in dating organic material that is tens of thousands of years old.
c) Solve u' = -au with a timestep of 500y, and simulate the radioactive decay for T = 20 000 y. Plot the solution. Write out the ﬁnal u(T) value and compare it with the exact value e^(-aT).
"""

from numpy import *
from matplotlib.pyplot import *

class Decay(object):
    def __init__(self, a):
        self.a = a

    def __call__(self, u, t):
        a = self.a
        return -a*u

class ODESolver(object):
    def __init__(self, f):
        self.f = lambda u, t: array(f(u, t), float)

    def initial_condition(self, u0):
        u0 = float(u0)
        self.u0 = u0

    def solve(self, time_points, terminate = None):
        if terminate is None:
            terminate = lambda u, t, step_no : False

        self.t = asarray(time_points)
        n = self.t.size
        self.u = zeros(n)
        self.u[0] = self.u0

        for k in range(n-1):
            self.k = k
            self.u[k+1] = self.advance()
            if terminate(self.u, self.t, self.k+1):
                break

        return self.t[:k+2], self.u[:k+2]



class RungeKutta4(ODESolver):
    def advance(self):
        u, f, k, t = self.u, self.f, self.k, self.t
        dt = t[k+1] - t[k]
        dt2 = dt/2.0
        K1 = dt*f(u[k], t[k])
        K2 = dt*f(u[k] + 0.5*K1, t[k]+dt2)
        K3 = dt*f(u[k] + 0.5*K2, t[k]+dt2)
        K4 = dt*f(u[k]+K3, t[k]+dt)
        u_new = u[k] + (1/6.0)*(K1 + 2*K2 + 2*K3 + K4)
        return u_new


def f(x):
    return exp((-log(2)/5600)*x)

t_points = linspace(0, 20000, 500)
y = Decay(a=log(2)/5600)

solver = RungeKutta4(y)
solver.initial_condition(1)
t, u = solver.solve(t_points)
print(f"the final value of u(t = 20 000 years) is {u[-1]} so around {round(100*u[-1])} percent \n"
      f"remaining radioactive carbon")
plot(t, u)
plot(t_points, f(t_points))
legend(["numerical approximation with RungeKutta4", "exact solution"])
savefig("radioactive_decay.png")
show()

"""
kjøreeksempel

the final value of u(t = 20 000 years) is 0.0841187620405777 so around 8.0 percent 
remaining radioactive carbon

Process finished with exit code 0
"""