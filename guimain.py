from tkinter import *
my_window = Tk()
my_window.title("Whole Sight Review")
canvas=Canvas(my_window, width = 800, height = 300)
canvas.pack()

myimage=PhotoImage(file='WholeSightLOGO.png')
canvas.create_image(0,0, anchor= NW, image=myimage)
canvas.button_1 = Button(my_window,  background = 'black', foreground = "aqua", text="ENTER")
canvas.button_1.pack()
my_window.mainloop()
