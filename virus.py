import random, sys
random.seed(42)
from person import *
from logger import *
from simulation import *

class Virus:

    def __init__(self, virus_name, mortality_rate, basic_repro_num):
        self.virus_name = virus_name
        self.mortality_rate = mortality_rate
        self.basic_repro_num = basic_repro_num
