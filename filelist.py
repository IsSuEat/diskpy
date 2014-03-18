import os
from utils import to_percent
__author__ = 'issue'
#todo think about including folder sizes

class FileList:
    """
    This class handles a given directory and provides information needed about it to create a chart
    """
    def __init__(self, directory):
        self.directory = directory
        self.data = self.get_files_and_size()
        self.filesize_percentage = to_percent(self.data)
        self.reprdata = self.group_small_files()

        print("fl init")
        #print(self.filedata)

    def get_files_and_size(self):
        """
        generates a list of files in a directory with file sizes passed as tuples
        """
        s = []
        for item in os.listdir(self.directory):
            if os.path.isfile(os.path.join(self.directory, item)):
                s.append(self.get_filesize(item))
        return s

    def get_filesize(self, file):
        """
        returns the size of a file in directory in bytes
        """
        filepath = os.path.join(self.directory, file)
        try:
            filesize = os.path.getsize(filepath)
        except OSError as e:
            print(e)

        return filepath, filesize

    def group_small_files(self):
        """
        if a file is smaller than 1 percent of the current total, we add it to a group of misc files and return the new
        data with the files grouped up
        """
        misc = [(k, v) for k, v in self.filesize_percentage if v < 1]
        #print(misc)
        newdata = [(k, v) for k, v in self.filesize_percentage if (k, v) not in misc]
        newdata.append(("misc", float(sum(v for _, v in misc))))
        #print(newdata)
        return newdata

#fl = FileList("/home/issue/tmp")
#print(fl.get_filesize("out.pdf"))
#print(fl.data)
#print(fl.group_small_files())