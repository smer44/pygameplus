from PIL import Image

# Define image size
size = 30

#assert (size % 2) , f" Size must be even"
size_half = size //2
# Define maxColor (example value, you can modify it)

real_max_color = 255
maxColor = 256  # Must be a multiple of 32
maxColor = maxColor// (size+1) * size


# Calculate the color step
color_step = maxColor // size

print("Generate image of size " ,size, "with color step",color_step, "having max color",maxColor   )

# Create a new image
img = Image.new("RGB", (size, size))

# Generate pixel colors
pixels = img.load()
image_name = "ref_image1.png"
colors = set()
for y in range(size-1,-1,-1):
    #yy = [yy, size-1-yy][yy%4]
    for x in range(size):
        red = [y,y+size_half-1][y%2] * color_step
        green =[x+size_half-1,x][x%2] * color_step
        #blue = [0,y+size_half+1,x+size_half-1,maxColor,x,y][(x+y)%6] * color_step
        blue = [0, real_max_color,real_max_color//2][(x + y) % 3]
        #xx = [size_half-x,x][x<= size_half]
        #yy = [size_half-y, y][y <= size_half]
        #xx,yy = (size - x+size_half if x > size_half else x), y
        xx, yy = x,y
        #xx, yy = x + size_half + size, y + size_half + size
        #pixels[(xx + size_half + size) % size, (yy + size_half + size) % size] = (red, green, blue)
        color = (red, green, blue)
        assert color not in colors, f"{color=} already present"
        colors.add(color)
        pixels[xx % size, yy % size] = (red, green, blue)

# Save the image as a PNG file
img.save(image_name)

print("Image saved as", image_name, "generated colors :" , len(colors))
