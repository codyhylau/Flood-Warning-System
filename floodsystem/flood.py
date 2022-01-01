from .station import MonitoringStation
from .utils import sorted_by_key
from .stationdata import update_water_levels



def stations_level_over_threshold(stations, tol):
    """returns the list of tuples of stations, relative water level (to typical high/low) that are over tol"""
    update_water_levels(stations)
    high_level_stations = []
    for i in range (len(stations)):
        if stations[i].relative_water_level() != None:
            if stations[i].relative_water_level() > tol:
                high_level_stations.append((stations[i].name, stations[i].relative_water_level()))
        
    return sorted_by_key(high_level_stations, 1, reverse=True)

def stations_highest_rel_level(stations, N):
    """returns list of N tuples of stations, relative water levels that are the highest"""
    return stations_level_over_threshold(stations, 0)[:N]

def get_relative(station,level):
    return (level-station.typical_range[0])/(station.typical_range[1]-station.typical_range[0])


