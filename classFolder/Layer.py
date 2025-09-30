import pyray
import pathlib
from classFolder.TypeLayer import TypeLayer

# Layer, mimic a layer (sprite) with his hown movement.
class Layer():
    defaultSizeX = 400
    defaultSizeY = 600
    pathMainFolder = pathlib.Path(__file__).parent.parent.resolve()
    defaultSource = pyray.Rectangle(0, 0, defaultSizeX, defaultSizeY)

    # constructor.
    def __init__(self, nameFile: str, isActive=True, typeLayer=None):
        
        # get path.
        pathFilePng = f"{Layer.pathMainFolder}/spryte/{nameFile}.png"

        # load texture.
        self.texture = pyray.load_texture(pathFilePng)

        # params.
        self.isActive = isActive
        self.typeLayer = typeLayer


    # function to draw the layer.
    def draw(self):

        if not self.isActive:
            return

        rectDest = pyray.Rectangle(
            0, 
            0, 
            Layer.defaultSizeX, 
            Layer.defaultSizeY
        )
        origin = pyray.Vector2(
            Layer.defaultSizeX / 2,
            Layer.defaultSizeY / 2
        )
        rotation = 0

        print(self.texture)

        # Doc : https://electronstudio.github.io/raylib-python-cffi/pyray.html#pyray.draw_texture_pro
        pyray.draw_texture_pro(
            texture=self.texture,
            source=Layer.defaultSource,
            dest=rectDest,
            origin=origin,
            rotation=rotation,
            tint=pyray.WHITE
        )
    

    # unload all alloc for layer.
    def destroy(self):

        pyray.unload_texture(self.texture)