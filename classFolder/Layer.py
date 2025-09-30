import pyray
import pathlib
from classFolder.TypeLayer import TypeLayer

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
        pathFilePng = f"{Layer.pathMainFolder}/spryte/{nameFile}.png"
        self.texture = pyray.load_texture(pathFilePng)

        # params.
        self.isActive = isActive
        self.typeLayer = typeLayer
        self.origine = origine or defaultSource

        # params eval during update.
        self.pos = pyray.Vector2(0, 0)
        self.rotate = 0
        self.update = update or (lambda t: True)


    # function to draw the layer.
    def draw(self, timeMilisec: int):

        # not draw if disable.
        if not self.isActive:
            return

        # not draw if disable by animation.
        if not self.update(timeMilisec):
            return

        rectDest = pyray.Rectangle(
            self.pos.x - self.origine.x, 
            self.pos.y - self.origine.y, 
            Layer.defaultSizeX, 
            Layer.defaultSizeY
        )

        # Doc : https://electronstudio.github.io/raylib-python-cffi/pyray.html#pyray.draw_texture_pro
        pyray.draw_texture_pro(
            self.texture,
            Layer.defaultSource,
            rectDest,
            origine,
            self.rotate,
            pyray.WHITE
        )
    

    # unload all alloc for layer.
    def destroy(self):

        pyray.unload_texture(self.texture)