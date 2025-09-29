import pyray # python3 -m pip install raylib==5.5.0.3
import asyncio # to call async func from a sync.

# Doc : https://electronstudio.github.io/raylib-python-cffi/pyray.html#pyray.Color

# ----------> Main function.

async def main():

    # TODO : 
    # resize window at a right size for pngtuber sprites.
    # make class Layers (like Entity).

    # build a window.
    pyray.init_window(500, 500, "pngtuberAilt_V3")
    backgroundColor = pyray.Color(0, 0, 255, 255)

    # loop update.
    while not pyray.window_should_close():

        pyray.begin_drawing()
        pyray.clear_background(backgroundColor)
        pyray.draw_text("Hello world", 190, 200, 20, pyray.BLACK)
        pyray.end_drawing()

        await asyncio.sleep(0)

    # close window.
    pyray.close_window()



asyncio.run(main())