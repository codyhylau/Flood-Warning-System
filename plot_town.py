from floodsystem.plot import plot_town
from floodsystem.stationdata import build_station_list


stations = build_station_list()
plot_town(stations, 10)