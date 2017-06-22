from abc import ABC, abstractmethod

'''
Base class for all simulation types (sim, paper, trade)
'''


class Bot(ABC):

    def __init__(self, args):
        super(Bot, self).__init__()
        self.args = args


    @abstractmethod
    def get_next(interval):
        pass
