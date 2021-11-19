from typing import get_origin
from ursina import *
from random import *
from game2 import *

class Player(Entity):
    def setValuer(self):
        pass

    def update(self):
        pass

    def input(self, key):
        speed = 0.15
        if key == "f":
            GameFunctions.interact()
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

class GameFunctions():
    def restart():
        global wins, loses, demon1, demon2, demon3, money1, money2, money3, door1, door2, door3, ruless, note1, gameCharacter, que2, ans1, ans2, ans3, note3, note4, note5, btn_next, note6, note7, btn_start, btn_yes, btn_no, note8, btn_zerro, btn_one, btn_two, btn_three, right2, wrong2, yes2, no2, proof, end, btn_nice
        scene.clear()
        loadGame1()
    def interact():
        global wins, loses, demon1, demon2, demon3, money1, money2, money3, door1, door2, door3, ruless, note1, gameCharacter, que2, ans1, ans2, ans3, note3, note4, note5, btn_next, note6, note7, btn_start, btn_yes, btn_no, note8, btn_zerro, btn_one, btn_two, btn_three, right2, wrong2, yes2, no2, proof, end, btn_nice
        if abs(gameCharacter.x - door1.x) < 1 and abs(gameCharacter.y - door1.y) < 1:
            door1.y = -10
            door2.y = -10
            door3.y = -10
            note3.y = -10
            if money1.y == 0:
                note4.y = 2.2
                que2.y = -10
                ans1.y = -10
                ans2.y = -10
                ans3.y = -10
                wins += 1
                if wins + loses == 6:
                    GameFunctions.checkwin()
                else:
                    btn_next.y = 0.2
            elif demon1.y == 0:
                note5.y = 2.2
                que2.y = -10
                ans1.y = -10
                ans2.y = -10
                ans3.y = -10
                loses += 1
                if wins + loses == 6:
                    GameFunctions.checkwin()
                else:
                    btn_next.y = 1.6
        if abs(gameCharacter.x - door2.x) < 1 and abs(gameCharacter.y - door2.y) < 1:
            door1.y = -10
            door2.y = -10
            door3.y = -10
            note3.y = -10
            if money2.y == 0:
                note4.y = 2.2
                que2.y = -10
                ans1.y = -10
                ans2.y = -10
                ans3.y = -10
                wins += 1
                if wins + loses == 6:
                    GameFunctions.checkwin()
                else:
                    btn_next.y = 1.6
            elif demon2.y == 0:
                note5.y = 2.2
                que2.y = -10
                ans1.y = -10
                ans2.y = -10
                ans3.y = -10
                loses += 1
                if wins + loses == 6:
                    GameFunctions.checkwin()
                else:
                    btn_next.y = 1.6
        if abs(gameCharacter.x - door3.x) < 1 and abs(gameCharacter.y - door3.y) < 1:
            door1.y = -10
            door2.y = -10
            door3.y = -10
            note3.y = -10
            if money3.y == 0:
                note4.y = 2.2
                que2.y = -10
                ans1.y = -10
                ans2.y = -10
                ans3.y = -10
                wins += 1
                if wins + loses == 6:
                    GameFunctions.checkwin()
                else:
                    btn_next.y = 1.6
            elif demon3.y == 0:
                note5.y = 2.2
                que2.y = -10
                ans1.y = -10
                ans2.y = -10
                ans3.y = -10
                loses += 1
                if wins + loses == 6:
                    GameFunctions.checkwin()
                else:
                    btn_next.y = 1.6
    def rules2():
        global wins, loses, demon1, demon2, demon3, money1, money2, money3, door1, door2, door3, ruless, note1, gameCharacter, que2, ans1, ans2, ans3, note3, note4, note5, btn_next, note6, note7, btn_start, btn_yes, btn_no, note8, btn_zerro, btn_one, btn_two, btn_three, right2, wrong2, yes2, no2, proof, end, btn_nice
        ruless.y = -10
        door1.y = 0
        door2.y = 0
        door3.y = 0
        money1.y = -10
        money2.y = -10
        money3.y = -10
        demon1.y = -10
        demon2.y = -10
        demon3.y = -10
        btn_next.y = -10
        note4.y = -10
        note5.y = -10
        gameCharacter.y = -2.2
        gameCharacter.x = 0
        note7.y = -10
        btn_start.y = -10
        note1.y = 1.6
        GameFunctions.note2()
        GameFunctions.game()
    def rulesFunct():
        print(1)
        global wins, loses, demon1, demon2, demon3, money1, money2, money3, door1, door2, door3, ruless, note1, gameCharacter, que2, ans1, ans2, ans3, note3, note4, note5, btn_next, note6, note7, btn_start, btn_yes, btn_no, note8, btn_zerro, btn_one, btn_two, btn_three, right2, wrong2, yes2, no2, proof, end, btn_nice
        ans1.y = -10
        ans2.y = -10
        ans3.y = -10
        ruless.x = 0
        ruless.y = 0
    def note2():
        global wins, loses, demon1, demon2, demon3, money1, money2, money3, door1, door2, door3, ruless, note1, gameCharacter, que2, ans1, ans2, ans3, note3, note4, note5, btn_next, note6, note7, btn_start, btn_yes, btn_no, note8, btn_zerro, btn_one, btn_two, btn_three, right2, wrong2, yes2, no2, proof, end, btn_nice
        que2.y = 2.2
        ans1.y = 1.6
        ans2.y = 1.6
        ans3.y = 1.6
    def ans11():
        global wins, loses, demon1, demon2, demon3, money1, money2, money3, door1, door2, door3, ruless, note1, gameCharacter, que2, ans1, ans2, ans3, note3, note4, note5, btn_next, note6, note7, btn_start, btn_yes, btn_no, note8, btn_zerro, btn_one, btn_two, btn_three, right2, wrong2, yes2, no2, proof, end, btn_nice
        que2.y = -10
        ans1.y = -10
        ans2.y = -10
        ans3.y = -10
        a = choice([2, 3])
        if a == 2:
            if money2.y != 0:
                door2.y = -10
                note3.y = 2.2
            else:
                door3.y = -10
                note3.y = 2.2
        elif a == 3:
            if money3.y != 0:
                door3.y = -10
                note3.y = 2.2
            else:
                door2.y = -10
                note3.y = 2.2
    def ans22():
        global wins, loses, demon1, demon2, demon3, money1, money2, money3, door1, door2, door3, ruless, note1, gameCharacter, que2, ans1, ans2, ans3, note3, note4, note5, btn_next, note6, note7, btn_start, btn_yes, btn_no, note8, btn_zerro, btn_one, btn_two, btn_three, right2, wrong2, yes2, no2, proof, end, btn_nice
        que2.y = -10
        ans1.y = -10
        ans2.y = -10
        ans3.y = -10
        a = choice([1, 3])
        if a == 1:
            if money1.y != 0:
                door1.y = -10
                note3.y = 2.2
            else:
                door3.y = -10
                note3.y = 2.2
        elif a == 3:
            if money3.y != 0:
                door3.y = -10
                note3.y = 2.2
            else:
                door1.y = -10
                note3.y = 2.2
    def ans33():
        global wins, loses, demon1, demon2, demon3, money1, money2, money3, door1, door2, door3, ruless, note1, gameCharacter, que2, ans1, ans2, ans3, note3, note4, note5, btn_next, note6, note7, btn_start, btn_yes, btn_no, note8, btn_zerro, btn_one, btn_two, btn_three, right2, wrong2, yes2, no2, proof, end, btn_nice
        que2.y = -10
        ans1.y = -10
        ans2.y = -10
        ans3.y = -10
        a = choice([1, 2])
        if a == 1:
            if money1.y != 0:
                door1.y = -10
                note3.y = 2.2
            else:
                door2.y = -10
                note3.y = 2.2
        elif a == 2:
            if money2.y != 0:
                door2.y = -10
                note3.y = 2.2
            else:
                door1.y = -10
                note3.y = 2.2
    def game():
        global wins, loses, demon1, demon2, demon3, money1, money2, money3, door1, door2, door3, ruless, note1, gameCharacter, que2, ans1, ans2, ans3, note3, note4, note5, btn_next, note6, note7, btn_start, btn_yes, btn_no, note8, btn_zerro, btn_one, btn_two, btn_three, right2, wrong2, yes2, no2, proof, end, btn_nice
        li1 = [1, 2, 3]
        shuffle(li1)
        if li1[0] == 1:
            money1.y = 0
            demon2.y = 0
            demon3.y = 0
        elif li1[1] == 1:
            money2.y = 0
            demon1.y = 0
            demon3.y = 0
        elif li1[2] == 1:
            money3.y = 0
            demon1.y = 0
            demon2.y = 0
    def checkwin():
        global wins, loses, demon1, demon2, demon3, money1, money2, money3, door1, door2, door3, ruless, note1, gameCharacter, que2, ans1, ans2, ans3, note3, note4, note5, btn_next, note6, note7, btn_start, btn_yes, btn_no, note8, btn_zerro, btn_one, btn_two, btn_three, right2, wrong2, yes2, no2, proof, end, btn_nice
        if wins >= 4:
            note6.y = 0
            btn_yes.y = -1.2
            btn_no.y = -1.2
            money1.y = -10
            money2.y = -10
            money3.y = -10
            demon1.y = -10
            demon2.y = -10
            demon3.y = -10
            btn_next.y = -10
            note4.y = -10
            note5.y = -10
            note1.y = -10
            que2.y = -10
            ans1.y = -10
            ans2.y = -10
            ans3.y = -10
            gameCharacter.y = -2.2
            gameCharacter.x = 0
        else:
            note7.y = 0
            btn_start.y = -.1
            money1.y = -10
            money2.y = -10
            money3.y = -10
            demon1.y = -10
            demon2.y = -10
            demon3.y = -10
            btn_next.y = -10
            note4.y = -10
            note5.y = -10
            note1.y = -10
            que2.y = -10
            ans1.y = -10
            ans2.y = -10
            ans3.y = -10
            gameCharacter.y = -2.2
            gameCharacter.x = 0
            wins = 0
            loses = 0
    def winss():
        global wins, loses, demon1, demon2, demon3, money1, money2, money3, door1, door2, door3, ruless, note1, gameCharacter, que2, ans1, ans2, ans3, note3, note4, note5, btn_next, note6, note7, btn_start, btn_yes, btn_no, note8, btn_zerro, btn_one, btn_two, btn_three, right2, wrong2, yes2, no2, proof, end, btn_nice
        note6.y = -10
        btn_no.y = -10
        btn_yes.y = -10
        note8.y = 0
        btn_zerro.y = -0.8
        btn_one.y = -0.8
        btn_two.y = -0.8
        btn_three.y = -0.8
    def correctans():
        global wins, loses, demon1, demon2, demon3, money1, money2, money3, door1, door2, door3, ruless, note1, gameCharacter, que2, ans1, ans2, ans3, note3, note4, note5, btn_next, note6, note7, btn_start, btn_yes, btn_no, note8, btn_zerro, btn_one, btn_two, btn_three, right2, wrong2, yes2, no2, proof, end, btn_nice
        right2.y = 0
        note8.y = -10
        btn_zerro.y = -10
        btn_one.y = -10
        btn_two.y = -10
        btn_three.y = -10
        yes2.y = -0.8
        no2.y = -0.8
    def wrongans():
        global wins, loses, demon1, demon2, demon3, money1, money2, money3, door1, door2, door3, ruless, note1, gameCharacter, que2, ans1, ans2, ans3, note3, note4, note5, btn_next, note6, note7, btn_start, btn_yes, btn_no, note8, btn_zerro, btn_one, btn_two, btn_three, right2, wrong2, yes2, no2, proof, end, btn_nice
        wrong2.y = 0
        note8.y = -10
        btn_zerro.y = -10
        btn_one.y = -10
        btn_two.y = -10
        btn_three.y = -10
        yes2.y = -0.8
        no2.y = -0.8
    def show_proof():
        global wins, loses, demon1, demon2, demon3, money1, money2, money3, door1, door2, door3, ruless, note1, gameCharacter, que2, ans1, ans2, ans3, note3, note4, note5, btn_next, note6, note7, btn_start, btn_yes, btn_no, note8, btn_zerro, btn_one, btn_two, btn_three, right2, wrong2, yes2, no2, proof, end, btn_nice
        proof.y = 0
        btn_nice.y = -.222
        yes2.y = -10
        no2.y = -10
        wrong2.y = -10
        right2.y = -10
    def show_end_note():
        global wins, loses, demon1, demon2, demon3, money1, money2, money3, door1, door2, door3, ruless, note1, gameCharacter, que2, ans1, ans2, ans3, note3, note4, note5, btn_next, note6, note7, btn_start, btn_yes, btn_no, note8, btn_zerro, btn_one, btn_two, btn_three, right2, wrong2, yes2, no2, proof, end, btn_nice
        end.y = 0
        yes2.y = -10
        no2.y = -10
        wrong2.y = -10
        right2.y = -10
        proof.y = -10
        btn_nice.y = -10
        menu = Button(parent = scene, model = "cube", x = 2, y = -1.3, z = 0.01, scale_x = 3, scale_y = 1.2, scale_z = 0.01, icon = "images/Menu.png")
        from menu import loadMenu
        menu.on_click = lambda: loadMenu()
        menu.always_on_top = True
        restart = Button(parent = scene, model = "cube", x = -2, y = -1.3, z = 0.01, scale_x = 3, scale_y = 1.2, scale_z = 0.01, icon = "images/Restart.png")
        restart.on_click = lambda: GameFunctions.restart()
        restart.always_on_top = True

