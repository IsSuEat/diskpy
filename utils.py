__author__ = 'issue'


def to_percent(data):
    """
    takes any key value data and outputs same data with value as percent
    """
    total = float(sum(v for _, v in data))
    data[:] = [(k, (v / total) * 100.0) for k, v in data]
    return data


def set_color(data):
    """
    iterates over the data; set a color for a k,v pair according to v size

    """
    for item in data:
        if item[1] > 33:  # item is a third of the total size color it red
            item += ('red',)
            print(item)

        pass

