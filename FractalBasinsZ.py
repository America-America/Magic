
#this will implement the newton's method to output the fractal basins of attraction figure.
from PIL import Image

# you can change the function here
def p(z):

    return (z ** 4) -1

# Please change the derivative of the function here 
def dp(z):

    return 4 * (z ** 3)


def n_method(f, fd, z):
    for i in range(45):
        zn = z - f(z) / fd(z)
        absol(f(z))
        if abs(zn - z) < 10e-4:
            return z
        z = zn
    pass

def absol(m):
    if abs(m) > 10e20:  # change these as necessary
        return None
    if abs(m) < 10e-14:
        return None

xmin = -1.0
xmax = 1.0
ymin = -1.0
ymax = 1.0

# add more colors if necessary
colors = [(51, 153, 255),(204, 102, 255),(204, 255, 153),(255, 0, 102)]

def plot(f, fd, img, img_size, name):
    results = []
    for y in range(img_size):
        z_y = y * (ymax - ymin) / (img_size - 1) + ymin
        for x in range(img_size):
            z_x = x * (xmax - xmin) / (img_size - 1) + xmin
            result = n_method(f, fd, complex(z_x, z_y))
            if result:
                flag = False
                for test_root in results:
                    e = 10e-3
                    if abs(test_root - result) < e:
                        result = test_root
                        flag = True
                        break
                if not flag:
                    results.append(result)
            if result:
                img.putpixel((x, y), colors[results.index(result)])
    print(results)
    img.save(name, "PNG")

f = lambda z: p(z)
fd = lambda z: dp(z)
plot(f, fd, Image.new("RGB", (1024, 1024), (255, 255, 255)), 1024, "z4minus1.png")