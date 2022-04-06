def setup():
    size(800, 600)
    background(255)
    translate(width / 2, height)
    drawTree(175, -90);
    
def drawTree(len_, angle):
    if len_ > 2:
        rotate(radians(angle))
        line(0, 0, len_, 0)
        translate(len_, 0)
        pushMatrix()
        drawTree(len_ * 0.75, -30)
        popMatrix()
        pushMatrix()
        drawTree(len_ * 0.66, 50)
        popMatrix()
