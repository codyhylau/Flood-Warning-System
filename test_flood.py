from floodsystem.flood import stations_level_over_threshold
from floodsystem.flood import stations_highest_rel_level
from floodsystem.stationdata import build_station_list
from floodsystem.stationdata import update_water_levels
from floodsystem.station import MonitoringStation 

def test_stations_level_over_threshold():
    """test for the function using the first entry of actual station list"""
    stations = build_station_list()
    station_list = [stations[0]]
    low_high = station_list[0].typical_range
    print("Typical range: ", low_high)
    update_water_levels(stations)
    new_level = station_list[0].latest_level
    print("Latest level: ", new_level)
    if new_level != None:
        relative_level = (new_level-low_high[0])/(low_high[1]-low_high[0])
    else:
        relative_level = None
    print("Relative level: ", relative_level)
    if relative_level != None:
        if relative_level > 0.8:
            assert stations_level_over_threshold(station_list, 0.8) == [(station_list[0].name, station_list[0].relative_water_level())]
        else:
            assert stations_level_over_threshold(station_list, 0.8) == []
    else:
        assert stations_level_over_threshold(station_list, 0.8) == []
       

def test_stations_highest_rel_level():
    """test for the function using first three entries in stations list"""
    stations = build_station_list()
    update_water_levels(stations)
    station_list = [stations[0], stations[1], stations[2]]

    #finding the station with the highest relative level
    if stations[0].relative_water_level() > stations[1].relative_water_level() and stations[0].relative_water_level() > stations[2].relative_water_level():
        highest = stations[0]
    elif stations[1].relative_water_level() > stations[0].relative_water_level() and stations[1].relative_water_level() > stations[2].relative_water_level():
        highest = stations[1]
    elif stations[2].relative_water_level() > stations[1].relative_water_level() and stations[2].relative_water_level() > stations[0].relative_water_level():
        highest = stations[2]
    
    #finding the station with the second highest level
    if highest == stations[1] and stations[2].relative_water_level() > stations[0].relative_water_level():
        middle = stations[2]
    elif highest == stations[1] and stations[0].relative_water_level() > stations[2].relative_water_level():
        middle = stations[0]

    elif highest == stations[2] and stations[1].relative_water_level() > stations[0].relative_water_level():
        middle = stations[1]
    elif highest == stations[2] and stations[1].relative_water_level() < stations[0].relative_water_level():
        middle = stations[0]

    elif highest == stations[0] and stations[1].relative_water_level() > stations[2].relative_water_level():
        middle = stations[1]
    elif highest == stations[0] and stations[1].relative_water_level() < stations[2].relative_water_level():
        middle = stations[2]
    
    #finding the station with the lowest level
    if highest == stations[0] and middle == stations[1]:
        lowest = stations[2]
    elif highest == stations[1] and middle == stations[0]:
        lowest = stations[2]
    
    elif highest == stations[1] and middle == stations[2]:
        lowest = stations[0]
    elif highest == stations[2] and middle == stations[1]:
        lowest = stations[0]

    elif highest == stations[0] and middle == stations[2]:
        lowest = stations[1]
    elif highest == stations[2] and middle == stations[0]:
        lowest = stations[1]

    
    assert stations_highest_rel_level(station_list, 3) == [(highest.name, highest.relative_water_level()), (middle.name, middle.relative_water_level()), (lowest.name, lowest.relative_water_level())]



    