def loadGame1():
    global wins, loses, demon1, demon2, demon3, money1, money2, money3, door1, door2, door3, ruless, note1, gameCharacter, que2, ans1, ans2, ans3, note3, note4, note5, btn_next, note6, note7, btn_start, btn_yes, btn_no, note8, btn_zerro, btn_one, btn_two, btn_three, right2, wrong2, yes2, no2, proof, end, btn_nice
    wins = 0
    loses = 0

    demon1 = Entity(model='cube', color=color.white, scale=(
        1.5, 2.1), x=-3, y=-10, z=0, texture="images/demon1.png")
    demon2 = Entity(model='cube', color=color.white, scale=(
        1.5, 2.1), x=0, y=-10, z=0, texture="images/demon1.png")
    demon3 = Entity(model='cube', color=color.white, scale=(
        1.5, 2.1), x=3, y=-10, z=0, texture="images/demon1.png")

    money1 = Entity(model='cube', color=color.white, scale=(
        1.5, 2.1), x=-3, y=-10, z=0, texture="images/money1.png")
    money2 = Entity(model='cube', color=color.white, scale=(
        1.5, 2.1), x=0, y=-10, z=0, texture="images/money1.png")
    money3 = Entity(model='cube', color=color.white, scale=(
        1.5, 2.1), x=3, y=-10, z=0, texture="images/money1.png")

    door1 = Entity(model='cube', always_on_top = True, color=color.white, scale=(
        1.5, 2), x=-3, y=0, z=0, texture="images/door1.jpg")
    door2 = Entity(model='cube', always_on_top = True, color=color.white, scale=(
        1.5, 2), x=0, y=0, z=0, texture="images/door1.jpg")
    door3 = Entity(model='cube', always_on_top = True, color=color.white, scale=(
        1.5, 2), x=3, y=0, z=0, texture="images/door1.jpg")

    ruless = Button(parent = scene, icon="images/rules.png", always_on_top = True, color=color.azure, scale_x = 12, scale_y = 8, y=-10, x=0)
    ruless.on_click = lambda: GameFunctions.rules2()
    note1 = Button(parent = scene, icon='images/note1.png', scale_x = 1.2, scale_y = 1.2, y=0, x=-6)
    note1.on_click = lambda: GameFunctions.rulesFunct()

    gameCharacter = Player(parent = scene, model='cube', always_on_top=True, scale_y=1.7,
                           scale_x=1.7, scale_z=0.0001, x=0, y=-2.2, texture="images/alex.gif")
    gameCharacter.sideMax = None
    gameCharacter.upMax = None 
    gameCharacter.z = -0.001

    que2 = Entity(parent = scene, model='cube', color=color.white, scale=(
        7, 4), x=0, y=-10, z=0, texture="images/note2.png")
    ans1 = Button(parent = scene, always_on_top = True, icon='images/ans1.png', scale_x = 0.8, scale_y = 0.8, y=-10, x=-1.2)
    ans1.on_click = lambda: GameFunctions.ans11()
    ans2 = Button(parent = scene, always_on_top = True, icon='images/ans2.png', scale_x = 0.8, scale_y = 0.8, y=-10, x=0)
    ans2.on_click = lambda: GameFunctions.ans22()
    ans3 = Button(parent = scene, always_on_top = True, icon='images/ans3.png', scale_x = 0.8, scale_y = 0.8, y=-10, x=1.2)
    ans3.on_click = lambda: GameFunctions.ans33()

    note3 = Entity(model='cube', color=color.white, scale=(
        7, 4), x=0, y=-10, z=0, texture="images/note3.png")
    note4 = Entity(model='cube', color=color.white, scale=(
        7, 4), x=0, y=-10, z=0, texture="images/right.png")
    note5 = Entity(model='cube', color=color.white, scale=(
        7, 4), x=0, y=-10, z=0, texture="images/wrong.png")

    btn_next = Button(parent = scene, icon='images/btn_next.png', scale_x = 1.2, scale_y = 1.2, y=-10, x=4.8)
    btn_next.on_click = lambda: GameFunctions.rules2()

    note6 = Entity(model='cube', color=color.white, scale=(
        10, 7), x=0, y=-10, z=0, texture="images/if_wins.png")
    note7 = Entity(model='cube', color=color.white, scale=(
        10, 7), x=0, y=-10, z=0, texture="images/if_loses.png")

    btn_start = Button(parent = scene, icon='images/btn_start.png',
                       scale_x = 2.4, scale_y = 1.2, y=-10, x=0)
    btn_start.on_click = lambda: GameFunctions.rules2()
    btn_start.always_on_top = True
    btn_yes = Button(parent = scene, always_on_top = True, icon='images/btn_yes.png',
                     scale_x = 1.2, scale_y = 1.2, y=-10, x=-1.6)
    btn_yes.on_click = lambda: GameFunctions.winss()
    btn_no = Button(parent = scene, always_on_top = True, icon='images/btn_no.png', scale_x = 1.2, scale_y = 1.2, y=-10, x=1.6)
    btn_no.on_click = lambda: GameFunctions.winss()

    window.fullscreen = False

    note8 = Entity(model='cube', color=color.white, scale=(
        10, 7), x=0, y=-10, z=0, texture="images/que_proof.png")

    btn_zerro = Button(parent = scene, always_on_top = True, icon='images/zerro.png', scale_x = 1.2, scale_y = 1.2, y=-10, x=-2.4)
    btn_zerro.on_click = lambda: GameFunctions.wrongans()
    btn_one = Button(parent = scene, always_on_top = True, icon='images/one.png', scale_x = 1.2, scale_y = 1.2, y=-10, x=-0.8)
    btn_one.on_click = lambda: GameFunctions.wrongans()
    btn_two = Button(parent = scene, always_on_top = True, icon='images/two.png', scale_x = 1.2, scale_y = 1.2, y=-10, x=0.8)
    btn_two.on_click = lambda: GameFunctions.correctans()
    btn_three = Button(parent = scene, always_on_top = True, icon='images/three.png', scale_x = 1.2, scale_y = 1.2, y=-10, x=2.4)
    btn_three.on_click = lambda: GameFunctions.wrongans()

    right2 = Entity(model='cube', color=color.white, scale=(
        10, 7), x=0, y=-10, z=0, texture="images/right2.png")
    wrong2 = Entity(model='cube', color=color.white, scale=(
        10, 7), x=0, y=-10, z=0, texture="images/wrong2.png")
    yes2 = Button(parent = scene, always_on_top = True, icon='images/yes2.png', scale_x = 1.2, scale_y = 1.2, y=-10, x=-1.6)
    yes2.on_click = lambda: GameFunctions.show_proof()
    no2 = Button(parent = scene, always_on_top = True, icon='images/no2.png', scale_x = 1.2, scale_y = 1.2, y=-10, x=1.6)
    no2.on_click = lambda: GameFunctions.show_end_note()
    proof = Entity(model='cube', color=color.white, scale=(
        15, 9), x=0, y=-10, z=0, texture="images/proof.png")
    end = Entity(model='cube', color=color.white, scale=(
        12, 9), x=0, y=-10, z=0, texture="images/end.png")
    btn_nice = Button(parent = scene, always_on_top = True, icon='images/btn_nice.png',
                      scale_x = 1.44, scale_y = 0.8, y=-10, x=6.2 )
    btn_nice.on_click = lambda: GameFunctions.show_end_note()

