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
    def __init__(self, nameFile: str, isActive=True, typeLayer=None):
        
        # load texture.
        pathFilePng = f"{Layer.pathMainFolder}/spryte/{nameFile}.png"
        self.texture = pyray.load_texture(pathFilePng)

        # params.
        self.isActive = isActive
        self.typeLayer = typeLayer

        # params eval during update.
        self.isActiveDuringAnime = True


    # function to draw the layer.
    def draw(self, timeMilisec: int):

        if not self.isActive:
            return

        #self.update(timeMilisec)

        rectDest = pyray.Rectangle(
            0, 
            0, 
            Layer.defaultSizeX, 
            Layer.defaultSizeY
        )
        rotation = 0

        # Doc : https://electronstudio.github.io/raylib-python-cffi/pyray.html#pyray.draw_texture_pro
        pyray.draw_texture_pro(
            self.texture,
            Layer.defaultSource,
            rectDest,
            Layer.defaultOrigine,
            rotation,
            pyray.WHITE
        )
    

    # unload all alloc for layer.
    def destroy(self):

        pyray.unload_texture(self.texture)