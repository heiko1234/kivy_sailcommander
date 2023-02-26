
import os
import yaml
import pathlib

# from dotenv import load_dotenv


# load_dotenv()

# local_run = os.getenv("LOCAL_RUN", False)
# local_run  # True


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
        # segel_lage: bb, st, nn  # backboard steuerboard, neutral
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
    
    def get_trim(self):
        return self._trim
    
    def get_right(self):
        if self._wind == "wind_00":
            self._wind = "wind_45"
            self._lage = "bb"
        elif self._wind == "wind_45":
            self._wind = "wind_90"
            self._lage = "bb"
        elif self._wind == "wind_90":
            self._wind = "wind_135"
            self._lage = "bb"
        elif self._wind == "wind_135":
            self._wind = "wind_180"
            self._lage = "nn"
        elif self._wind == "wind_180":
            self._wind = "wind_225"
            self._lage = "st"
        elif self._wind == "wind_225":
            self._wind = "wind_270"
            self._lage = "st"
        elif self._wind == "wind_270":
            self._wind = "wind_315"
            self._lage = "st"
        elif self._wind == "wind_315":
            self._wind = "wind_00"
            self._lage = "nn"

    def get_left(self):
        if self._wind == "wind_00":
            self._wind = "wind_315"
            self._lage = "st"
        elif self._wind == "wind_315":
            self._wind = "wind_270"
            self._lage = "st"
        elif self._wind == "wind_270":
            self._wind = "wind_225"
            self._lage = "st"
        elif self._wind == "wind_225":
            self._wind = "wind_180"
            self._lage = "nn"
        elif self._wind == "wind_180":
            self._wind = "wind_135"
            self._lage = "bb"
        elif self._wind == "wind_135":
            self._wind = "wind_90"
            self._lage = "bb"
        elif self._wind == "wind_90":
            self._wind = "wind_45"
            self._lage = "bb"
        elif self._wind == "wind_45":
            self._wind = "wind_00"
            self._lage = "nn"

    def segel_trim(self, trim):
        if self._segel == "up":
            if trim == "rs" or trim == "hw":
                self._trim == trim

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

    # def wende(self):
    #     if (self._segel == "up") and (self._trim=="hw"):
    #         if self._lage=="bb" and self._wind=="wind_45":
    #             self._lage="st"
    #             self._wind="wind_315"
    #         elif self._lage=="st" and self._wind=="wind_315":
    #             self._lage="bb"
    #             self._wind="wind_45"

    # def halse_prep(self):
    #     if (self._segel == "up") and (self._trim=="rs"):
    #         if self._lage=="bb" and self._wind=="wind_135":
    #             self._trim=="hw"
    #         elif self._lage=="st" and self._wind=="wind_225":
    #             self._trim=="hw"

    # def halse(self):
    #     if (self._segel == "up") and (self._trim=="hw"):
    #         if self._lage=="bb" and self._wind=="wind_135":
    #             self._lage="st"
    #             self._wind="wind_225"
    #         elif self._lage=="st" and self._wind=="wind_225":
    #             self._lage="bb"
    #             self._wind="wind_135"

    # def patent_halse(self):
    #     if (self._segel == "up") and (self._trim=="rs"):
    #         if self._lage=="bb":
    #             self._lage="st"
    #         elif self._lage=="st":
    #             self._lage="bb"
    #         if self._wind=="wind_90":
    #             self._wind="wind_270"
    #         elif self._wind=="wind_270":
    #             self._wind="wind_90"

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

        self._active_scenario = "Initial"
        self._step=0

        # if local_run:
        # self._scenario_config = read_configuration("./sailcommander/command_scenarion_config.yaml")
        # else:
        # path_abs = os.path.abspath(__file__)
        # print(path_abs)
        # BUG bei buildozer: patho not found when absolute paths are added. 
        path_abs = pathlib.Path(__file__).parent.resolve()
        newpath=pathlib.Path.joinpath(path_abs, "command_scenarion_config.yaml")
        self._scenario_config = read_configuration(newpath)
        # self._scenario_config = read_configuration("./command_scenarion_config.yaml")
        # self._scenario_config = None

    def select_scenario(self, scenario):
        self._active_scenario = scenario

    def hint_command(self, scenario):

        if scenario != self._active_scenario:
            step=0

        else:
            step = self._step

        try:
            if step<len(self._scenario_config[scenario]):

                stepkeys=self._scenario_config[scenario][step].keys()
                output = []
                for key in stepkeys:
                    output.append(key)
                stepname = output[0]

                # make it all lower
                step_commando_lower = self._scenario_config[scenario][step][stepname]["Commando"]
            
                return step_commando_lower
            
            else:
                return "Wähle ein neues Szenario"
        
        except KeyError:
            return "Szenario wählen"


    def process_scenario(self, scenario, commando, wind=None, segel=None, lage=None):

        # if self._active_scenario == scenario:
        #     print("same scenario")

        if self._active_scenario != scenario:
            # print("new scenario")
            self._active_scenario = scenario
            self._step = 0

        try:
            if self._step<len(self._scenario_config[self._active_scenario]):

                stepkeys=self._scenario_config[self._active_scenario][self._step].keys()
                output = []
                for key in stepkeys:
                    output.append(key)
                stepname = output[0]

                # make it all lower
                step_commando_lower = self._scenario_config[self._active_scenario][self._step][stepname]["Commando"]
                step_commando_lower = step_commando_lower.lower()
                commando_lower = commando.lower()

                bedingung_true = True

                # TODO: check if Bedingung in config und dann...
                if "Bedingung" in self._scenario_config[self._active_scenario][self._step][stepname].keys():
                    #print(self._scenario_config[self._active_scenario][self._step][stepname].keys())
                    if "wind" in self._scenario_config[self._active_scenario][self._step][stepname]["Bedingung"].keys():
                        #print(self._scenario_config[self._active_scenario][self._step][stepname]["Bedingung"].keys())
                        if wind in self._scenario_config[self._active_scenario][self._step][stepname]["Bedingung"]["wind"]:
                            bedingung_true = True
                        else:
                            bedingung_true = False 


                if (step_commando_lower == commando_lower) and bedingung_true:
                    step_number = self._step
                    self._step=self._step+1
                    return self._scenario_config[self._active_scenario][step_number][stepname]["Antwort"], self._scenario_config[self._active_scenario][step_number][stepname]["Boot"]["segel"]

                elif (step_commando_lower == commando_lower) and not bedingung_true:
                    return "Kommando richtig, Bedingungen falsch", None

                else:
                    return "Falsches Kommando", None

            else:
                return "keine weiteren Kommandos notwendig", None
        except KeyError:
            return "Neues Szenario"




