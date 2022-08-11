# Minjun Kim
# Term Project - "Complex Beauti.py"
from cmu_112_graphics import *
import sys
from btns import *

# change recursion depth limit 
# https://stackoverflow.com/questions/3323001/what-is-the-maximum-recursion-depth-in-python-and-how-to-increase-it
sys.setrecursionlimit(5000)

def appStarted(app):
    # julia set controls (All values can be user-controlled)
    app.c = complex(0, 0)
    juliaReset(app)

    # unchanging
    app.juliaWidth = 480 #600
    app.juliaHeight = 360 #540
    app.juliaImage = Image.new('RGB', (app.juliaWidth, app.juliaHeight), app.color)
    app.timerDelay = 40

    # booleans for displays
    app.julia = False
    app.loading = False
    app.animateScreen = False
    
    # UI images
    # https://www.flaticon.com/
    app.upArrow = app.loadImage('images/upArrow.png')
    app.upArrow = app.scaleImage(app.upArrow, 1/10)

    app.downArrow = app.loadImage('images/downArrow.png')
    app.downArrow = app.scaleImage(app.downArrow, 1/9)

    app.leftArrow = app.loadImage('images/leftArrow.png')
    app.leftArrow = app.scaleImage(app.leftArrow, 1/10)

    app.rightArrow = app.loadImage('images/rightArrow.png')
    app.rightArrow = app.scaleImage(app.rightArrow, 1/10)

    app.plus = app.loadImage('images/plus.png')

    app.minus = app.loadImage('images/minus.png')

    app.paintbrush = app.loadImage('images/paintbrush.png')
    app.paintbrush = app.scaleImage(app.paintbrush, 1/10)

        # GIF animation
        # https://stackoverflow.com/questions/51523994/extract-key-frames-from-gif-using-python    
    
    # cycle (the recursive <-> normal button image)
    temp = Image.open('images/ecosofy-organic.gif')
    app.cycleSize = temp.n_frames

    for i in range(temp.n_frames):
        temp.seek(i)
        temp.save(f"cycle/{i}.png")
    
    app.currCycle = 0
    updateCycle(app)

    # julia animation
    app.juliaSize = 0
    app.currJulia = 0
    app.currJuliaPath = ""
    app.juliaAni = app.loadImage("images/julia_set.gif")
    app.juliaAni = app.scaleImage(app.juliaAni,1/3)

    app.colorCircle = app.loadImage('images/colorCircle.png')
    app.colorCircle = app.scaleImage(app.colorCircle, 1/6)

    app.btn = app.loadImage('images/button.png')
    app.btn = app.scaleImage(app.btn, 1/4)

    # Buttons
        #Change display 
    app.juliaButton = btns(app.width/2, app.height/3, app.btn)
    app.backButton = btns(10+app.btn.width/2, 25, app.btn)
    app.animateButton = btns(app.width/2, app.height*2/3, app.btn)
        
        # animation
    app.aniBackButton = btns(10+app.btn.width/2, 25, app.btn)

        # color switch control
    app.colorButton = btns(app.width/2 + app.juliaWidth/6, 57.5+app.juliaHeight, app.btn)
    app.colorScreen = False
    app.colorBackButton = btns(10+app.btn.width/2, 25, app.btn)
    app.colorApplyButton = btns(app.width - (10+app.btn.width/2), 25, app.btn)
    app.getColorButton = btns(app.width*2/5, app.height/2, app.colorCircle)
    app.inputColor = app.color

        # complementary color <-> white
    #app.compl = btns(x, y, app.btn)
    
        # maxIter control
    x = app.width/2 + app.juliaWidth/2 + 37.5
    app.smallIterInc = btns(x, (app.juliaHeight/4)-28, app.upArrow)
    app.smallIterDec = btns(x, (app.juliaHeight/2)-28, app.downArrow)
    app.bigIterInc = btns(x, (app.juliaHeight*3/4)-28, app.upArrow)
    app.bigIterDec = btns(x, app.juliaHeight-28, app.downArrow)
    
        # recursive/normal switch control
        # canvas.create_rectangle(app.width/2 - app.juliaWidth/2, 20+app.juliaHeight, app.width/2 + app.juliaWidth/2, 95+app.juliaHeight)
    app.recurButton = btns(app.width/2 - app.juliaWidth/6, 57.5+app.juliaHeight, app.btn)

    # # zoom control
    # app.zoomIn = button(x, y, app.plus)
    # app.zoomOut = button(x, y, app.minus)

def updateCycle(app):
    app.currCyclePath = f"cycle/{app.currCycle}.png"
    app.cycle = app.loadImage(app.currCyclePath)
    app.cycle = app.scaleImage(app.cycle,1/10)

