# utilities.py
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