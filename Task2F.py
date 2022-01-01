from floodsystem.stationdata import build_station_list
from floodsystem.plot import plot_water_level_with_fit
from floodsystem.datafetcher import fetch_measure_levels
from datetime import datetime, timedelta
from floodsystem.flood import stations_highest_rel_level
from floodsystem.station import MonitoringStation

stations = build_station_list()

def run():
    """Requirements for Task 2F"""
    top_stations = stations_highest_rel_level(stations, 5)
    for i in range (5):

        station = top_stations[i][0]
        for items in stations:
                if items.name == station:
                    plot_station = items
        dt = 2
        time, levels = fetch_measure_levels(plot_station.measure_id,dt=timedelta(days=dt))

        plot_water_level_with_fit(plot_station, time, levels,4)
    

if __name__ == "__main__":
    run() 