def updateJulia(app):
    app.currJuliaPath = f"juliaSet/{app.currJulia}.png"
    app.juliaAni = app.loadImage(app.currJuliaPath)
    app.juliaAni = app.scaleImage(app.juliaAni, 1/3)

# Reset to default values
def juliaReset(app):
    app.zoom = 1
    app.dx = 0
    app.dy = 0
    app.escapeRadius = 2
    app.color = (0, 12, 179)
    app.complCol = False
    app.maxIter = 100
    app.recursive = False

# True if string input is able to be converted to float, false if not
# https://www.programiz.com/python-programming/examples/check-string-number 
def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

# Get "c" value input
def juliaInput(app):
    temp = app.getUserInput('Enter the real part for your c (-1 to 1)')
    
    if temp != None:
        while not isfloat(temp) or float(temp) < -1 or float(temp) > 1:
            temp = app.getUserInput('Invalid input, please re-enter the real part for your c (-1 to 1)')
            if temp == None:
                break

        if temp != None:
            real = float(temp)
            temp = app.getUserInput('Enter the imaginary part for your c (-1 to 1)')
            
            if temp != None:
                while not isfloat(temp) or float(temp) < -1 or float(temp) > 1:
                    temp = app.getUserInput('Invalid input, please re-enter the imaginary part for your c (-1 to 1)')
                    if temp == None:
                        break
            
                if temp != None:
                    imag = -1*float(temp)
                        
                    temp = complex(real, imag)
                    app.c = temp
                    getJuliaSet(app)

def colorInput(app):
    input = app.getUserInput('Enter the desired color in rgb value separated in spaces! (Ex. \"0 12 179\")')
    
    if input != None:
        temp = input.split(" ")
        while (len(temp) != 3 or not temp[0].isdigit() or not temp[1].isdigit() or not temp[2].isdigit() or 
                int(temp[0]) < 0 or int(temp[0]) > 255 or int(temp[1]) < 0 or int(temp[1]) > 255 or int(temp[2]) < 0 or int(temp[2]) > 255):
            input = app.getUserInput('Invalid input, please enter the desired color in rgb value separated in spaces! (Ex. \"0 12 179\")')
            if input == None:
                break
            temp = input.split(" ")
        if input != None:
            app.inputColor = (int(temp[0]), int(temp[1]), int(temp[2]))


def keyPressed(app, event):
    # Move julia set
    if event.key == "Up":
        app.dy += 0.2
        getJuliaSet(app)
    elif event.key == "Down":
        app.dy -= 0.2
        getJuliaSet(app)
    elif event.key == "Right":
        app.dx -= 0.2 
        getJuliaSet(app)   
    elif event.key == "Left":
        app.dx += 0.2
        getJuliaSet(app)

def mousePressed(app, event):
    # main screen
    if not app.julia and not app.animateScreen:
        # regular julia set button
        if app.juliaButton.clicked(event.x, event.y):
            juliaInput(app)

        # animation button
        elif app.animateButton.clicked(event.x, event.y):
            app.animateScreen = True
            # julia animation
            temp = Image.open('images/julia_set.gif')
            app.juliaSize = temp.n_frames

            for i in range(temp.n_frames):
                temp.seek(i)
                temp.save(f"juliaset/{i}.png")

            app.currJulia = 0
            updateJulia(app)
            

    # animate screen
    if app.animateScreen:
        # back button
        if app.aniBackButton.clicked(event.x, event.y):
            app.animateScreen = False

    # julia set screen
    if app.julia:
        # back
        if app.backButton.clicked(event.x, event.y):
            app.julia = False
            juliaReset(app)
            
        # maxIter control
        if app.smallIterInc.clicked(event.x, event.y):
            app.maxIter += 10
            getJuliaSet(app)
        elif app.smallIterDec.clicked(event.x, event.y):
            if app.maxIter - 10 > 0:
                app.maxIter -= 10
                getJuliaSet(app)
        elif app.bigIterInc.clicked(event.x, event.y):
            app.maxIter += 50
            getJuliaSet(app)
        elif app.bigIterDec.clicked(event.x, event.y):
            if app.maxIter - 50 > 0:
                app.maxIter -= 50
                getJuliaSet(app)

        # recursive switch
        elif app.recurButton.clicked(event.x, event.y):
            app.recursive = not app.recursive
            getJuliaSet(app)

        # color switch
        elif app.colorButton.clicked(event.x, event.y):
            app.julia = False
            app.colorScreen = True
            app.inputColor = app.color

        
    
    # color pick screen
    if app.colorScreen:
        if app.colorBackButton.clicked(event.x, event.y):
            app.julia = True
            app.colorScreen = False
            app.inputColor = app.color
            juliaReset(app)
        
        elif app.getColorButton.clicked(event.x, event.y):
            colorInput(app)

        elif app.colorApplyButton.clicked(event.x, event.y):
            app.color = app.inputColor
            getJuliaSet(app)
            app.colorScreen = False
            app.julia = True

