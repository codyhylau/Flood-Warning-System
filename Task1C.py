from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_within_radius
def run():
    """Requirements for Task 1C"""

      # Build list of stations
    stations = build_station_list()
    print(stations_within_radius(stations, (52.2053, 0.1218), 10))

if __name__ == "__main__":
    run()
