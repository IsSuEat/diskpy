__author__ = 'issue'
import os
import sys
import argparse
import random
from filelist import FileList
from PyQt4 import QtGui
from gui import MainWindow

color_list = ['red', 'blue', 'green', 'yellow', 'black', 'magenta', "white"]

parser = argparse.ArgumentParser(description="Display filesystem usage as pie chart")
parser.add_argument('directory', help="directory to create chart for")
parser.add_argument('-gui', action="store_true", help="draw a qt4 gui instead of matplot")
args = parser.parse_args()

if not os.path.isdir(args.directory):
    print("not a valid directory")
    sys.exit(1)
else:
    fl = FileList(args.directory)  # initialize filelist for directory
    with open("data.txt", "w") as f:  # temp hackaround for gui
        text = ""
        for item in fl.reprdata:
            text += item[0] + "," + str(item[1]) + "," + random.choice(color_list) + "\n"

        f.write(str(text))

    if args.gui:

        app = QtGui.QApplication(sys.argv)
        window = MainWindow()
        window.show()
        sys.exit(app.exec_())

    else:
        try:
            from chart import Chart
        except ImportError:
            print("matplotlib not installed")
            sys.exit(1)

        piechart = Chart(fl.reprdata)
        piechart.create_pie()

