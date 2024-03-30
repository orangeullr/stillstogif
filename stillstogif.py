import glob
import sys
import os
import imageio.v2 as imageio
from progress.bar import Bar


def printHelp():
    help = '''
      stilltogif.py is a python script to convert a series of images into one GIF image.
      To use this python script, please use the following format:
      
      stillstogif.py <gif> <duration in ms> <still image directory>
      
      Example:
        stillstogif mygif.gif ./stills_directory
    '''
    print(help)
               
def make_gif(frame_folder,filename,dur):
    try:
        with imageio.get_writer(filename, mode='I', duration=dur,  palettesize=32, quantizer='nq') as writer:
            filenames = os.listdir(frame_folder)
            length = len(filenames)
            with Bar('Processing', max=length) as bar:
                for filename in filenames:
                    bar.next()
                    image = imageio.imread(frame_folder + "/" + filename)
                    writer.append_data(image)
            print("Images have been processed. Please wait...")
    except Exception as e:
        print(e)
        sys.exit(1)
        
if __name__ == "__main__":
    if(len(sys.argv) != 4):
        printHelp()
        print(sys.argv)
        sys.exit(1)
    try:
        filename=str(sys.argv[1])
        duration = float(sys.argv[2])
        frame_folder = str(sys.argv[3])
        if(os.path.isdir(sys.argv[3]) and  duration > 0):
            make_gif(frame_folder,filename,duration)
            sys.exit(0)
        else:
            printHelp()
            sys.exit(1)
    except IOError:
        printHelp()
        print(sys.argv)
        sys.exit(1)