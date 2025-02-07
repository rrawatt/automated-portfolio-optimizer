# utilities.py
import numpy as np

class UtilityMixin:
    @staticmethod
    def calculate_turnover(old_weights, new_weights):
        """Calculate portfolio turnover between two weight vectors."""
        return np.sum(np.abs(new_weights - old_weights)) / 2
