from ursina import *
from game1 import *
from game2 import *

def menuButton():
    global levelInfo
    menu = Button(parent = scene, model = "cube", x = 5, y = -3, z = 0.01, scale_x = 3, scale_y = 1.2, scale_z = 0.01, icon = "menu/Menu.png")
    menu.on_click = lambda: loadMenu()
    levelInfo.append(menu)

def menuButton2():
    menu = Button(parent = scene, model = "cube", x = 5, y = -3, z = 0.01, scale_x = 3, scale_y = 1.2, scale_z = 0.01, icon = "menu/Menu.png")
    menu.on_click = lambda: loadMenu()

def levels():
    global levelInfo
    levelInfo = []
    scene.clear()
    levels = Entity(parent = scene, model = "cube", x = 0, y = 3, z = 0.01, scale_x = 3, scale_y = 1.2, scale_z = 0, texture = "menu/Levels.png")

    def startGame1():
        for x in levelInfo:
            destroy(x, delay = 0)
        loadGame1()
    def startGame2():
        for x in levelInfo:
            destroy(x, delay = 0)
        loadGame2()

    game1 = Button(parent = scene, model = "cube", x = -4, y = 1, z = 0.01, scale_x = 2, scale_y = 2, scale_z = 0.01, icon = "menu/LevelFalse.png")
    game1.on_click = lambda: startGame1()
    game1Nr = Entity(parent = scene, model = "cube", x = -4, y = 1, z = 0.01, scale_x = 1.5, scale_y = 1.5, scale_z = 0.01, texture = "menu/1.png")
    game2 = Button(parent = scene, model = "cube", x = -1.5, y = 1, z = 0.01, scale_x = 2, scale_y = 2, scale_z = 0.01, icon = "menu/LevelFalse.png")
    game2.on_click = lambda: startGame2()
    game2Nr = Entity(parent = scene, model = "cube", x = -1.5, y = 1, z = 0.01, scale_x = 1.5, scale_y = 1.5, scale_z = 0.01, texture = "menu/2.png")
    menuButton()
    levelInfo.append(levels)
    levelInfo.append(game1)
    levelInfo.append(game2)
    levelInfo.append(game1Nr)
    levelInfo.append(game2Nr)

def authors():
    scene.clear()
    authors = Entity(model = "cube", x = 0, y = 0, z = 0.05, scale_x = 14, scale_y = 8, scale_z = 0, texture = "menu/authorsMenu.png")
    menuButton2()

def controls():
    scene.clear()
    authors = Entity(model = "cube", x = 0, y = 0, z = 0.05, scale_x = 14, scale_y = 8, scale_z = 0, texture = "menu/controlsMenu.png")
    menuButton2()

def loadMenu():
    scene.clear()
    levelsButton = Button(parent = scene, model = "cube", x = 0, y = 1.5, z = 0.01, scale_x = 3, scale_y = 1.2, scale_z = 0.01, icon = "menu/Levels.png")
    levelsButton.on_click = lambda: levels()
    levelsButton.always_on_top = True
    controlsButton = Button(parent = scene, model = "cube", x = 0, y = 0, z = 0.01, scale_x = 3, scale_y = 1.2, scale_z = 0.01, icon = "menu/controls.png")
    controlsButton.on_click = lambda: controls()
    controlsButton.always_on_top = True
    authorsButton = Button(parent = scene, model = "cube", x = 0, y = -1.5, z = 0.01, scale_x = 3, scale_y = 1.2, scale_z = 0.01, icon = "menu/authors.png", color = "#AFAFAF")
    authorsButton.always_on_top = True
    authorsButton.on_click = lambda: authors()
    exitButton = Button(parent = scene, model = "cube", x = 0, y = -3, z = 0.01, scale_x = 3, scale_y = 1.2, scale_z = 0.01, icon = "menu/exit.png")
    exitButton.on_click = lambda: app.quit()
    exitButton.always_on_top = True