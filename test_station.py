# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""Unit test for the station module"""

from floodsystem.station import MonitoringStation

fake_station = {"name":"fake 1", "coord":(52.2286, 0.08393889), "typical_range": (7, 4), "river": "rio", "town": "sim_city"}
fake = MonitoringStation("omg_1", "measure_1", "fake 1", (52.2286, 0.08393889), (7, 4), "rio", "sim_city")
fake_list = [fake]
def test_create_monitoring_station():

    # Create a station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    assert s.station_id == s_id
    assert s.measure_id == m_id
    assert s.name == label
    assert s.coord == coord
    assert s.typical_range == trange
    assert s.river == river
    assert s.town == town

from floodsystem.station import inconsistent_typical_range_stations
from floodsystem.stationdata import build_station_list
stations=build_station_list()

def test_inconsistent_typical_range_stations():
    """Test returning inconsistent stations"""
    inconsistent_station = inconsistent_typical_range_stations(fake_list)
    assert inconsistent_station == ["fake 1"]
    
   