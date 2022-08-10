# Minjun Kim
# Term Project - "Complex Beauti.py"
#

import cmath, math, sys
from cmu_112_graphics import *

# change recursion depth limit 
# https://stackoverflow.com/questions/3323001/what-is-the-maximum-recursion-depth-in-python-and-how-to-increase-it
sys.setrecursionlimit(10000)

def appStarted(app):
    app.zoom = 1
    app.dx = 0
    app.dy = 0
    app.escapeRadius = 2
    app.color = (0, 12, 179)
    app.c = complex(-0.7, 0.27015)
    app.maxIter = 30
    app.julia = False
    app.loading = False
    app.juliaWidth = 480 #600
    app.juliaHeight = 360 #540
    app.juliaImage = Image.new('RGB', (app.juliaWidth, app.juliaHeight), app.color)
    app.idict = dict()

    #images
    app.upArrow = app.loadImage('images/upArrow.png')

def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

def juliaInput(app):
    temp = app.getUserInput('Enter the real part for your c')
    
    if temp != None:
        while not isfloat(temp):
            temp = app.getUserInput('Invalid input, please re-enter the real part for your c')

        if temp != None:
            real = float(temp)
            temp = app.getUserInput('Enter the imaginary part for your c')
            
            if temp != None:
                while not isfloat(temp):
                    temp = app.getUserInput('Invalid input, please re-enter the imaginary part for your c')
            
                if temp != None:
                    imag = -1*float(temp)
                        
                    temp = complex(real, imag)
                    app.c = temp
                    getJuliaSet(app)

def keyPressed(app, event):
    if event.key == "Up":
        app.dy += 0.2
        getJuliaSet(app)
    elif event.key == "Down":
        app.dy -= 0.2
        getJuliaSet(app)
    elif event.key == "Right":
        app.dx += 0.2 
        getJuliaSet(app)   
    elif event.key == "Left":
        app.dx -= 0.2
        getJuliaSet(app)

def mousePressed(app, event):
    if not app.julia and event.x > app.width/8 and event.x < app.width/4 and event.y > 60 and event.y < 100:
        juliaInput(app)

def timerFired(app):
    pass

def colorPicker(app, r, g, b, i):
    if i == 0:
        (r, g, b) = (255-app.color[0], 255-app.color[1], 255-app.color[2])

    else:
        (r, g, b) = (app.color[0] + int((255-app.color[0])*(1-(i/app.maxIter))),
                    app.color[1] + int((255-app.color[1])*(1-(i/app.maxIter))), 
                    app.color[2] + int((255-app.color[2])*(1-(i/app.maxIter))))
    if r > 255:
        r = 255-app.color[0]
    if g > 255:
        g = 255-app.color[1]
    if b > 255:
        b = 255-app.color[2]
    return (r, g, b)

def recursiveJulia(app, z, i):
    tempz = z*z + app.c
    if i == 0:
        return 0
    elif tempz.real**2 + tempz.imag**2 >= app.escapeRadius**2:
        return 1
    elif z in app.idict:
        return app.idict[z]
    elif z not in app.idict:
        app.idict[z] = 1 + recursiveJulia(app, tempz, i-1)
        return app.idict[z]
    else:
        return 1 + recursiveJulia(app, tempz, i-1)
    

def getJuliaSet(app):
    for x in range(app.juliaWidth):
        for y in range(app.juliaHeight):
            app.x = x
            app.y = y
            z = complex((2*(x-(app.juliaWidth/2)))/(app.zoom*app.juliaWidth*0.5) + app.dx, 
            (1.5*(y-(app.juliaHeight/2)))/(app.zoom*app.juliaHeight*0.5) + app.dy)
            
            i = app.maxIter
            #i = app.maxIter-recursiveJulia(app, z, app.maxIter)
            while z.real**2 + z.imag**2 < app.escapeRadius**2 and i > 0:
                # if z in app.idict:
                #     print("a")
                #     i -= app.idict[z] - 1
                #     break
                z = z*z + app.c
                i-=1
            
            #if app.idict[z] :
                

            r, g, b = 0, 0, 0
            r, g, b = colorPicker(app, r, g, b, i)
            
            #print(x, y, i, r, g, b)
            app.juliaImage.putpixel((x,y), (r, g, b))
    app.julia = True

def drawJuliaSetScreen(app, canvas):
    if app.julia:
        #print("a")
        canvas.create_image(app.width/2, app.juliaHeight/2 + 20, image=ImageTk.PhotoImage(app.juliaImage))
        canvas.create_rectangle(app.width/2 + app.juliaWidth/2, 20, app.width/2 + app.juliaWidth/2 + 75, 20+app.juliaHeight)
        canvas.create_rectangle(app.width/2 - app.juliaWidth/2, 20, app.width/2 - app.juliaWidth/2 - 75, 20+app.juliaHeight)
        canvas.create_rectangle(app.width/2 - app.juliaWidth/2, 20+app.juliaHeight, app.width/2 + app.juliaWidth/2, 95+app.juliaHeight)

def drawMainScreen(app, canvas):
    if not app.julia and not app.loading:
        canvas.create_rectangle(app.width/8, 60, app.width/4, 100)
        canvas.create_text(app.width*3/16, 80, text = "Julia")

def redrawAll(app, canvas):
    drawMainScreen(app, canvas)
    drawJuliaSetScreen(app, canvas)

def main():
    runApp(width=1600, height=900)

if __name__ == '__main__':
    main()