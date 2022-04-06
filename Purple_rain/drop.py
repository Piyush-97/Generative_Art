
def translate(value, leftMin, leftMax, rightMin, rightMax):
    # Figure out how 'wide' each range is
    leftSpan = leftMax - leftMin
    rightSpan = rightMax - rightMin

    # Convert the left range into a 0-1 range (float)
    valueScaled = float(value - leftMin) / float(leftSpan)

    # Convert the 0-1 range into a value in the right range.
    return rightMin + (valueScaled * rightSpan)

class Drop():
    def __init__(self):
        self.x = random(640)
        self.y = random(-200, -50)
        self.z = random(0, 20)
        self.yspeed = translate(self.z, 0, 20, 4, 10)
        self.len_ = translate(self.z, 0, 20, 10, 40)
        
    def fall(self):
        self.y += self.yspeed
        self.yspeed += 0.01
        if self.y > 360:
            self.y = random(-200, -100)
            self.yspeed = translate(self.z, 0, 20, 4, 10)
        
    def show(self):
        thick = translate(self.z, 0, 20, 1, 2)
        strokeWeight(thick)
        stroke(138, 43, 226)
        line(self.x, self.y, self.x, self.y+10)
