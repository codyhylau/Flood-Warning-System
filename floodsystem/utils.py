# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains utility functions.

"""


def sorted_by_key(x, i, reverse=False):
    """sort by key"""
    # Sort by distance
    def key(element):
        return element[i]

    return sorted(x, key=key, reverse=reverse)

from math import radians, cos, sin, asin, sqrt
def haversine(a, b):
    """Calculate the distance between two points 
    on the earth in km """
    # convert decimal degrees to radians 
    lon1, lat1, lon2, lat2 = map(radians, [a[0], a[1], b[0], b[1]])

    # haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    r = 6371 # Radius of earth in kilometers. Use 3956 for miles
    return c * r

def rate(dydx):
    if dydx > 0:
        return 'rising'
    elif dydx == 0:
        return 'N/A'
    else:
        return 'falling'
