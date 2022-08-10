class btns():
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.img = img

    def clicked(self, px, py):
        if (px > self.x-self.img.width/2 and px < self.x+self.img.width/2 
        and py > self.y-self.img.height/2 and py < self.y+self.img.height/2):
            return True
        return False
