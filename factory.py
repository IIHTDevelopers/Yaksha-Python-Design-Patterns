from abc import ABC
from abc import abstractmethod


class Investment(ABC):

    @abstractmethod
    def lockin_period(self):
        pass

    @abstractmethod
    def interest_rate(self):
        pass

class PF(Investment):
    """
    Implement PF class which inherits class Investment and implements lockin_period(return 5) and interest_rate(return 5.5)
    """
    pass

class PPF(Investment):
    """
    Implement PPF class which inherits class Investment and implements lockin_period(return 15) and interest_rate(return 8)
    """
    pass

class ELSS(Investment):
    """
    Implement ELSS class which inherits class Investment and implements lockin_period(return 3) and interest_rate(return 10)
    """
    pass
    
def SavingsFactory(scheme):
    """
        Define Factory method that accepts a scheme, in this case ("pf", "ppf", "elss") and returns respective object
    """
    pass

