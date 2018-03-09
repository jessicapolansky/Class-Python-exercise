#Exercise 1. Hello
def greeting(name):
    print("Hello {}".format(name))
if __name__ == "__main__":
    greeting(input("Give a name? "))

#Exercise 2. y = x + 1
import matplotlib
matplotlib.use("Agg")

from matplotlib import pyplot
import matplotlib.pyplot as plot

def f2(x):
    return x + 1

    
xs = list(range(-3, 3))
ys = []
for x in xs:
    ys.append(f2(x))

plot.plot(xs, ys)
pyplot.savefig('plotEx2.png')
pyplot.close()

#Exercise 3. Square of x
import matplotlib
matplotlib.use("Agg")

from matplotlib import pyplot
import matplotlib.pyplot as plot

def f3(x):
    return x * x
    
xs = list(range(-100, 100))
ys = []
for x in xs:
    ys.append(f3(x))

plot.plot(xs, ys)
pyplot.savefig('plotEx3.png')
pyplot.close()

#Exercise 4. Odd or Even
import matplotlib
matplotlib.use("Agg")

from matplotlib import pyplot
import matplotlib.pyplot as plot

def f4(x):
    if (x % 2) == 0:
        return -1
    else:
        return 1
    
xs = list(range(-5, 6))
ys = []
for x in xs:
    ys.append(f4(x))

plot.bar(xs, ys)
pyplot.savefig('plotEx4.png')
pyplot.close() 

#Exercise 5. Sine
import matplotlib
matplotlib.use("Agg")

from matplotlib import pyplot
import matplotlib.pyplot as plot
from math import sin

def f5(x):
    return sin(x)
    
xs = list(range(-5, 6))
ys = []
for x in xs:
    ys.append(f5(x))

plot.plot(xs, ys)
pyplot.savefig('plotEx5.png')
pyplot.close() 

#Exercise 6. Sine 2
from numpy import arange
import matplotlib
matplotlib.use("Agg")

from matplotlib import pyplot
import matplotlib.pyplot as plot
from math import sin

def f6(x):
    return sin(x)
    
xs = list(arange(-5, 6, 0.1))
ys = []
for x in xs:
    ys.append(f6(x))

plot.plot(xs, ys)
pyplot.savefig('plotEx6.png')
pyplot.close() 

#Exercise 7. Degree Conversion
import matplotlib
matplotlib.use("Agg")

from matplotlib import pyplot
import matplotlib.pyplot as plot

def f7(x):
    return ((x * (9 / 5)) - 32)

    
xs = list(range(-40, 200))
ys = []
for x in xs:
    ys.append(f7(x))

plot.plot(xs, ys)
plot.grid(True)
pyplot.savefig('plotEx7.png')
pyplot.close()

#Exercise 8. Play again?
def game8():
    x = input("Do you want to play again? (Y or N) ").upper
    if x == "Y":
        return True
    else:
        return False
game8()

#Exercise 9. Play again? Again
def game9():
    while True:
        y = input("Do you want to play again? (Y or N) ")
        if y not in ('Y', 'N'):
            print("Invalid input, please try again.")
        elif y == "Y":
            return True
        else:
            return False
game9()