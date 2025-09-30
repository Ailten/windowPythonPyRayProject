import pyray # python3 -m pip install raylib==5.5.0.3
import asyncio # to call async func from a sync.
from classFolder.Layer import Layer
from classFolder.TypeLayer import TypeLayer

# Doc : https://electronstudio.github.io/raylib-python-cffi/pyray.html#pyray.Color

# ----------> Main function.

async def main():

    # TODO : 
    # set rotation (and origine).
    # set translation.
    # set animation blink.
    # set animation talk.


    # build a window.
    pyray.init_window(Layer.defaultSizeX, Layer.defaultSizeY, "pngtuberAilt_V3")
    backgroundColor = pyray.Color(0, 0, 255, 255)
    fps = 30
    pyray.set_target_fps(fps)
    timeMilisec = 0
    timeIncrement = 1000/fps

    layers = [
        Layer("axoHat2", 
            isActive=False, 
            typeLayer=[TypeLayer.HAT, TypeLayer.AXO_HAT]),
        Layer("couetteLeft"),
        Layer("couetteRight"),
        Layer("couetteUpLeft"),
        Layer("tronc", 
            typeLayer=[TypeLayer.TRONC, TypeLayer.DEFAULT_TRONC]),
        Layer("maidTronc", 
            isActive=False, 
            typeLayer=[TypeLayer.TRONC, TypeLayer.MAID]),
        Layer("face"),
        Layer("couetteUpRight"),
        Layer("mouth"),
        Layer("mouthOpenMid"),
        Layer("mouthOpen"),
        Layer("eyes"),
        Layer("eyesClose"),
        Layer("maidHat", 
            isActive=False, 
            typeLayer=[TypeLayer.HAT, TypeLayer.MAID]),
        Layer("hairTop"),
        Layer("eyesBorder"),
        Layer("axoHat1", 
            isActive=False, 
            typeLayer=[TypeLayer.HAT, TypeLayer.AXO_HAT])
    ]

    # loop update.
    while not pyray.window_should_close():

        pyray.begin_drawing()
        pyray.clear_background(backgroundColor)
        
        # draw layers.
        for l in layers:
            l.draw(timeMilisec)

        pyray.end_drawing()

        # increase time.
        timeMilisec += timeIncrement


    # free layers.
    for l in layers:
        l.destroy()

    # close window.
    pyray.close_window()



asyncio.run(main())