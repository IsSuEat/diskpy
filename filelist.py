import os
import logging
from utils import to_percent

__author__ = 'issue'



def get_foldersize(path):
    total_size = 0
    res = []
    for root, dirs, files in os.walk(path):
        depth = root[len(path) + len(os.path.sep):].count(os.path.sep)
        # if depth  == 2:
        #    res += [os.path.join(root, d, f) for d,f in dirs,files]

        #   dirs[:] = []
        # print(res)
        for f in files:
            filepath = os.path.join(root, f)
            try:
                total_size += os.path.getsize(filepath)
            except OSError as e:
                logging.warn("File not found (maybe broken link): " + e.filename)
    return total_size


class FileList(object):
    """
    This class handles a given directory and provides information needed about it to create a chart
    """
    ignored_files = [".fscache", ".directory"]
    ignored_folders = ["/dev", "/proc", "/run", "/media", "/sys"]

    def __init__(self, directory):
        self.directory = directory
        self.filecount = 0
        self.data = self.get_files_and_size()
        logging.info("Done scanning files")

        self.filesize_percentage = to_percent(self.data)
        self.reprdata = self.group_small_files()

        print("fl init")

    def get_files_and_size(self):
        """
        generates a list of files and folders in a directory with file sizes passed as tuples
        """
        s = []

        for item in os.listdir(self.directory):
            if os.path.isfile(os.path.join(self.directory, item)):
                if any(os.path.basename(os.path.join(self.directory, item)) in ignored for ignored in
                       self.ignored_files):
                    pass
                else:
                    s.append(self.get_filesize(item))
            else:  # we hit a dir
                if any(item in ignored for ignored in self.ignored_folders):

                    pass
                else:
                    s.append(tuple([item, get_foldersize(os.path.join(self.directory, item))]))



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

        return file, filesize

    def group_small_files(self):
        """
        if a file is smaller than 1 percent of the current total, we add it to a group of misc files and return the new
        data with the files grouped up
        """
        misc = [(k, v) for k, v in self.filesize_percentage if v < 1]
        newdata = [(k, v) for k, v in self.filesize_percentage if (k, v) not in misc]
        newdata.append(("misc", float(sum(v for _, v in misc))))
        return newdata

    def prepare_data(self):
        pass



#fl = FileList("/home/issue/tmp")

#print(get_foldersize("/home/issue/tmp"))
        #print(fl.data)
        #print(fl.group_small_files())
