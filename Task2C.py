from floodsystem.stationdata import build_station_list
from floodsystem.flood import stations_highest_rel_level
from floodsystem.station import MonitoringStation

stations = build_station_list()

def run():
    """Requirements for Task 2C"""
    print(stations_highest_rel_level(stations, 10))
    
    

if __name__ == "__main__":
    run() 