# Potentially for animation/rotation of julia set (after MVP)
def timerFired(app):
    if app.julia:
        app.currCycle = app.currCycle + 1 if app.currCycle < app.cycleSize-1 else 0
        updateCycle(app)
    if app.animateScreen:
        app.currJulia = app.currJulia + 1 if app.currJulia < app.juliaSize-1 else 0
        updateJulia(app)

def rgbToHex(rgb):
    return "#" + '%02x%02x%02x' % rgb

# Picks a color for given i (maxIter-i is the amount of iterations done before failing check)
def colorPicker(app, r, g, b, i):
    # complementary color calculation for pixels that accomplishes all maxIter iterations
    # https://www.101computing.net/complementary-colours-algorithm/ 
    if i == 0:
        (r, g, b) = (255-app.color[0], 255-app.color[1], 255-app.color[2]) if app.complCol else (255, 255, 255)

    else:
        # The color is scaled from the base color to white
        (r, g, b) = (app.color[0] + int((255-app.color[0])*(1-(i/app.maxIter))),
                    app.color[1] + int((255-app.color[1])*(1-(i/app.maxIter))), 
                    app.color[2] + int((255-app.color[2])*(1-(i/app.maxIter))))
    if r > 255:
        r = 255-app.color[0] if app.complCol else 255
    if g > 255:
        g = 255-app.color[1] if app.complCol else 255
    if b > 255:
        b = 255-app.color[2] if app.complCol else 255
    return (r, g, b)

# The recursive method of constructing the julia set. (Uses dictionary/Dynamic Programming)
# Any visited values will be stored in the dictionary, and if the value is encountered 
# again in one of the future z's iterations, the value is instantly returned, 
# without having to iterate through the same values again. 
def recursiveJulia(app, z, i, idict):
    tempz = z*z + app.c
    if i == 0:
        return 0
    elif tempz.real**2 + tempz.imag**2 >= app.escapeRadius**2:
        return 1
    elif z in idict:
        return idict[z]
    elif z not in idict:
        idict[z] = 1 + recursiveJulia(app, tempz, i-1, idict)
        return idict[z]
    else:
        return 1 + recursiveJulia(app, tempz, i-1, idict)
    
# This google doc contains all the external websites used to further my understanding on the material in order to 
# implement this algorithm
# https://docs.google.com/document/d/1ACTq_AqFXH2byIl9DNLnuk8mpxn3MBKcLcbJy8ZYnv4/edit
def getJuliaSet(app):
    for x in range(app.juliaWidth):
        for y in range(app.juliaHeight):
            app.x = x
            app.y = y
            z = complex((2*(x-(app.juliaWidth/2)))/(app.zoom*app.juliaWidth*0.5) + app.dx, 
            (1.5*(y-(app.juliaHeight/2)))/(app.zoom*app.juliaHeight*0.5) + app.dy)
            
            if app.recursive:
                idict = dict()
                i = app.maxIter-recursiveJulia(app, z, app.maxIter, idict)
            else:
                i = app.maxIter
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

def drawAnimateScreen(app, canvas):
    if app.animateScreen:
        # Back button
        canvas.create_image(app.aniBackButton.x, app.aniBackButton.y, image=ImageTk.PhotoImage(app.aniBackButton.img))
        canvas.create_text(app.aniBackButton.x, app.aniBackButton.y-3, font = ("MS Sans Serif", 12), text = "Back")

        # Animation display
        canvas.create_image(app.width/2, app.height/2, image=ImageTk.PhotoImage(app.juliaAni))
        canvas.create_text(app.width/2, 60, font = ("MS Sans Serif", 16, "bold"), text = "Animation of given r value from calling \"juliaAni.py\"")

# Draws the color change screen
def drawColorScreen(app, canvas):
    if app.colorScreen:
        # Back button
        canvas.create_image(app.colorBackButton.x, app.colorBackButton.y, image=ImageTk.PhotoImage(app.colorBackButton.img))
        canvas.create_text(app.colorBackButton.x, app.colorBackButton.y-3, font = ("MS Sans Serif", 12), text = "Back")

        # Input button
        canvas.create_image(app.getColorButton.x, app.getColorButton.y, image=ImageTk.PhotoImage(app.getColorButton.img))

        # Color display
        canvas.create_rectangle(app.width*2/3-100, app.height/2-100, app.width*2/3+100, app.height/2+100, fill = rgbToHex(app.inputColor), width = 0)

        # Apply button
        canvas.create_image(app.colorApplyButton.x, app.colorApplyButton.y, image=ImageTk.PhotoImage(app.colorApplyButton.img))
        canvas.create_text(app.colorApplyButton.x, app.colorApplyButton.y-3, font = ("MS Sans Serif", 12), text = "Apply")

