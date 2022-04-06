

from drop import Drop

drops = [Drop() for i in range(500)]

def setup():
    size(640, 360)
    
        
def draw():
    background(230, 230, 250)
    for drop in drops:
        drop.fall()
        drop.show()
        
