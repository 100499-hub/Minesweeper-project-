from tkinter import *
import settings
import utils

root = Tk()


root.configure(bg="black")
root.geometry(f'{settings.width}x{settings.height}')
root.title("Minesweeper Game")
root.resizable(False, False)

top_frame = Frame(
    root,
    bg='black',
    width=settings.width,
    height=utils.heigth_prct(25)
)
top_frame.place(x=0, y=0)

left_frame = Frame(
    root,
    bg='black',
    width=utils.width_prct(25),
    height=utils.heigth_prct(75)
)

left_frame.place(x=0, y=utils.heigth_prct(25))

center_frame = Frame(
    root,
    bg='black',
    width=utils.width_prct(75),
    height=utils.heigth_prct(75)
)
center_frame.place(
    x=utils.width_prct(25),
    y=utils.heigth_prct(25)
)

# Run the window
root.mainloop()
