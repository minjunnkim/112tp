import colorsys
from cmu_112_graphics import *

def appStarted(app):
    app.colorHSV = (0.5, 0.5, 0.4)

def redrawAll(app, canvas):
    canvas.create_rectangle( 200, 300, 400, 500, fill = colorsys.hsv_to_rgb(app.colorHSV))

runApp(width = 1920, height = 1080)