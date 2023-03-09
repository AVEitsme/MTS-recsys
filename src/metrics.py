import pandas as pd
import numpy as np

from abc import ABC, abstractmethod


class MetricAtK(ABC):
    """Represents abstract base class to calculate metric's at k."""
    def __init__(self, K: int):
        """
        Args:
            K (int): Count of recommendations.
        """
        self.K = K

    @abstractmethod
    def calculate(self, pred: pd.Series, true: pd.Series) -> float:
        """Represents method to calculate metric at k.

        Args:
            pred (pd.Series): Predicted items.
            true (pd.Series): Real items.

        Returns:
            float: Returns value of calculated metric.
        """


class PrecisionAtK(MetricAtK):
    
    def calculate(self, pred: pd.Series, true: pd.Series) -> float:
        return len(np.intersect1d(pred, true)) / self.K


class RecallAtK(MetricAtK):
    
    def calculate(self, pred: pd.Series, true: pd.Series) -> float:
        if len(true) == 0:
            return 0.0
        return len(np.intersect1d(pred, true)) / len(true)
    

class FOneScoreAtK(MetricAtK):
    
    def __init__(self, K: int):
        super().__init__(K)
        self.precision = PrecisionAtK(K)
        self.recall = RecallAtK(K)

    def calculate(self, pred: pd.Series, true: pd.Series) -> float:
        prec = self.precision.calculate(pred, true)
        rec = self.recall.calculate(pred, true)
        if (prec == 0) and (rec == 0):
            return 0.0
        return (2 * prec * rec) / (prec + rec)


class AveragePrecision(MetricAtK):

    def calculate(self, pred: pd.Series, true: pd.Series) -> float:
        def ap(i):
            relevant = pred[i - 1] in true.values
            if not relevant:
                return 0.0
            return PrecisionAtK(i).calculate(pred[:i], true[:i])
        return np.vectorize(ap)(np.arange(1, self.K + 1)).sum() / self.K