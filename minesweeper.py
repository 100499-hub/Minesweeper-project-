from tkinter import *
import settings
import utils
from cell import Cell

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


for x in range(settings.grid_size):
    for y in range(settings.grid_size):
        c = Cell(x, y)
        c.create_btn_object(center_frame)
        c.cell_btn_object.grid(
            column=y, row=x
        )
# Call the label from the Cell class
Cell.create_cell_count_label(left_frame)
Cell.cell_count_label_object.place(
    x=0,
    y=0
)

Cell.randomize_mines()

# Run the window
root.mainloop()
