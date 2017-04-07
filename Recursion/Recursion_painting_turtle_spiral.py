import turtle

def makeSpiral(lineLength,t):
    if lineLength>0:
        t.forward(lineLength)
        t.right(90)
        makeSpiral(lineLength-5,t)



t=turtle.Turtle()
makeSpiral(75,t)
