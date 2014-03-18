__author__ = 'issue'
import os
import matplotlib.pyplot as plt
import argparse

parser = argparse.ArgumentParser(description="Display filesystem usage as pie chart")
parser.add_argument('directory', help="directory to create chart for")
args = parser.parse_args()


def gettotalsize(path):
    """
    walk all files, stat their size and add the sizes
    returns size of a folder in bytes
    """
    total_size = 0
    for root, dirs, files in os.walk(path):
        for f in files:
            filepath = os.path.join(root, f)
            total_size += os.path.getsize(filepath)
    return total_size


def getfilesize(file):
    filepath = os.path.join(args.directory, file)
    filesize = os.path.getsize(filepath)
    return filepath, filesize


def createnameandsize():
    """
    returns a list with tuples of fully qualified path and filesize in bytes
    """
    s = []
    for root, dirs, filenames in os.walk(args.directory):
        for f in filenames:
            #print(getfilesize(f))
            s.append(getfilesize(f))
    return s


def to_percent(data):
    """
    takes any key value data and outputs same data with value as percent
    """
    total = float(sum(v for _, v in data))
    data[:] = [(k, (v / total)*100.0) for k, v in data]
    return data



def create_pie(data):

    #print(percentages)
    plt.axis("equal")
    plt.pie(
        x=[v for k, v in data],
        labels=[k for k,v in data],
        autopct="%1.1f%%"
    )
    plt.show()

#testing
stuff = createnameandsize()
create_pie(to_percent(stuff))
#print(to_percent(stuff))
#print(createnameandsize())
#print(gettotalsize(args.directory))
#print(str(getfilesize("out.pdf")[0]) + " is " + str(getfilesize("out.pdf")[1]))
