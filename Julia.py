import cmath, math
from cmu_112_graphics import *

def appStarted(app):
    app.zoom = 1
    app.dx = 0
    app.dy = 0
    app.escapeRadius = 2
    app.color = (26, 31, 163)
    app.c = complex(-0.7, 0.27015)
    app.maxIter = 1000
    app.screen = dict()
    app.julia = False
    app.loading = False

    #color presets
    app.preRed = [(255, 0, 0), ]

def keyPressed(app, event):
    c = False
    if event.key == 'j':
        try:
            real = float(app.getUserInput('Enter the real part for your c'))
        except ValueError:
            print("asdfasdf")
            app.message = 'Invalid input. Please enter a number'
            c = True
            
        try:
            imag = float(app.getUserInput('Enter the imaginary part for your c'))
        except ValueError:
            app.message = 'Invalid input. Please enter a number'
            c = True
            
        temp = complex(real, imag)
        app.c = temp
        getJuliaSet(app)

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
        getJuliaSet(app)
        app.loading = True

def timerFired(app):
    pass

def rgbToHex(r, g, b):
    return f'#{r:02x}{g:02x}{b:02x}'

def colorPicker(app, r, g, b, i):
    if i == 0:
        (r, g, b) = (0, 0, 0)

    elif i < app.maxIter//10:
        (r, g, b) = (255, 255, 255)
    
    elif i < app.maxIter//8:
        (r, g, b) = (app.color[0] + int((255-app.color[0])*(8/9)), 
                    app.color[1] + int((255-app.color[1])*(8/9)), 
                    app.color[2] + int((255-app.color[2])*(8/9)))
        
    elif i < app.maxIter//4:
        (r, g, b) = (app.color[0] + int((255-app.color[0])*(7/9)), 
                    app.color[1] + int((255-app.color[1])*(7/9)), 
                    app.color[2] + int((255-app.color[2])*(7/9)))

    elif i < (app.maxIter*3)//8:
        (r, g, b) = (app.color[0] + int((255-app.color[0])*(6/9)), 
                    app.color[1] + int((255-app.color[1])*(6/9)), 
                    app.color[2] + int((255-app.color[2])*(6/9)))

    elif i < app.maxIter//2:
        (r, g, b) = (app.color[0] + int((255-app.color[0])*(5/9)), 
                    app.color[1] + int((255-app.color[1])*(5/9)), 
                    app.color[2] + int((255-app.color[2])*(5/9)))

    elif i < (app.maxIter*5)//8:
        (r, g, b) = (app.color[0] + int((255-app.color[0])*(4/9)), 
                    app.color[1] + int((255-app.color[1])*(4/9)), 
                    app.color[2] + int((255-app.color[2])*(4/9)))

    elif i < (app.maxIter*3)//4:
        (r, g, b) = (app.color[0] + int((255-app.color[0])*(3/9)), 
                    app.color[1] + int((255-app.color[1])*(3/9)), 
                    app.color[2] + int((255-app.color[2])*(3/9)))

    elif i < (app.maxIter*7)//8:
        (r, g, b) = (app.color[0] + int((255-app.color[0])*(2/9)), 
                    app.color[1] + int((255-app.color[1])*(2/9)), 
                    app.color[2] + int((255-app.color[2])*(2/9)))

    else:
        (r, g, b) = app.color

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
            
            print(i, r, g, b)

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