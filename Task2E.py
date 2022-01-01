from floodsystem.plot import plot_water_levels
from floodsystem.stationdata import build_station_list
from floodsystem.station import MonitoringStation
from datetime import datetime, timedelta
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.flood import stations_highest_rel_level

stations = build_station_list()

def run():
    top_stations = stations_highest_rel_level(stations, 5)
    for i in range (5):

        station = top_stations[i][0]
        for items in stations:
                if items.name == station:
                        plot_station = items
        dt = 10
        time, levels = fetch_measure_levels(plot_station.measure_id,
                                     dt=timedelta(days=dt))
        print(plot_water_levels(plot_station, time, levels))

    
    

if __name__ == "__main__":
    run() 