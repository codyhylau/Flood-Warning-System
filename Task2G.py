from floodsystem import geo
from floodsystem.stationdata import build_station_list
from floodsystem.analysis import polyfit
from floodsystem.datafetcher import fetch_measure_levels
from datetime import datetime, timedelta
from floodsystem.flood import stations_highest_rel_level, stations_level_over_threshold, get_relative
from floodsystem.station import MonitoringStation
import numpy as np
import matplotlib.dates
from floodsystem.utils import sorted_by_key, rate
from floodsystem.plot import plot_water_level_with_fit, plot_town


def run():
    """Requirement for Task2G"""
    all_stations = build_station_list()

    n = 50 #number of stations to fetch data from
    dt = 4 #days to go back
    r = 5 #distance for surrounding towns
    top_stations = stations_highest_rel_level(all_stations, N=n)
    list1 = []
    for i in range (n):

        if all_stations[i].typical_range_consistent == False:
            pass
        
        station = top_stations[i][0]
        for items in all_stations:
                if items.name == station:
                    name = items
                    break

        next_day = matplotlib.dates.date2num(datetime.now()) + 1 
        time, levels = fetch_measure_levels(name.measure_id,dt=timedelta(days=dt))
        poly, shift = polyfit(time, levels, 4)
        dydx2 = np.polyder(poly,2)
        list1.append((name, round(get_relative(name,poly(next_day-shift)),3), dydx2(next_day-shift)))

    list2=sorted_by_key(list1, 2, reverse=True)

    severe,severe1,high,high1,moderate,moderate1,low,low1,dict1 = [],[],[],[],[],[],[],[],{}

    for i in range(len(list2)):
        radius_list = geo.stations_within_radius(all_stations, list2[i][0].coord, r)
        if list2[i][1] >= 2: 
            if list2[i][0].town not in dict1:
                dict1[list2[i][0].town] = [4,list2[i][1],list2[i][2]]
            elif dict1[list2[i][0].town][0] < 4:
                dict1[list2[i][0].town] = [4,list2[i][1],list2[i][2]]
            for stations in radius_list:
                if stations not in dict1 and stations not in severe1:
                    severe1.append(stations)
        elif list2[i][1] >= 1.6: 
            if list2[i][0].town not in dict1:
                dict1[list2[i][0].town] = [3,list2[i][1],list2[i][2]]
            elif dict1[list2[i][0].town][0] < 3:
                dict1[list2[i][0].town] = [3,list2[i][1],list2[i][2]]
            for stations in radius_list:
                if stations not in dict1 and stations not in high1:
                    high1.append(stations)
        elif list2[i][1] >= 1.2:
            if list2[i][0].town not in dict1:
                dict1[list2[i][0].town] = [2,list2[i][1],list2[i][2]]
            elif dict1[list2[i][0].town][0] < 2:
                dict1[list2[i][0].town] = [2,list2[i][1],list2[i][2]]
            for stations in radius_list:
                if stations not in dict1 and stations not in moderate1:
                    moderate1.append(stations)
        elif list2[i][1] >= 0.8:
            if list2[i][0].town not in dict1:
                dict1[list2[i][0].town] = [1,list2[i][1],list2[i][2]]
            elif dict1[list2[i][0].town][0] < 1:
                dict1[list2[i][0].town] = [1,list2[i][1],list2[i][2]]
            for stations in radius_list:
                if stations not in dict1 and stations not in low1:
                    low1.append(stations)

    for town, levels in dict1.items():
        if levels[0] == 4:
            severe.append((town, levels[1], levels[2]))
        if levels[0] == 3:
            high.append((town, levels[1], levels[2]))
        if levels[0] == 2:
            moderate.append((town, levels[1], levels[2]))
        if levels[0] == 1:
            low.append((town, levels[1], levels[2]))
    print('')
    print("Town......relative level...rate of change of gradient")
    print('')
    print("***SEVERE***:")
    for i in range(len(severe)):
        print(severe[i][0], severe[i][1], rate(severe[i][2]))
    print('surrounding towns:')
    print(severe1)
    print('')
    print("***HIGH***:")
    for i in range(len(high)):
        print(high[i][0], high[i][1], rate(high[i][2]))
    print('surrounding towns:')
    print(high1)
    print('')
    print("***MODERATE***:")
    for i in range(len(moderate)):
        print(moderate[i][0], moderate[i][1], rate(moderate[i][2]))
    print('surrounding towns:')
    print(moderate1)
    print('')
    print("***LOW***:")
    for i in range(len(low)):
        print(low[i][0], low[i][1], rate(low[i][2]))
    print('surrounding towns:')
    print(low1)

    print('')
    print('')
    print('To see a time-water level graph, type in the town name')
    
    plot_town(all_stations, dt)
            
            
if __name__ == "__main__":
    run() 