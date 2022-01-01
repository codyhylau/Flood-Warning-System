from floodsystem.plot import plot_water_levels
from floodsystem.plot import plot_water_level_with_fit
from floodsystem.stationdata import build_station_list
from floodsystem.datafetcher import fetch_measure_levels
from datetime import datetime, timedelta
def test_plot_water_levels():
    stations = build_station_list()
    station = stations[0]
    dt = 10
    dates, levels = fetch_measure_levels(station.measure_id,
                                     dt=timedelta(days=dt))
    plot_water_levels(station, dates, levels)
    assert len(dates) == len(levels)