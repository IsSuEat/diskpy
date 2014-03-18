__author__ = 'issue'

def to_percent(data):
    """
    takes any key value data and outputs same data with value as percent
    """
    total = float(sum(v for _, v in data))
    data[:] = [(k, (v / total)*100.0) for k, v in data]
    return data
