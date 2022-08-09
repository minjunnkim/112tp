# Minjun Kim
# Term Project - "Complex Beauti.py"
#

import cmath, math
from cmu_112_graphics import *

def appStarted(app):
    app.zoom = 1
    app.dx = 0
    app.dy = 0
    app.escapeRadius = 2
    app.color = (65, 38, 145)
    app.c = complex(-0.7, 0.27015)
    app.maxIter = 5000
    app.screen = dict()
    app.julia = False
    app.loading = False
    app.brightness = 1
    app.juliaWidth = 600
    app.juliaHeight = 450
    app.juliaImage = Image.new('RGB', (app.juliaWidth, app.juliaHeight), app.color)

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
    return

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
        (r, g, b) = (0, 0, 0)

    else:
        (r, g, b) = (app.color[0] + int((255-app.color[0])*app.brightness*(1-(i/app.maxIter))),
                    app.color[1] + int((255-app.color[1])*app.brightness*(1-(i/app.maxIter))), 
                    app.color[2] + int((255-app.color[2])*app.brightness*(1-(i/app.maxIter))))
        if r > 255:
            r = 0
        if g > 255:
            g = 0
        if b > 255:
            b = 0
    return (r, g, b)

def getJuliaSet(app):
    app.loading = True
    for x in range(app.juliaWidth):
        for y in range(app.juliaHeight):
            app.x = x
            app.y = y
            z = complex((1.7*(x-(app.juliaWidth/2)))/(app.zoom*app.juliaWidth*0.5) + app.dx, 
            (1.2*(y-(app.juliaHeight/2)))/(app.zoom*app.juliaHeight*0.5) + app.dy)
            
            i = app.maxIter
            while z.real**2 + z.imag**2 < app.escapeRadius**2 and i > 0:
                z = z*z + app.c
                i-=1
            
            r, g, b = 0, 0, 0
            r, g, b = colorPicker(app, r, g, b, i)
            
            #print(x, y, i, r, g, b)
            app.juliaImage.putpixel((x,y), (r, g, b))
    app.loading = False
    app.julia = True

def drawJuliaSet(app, canvas):
    if app.julia:
        canvas.create_image(app.width/2, app.juliaHeight/2 + 20, image=ImageTk.PhotoImage(app.juliaImage))

def drawLoadingScreen(app, canvas):
    if app.loading:
        print("a")
        canvas.create_text(app.width/2, app.height/2, text = ("|" * int((app.x/app.juliaWidth)*20)) + ("-" * (1-(int((app.x/app.juliaWidth)*20)))))

def drawMainScreen(app, canvas):
    if not app.julia and not app.loading:
        canvas.create_rectangle(app.width/8, 60, app.width/4, 100)
        canvas.create_text(app.width*3/16, 80, text = "Julia")

def redrawAll(app, canvas):
    drawLoadingScreen(app, canvas)
    drawMainScreen(app, canvas)
    drawJuliaSet(app, canvas)

def main():
    runApp(width=1600, height=900)

if __name__ == '__main__':
    main()