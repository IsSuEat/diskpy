import os
import sys

__author__ = 'issue'
import argparse
from chart import Chart
from filelist import FileList
from utils import to_percent


parser = argparse.ArgumentParser(description="Display filesystem usage as pie chart")
parser.add_argument('directory', help="directory to create chart for")
args = parser.parse_args()

if not os.path.isdir(args.directory):
    print("not a valid directory")
    sys.exit(1)
else:

    fl = FileList(args.directory)
    piechart = Chart(fl.reprdata)
    piechart.create_pie()

