from ursina import *
from random import *

class Player(Entity):
    pleyer = None
    roomItems = []
    
    def interact(self):
        for item in Player.roomItems:
            information = self.intersects(item)
            if information.hit:
                if information.entity.game == "dice":
                    information.entity.dice()
                    break
                elif information.entity.game == "card":
                    information.entity.card()
                    break
                elif information.entity.game == "coin":
                    information.entity.coin()
                    break
                
    def setValuer(self):
        pass
    def update(self):
        pass
    def input(self, key):
        speed = 0.15
        if key == "f":
            Player.interact(self)
        if (held_keys["a"] or held_keys["left arrow"]) and self.sideMax != "left":
            self.x -= speed
            self.sideMax = None
        if (held_keys["d"] or held_keys["right arrow"]) and self.sideMax != "right":
            self.x += speed
            self.sideMax = None
        if (held_keys["w"] or held_keys["up arrow"]) and self.upMax != "up":
            self.y += speed/2
            self.upMax = None
        if (held_keys["s"] or held_keys["down arrow"]) and self.upMax != "down":
            self.y -= speed/2
            self.upMax = None

class miniGames(Entity):
    miniGamesScreen = None
    activeGame = False

    score = 200
    games = 21
    scoreList = []
    gamesList = []

    def checkWin():
        if miniGames.games == 0 or miniGames.score <= 0:
            miniGames.leaveMinigame()
            miniGames.activeGame = True

            if miniGames.score >= 100:
                scene.clear()
                end = Entity(parent = scene, model = "cube", x = 0, y = 0, z = 0.3, scale_x = 10, scale_y = 6, scale_z = 0, texture = "game2/end.png")
                win1 = Button(parent = scene, model = "cube", x = 3, y = -2, z = 0.10, scale_x = 3, scale_y = 1.5, scale_z = 0.01, icon = "game2/menu.png")
                from menu import loadMenu
                win1.on_click = lambda: loadMenu()
                from game1 import loadGame1
                def temp():
                    scene.clear()
                    loadGame2()
                win2 = Button(parent = scene, model = "cube", x = -3, y = -2, z = 0.10, scale_x = 3, scale_y = 1.5, scale_z = 0.01, icon = "game2/retryButton.png")
                win2.on_click = lambda: temp()
            else:
                scene.clear()
                end = Entity(parent = scene, model = "cube", x = 0, y = 0, z = 0.3, scale_x = 10, scale_y = 6, scale_z = 0, texture = "game2/retry.png")
                lose = Button(parent = scene, model = "cube", x = 3, y = -2, z = 0.10, scale_x = 3, scale_y = 1.5, scale_z = 0.01, icon = "game2/retryButton.png")
                def temp():
                    miniGames.miniGamesScreen = None
                    miniGames.activeGame = False
                    score = 200
                    miniGames.score = score
                    games = 21
                    miniGames.games = games
                    miniGames.scoreList = []
                    miniGames.gamesList = []
                    Player.roomItems = []
                    Player.pleyer = None
                    loadGame2()
                lose.on_click = lambda: temp()
    def leaveMinigame():
        miniGames.hideRules(1)
        for x in miniGames.miniGamesScreen.items:
            destroy(x, delay = 0)
        destroy(miniGames.miniGamesScreen, delay = 0)
        miniGames.miniGamesScreen = None
        miniGames.activeGame = False
    def shuffleDice(shuffle, start, end, count, color):
        games = miniGames.games
        games -= 1
        miniGames.renderScore(2, games, "g")
        colorList = color
        numers = []
        for x in range(0, count):
            numers.append(randint(start, end))

        shuffle.numers = numers

        for x in range(0, count):
            shuffle.output[x].texture = colorList[numers[x] - 1]
        miniGames.games = games
    def diceGame(main):
        shuffle = Button(parent = scene, x = 4, y = 0.5, z = -0.2, scale_x = 2, scale_y = 6, scale_z = 0.01)
        shuffle.always_on_top = True
        shuffle.visible = False
        shuffle.output = []

        def temp(shuffle):
            miniGames.shuffleDice(shuffle, 1, 6, 3, ["game2/dice1.png", "game2/dice2.png", "game2/dice3.png", "game2/dice4.png", "game2/dice5.png", "game2/dice6.png"])

            score = miniGames.score
            if shuffle.numers[0] == shuffle.numers[1] and shuffle.numers[1] == shuffle.numers[2]:
                score += 10
            else:
                score -= 10
            miniGames.renderScore(4.5, score, "s")
            miniGames.score = score
                
            miniGames.checkWin()

        shuffle.on_click = lambda: temp(shuffle)

        output1 = Entity(model = "cube", x = -2.5, y = -0.8, z = -0.1, scale_x = 1, scale_y = 1, scale_z = 0.01, texture = "game2/dice6.png")
        shuffle.output.append(output1)

        output2 = Entity(model = "cube", x = -0.4, y = -0.8, z = -0.1, scale_x = 1, scale_y = 1, scale_z = 0.01, texture = "game2/dice6.png")
        shuffle.output.append(output2)

        output3 = Entity(model = "cube", x = 1.7, y = -0.8, z = -0.1, scale_x = 1, scale_y = 1, scale_z = 0.01, texture = "game2/dice6.png")
        shuffle.output.append(output3)

        main.items.append(shuffle)
        main.items.append(output1)
        main.items.append(output2)
        main.items.append(output3)
    def cardGame(main):
        shuffle = Button(parent = scene, x = 4, y = 0.5, z = -0.03, scale_x = 2, scale_y = 6, scale_z = 0.01)
        shuffle.always_on_top = True
        shuffle.visible = False
        shuffle.output = []
        shuffle.numers = []

        def temp(shuffle):
            miniGames.shuffleDice(shuffle, 1, 13, 4, ["game2/card1_Heart.png", "game2/card2_Heart.png", "game2/card3_Heart.png", "game2/card4_Heart.png", "game2/card5_Heart.png", "game2/card5_Heart.png", "game2/card6_Heart.png", "game2/card7_Heart.png", "game2/card8_Heart.png", "game2/card9_Heart.png", "game2/card10_Heart.png", "game2/card11_Heart.png", "game2/card12_Heart.png", "game2/card13_Heart.png"])
            
            dic = {}

            for x in shuffle.numers:
                try:
                    dic[x] += 1
                except:
                    dic[x] = 1

            y = True
            for x in dic:
                if dic[x] >= 2:
                    y = False
                    print("Add score Cards")
                    score = miniGames.score
                    if dic[x] == 4:
                        score += 20
                    elif dic[x] == 3:
                        score += 15
                    else:
                        score += 10
                    miniGames.renderScore(4.5, score, "s")
                    miniGames.score = score
            score = miniGames.score
            if y:
                score -= 10
                miniGames.score = score
            miniGames.checkWin()

        shuffle.on_click = lambda: temp(shuffle)

        output1 = Entity(model = "cube", x = -2.925, y = -0.95, z = -0.1, scale_x = 1, scale_y = 1.2, scale_z = 0.01, texture = "game2/card1_Heart.png")
        shuffle.output.append(output1)

        output2 = Entity(model = "cube", x = -1.15, y = -0.95, z = -0.1, scale_x = 1, scale_y = 1.2, scale_z = 0.01, texture = "game2/card1_Heart.png")
        shuffle.output.append(output2)

        output3 = Entity(model = "cube", x = 0.5, y = -0.95, z = -0.1, scale_x = 1, scale_y = 1.2, scale_z = 0.01, texture = "game2/card1_Heart.png")
        shuffle.output.append(output3)

        output4 = Entity(model = "cube", x = 2.25, y = -0.95, z = -0.1, scale_x = 1, scale_y = 1.2, scale_z = 0.01, texture = "game2/card1_Heart.png")
        shuffle.output.append(output4)

        main.items.append(shuffle)
        main.items.append(output1)
        main.items.append(output2)
        main.items.append(output3)
        main.items.append(output4)
    def coinGame(main):
        shuffle = Button(parent = scene, x = 4, y = 0.5, z = -0.03, scale_x = 2, scale_y = 6, scale_z = 0.01)
        shuffle.always_on_top = True
        shuffle.visible = False
        shuffle.output = []
        shuffle.numers = []

        def temp(shuffle):
            miniGames.shuffleDice(shuffle, 1, 2, 1, ["game2/coinHead.png", "game2/coinNumb.png"])

            score = miniGames.score
            if shuffle.numers[0] == 1:
                score += 10
            else:
                score -= 10
            miniGames.renderScore(4.5, score, "s")
            miniGames.score = score
            
            miniGames.checkWin()

        shuffle.on_click = lambda: temp(shuffle)

        output1 = Entity(model = "cube", x = -0.4, y = -0.8, z = -0.1, scale_x = 1, scale_y = 1, scale_z = 0.01, texture = "game2/coinNumb.png")
        shuffle.output.append(output1)

        main.items.append(shuffle)
        main.items.append(output1)
    def gamePanel(gameTipe):
        if gameTipe == "dice":
            rules.icon = "game2/rules1.png"
            miniGames.hideRules(2)
            gameImage = "game2/slot1.png"
        elif gameTipe == "card":
            rules.icon = "game2/rules2.png"
            miniGames.hideRules(2)
            gameImage = "game2/slot2.png"
        elif gameTipe == "coin":
            rules.icon = "game2/rules3.png"
            miniGames.hideRules(2)
            gameImage = "game2/slot3.png"
        
        gamePanel = Entity(model = "cube", x = 0, y = 0, z = -0.05, scale_x = 10, scale_y = 7, scale_z = 0, texture = gameImage)

        gamePanel.items = []

        close = Button(parent = scene, x = 5, y = -3, z = -0.03, scale_x = 3.5, scale_y = 1.5, scale_z = 0.01, icon = "game2/leave.png")
        close.on_click = lambda: miniGames.leaveMinigame()
        close.always_on_top = True
        gamePanel.items.append(close)
        
        miniGames.miniGamesScreen = gamePanel
        
        if gameTipe == "dice":
            miniGames.diceGame(gamePanel)
        elif gameTipe == "card":
            miniGames.cardGame(gamePanel)
        elif gameTipe == "coin":
            miniGames.coinGame(gamePanel)

        return gamePanel
    def dice(self):
        if not miniGames.activeGame:
            miniGames.activeGame = True
            gamePanel = miniGames.gamePanel("dice")
    def card(self):
        if not miniGames.activeGame:
            miniGames.activeGame = True
            gamePanel = miniGames.gamePanel("card")
    def coin(self):
        if not miniGames.activeGame:
            miniGames.activeGame = True
            gamePanel = miniGames.gamePanel("coin")
    def renderScore(start, text, itemList):
        scoreList = miniGames.scoreList
        gamesList = miniGames.gamesList

        if itemList == "s":
            tempList = scoreList
        elif itemList == "g":
            tempList = gamesList

        for x in tempList:
            destroy(x, delay = 0)
        
        tempList = []
        
        text = str(text)
        z = 0
        for x in text:
            number = Entity(parent = scene, model = "cube", x = start + (z * 0.5), y = 3, z = 0, scale_x = 0.4, scale_y = 0.75, scale_z = 0.01, texture = "Nr" + str(x) + ".png")
            tempList.append(number)
            z += 1

        if itemList == "s":
            scoreList = tempList
        elif itemList == "g":
            gamesList = tempList

        miniGames.scoreList = scoreList
        miniGames.gamesList = gamesList
    def hideRules(hiding):
        global rules, showRules, showOdss1, showOdss2, showOdss3
        if hiding == 1:
            rules.enabled = False
            showOdss1.enabled = True
            showOdss2.enabled = True
            showOdss3.enabled = True
            showRules.enabled = True
        elif hiding == 2:
            rules.enabled = True
            showOdss1.enabled = False
            showOdss2.enabled = False
            showOdss3.enabled = False
            showRules.enabled = False

