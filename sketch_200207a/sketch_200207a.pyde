moveX = moveY = 0

def setup():
    size(100, 100)
    
def draw():
    global moveX, moveY
    background(204)
    
    if (mousePressed == True):
        strokeWeight(7)
        stroke(242, 204, 47, 204)
        line(moveX, moveY, 100, 100)
    else:
        noStroke()
        fill(0)
        ellipse(moveX, moveY, 33, 33)

def mouseMoved():
    global dragX, dragY, moveX, moveY
    moveX = mouseX
    moveY = mouseY
    
