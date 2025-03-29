"""
Module: utilities.py

Purpose:
    Provides utility functions and mixins that support various operations across the codebase,
    including the calculation of portfolio turnover and saving Plotly figures as images.

Classes and Functions:
    UtilityMixin:
        Methods:
            - calculate_turnover(old_weights, new_weights):
                  Computes the turnover between two sets of portfolio weights by calculating the half-sum of the absolute differences.
    save_fig(fig, filepath):
        Attempts to save a Plotly figure to an image file using Kaleido. If the primary method fails,
        it falls back to an alternative method to save the image, and prints messages indicating success or failure.
"""

import numpy as np

class UtilityMixin:
    @staticmethod
    def calculate_turnover(old_weights, new_weights):
        """Calculate portfolio turnover between two weight vectors."""
        return np.sum(np.abs(new_weights - old_weights)) / 2
    
def save_fig(fig, filepath):
    """
    Attempts to save a Plotly figure to an image file using Kaleido.
    If fig.write_image() fails, it falls back to using fig.to_image().
    """
    try:
        fig.write_image(filepath, engine="kaleido")
        print(f"Saved figure to {filepath} using write_image().")
    except Exception as e:
        print(f"write_image() failed for {filepath}: {e}")
        try:
            # Fallback: use to_image() to get image bytes and write manually
            img_bytes = fig.to_image(format="png", engine="kaleido")
            with open(filepath, "wb") as f:
                f.write(img_bytes)
            print(f"Saved figure to {filepath} using to_image() fallback.")
        except Exception as e:
            print(f"Fallback failed for {filepath}: {e}")