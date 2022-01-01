"""Unit test for geo module"""

import floodsystem.geo
from floodsystem.stationdata import build_station_list, MonitoringStation
stations=build_station_list()

fake =  MonitoringStation("label", "measure", "fakename", (52.2286,0.08393889),  (7,4),  "rio", "simcity")
fakelist = [fake]

def test_stations_by_distance():
        """Test returning station name and distance"""
        assert round(floodsystem.geo.stations_by_distance(fakelist, (52.2053, 0.1218))[0][2],1) == 4.9

def test_stations_within_radius():
        """Test returning stations within a radius r of coordinate x"""
        assert floodsystem.geo.stations_within_radius(fakelist, (52.2053, 0.1218), 5) == ["simcity"]
        assert floodsystem.geo.stations_within_radius(fakelist, (52.2053, 0.1218), 4.5) == []

def test_rivers_with_station():
        """Test returning names of the rivers with a monitoring station"""
        assert floodsystem.geo.rivers_with_station(fakelist) == ["rio"]
        assert len(floodsystem.geo.rivers_with_station(fakelist)) == 1

def test_stations_by_river():
        """Test returning rivers and corresponding stations"""
        assert floodsystem.geo.stations_by_river(fakelist)["rio"] == ['fakename']
        assert len(floodsystem.geo.stations_by_river(fakelist)["rio"]) == 1

def test_rivers_by_station_number():   
        """Test returning rivers with number of stations"""
        assert floodsystem.geo.rivers_by_station_number(fakelist,5)[0][1] == 1