import pyray # python3 -m pip install raylib==5.5.0.3
import asyncio # to call async func from a sync.
from classFolder.Layer import Layer
from classFolder.TypeLayer import TypeLayer

# Doc : https://electronstudio.github.io/raylib-python-cffi/pyray.html#pyray.Color

# ----------> Main function.

async def main():

    # TODO : 
    # send origin to all layers need a specify one.
    # send typeLayer.

    # build a window.
    pyray.init_window(Layer.defaultSizeX, Layer.defaultSizeY, "pngtuberAilt_V3")
    backgroundColor = pyray.Color(0, 0, 255, 255)

    layers = [
        Layer("axoHat2", isActive=False, typeLayer=[TypeLayer.HAT, TypeLayer.AXO_HAT]),
        Layer("couetteLeft"),
        Layer("couetteRight"),
        Layer("couetteUpLeft"),
        Layer("tronc", typeLayer=[TypeLayer.TRONC, TypeLayer.DEFAULT_TRONC]),
        Layer("maidTronc", isActive=False, typeLayer=[TypeLayer.TRONC, TypeLayer.MAID]),
        Layer("face"),
        Layer("couetteUpRight"),
        Layer("mouth"),
        Layer("mouthOpenMid"),
        Layer("mouthOpen"),
        Layer("eyes"),
        Layer("eyesClose"),
        Layer("maidHat", isActive=False, typeLayer=[TypeLayer.HAT, TypeLayer.MAID]),
        Layer("hairTop"),
        Layer("eyesBorder"),
        Layer("axoHat1", isActive=False, typeLayer=[TypeLayer.HAT, TypeLayer.AXO_HAT])
    ]

    # loop update.
    while not pyray.window_should_close():

        pyray.begin_drawing()
        pyray.clear_background(backgroundColor)
        
        # draw layers.
        for l in layers:
            l.draw()

        pyray.end_drawing()

        # wait update (frame rate).
        await asyncio.sleep(0)


    # free layers.
    for l in layers:
        l.destroy()

    # close window.
    pyray.close_window()



asyncio.run(main())