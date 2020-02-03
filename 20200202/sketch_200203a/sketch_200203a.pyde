y = 50.0
speed = 1.0
radius = 15.0

def setup():
    size(100, 100)
    noStroke()
    ellipseMode(RADIUS)
    
def draw():
    global y
    background(0)
    ellipse(33, y, radius, radius)
    y = y + speed
    if (y > height+radius):
        y = -radius
