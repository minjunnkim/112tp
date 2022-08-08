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

def keyPressed(app, event):
    pass

def mousePressed(app, event):
    pass

def timerFired(app):
    pass

def rgbToHex(r, g, b):
    return f'#{r:02x}{g:02x}{b:02x}'

def drawJuliaSet(app, canvas):
    for x in range(app.width):
        for y in range(app.height):
            z = complex((1.5*(x-(app.width/2)))/(app.zoom*app.width*0.5) + app.dx, 
            (y-(app.height/2))/(app.zoom*app.height*0.5) + app.dy)
            
            i = app.maxIter
            while z.real**2 + z.imag**2 < app.escapeRadius**2 and i > 1:
                z = z*z + app.c
                i-=1
            
            r = int(app.color[0]*(i/app.maxIter))
            g = int(app.color[1]*(i/app.maxIter))
            b = int(app.color[2]*(i/app.maxIter))

            r = 0 if r < 0 else r
            g = 0 if g < 0 else g
            b = 0 if b < 0 else b
            
            color = rgbToHex(r, g, b)
            print(color)
            canvas.create_rectangle(x, x, y+1, y+1, fill = color)

def redrawAll(app, canvas):
    drawJuliaSet(app, canvas)

def main():
    runApp(width=1920, height=1080)

if __name__ == '__main__':
    main()