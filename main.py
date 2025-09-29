import pyray # python3 -m pip install raylib==5.5.0.3
import asyncio # to call async func from a sync.


# ----------> Main function.

async def main():

    # build a window.
    pyray.init_window(500, 500, "Test")

    while not pyray.window_should_close():

        pyray.begin_drawing()
        pyray.clear_background(pyray.BLUE)
        pyray.draw_text("Hello world", 190, 200, 20, pyray.BLACK)
        pyray.end_drawing()
        await asyncio.sleep(0)

    # close window.
    pyray.close_window()



asyncio.run(main())