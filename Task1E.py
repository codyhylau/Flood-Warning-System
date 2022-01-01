from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_by_station_number

def run():
    """Requirements for Task 1E"""

    stations = build_station_list()
    print(rivers_by_station_number(stations,6))

if __name__ == "__main__":
    run()