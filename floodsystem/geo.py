# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from floodsystem.utils import sorted_by_key, haversine
from floodsystem.station import MonitoringStation


def stations_by_distance(stationclass, p):
    """for Task1B, to  return a list of (station, distance) tuples"""

    list_1b=[]
    for i in range(len(stationclass)):
        list_1b.append((stationclass[i].name, stationclass[i].town, haversine(stationclass[i].coord, p)))
    list_1b_sorted=sorted_by_key(list_1b,2)
    return list_1b_sorted


def stations_within_radius(stationclass, centre, r):
    """for Task1C, to return a list of stations within radius r of coordinate centre"""

    list_1c = []
    for i in range(len(stationclass)):
        distance = haversine(centre, stationclass[i].coord )
        if distance < r:
            list_1c.append(stationclass[i].town)
    return list_1c

def rivers_with_station(stations):
    """for Task1D, to return a set of river names for given stations (no dublicates)"""
    list_1d=[]
    for i in range(len(stations)):
        if stations[i].river not in list_1d:
            list_1d.append(stations[i].river)
        else:
            pass       
    return list_1d

def stations_by_river(stations):
    """for Task1D, to return a dictionary that maps rivers to stations"""
    dict_1d={}
    for i in range(len(stations)):
        if stations[i].river in dict_1d:
            dict_1d[stations[i].river].append(stations[i].name)
        else:
            dict_1d[stations[i].river]=[]
            dict_1d[stations[i].river].append(stations[i].name)
    return dict_1d

def rivers_by_station_number(stations, N):
    """for Task1E, to return a list of tuples of river name and corresponding number of stations"""
    dict_1e={}
    for i in range(len(stations)):
        if stations[i].river in dict_1e:
            dict_1e[stations[i].river]+=1
        else:
            dict_1e[stations[i].river]=1
    list_1e=[]
    for j,k in dict_1e.items():
        list_1e.append((j,k))
    list_1e_sorted=sorted_by_key(list_1e,1,True)
    
    list_1e_final=[]
    m=0
    for n in range(len(list_1e_sorted)):
        if m<N:
            list_1e_final.append(list_1e_sorted[n])
            m+=1
        elif list_1e_sorted[n][1]==list_1e_sorted[n-1][1]:
            list_1e_final.append(list_1e_sorted[n])
        else:
            break
    return list_1e_final