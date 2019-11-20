from cmu_112_graphics import *
from tkinter import *
import random

class StartScreenMode(Mode):
    def redrawAll(mode, canvas):
        font = 'Arial 26 bold'
        canvas.create_text(mode.width/2,
                           150, text='This demos a ModalApp!', font=font)
        canvas.create_oval(mode.width/2-50, mode.height*3/4-50,
                           mode.width/2+50, mode.height*3/4+50,
                           fill = 'light blue')
        canvas.create_text(mode.width/2, mode.height*3/4, text = 'START GAME')

    def mousePressed(mode, event):
        if (event.x < mode.width/2+50 and event.x > mode.width/2-50 and
            event.y < mode.height*3/4+50 and event.y > mode.height*3/4-50):
            mode.app.setActiveMode(mode.app.gameMode)

class GameMode(Mode):
    def appStarted(mode):
        mode.score = 0
        mode.randomFruit()
        mode.dy = 10
        mode.cy = mode.height
        mode.maxheight = random.randint(mode.height//3, mode.height*2//3)
        mode.cx = random.randint(mode.width//5, mode.width*4//5)
        mode.r = 20
        mode.score = 0
        mode.fruitList = []

    def randomFruit(mode):
        watermelonURL = ('https://vignette.wikia.nocookie.net/'+
                        'fruitninja/images/d/d6/Watermelon.svg/'+
                        'revision/latest/scale-to-width-down/'+
                        '170?cb=20170717192054')
        watermelon = mode.loadImage(watermelonURL)
        mode.watermelon = mode.scaleImage(watermelon, 1/4)
        mangoURL = ('https://vignette.wikia.nocookie.net/'+
                    'fruitninja/images/4/4d/Mango.svg/revision/latest/'+
                    'scale-to-width-down/170?cb=20170717213335')
        mango = mode.loadImage(mangoURL)
        mode.mango = mode.scaleImage(mango, 1/4)
        pineappleURL = ('https://vignette.wikia.nocookie.net/'+
                        'fruitninja/images/4/4b/Pineapple.svg/revision/'+
                        'latest/scale-to-width-down/170?cb=20170717213425')
        pineapple = mode.loadImage(pineappleURL)
        mode.pineapple = mode.scaleImage(pineapple, 1/4)
        coconutURL = ('https://vignette.wikia.nocookie.net/'+
                      'fruitninja/images/f/f1/Coconut.svg/revision/latest/'+
                      'scale-to-width-down/170?cb=20170717213508')
        coconut = mode.loadImage(coconutURL)
        mode.coconut = mode.scaleImage(coconut, 1/4)
        strawberryURL = ('https://vignette.wikia.nocookie.net/fruitninja/'+
                      'images/e/e2/Strawberry.svg/revision/latest/'+
                      'scale-to-width-down/170?cb=20170717213604')
        strawberry = mode.loadImage(strawberryURL)
        mode.strawberry = mode.scaleImage(strawberry, 1/4)
        greenAppleURL = ('https://vignette.wikia.nocookie.net/fruitninja/'+
                      'images/9/98/Green_Apple.svg/revision/latest/'+
                      'scale-to-width-down/170?cb=20170717213716')
        greenApple = mode.loadImage(greenAppleURL)
        mode.greenApple = mode.scaleImage(greenApple, 1/4)
        redAppleURL = ('https://vignette.wikia.nocookie.net/fruitninja/'+
                       'images/1/16/Red_Apple.svg/revision/latest/'+
                       'scale-to-width-down/170?cb=20170717213652')
        redApple = mode.loadImage(redAppleURL)
        mode.redApple = mode.scaleImage(redApple, 1/4)
        kiwiURL = ('https://vignette.wikia.nocookie.net/fruitninja/'+
                   'images/1/16/Kiwi_Fruit.svg/revision/latest/'+
                   'scale-to-width-down/170?cb=20170717213827')
        kiwi = mode.loadImage(kiwiURL)
        mode.kiwi = mode.scaleImage(kiwi, 1/4)
        bananaURL = ('https://vignette.wikia.nocookie.net/fruitninja/'+
                     'images/2/29/Banana.svg/revision/latest/'+
                     'scale-to-width-down/150?cb=20170717213901')
        banana = mode.loadImage(bananaURL)
        mode.banana = mode.scaleImage(banana, 1/4)
        lemonURL = ('https://vignette.wikia.nocookie.net/fruitninja/'+
                    'images/f/fa/Lemon.svg/revision/latest/'+
                    'scale-to-width-down/170?cb=20170717214018')
        lemon = mode.loadImage(lemonURL)
        mode.lemon = mode.scaleImage(lemon, 1/4)
        limeURL = ('https://vignette.wikia.nocookie.net/fruitninja/'+
                   'images/e/ed/Lime.svg/revision/latest/'+
                   'scale-to-width-down/170?cb=20170717214049')
        lime = mode.loadImage(limeURL)
        mode.lime = mode.scaleImage(lime, 1/4)
        orangeURL = ('https://vignette.wikia.nocookie.net/fruitninja/'+
                     'images/4/45/Orange.svg/revision/latest/'+
                     'scale-to-width-down/170?cb=20170717214114')
        orange = mode.loadImage(orangeURL)
        mode.orange = mode.scaleImage(orange, 1/4)
        plumURL = ('https://vignette.wikia.nocookie.net/fruitninja/'+
                   'images/0/07/Plum.svg/revision/latest/'+
                   'scale-to-width-down/170?cb=20170717214141')
        plum = mode.loadImage(plumURL)
        mode.plum = mode.scaleImage(plum, 1/4)
        pearURL = ('https://vignette.wikia.nocookie.net/fruitninja/'+
                   'images/0/07/Pear.svg/revision/latest/'+
                   'scale-to-width-down/170?cb=20170717214204')
        pear = mode.loadImage(pearURL)
        mode.pear = mode.scaleImage(pear, 1/4)
        passionFruitURL = ('https://vignette.wikia.nocookie.net/'+
                           'fruitninja/images/7/74/Passionfruit.svg/'+
                           'revision/latest/scale-to-width-down/'+
                           '170?cb=20170717214258')
        passionFruit = mode.loadImage(passionFruitURL)
        mode.passionFruit = mode.scaleImage(passionFruit, 1/4)
        mode.fruits = random.choice([mode.watermelon,mode.mango,mode.pineapple,
                                     mode.coconut,mode.strawberry,
                                     mode.greenApple,mode.redApple,mode.kiwi,
                                     mode.banana,mode.lemon,mode.lime,
                                     mode.orange,mode.plum,mode.pear,
                                     mode.passionFruit])
        #mode.fruitList.append(mode.fruits)

    def timerFired(mode):
        mode.doMove()

    def doMove(mode):
        mode.cy -= mode.dy
        if mode.cy < mode.maxheight:
            mode.dy = -mode.dy

    def mousePressed(mode, event):
        dist = ((mode.cx - event.x)**2 + (mode.cy - event.y)**2)**.5
        if dist <= mode.r:
            mode.score += 1
            #mode.fruitList.pop()
            mode.cx = random.randint(mode.width//5, mode.width*4//5)
            mode.cy = mode.height
            mode.randomFruit()

    def redrawAll(mode, canvas):
        canvas.create_text(mode.width/5, mode.height/8,
                           text = f'Score: {mode.score}',font = 'Arial 26 bold')
       # for fruit in mode.fruitList:
        canvas.create_image(mode.cx,mode.cy,
                            image=ImageTk.PhotoImage(mode.fruits))        
    
class MyModalApp(ModalApp):
    def appStarted(app):
        app.startScreenMode = StartScreenMode()
        app.gameMode = GameMode()
        #app.helpMode = HelpMode()
        app.setActiveMode(app.startScreenMode)

MyModalApp(width = 600, height = 400)
