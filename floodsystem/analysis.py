import numpy as np
from datetime import datetime
from floodsystem.datafetcher import fetch_measure_levels
import matplotlib.dates

def polyfit(dates, levels, p):
    """given the water level time history (dates, levels) for a station computes a least-squares fit of a polynomial of 
    degree p to water level data. return a tuple of the polynomial object and any shift of the time (date) axis"""

    days = matplotlib.dates.date2num(dates)
    if days != []:
        shift = days[-1]
        for i in range(len(days)):
            days[i] -= shift

        coeff = np.polyfit(days, levels, p)
        poly = np.poly1d(coeff)
        return (poly, shift)
    else:
        return (np.poly1d([0]*p),0)

    
    
