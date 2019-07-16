canvas_x = 600
canvas_y = 600
rectangle_count = 3
rectangle_height = 70
rectangle_width = canvas_x / rectangle_count
print(rectangle_width)


def setup(): #Runs once
    size(600, 600)
    background(255, 255, 255)
     # Add the 3 rectangles at the top of Paint
    rect(0, 0, rectangle_width, rectangle_height)
    #Color 1
    fill(204, 20, 72)
    rect(rectangle_width, 0, rectangle_width, rectangle_height)
    #Color 2
    fill(20, 204, 149)
    rect(2*rectangle_width, 0, rectangle_width, rectangle_height)
    noStroke()
    
    
def draw(): #Runs over and over
    if keyPressed and key == 'c':
        background(255, 255, 255) #Clear the canvas  
        #Add the 3 rectsngles at the top of paint                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
    if mousePressed and mouseY > rectangle_height + 50:
       # fill(216, 191, 216) #Thistle
        ellipse(mouseX, mouseY, 100, 100) #Draw with the pen
    # Purple box (box 2) is at Top Left: 200, 0 Top Right: 400, 0 Bottom Left: 200, 70 Bottom Right: 400, 70
    #200-400 in X
    #0-70 in Y
    if (mouseX > rectangle_width and mouseX < rectangle_width*2 and mouseY < rectangle_height):
        print("in box 2")
        fill(204, 20, 72)
    elif (mouseX > rectangle_width*2 and mouseX < rectangle_width*3 and mouseY < rectangle_height):
        print("in box 3")
        fill(20, 204, 149)
    else:
        print("")
       
