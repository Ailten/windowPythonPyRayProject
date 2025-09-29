import pyray # python3 -m pip install raylib==5.5.0.3
import asyncio # to call async func from a sync.
from classFolder.Layer import Layer

# Doc : https://electronstudio.github.io/raylib-python-cffi/pyray.html#pyray.Color

# ----------> Main function.

async def main():

    # TODO : 
    # resize window at a right size for pngtuber sprites.
    # make class Layers (like Entity).

    # build a window.
    pyray.init_window(Layer.defaultSizeX, Layer.defaultSizeY, "pngtuberAilt_V3")
    backgroundColor = pyray.Color(0, 0, 255, 255)

    layers = [
        Layer("axoHat2", isActive=False),
        Layer("couetteLeft"),
        Layer("couetteRight"),
        Layer("couetteUpLeft"),
        Layer("tronc"),
        Layer("maidTronc", isActive=False),
        Layer("face"),
        Layer("couetteUpRight"),
        Layer("mouth"),
        Layer("mouthOpenMid"),
        Layer("mouthOpen"),
        Layer("eyes"),
        Layer("eyesClose"),
        Layer("maidHat", isActive=False),
        Layer("hairTop"),
        Layer("eyesBorder"),
        Layer("axoHat1", isActive=False)
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