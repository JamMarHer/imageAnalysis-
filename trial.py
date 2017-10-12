import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import sys
from mpl_toolkits.mplot3d import axes3d
import matplotlib.animation  as animation
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from matplotlib import cm
#from mayavi import mlab


def main(img):
    image = Image.open(img).convert('L')
    image.save('grey.jpg')
    imageArray = np.array(image)
    block = analyze(imageArray)
    return block

def analyze(array):
    y_values = []
    x_values = []
    representing_value = []
    count_y = 0
    count_x = 0
    blocksDataHold = []
    for y_values_list in array:
        y_values.append(count_y)
        count_y += 1
        if count_y == 50:
            break
        for value in y_values_list:
            x_values.append(count_x)
            count_x += 1
            representing_value.append(value)
            blocksDataHold.append(dict({'x':count_x, 'y':count_y, 'val':value}))
        count_x = 0

    return blocksDataHold

def postProcessing(totalBlock):
    x = []
    y = []
    z = []

    for key in totalBlock:
        x.append(key['x'])
        y.append(key['y'])
        z.append(key['val'])

    return x, y, z

def report(blocks):
    for key in blocks:
        print 'ID: {}. Average: {}. Min: {}. Max: {}. Length: {}'.format(key, blocks[key]['avg'],\
            blocks[key]['min'], blocks[key]['max'], blocks[key]['len'])


# y: 600; current value.
# x: 1000; current value of the second iteration.
# z: 0 - 500; actual value of the array so basically array[y][x]

def graph(block):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Grab some test data.
    X, Y, Z = postProcessing(block)
    X, Y = np.meshgrid(X, Y)

    # Plot a basic wireframe.
    ax.set_zlim(0, 350)
    ax.zaxis.set_major_locator(LinearLocator(10))
    ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
    surf = ax.plot_surface(X, Y, Z,color='b', cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)
    fig.colorbar(surf, shrink=0.5, aspect=5)
    plt.show()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print 'Please provide an image.'
        exit()

    block = main(sys.argv[1])
    graph(block)
