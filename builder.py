import numpy as np

class IBuilder:

    def addSum(self, value):
        pass

    def addMean(self, value):
        pass

    def addMin(self, value):
        pass

    def addMax(self, value):
        pass

    def return_stats(self):
        return ''

class StatsGenerator:
    def __init__(self, data):
        self.data = data

    def stats():
        """
            Implement your builder generator method here which accepts builder object and returns stats in respective format.
        """
        pass

class StatsListBuilder:
    """
        Implements all the methods of IBuilder interface and returns the stats as a list 
    """
    def __init__(self):
        self._list = list()


class StatsJsonBuilder:
    """
        Implements all the methods of IBuilder interface and returns the stats as a json 
    """
    def __init__(self):
        self._json = {'sum' : 0.0, 'avg': 0.0, 'min': 0.0, 'max': 0.0}
