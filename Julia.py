import cmath, math
from cmu_112_graphics import *

def appStarted(app):
    app.zoom = 1
    app.dx = 0
    app.dy = 0
    app.escapeRadius = 2
    app.color = (255, 0, 0)
    app.c = complex(-0.7, 0.27015)
    app.maxIter = 255
    app.julia = False

def keyPressed(app, event):
    pass

def mousePressed(app, event):
    if not app.julia and event.x > app.width/8 and event.x < app.width/4 and event.y > 60 and event.y < 100:
        try:
            real = float(app.getUserInput('Enter the real part for your c'))
        except ValueError:
            app.message = 'Invalid input. Please enter a number'
            return
        try:
            imag = float(app.getUserInput('Enter the imaginary part for your c'))
        except ValueError:
            app.message = 'Invalid input. Please enter a number'
            return
        temp = complex(real, imag)
        app.c = temp
        print(app.c)
        app.julia = True

def timerFired(app):
    pass

def rgbToHex(r, g, b):
    return f'#{r:02x}{g:02x}{b:02x}'

def drawJuliaSet(app, canvas):
    if app.julia:
        for x in range(app.width):
            for y in range(app.height):
                z = complex((1.5*(x-(app.width/2)))/(app.zoom*app.width*0.5) + app.dx, 
                (y-(app.height/2))/(app.zoom*app.height*0.5) + app.dy)
                
                i = app.maxIter
                while z.real**2 + z.imag**2 < app.escapeRadius**2 and i > 1:
                    z = z*z + app.c
                    i-=1
                
                #print(app.color, i, app.maxIter)
                r = i << 21
                g = i << 10
                b = i * 8
                color = rgbToHex(r, g, b)
                #print((x,y), (x+1,y+1), color)
                canvas.create_rectangle(x, y, x+1, y+1, fill = color, width = 0)

def drawMainScreen(app, canvas):
    if not app.julia:
        canvas.create_rectangle(app.width/8, 60, app.width/4, 100)
        canvas.create_text(app.width*3/16, 80, text = "Julia")


def redrawAll(app, canvas):
    drawMainScreen(app, canvas)
    drawJuliaSet(app, canvas)

def main():
    runApp(width=320, height=240)

if __name__ == '__main__':
    main()