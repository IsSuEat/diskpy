__author__ = 'issue'
import argparse
from chart import Chart
from filelist import FileList
from utils import to_percent


parser = argparse.ArgumentParser(description="Display filesystem usage as pie chart")
parser.add_argument('directory', help="directory to create chart for")
args = parser.parse_args()


fl = FileList(args.directory)
piechart = Chart(fl.reprdata)
piechart.create_pie()

