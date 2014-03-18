__author__ = 'issue'
import matplotlib.pyplot as plt
#todo draw on qt gui

class Chart:

    def __init__(self, data):
        self.data = data
        print("chart init")


    def create_pie(self):
        """
        expects data in key value format, value should be percentage
        """

        plt.axis("equal")
        plt.pie(
            x=[v for k, v in self.data],
            labels=[k for k,v in self.data],
            autopct="%1.1f%%"
        )
        plt.show()