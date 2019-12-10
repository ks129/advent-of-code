#Importing modules
from PIL import Image

#Getting input
print('Insert your puzzle input:')
inp = input()

#Part 1 generator
def run1(d):
    picture = list(d)
    img = picture[:25*6]
    f = 100000000000000000000
    res = 0
    while picture:
        l = picture[:25*6]
        picture = picture[25*6:]
        size = l.count('0')
        if size < f:
            f = size
            res = l.count('1') * l.count('2')
    return res

#Part 2 Generator
def run2(d):
#Defining vars
    layers = []
    width = 25
    height = 6
    
    #Creating image
    image = Image.new("RGB", (width + 1, height + 1), color='black')
    #Loading pixels
    pixels = image.load()
    
    #Generating layers
    while len(d):
        layer = []
  
        #Generating rows
        for i in range(height):
            r = []
            for g in d[:width]:
                r.append(g)
            d = d[width:]
            layer.append(r)
        #Appending layers list
        layers.append(layer)

    #Defining img as top layer
    img = layers[0]

    #Checking is top layer pixels tranparent. If yes, try to find first layer that have this pixel not transparent
    for l in layers[1:]:
        for y in range(height):
            for x in range(width):
                if img[y][x] == "2":
                    if l[y][x] != "2":
                        img[y][x] = l[y][x]

    #Defining x, y
    x, y = 0, 0
    
    #Modifying pixels color
    for line in img:
        y += 1
        x = 0
        for i in line:
            x += 1
            if i == "0":
                pixels[x, y] = (0, 0, 0)
            elif i == "1":
                pixels[x, y] = (255, 255, 255)
                
    #Saving image
    image.save('output.png', "PNG")
                      
    #Return text
    printline = "Output saved to output.png"
    return printline
    

#Running generators and storage outputs to vars
p1 = run1(inp)
p2 = run2(inp)

#Printing output
print(f'Part 1 Result is {p1}')
print(f'Part 2 Result is:\n{p2}')
