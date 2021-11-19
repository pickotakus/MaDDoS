from typing import get_origin
from menu import *
from game1 import *
from game2 import *
from ursina import *
from random import *

app = Ursina()
from menu import loadMenu

loadMenu()
#loadGame1()

app.run()
