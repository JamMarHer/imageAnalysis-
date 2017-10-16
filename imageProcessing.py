import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import sys
from mpl_toolkits.mplot3d import axes3d
import matplotlib.animation  as animation
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from matplotlib import cm
#from mayavi import mlab

GREYS = 'greys/'


def main(img):
    image = Image.open(img).convert('L')
    image.save('{}grey.jpg'.format(GREYS))
    imageArray = np.array(image)
    block, imageStudy = analyze(imageArray)
    return block, imageStudy

def analyze(array):

    representing_value = []
    count_y = 0
    count_x = 0
    blocksDataHold = []
    for y_values_list in array:
        count_y += 1
    #    if count_y == 50:
    #        break
        for value in y_values_list:
            count_x += 1
            representing_value.append(value)
            blocksDataHold.append(dict({'x':count_x, 'y':count_y, 'val':value}))
        count_x = 0
    imageStudy  = {'shades': len(set(representing_value)), 'min':min(representing_value), 'max':max(representing_value)}
    return blocksDataHold, imageStudy

def postProcessing(totalBlock):
    x = []
    y = []
    z = []

    for key in totalBlock:
        x.append(key['x'])
        y.append(key['y'])
        z.append(key['val'])

    return x, y, z

# y: 600; current value.
# x: 1000; current value of the second iteration.
# z: 0 - 500; actual value of the array so basically array[y][x]

def graph(block):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Grab some test data.
    X, Y, Z = postProcessing(block)

    surf = ax.plot(X, Y, Z)
    plt.show()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print 'Please provide an image.'
        exit()

    block, imageStudy= main(sys.argv[1])
    print 'Data about image: {}'.format(imageStudy)
    graph(block)
