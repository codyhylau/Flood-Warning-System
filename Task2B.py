from floodsystem.stationdata import build_station_list
from floodsystem.flood import stations_level_over_threshold
from floodsystem.station import MonitoringStation

stations = build_station_list()

def run():
    """Requirements for Task 2B"""
    print(stations_level_over_threshold(stations, 0.8))
    
    

if __name__ == "__main__":
    run() 


    