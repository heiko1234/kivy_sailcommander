
import os
import yaml

from dotenv import load_dotenv


load_dotenv()

local_run = os.getenv("LOCAL_RUN", False)


def read_configuration(configuration_file_path):
    """
    This function reads the configuration from the given path (yaml file)
    Args:
        configuration_file_path ([str]): path to yaml configuration
    Returns:
        [dict]: yaml config. used in this pipeline script as a dict
    """
    with open(configuration_file_path) as file:
        configuration = yaml.full_load(file)
    return configuration


class sail_infos:
    def __init__(self):
        self._wind = "wind_00" 
        self._segel = "down"
        self._lage = "bb"
        self._trim = "hw"
        self._status = "ready"

        # segel: up, down
        # segel_lage: bb, st
        # segel_trim: hw = hart am wind, rs=raumschots

    def update_wind(self, wind):
        self._wind=wind
    
    def update_segel(self, segel):
        self._segel = segel
    
    def update_wind_and_segel(self, wind, segel):
        self._wind=wind
        self._segel=segel
    
    def get_segel(self):
        return self._segel
    
    def get_wind(self):
        return self._wind
    
    def get_status(self):
        return self._status
    
    def get_wind_segel(self):
        return self._wind, self._segel
    
    def get_right(self):
        if self._wind == "wind_00":
            self._wind = "wind_45"
        elif self._wind == "wind_45":
            self._wind = "wind_90"
        elif self._wind == "wind_90":
            self._wind = "wind_135"
        elif self._wind == "wind_135":
            self._wind = "wind_180"
        elif self._wind == "wind_180":
            self._wind = "wind_225"
        elif self._wind == "wind_225":
            self._wind = "wind_270"
        elif self._wind == "wind_270":
            self._wind = "wind_315"
        elif self._wind == "wind_315":
            self._wind = "wind_00"

    def get_left(self):
        if self._wind == "wind_00":
            self._wind = "wind_315"
        elif self._wind == "wind_315":
            self._wind = "wind_270"
        elif self._wind == "wind_270":
            self._wind = "wind_225"
        elif self._wind == "wind_225":
            self._wind = "wind_180"
        elif self._wind == "wind_180":
            self._wind = "wind_135"
        elif self._wind == "wind_135":
            self._wind = "wind_90"
        elif self._wind == "wind_90":
            self._wind = "wind_45"
        elif self._wind == "wind_45":
            self._wind = "wind_00"

    def segel_dichter(self):
        if self._segel == "up":
            if self._trim == "rs":
                self._trim = "hw"
    
    def segel_lose(self):
        if self._segel == "up":
            if self._trim =="hw":
                self._trim ="rs"

    def segel_up(self):
        if self._segel == "down":
            self._segel = "up"
    
    def segel_down(self):
        if self._segel == "up":
            self._segel = "down"

    def wende(self):
        if (self._segel == "up") and (self._trim=="hw"):
            if self._lage=="bb" and self._wind=="wind_45":
                self._lage="st"
                self._wind="wind_315"
            elif self._lage=="st" and self._wind=="wind_315":
                self._lage="bb"
                self._wind="wind_45"

    def halse_prep(self):
        if (self._segel == "up") and (self._trim=="rs"):
            if self._lage=="bb" and self._wind=="wind_135":
                self._trim=="hw"
            elif self._lage=="st" and self._wind=="wind_225":
                self._trim=="hw"

    def halse(self):
        if (self._segel == "up") and (self._trim=="hw"):
            if self._lage=="bb" and self._wind=="wind_135":
                self._lage="st"
                self._wind="wind_225"
            elif self._lage=="st" and self._wind=="wind_225":
                self._lage="bb"
                self._wind="wind_135"

    def patent_halse(self):
        if (self._segel == "up") and (self._trim=="rs"):
            if self._lage=="bb":
                self._lage="st"
            elif self._lage=="st":
                self._lage="bb"
            if self._wind=="wind_90":
                self._wind="wind_270"
            elif self._wind=="wind_270":
                self._wind="wind_90"

    def get_sail_pic(self):
        if self._segel=="up":
            output = f"sail_up_{self._lage}_{self._trim}.png"
            return output

        else:
            return "sail_down_bb.png"    

    def get_wind_pic(self):
        output = f"{self._wind}.png"
        return output


class sail_scenario:
    def __init__(self):

        self._active_scenario = None
        self._step=None

    def choose_scenario(self, scenario="wende"):
        self._active_scenario = scenario





config=read_configuration(configuration_file_path="./sailcommander/command_config.yaml")

config["Einfach"]["Wende"]










