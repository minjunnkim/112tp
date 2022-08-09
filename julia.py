# import cmath
# from cmu_112_graphics import *

# class julia():
#     def __init__(self, c):
#         self.c = c
#         self.color = (65, 38, 145)
#         self.escRad = 2
#         self.maxIter = 5000
#         self.brn = 1
#         self.zoom = 1
#         self.width = 600
#         self.height = 540
#         self.dx = 0
#         self.dy = 0
#         self.juliaImage = Image.new('RGB', (self.width, self.height), self.color)
#         self.idict = dict()

#     # private methods
#     # https://www.geeksforgeeks.org/private-methods-in-python/
#     def __juliaPixelColor(self, i):
#         if i == 0:
#             (r, g, b) = (0, 0, 0)

#         else:
#             (r, g, b) = (self.color[0] + int((255-self.color[0])*self.brn*(1-(i/self.maxIter))),
#                         self.color[1] + int((255-self.color[1])*self.brn*(1-(i/self.maxIter))), 
#                         self.color[2] + int((255-self.color[2])*self.brn*(1-(i/self.maxIter))))
#             if r > 255:
#                 r = 0
#             if g > 255:
#                 g = 0
#             if b > 255:
#                 b = 0
#         return (r, g, b)

#     def __getJuliaSet(self):

#         for x in range(self.width):
#             for y in range(self.height):
#                 z = complex((1.7*(x-(self.width/2)))/(self.zoom*self.width*0.5) + self.dx, 
#                 (1.2*(y-(self.height/2)))/(self.zoom*self.height*0.5) + self.dy)
                
#                 i = self.maxIter
#                 while z.real**2 + z.imag**2 < self.escRad**2 and i > 0:
#                     if z in self.idict:
#                         i -= self.idict[z]
#                         break
#                     else:
#                         self.idict[z] = self.maxIter-i
#                     z = z*z + self.c
#                     i-=1
                
#                 r, g, b = 0, 0, 0
#                 r, g, b = self.__juliaPixelColor(self, i)
                
#                 print(x, y, i, r, g, b)
#                 self.juliaImage.putpixel((x,y), (r, g, b))
#         return self.juliaImage
    
#     def zoomInOut(self, n):
#         if not(n == -1 and self.zoom == 1):
#             self.zoom += n
#             self.__getJuliaSet()
    

#     def getImage(self):
#         pass