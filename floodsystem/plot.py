import matplotlib.pyplot as plt
import matplotlib
from .station import MonitoringStation
from .analysis import polyfit
import numpy as np
from .flood import stations_highest_rel_level
from .datafetcher import fetch_measure_levels
from datetime import timedelta

def plot_water_levels(station, dates, levels):
    """plot graphs of relative water level against dates"""
    time = dates
    plt.plot(time, levels,label='water level')
    high = [station.typical_range[1]] * len(time)
    low = [station.typical_range[0]] * len(time)

    plt.plot(time, low, label='low')
    plt.plot(time, high,label='high')
    # Add axis labels, rotate date labels and add plot title
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45)
    plt.title(station.name)
    plt.legend(loc = 'upper right')

    # Display plot
    plt.tight_layout()

    plt.show()

def plot_water_level_with_fit(station, dates, levels, p):
    """plot graphs of relative water level against dates, with least-squares polynomial curve"""
    time = dates
    plt.plot(time, levels, label = 'water level')
    high = [station.typical_range[1]] * len(time)
    low = [station.typical_range[0]] * len(time)

    plt.plot(time, low, label='low')
    plt.plot(time, high, label = 'high')


    #polynomial
    days = matplotlib.dates.date2num(dates)
    days_list = np.asarray(days)
    poly,shift = polyfit(dates, levels, p)
    plt.plot(time, poly(days_list-shift), label = 'polynomial')

    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45)
    plt.title(station.name)
    plt.legend(loc = 'upper right')

    plt.tight_layout()

    plt.show()

def plot_town(all_stations, dt):
    townname = input()
    towns = []
    for items in all_stations:
        if items.town == townname:
            towns.append(items)
    top_town = stations_highest_rel_level(towns, N=1)
    if top_town == []:
        print("please enter a valid town name, with first letter capital")
        plot_town(all_stations,dt)

    else:
        for items in all_stations:       
            if items.name == top_town[0][0]:
                name1 = items
                break
        time, levels = fetch_measure_levels(name1.measure_id,dt=timedelta(days=dt))
        plot_water_level_with_fit(name1, time, levels,4)