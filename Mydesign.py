def circle(t,num_of_sides,dist,angle,radius):
  for times in range(num_of_sides):
      t.forward(dist)
      t.right(angle)
      t.circle(radius)
      
def shape(t,num_of_sides,dist,angle,radius):
    for times in range(num_of_sides):
        t.forward(dist)
        t.right(angle)
        t.circle(radius)
"""
def design(t,num_of_sides,dist,angle,radius):
    t.penup()
    t.left(88)
    t.forward(550)
    t.left(58)
    t.pendown()
    t.forward(25)
    t.right(8)
    t.circle(100)  
    for times in range(50):
            t.forward(dist)
            t.left(angle)
            t.circle(radius)

def mine(t,num_of sides
"""
