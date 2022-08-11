# Animates and saves a gif of the animation
# References:
# https://medium.com/@er_95882/animating-fractals-with-python-julia-and-maldelbrot-sets-e65a04549423 
# https://en.wikipedia.org/wiki/Julia_set#
# https://isquared.digital/visualizations/2020-06-26-julia-set/
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# ignore warnings
import warnings
warnings.filterwarnings("ignore")

def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False


def getAniJuliaSet(zx, zy, cx, cy, threshold):
    # initial conditions
    z = complex(zx, zy)
    c = complex(cx, cy)
    
    for i in range(threshold):
        z = z**2 + c
        if abs(z) > 4.:  # it diverged
            return i
        
    return threshold - 1  # it didn't diverge

x_start, y_start = -2, -2  # an interesting region starts here
width, height = 4, 4  # for 3 units to the left and to the right
density_per_unit = 200  # how many pixles per unit

re = np.linspace(x_start, x_start + width, width * density_per_unit )  # real axis
im = np.linspace(y_start, y_start + height, height * density_per_unit)  # imaginary axis
threshold = 20  # max allowed iterations
frames = 144  # number of frames in the animation

r = 0.7885

# Get input
# https://www.w3schools.com/python/ref_func_input.asp 
x = None
while x != "cancel" and (x == None or not isfloat(x) or float(x) < -1 or float(x) > 1):
    x = input("Enter the r value for animation! (-1 to 1) Type \"cancel\" to exit\n")

if x != "cancel":
    r = float(x)

# represent the "c" value using inputted "r" value c = r*cos(a) + i*r*sin(a) = r*e^{i*a}
a = np.linspace(0, 2*np.pi, frames)

fig = plt.figure(figsize=(10, 10))
ax = plt.axes()

def animate(i):
    # clear axes object
    ax.clear()
    ax.set_xticks([], [])
    ax.set_yticks([], [])
    
    X = np.empty((len(re), len(im)))  # the initial array-like image
    cx, cy = r * np.cos(a[i]), r * np.sin(a[i])
    
    # fill-in the image with the number of interations
    for i in range(len(re)):
        for j in range(len(im)):
            X[i, j] = getAniJuliaSet(zx=re[i], zy=im[j], cx=cx, cy=cy, threshold=threshold)
    
    img = ax.imshow(X.T, interpolation="hamming", cmap='magma')
    return [img]

# call the animator	 
anim = animation.FuncAnimation(fig, animate, frames=frames, interval=50, blit=True)

# save the gif to images file
anim.save('images/julia_set.gif', writer='Pillow')




