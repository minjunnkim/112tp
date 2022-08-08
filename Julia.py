# Minjun Kim
# 

import cmath, math, colorsys
from cmu_112_graphics import *

def appStarted(app):
    app.zoom = 1
    app.dx = 0
    app.dy = 0
    app.escapeRadius = 2
    app.color = (2, 5, 89)
    app.c = complex(-0.7, 0.27015)
    app.maxIter = 5000
    app.screen = dict()
    app.julia = False
    app.loading = False
    app.brightness = 32

def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

def juliaInput(app):
    temp = app.getUserInput('Enter the real part for your c')
    
    while not isfloat(temp):
        temp = app.getUserInput('Invalid input, please re-enter the real part for your c')
    
    real = temp

    temp = app.getUserInput('Enter the imaginary part for your c')
    
    while not isfloat(temp):
        temp = app.getUserInput('Invalid input, please re-enter the imaginary part for your c')
    
    imag = temp
        
    temp = complex(real, imag)
    app.c = temp
    getJuliaSet(app)

def keyPressed(app, event):
    if event.key == 'j':
        juliaInput(app)

def mousePressed(app, event):
    if not app.julia and event.x > app.width/8 and event.x < app.width/4 and event.y > 60 and event.y < 100:
        juliaInput(app)

def timerFired(app):
    pass

def rgbToHex(r, g, b):
    return f'#{r:02x}{g:02x}{b:02x}'

def colorPicker(app, r, g, b, i):

    #(h, s, v) = colorsys.rgb_to_hsv(app.color[0]/255, app.color[1]/255, app.color[2]/255)

    if i == 0:
        (r, g, b) = (0, 0, 0)

    else:
        # (h, s, v) = (h * (1-(i/app.maxIter)), s, v)
        # (r, g, b) = colorsys.hsv_to_rgb(h, s, v)
        # (r, g, b) = (int(r*255), int(g*255), int(b*255))
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
    for x in range(app.width):
        for y in range(app.height):
            app.x = x
            app.y = y
            z = complex((1.5*(x-(app.width/2)))/(app.zoom*app.width*0.5) + app.dx, 
            (1.3*(y-(app.height/2)))/(app.zoom*app.height*0.5) + app.dy)
            
            i = app.maxIter
            while z.real**2 + z.imag**2 < app.escapeRadius**2 and i > 0:
                z = z*z + app.c
                i-=1

            r, g, b = 0, 0, 0
            r, g, b = colorPicker(app, r, g, b, i)
            
            #print(i, r, g, b)

            color = rgbToHex(r, g, b)
            temp = app.screen.get(color, set())
            temp.add((x,y))
            app.screen[color] = temp
    app.julia = True


def drawJuliaSet(app, canvas):
    keys = set(app.screen.keys())
    for a in keys:
        for (x,y) in app.screen[a]:
            canvas.create_rectangle(x, y, x+1, y+1, fill = a, width = 0)

def drawLoadingScreen(app, canvas):
    pass

def drawMainScreen(app, canvas):
    if not app.julia:
        canvas.create_rectangle(app.width/8, 60, app.width/4, 100)
        canvas.create_text(app.width*3/16, 80, text = "Julia")

def redrawAll(app, canvas):
    drawMainScreen(app, canvas)
    drawLoadingScreen(app, canvas)
    drawJuliaSet(app, canvas)

def main():
    runApp(width=480, height=360)

if __name__ == '__main__':
    main()