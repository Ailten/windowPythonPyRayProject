import pyray
import pathlib
from classFolder.TypeLayer import TypeLayer
import math
from classFolder.Microphone import Microphone

# Layer, mimic a layer (sprite) with his hown movement.
class Layer():

    # static attributes.
    defaultSizeX = 400
    defaultSizeY = 600
    pathMainFolder = pathlib.Path(__file__).parent.parent.resolve()
    defaultSource = pyray.Rectangle(0, 0, defaultSizeX, defaultSizeY)
    defaultOrigine = pyray.Vector2(0, 0)

    # constructor.
    def __init__(self, nameFile: str, isActive=True, typeLayer=None, origine=None, update=None):
        
        # load texture.
        self.name = nameFile
        pathFilePng = f"{Layer.pathMainFolder}/spryte/{nameFile}.png"
        self.texture = pyray.load_texture(pathFilePng)

        # params.
        self.isActive = isActive
        self.typeLayer = typeLayer
        self.origine = origine or Layer.defaultOrigine

        # params eval during update.
        self.pos = pyray.Vector2(0, 0)
        self.rotate = 0
        self.update = update or (lambda s, t: True)


    # function to draw the layer.
    def draw(self, timeMilisec: int):

        # not draw if disable.
        if not self.isActive:
            return

        # not draw if disable by animation.
        if not self.update(self, timeMilisec):
            return

        rectDest = pyray.Rectangle(
            self.pos.x + self.origine.x, 
            self.pos.y + self.origine.y, 
            Layer.defaultSizeX, 
            Layer.defaultSizeY
        )

        # Doc : https://electronstudio.github.io/raylib-python-cffi/pyray.html#pyray.draw_texture_pro
        pyray.draw_texture_pro(
            self.texture,
            Layer.defaultSource,
            rectDest,
            self.origine,
            self.rotate,
            pyray.WHITE
        )
    

    # unload all alloc for layer.
    def destroy(self):

        pyray.unload_texture(self.texture)


    # ----------> function update for animation.

    @staticmethod
    def getCosTime(timeMilisec):
        timeSpeeded = timeMilisec * 0.0015
        return math.cos(timeSpeeded)

    # use for movement head (and all link to head).
    @staticmethod
    def faceUpdate(self, timeMilisec):
        i = Layer.getCosTime(timeMilisec)
        rangePosY = 8
        BaseRangePos = 10
        self.pos.y = BaseRangePos
        self.pos.y += i * rangePosY
        return True

    # use for movement couette.
    @staticmethod
    def couetteUpdate(self, timeMilisec):
        Layer.faceUpdate(self, timeMilisec)
        i = Layer.getCosTime(timeMilisec)
        clockRotate = (1) if self.name.endswith("Left") else (-1)
        rangeRotate = (10) if self.name.startswith("couetteUp") else (18)
        self.rotate = rangeRotate * i * clockRotate
        return True

    # use for blink.
    @staticmethod
    def blinkUpdate(self, timeMilisec):
        Layer.faceUpdate(self, timeMilisec)
        i = timeMilisec * 0.001
        i = (i / 2.8) %1.0
        isBlinkTime = i < 0.08
        isLayerBlink = self.name.startswith("eyesClose")
        return isBlinkTime == isLayerBlink

    # use for mouth.
    @staticmethod
    def mouthUpdate(self, timeMilisec):
        Layer.faceUpdate(self, timeMilisec)
        decibel = Microphone.decibel
        minTalkValue = 0
        maxTalkValue = 12
        if decibel <= minTalkValue and self.name.startswith("mouth"):
            return True
        if decibel > minTalkValue and decibel <= maxTalkValue and self.name.startswith("mouthOpenMid"):
            return True
        if decibel > maxTalkValue and self.name.startswith("mouthOpen"):
            return True
        return False

