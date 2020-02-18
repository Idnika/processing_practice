angle = 0.0

def setup():
    size(100, 100)
    noStroke()
    
def draw():
    global angle
    
    background(0)
    
    fill(204)
    rect(0, 44, 100, 12)
    
    translate(width/2, height/2)
    scale(0.75)
    rotate(angle)
    
    fill(102)
    beginShape()
    vertex(-25, -50)
    vertex(25, -50)
    vertex(25, 50)
    vertex(-25, 50)
    
    beginContour()
    vertex(-15, -30)
    vertex(-15, -10)
    vertex(15, -10)
    vertex(15, -30)
    endContour()
    
    beginContour()
    vertex(-15, 10)
    vertex(-15, 30)
    vertex(15, 30)
    vertex(15, 10)
    endContour()
    
    endShape()
    
    angle += 0.01
