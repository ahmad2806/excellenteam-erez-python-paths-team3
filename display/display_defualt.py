import display.display as display
from pylab import *
from configrations import image_path


class DisplayDefualt(display.Display):

    def __init__(self):
        pass

    def display(self, pathes, objs):
        print("in display defualt")
        bg = imread(image_path)
        imshow(bg)
        # print(pathes)
        # print(objs)
        # sample_objs = objs[objs > 50].sample(100)

        for t, n in objs.iteritems():
            o = pathes.loc[t]
            plt.plot(o.x, o.y, label=n)
        show()
        pass
