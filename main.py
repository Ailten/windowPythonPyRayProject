import pyray # python3 -m pip install raylib==5.5.0.3
import asyncio # to call async func from a sync.
from classFolder.Layer import Layer
from classFolder.TypeLayer import TypeLayer
from classFolder.Microphone import Microphone

# Doc : https://electronstudio.github.io/raylib-python-cffi/pyray.html#pyray.Color

# ----------> Main function.

async def main():

    # TODO : 

    # debug decibel get (function static updateMicrophone is not call, maybe lock in the main async loop).
    # debug amount of decibel min and max on animation mouth.


    # build a window.
    pyray.init_window(Layer.defaultSizeX, Layer.defaultSizeY, "pngtuberAilt_V3")
    backgroundColor = pyray.Color(0, 0, 255, 255)
    fps = 30
    pyray.set_target_fps(fps)
    timeMilisec = 0
    timeIncrement = int(1000/fps)

    layers = [
        Layer("axoHat2", 
            isActive=False, 
            typeLayer=[TypeLayer.HAT, TypeLayer.AXO_HAT],
            update=Layer.faceUpdate),
        Layer("couetteLeft",
            origine=pyray.Vector2(158, 488),
            update=Layer.couetteUpdate),
        Layer("couetteRight",
            origine=pyray.Vector2(250, 480),
            update=Layer.couetteUpdate),
        Layer("couetteUpLeft",
            origine=pyray.Vector2(147, 345),
            update=Layer.couetteUpdate),
        Layer("tronc", 
            typeLayer=[TypeLayer.TRONC, TypeLayer.DEFAULT_TRONC]),
        Layer("maidTronc", 
            isActive=False, 
            typeLayer=[TypeLayer.TRONC, TypeLayer.MAID]),
        Layer("face",
            update=Layer.faceUpdate),
        Layer("couetteUpRight",
            origine=pyray.Vector2(270, 345),
            update=Layer.couetteUpdate),
        Layer("mouth",
            update=Layer.mouthUpdate),
        Layer("mouthOpen",
            update=Layer.mouthUpdate),
        Layer("eyes",
            update=Layer.blinkUpdate),
        Layer("eyesClose",
            update=Layer.blinkUpdate),
        Layer("maidHat", 
            isActive=False, 
            typeLayer=[TypeLayer.HAT, TypeLayer.MAID]),
        Layer("hairTop",
            update=Layer.faceUpdate),
        Layer("eyesBorder",
            update=Layer.blinkUpdate),
        Layer("axoHat1", 
            isActive=False, 
            typeLayer=[TypeLayer.HAT, TypeLayer.AXO_HAT],
            update=Layer.faceUpdate)
    ]

    # loop update.
    while not pyray.window_should_close():

        pyray.begin_drawing()
        pyray.clear_background(backgroundColor)

        # get decibel from microphone.
        asyncio.create_task(Microphone.updateDecibel())
        
        # get decibel (fix for all the loop update).
        decibel = Microphone.decibel
        #print(f"Db : {decibel}")

        # draw layers.
        for l in layers:
            if not l.isActive:
                continue
            if not l.update(l, timeMilisec, decibel):
                continue
            l.draw(timeMilisec)

        # increase time.
        timeMilisec += timeIncrement

        await asyncio.sleep(0.01)

        pyray.end_drawing()


    # free layers.
    for l in layers:
        l.destroy()

    # close window.
    pyray.close_window()


# ---------->

# call main.
asyncio.run(main())