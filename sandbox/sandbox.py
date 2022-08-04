"""Sandbox."""
import logging
import netCDF4


class Sandbox():
    """Sandbox."""

    def __init__(self):
        """Init."""
        print("Hello sandbox")

    def play(self):
        """Play."""
        logging.info("play")
        logging.debug("debug play")
        filename = "https://thredds.met.no/thredds/dodsC/meps25epsarchive/2022/04/28/meps_det_2_5km_20220428T03Z.nc"
        file_handler = netCDF4.Dataset(filename, "r")
        print(file_handler)