def loadGame2():
    global rules, showRules, showOdss1, showOdss2, showOdss3
    scene.clear()
    Player.pleyer = None
    roomItems = []
    score = 200
    miniGames.score = score
    games = 21
    miniGames.games = games

    player = Player(model = "cube", collider = "box", x = 0, y = -3, z = 0.01, scale_x = 1.7, scale_y = 1.7, scale_z = 0.01, texture = "images/alex.gif")
    Player.player = player
    player.sideMax = None
    player.upMax = None
    player.z = -0.001

    arcade1 = Entity(parent = scene, model = "cube", x = -4, y = 0, z = 0.05, scale_x = 2, scale_y = 2, scale_z = 0, texture = "game2/arcade1.png")
    game1 = miniGames(parent = scene, collider = "box", x = -4, y = 0, z = 0, scale_x = 2, scale_y = 2, scale_z = 0.02, color="#FF0000")
    roomItems.append(game1)
    game1.game = "dice"

    arcade2 = Entity(parent = scene, model = "cube", x = 0, y = 0, z = 0.05, scale_x = 2, scale_y = 2, scale_z = 0, texture = "game2/arcade2.png")
    game2 = miniGames(parent = scene, collider = "box", x = 0, y = 0, z = 0, scale_x = 2, scale_y = 2, scale_z = 0.02, color="#FF0000")
    roomItems.append(game2)
    game2.game = "card"

    arcade3 = Entity(parent = scene, model = "cube", x = 4, y = 0, z = 0.05, scale_x = 2, scale_y = 2, scale_z = 0, texture = "game2/arcade3.png")
    game3 = miniGames(parent = scene, collider = "box", x = 4, y = 0, z = 0, scale_x = 2, scale_y = 2, scale_z = 0.02, color="#FF0000")
    roomItems.append(game3)
    game3.game = "coin"

    rules = Button(parent = scene, model = "cube", x = 0, y = 0, z = 0.10, scale_x = 10, scale_y = 4.5, scale_z = 0.04, icon = "game2/rulesAll.png")
    rules.on_click = lambda: miniGames.hideRules(1)
    rules.always_on_top = True
    rules.enabled = False

    def temp():
        rules.icon = "game2/rulesAll.png"
        miniGames.hideRules(2)
    showRules = Button(parent = scene, model = "cube", x = -6.5, y = 1.5, z = -0.15, scale_x = 1, scale_y = 1, scale_z = 0.01, icon = "images/note1.png")
    showRules.on_click = lambda: temp()
    showRules.always_on_top = True
    showRules.enabled = True

    def odss1():
        rules.icon = "game2/diceOdss.png"
        miniGames.hideRules(2)
    showOdss1 = Button(parent = scene, model = "cube", x = -6.5, y = 0.3, z = -0.15, scale_x = 1, scale_y = 1, scale_z = 0.01, icon = "game2/dice.png")
    showOdss1.on_click = lambda: odss1()
    showOdss1.always_on_top = True
    showOdss1.enabled = True

    def odss2():
        rules.icon = "game2/cardsOdss.png"
        miniGames.hideRules(2)
    showOdss2 = Button(parent = scene, model = "cube", x = -6.5, y = -0.9, z = -0.15, scale_x = 1, scale_y = 1, scale_z = 0.01, icon = "game2/cards.png")
    showOdss2.on_click = lambda: odss2()
    showOdss2.always_on_top = True
    showOdss2.enabled = True

    def odss3():
        rules.icon = "game2/coinsOdss.png"
        miniGames.hideRules(2)
    showOdss3 = Button(parent = scene, model = "cube", x = -6.5, y = -2.1, z = -0.15, scale_x = 1, scale_y = 1, scale_z = 0.01, icon = "game2/coins.png")
    showOdss3.on_click = lambda: odss3()
    showOdss3.always_on_top = True
    showOdss3.enabled = True

    miniGames.renderScore(4.5, miniGames.score, "s")
    miniGames.renderScore(2, miniGames.games, "g")

    Player.roomItems = roomItems