# Draws the julia set visualization screen
def drawJuliaSetScreen(app, canvas):
    if app.julia:
        # Julia Visualization
        canvas.create_image(app.width/2, app.juliaHeight/2 + 20, image=ImageTk.PhotoImage(app.juliaImage))

        # Back button
        canvas.create_image(app.backButton.x, app.backButton.y, image=ImageTk.PhotoImage(app.backButton.img))
        canvas.create_text(app.backButton.x, app.backButton.y-3, font = ("MS Sans Serif", 12), text = "Back")

        # maxIter display/control buttons
            # Header/display
        canvas.create_text(app.width/2 + app.juliaWidth/2 + 100, (app.smallIterDec.y + app.bigIterInc.y)/2, 
                            font = ("MS Sans Serif", 16), anchor = "w", 
                            text = f"Increase/Decrease Maximum Iteration\nCurrent: {app.maxIter}")
        
            # +10
        canvas.create_image(app.smallIterInc.x, app.smallIterInc.y, image=ImageTk.PhotoImage(app.smallIterInc.img))
        canvas.create_text(app.smallIterInc.x, app.smallIterInc.y+app.smallIterInc.img.height/2 + 7, font = ("MS Sans Serif", 12), text = "+10")

            # -10
        canvas.create_image(app.smallIterDec.x, app.smallIterDec.y, image=ImageTk.PhotoImage(app.smallIterDec.img))
        canvas.create_text(app.smallIterInc.x, app.smallIterDec.y+app.smallIterDec.img.height/2 + 7, font = ("MS Sans Serif", 12), text = "-10")
        
            # +50
        canvas.create_image(app.bigIterInc.x, app.bigIterInc.y, image=ImageTk.PhotoImage(app.bigIterInc.img))
        canvas.create_text(app.smallIterInc.x, app.bigIterInc.y+app.bigIterInc.img.height/2 + 7, font = ("MS Sans Serif", 12), text = "+50")

            # -50
        canvas.create_image(app.bigIterInc.x, app.bigIterDec.y, image=ImageTk.PhotoImage(app.bigIterDec.img))
        canvas.create_text(app.smallIterInc.x, app.bigIterDec.y+app.bigIterDec.img.height/2 + 7, font = ("MS Sans Serif", 12), text = "-50")

        # recursive <-> normal switch button/cycle
        canvas.create_image(app.recurButton.x, app.recurButton.y, image=ImageTk.PhotoImage(app.recurButton.img))
        msg = "To normal" if app.recursive else "To recursive"
        canvas.create_text(app.recurButton.x, app.recurButton.y-3, font = ("MS Sans Serif", 12), text = msg)
        canvas.create_image(app.recurButton.x - app.recurButton.img.width/2 - 15 - app.cycle.width/2, app.recurButton.y, image=ImageTk.PhotoImage(app.cycle))

        # color switch button/paintbrush
        canvas.create_image(app.colorButton.x, app.colorButton.y, image=ImageTk.PhotoImage(app.colorButton.img))
        canvas.create_text(app.colorButton.x, app.colorButton.y-3, font = ("MS Sans Serif", 12), text = "Change Color")
        canvas.create_image(app.colorButton.x + app.colorButton.img.width/2 + 15 + app.paintbrush.width/2, app.colorButton.y, image=ImageTk.PhotoImage(app.paintbrush))

        # button-holding rectangle outlines
            # right box
        canvas.create_rectangle(app.width/2 + app.juliaWidth/2, 20, app.width/2 + app.juliaWidth/2 + 75, 20+app.juliaHeight)

            # left box
        canvas.create_rectangle(app.width/2 - app.juliaWidth/2, 20, app.width/2 - app.juliaWidth/2 - 75, 20+app.juliaHeight)

            # bottom box
        canvas.create_rectangle(app.width/2 - app.juliaWidth/2, 20+app.juliaHeight, app.width/2 + app.juliaWidth/2, 95+app.juliaHeight)

# Draws the main screen
def drawMainScreen(app, canvas):
    if not app.julia and not app.colorScreen and not app.animateScreen and not app.loading:
        canvas.create_image(app.juliaButton.x, app.juliaButton.y, image=ImageTk.PhotoImage(app.juliaButton.img))
        canvas.create_image(app.animateButton.x, app.animateButton.y, image=ImageTk.PhotoImage(app.animateButton.img))
        canvas.create_text(app.width/2, app.height/3-3, text = "Julia")
        canvas.create_text(app.width/2, app.height*2/3-3, text = "Animation")


def redrawAll(app, canvas):
    drawAnimateScreen(app, canvas)
    drawColorScreen(app, canvas)
    drawMainScreen(app, canvas)
    drawJuliaSetScreen(app, canvas)

def main():
    runApp(width=1600, height=900)

if __name__ == '__main__':
    main()