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
        return len(set(pred) & set(true)) / self.K


class RecallAtK(MetricAtK):
    def calculate(self, pred: pd.Series, true: pd.Series) -> float:
        return len(set(pred) & set(true)) / len(true) if len(true) != 0 else 0.0
    

class FOneScoreAtK(MetricAtK):
    def __init__(self, K: int):
        super().__init__(K)
        self.precision = PrecisionAtK(K)
        self.recall = RecallAtK(K)

    def calculate(self, pred: pd.Series, true: pd.Series) -> float:
        prec = self.precision.calculate(pred, true)
        rec = self.recall.calculate(pred, true)
        return (2 * prec * rec) / (prec + rec) if prec != 0 or rec != 0 else 0.0
