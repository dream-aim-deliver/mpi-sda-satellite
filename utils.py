"""utils

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1aguoynCs-cJ81RbK8ycpbPz8pakIUvc-
"""

from typing import Any, Optional, Tuple
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime, timedelta


def plot_image(
    image: np.ndarray, factor: float = 1.0, clip_range: Optional[Tuple[float, float]] = None, **kwargs: Any
) -> None:
    """Utility function for plotting RGB images."""
    fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(15, 15))
    if clip_range is not None:
        ax.imshow(np.clip(image * factor, *clip_range), **kwargs)
    else:
        ax.imshow(image * factor, **kwargs)
    ax.set_xticks([])
    ax.set_yticks([])
    plt.gca().set_axis_off()
    ax.set_frame_on(False)


def save_image(
    image: np.ndarray, filename: str, factor: float = 1.0, clip_range: Optional[Tuple[float, float]] = None, **kwargs: Any
) -> None:
    """Utility function for saving RGB images to a file."""
    fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(15, 15))
    if clip_range is not None:
        ax.imshow(np.clip(image * factor, *clip_range), **kwargs)
    else:
        ax.imshow(image * factor, **kwargs)
    ax.set_xticks([])
    ax.set_yticks([])
    plt.gca().set_axis_off()
    plt.margins(0,0)
    plt.savefig(filename, bbox_inches="tight",pad_inches = 0)
    plt.close()




def date_range(start_date, end_date):
    start_date = datetime.strptime(start_date, "%Y-%m-%d")
    end_date = datetime.strptime(end_date, "%Y-%m-%d")
    
    date_list = [((start_date + timedelta(days=x)).strftime("%Y-%m-%d"),
                  (start_date + timedelta(days=x+1)).strftime("%Y-%m-%d"))
                 for x in range((end_date-start_date).days + 1)]
    return date_list

