"""Unit test for the analysis module"""
from floodsystem.stationdata import build_station_list
from floodsystem.analysis import polyfit
from datetime import datetime, timedelta
from floodsystem.datafetcher import fetch_measure_levels
import numpy as np



dates = list(range(1000, 1200))
levels = list(range(3, 203))
def test_polyfit():
        """test polyfit with levels that varies linearly with dates, to make sure that the coefficients 
        of the x squared and above terms are 0"""
        shift = dates[0]
        for i in range(len(dates)):
                dates[i] -= shift
        coeff = np.polyfit(dates, levels, 4)
        assert [round(coeff[0],5), round(coeff[1],5), round(coeff[2],5)]  == [0, 0, 0]