# boat_sail_info = sail_infos()

# boat_sail_info.get_left()


# commandos=sail_scenario()

# commandos.hint_command(scenario="Wende")
# commandos.hint_command(scenario="Halse")



# commandos.process_scenario(scenario="Wende", commando="Klar zur wende", wind=None, segel=None, lage=None)

# commandos.process_scenario(scenario="Wende", commando="Ree", wind=None, segel=None, lage=None)

# commandos.process_scenario(scenario="Wende", commando="Über die Segel", wind=None, segel=None, lage=None)

# commandos.process_scenario(scenario="Wende", commando="Neuer Kurs am Wind", wind=None, segel=None, lage=None)



# commandos.process_scenario(scenario="Wende", commando="Klar zur wende", wind=None, segel=None, lage=None)


# commandos.process_scenario(scenario="Halse", commando="Klar zur wende", wind=None, segel=None, lage=None)






# config=read_configuration(configuration_file_path="./sailcommander/command_scenarion_config.yaml")
# # #
# # config["Wende"][0]
# # config["Wende"][0].keys()

# # step=config["Wende"][0].keys()
# # step

# # output = []
# # for key in step:
# #     output.append(key)

# # step = output[0]
# # step

# # config["Wende"][0]["Step1"]

# # config["Wende"][0][step]["Commando"]
# # config["Wende"][0][step]["Antwort"]
# # config["Wende"][0][step]["Boot"]

# # config["Wende"][0][step]["Boot"]["segel"]
# # config["Wende"][0][step]["Boot"]["lage"]
# # config["Wende"][0][step]["Boot"]["wind"]


# config["Halse"]

# config["Wende"]
# len(config["Wende"])
