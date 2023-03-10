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
    

class FScoreAtK(MetricAtK):
    
    def __init__(self, K: int, beta: float = 1):
        super().__init__(K)
        self.precision = PrecisionAtK(K)
        self.recall = RecallAtK(K)
        self.beta = beta

    def calculate(self, pred: pd.Series, true: pd.Series) -> float:
        prec = self.precision.calculate(pred, true)
        rec = self.recall.calculate(pred, true)
        if (prec == 0) and (rec == 0):
            return 0.0
        return ((1 + self.beta ** 2) * prec * rec) / (self.beta ** 2 * prec + rec)


class AveragePrecisionAtK(MetricAtK):

    def calculate(self, pred: pd.Series, true: pd.Series) -> float:
        def ap(i):
            relevant = pred[i - 1] in true.values
            if not relevant:
                return 0.0
            return PrecisionAtK(i).calculate(pred[:i], true[:i])
        return np.vectorize(ap)(np.arange(1, self.K + 1)).sum() / self.K
    

class CamulativeGainAtK(MetricAtK):

    def calculate(self, pred: pd.Series, true: pd.Series) -> float:
        return (pred == true).sum()
    

class DiscountedCamulativeGainAtK(MetricAtK):

    def calculate(self, pred: pd.Series, true: pd.Series) -> float:
        def dcg(i):
            relevant = pred[i - 1] in true.values
            if not relevant:
                return 0.0
            return 1 / np.log2(i + 1)
        return sum(np.vectorize(dcg)(np.arange(1, self.K + 1)))
    

class NormalizedDiscountedCamulativeGainAtK(MetricAtK):

    def calculate(self, pred: pd.Series, true: pd.Series) -> float:
        dcg = DiscountedCamulativeGainAtK(self.K).calculate(pred, true)
        idcg = (1 / np.log2(np.arange(1, self.K + 1) + 1)).sum()
        return dcg / idcg