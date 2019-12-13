# Programmer - python_scripts (Abhijith Warrier)

# PYTHON GUI TO CREATE A SIMPLE NOTEPAD

# Importing necessary packages
import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter import  messagebox

# Creating class TkLogin
class TkNotepad(tk.Frame):

    # Initializing
    def __init__(self, master):

        Frame.__init__(self, master)
        self.CreateWidgets()

#---

    # Creating Widgets
    def CreateWidgets(self):

        self.saveFileLabel = Label(self, text="SAVE FILE : ", font = "bold")
        self.saveFileLabel.grid(row = 0,column = 0,pady = 10, padx = 10)

        self.saveFileEntry = Entry(self, width = 50, textvariable = file,
                                   bg = "silver")
        self.saveFileEntry.grid(row = 0,column = 1,pady = 10, padx = 10)

        self.FileBrowseButton = Button(self, text ="BROWSE", width = 20,
                                       command = self.Browse, bg = "yellow")
        self.FileBrowseButton.grid(row = 0,column = 2,pady = 10, padx = 10)

        self.saveFileLabel = Label(self, text="FILE TEXT : ", font = "bold")
        self.saveFileLabel.grid(row = 1,column = 0)

        self.writeFileText = Text(self, width = 80, height = 30,bg = "silver")
        self.writeFileText.grid(row = 2,column = 0,columnspan = 3,
                                pady = 10, padx = 10)

        self.ClearText = Button(self, text ="CLEAR TEXT", width = 20,
                                command = self.Clear, bg = "red")
        self.ClearText.grid(row = 3,column = 0,pady = 10, padx = 10)

        self.FileWrite = Button(self, text ="SAVE TEXT", width = 20,
                                command = self.Write, bg = "green")
        self.FileWrite.grid(row = 3,column = 2,pady = 10, padx = 10)

#---

    # Function to browse and save the file
    def Browse(self):

        fileName = filedialog.asksaveasfilename(initialdir = "C:\Python\PyNotepad",
                                filetypes = (("Text File (*.txt)","*.txt"),
                                ("DOC File (*.doc)","*.doc"), ("All File")))
        self.saveFileEntry.insert(0,fileName)

    # Function to Clear the contents of the Text
    def Clear(self):
        self.writeFileText.delete("1.0",END)

    # Function to Write the contents of the Text to the File
    def Write(self):
        fileWrite = file.get()

        # Openining the file with mode as w (write)
        fileOpen = open(fileWrite,"w")

        # Getting the contents of the Text widget from the beginning
        # till the end
        textToWrite = self.writeFileText.get("1.0",END)

        # Writing the contents to the file
        fileOpen.write(textToWrite)

        # Displaying message
        messagebox.showinfo("SUCCESS!","FILE SAVED")
#---

# Creating object root of tk
root = tk.Tk()

# Setting title
root.title("PyNotepad")

# Disabling resizing of window
root.resizable(False, False)

# Setting size
root.geometry("690x620")

# Creating tkinter variable
file = StringVar(root)

# Creating object of class SimpleCal
frame = TkNotepad(root)

# Organising label before placing them
# in parent
frame.pack()

# Defining infinite loop to run application
frame.mainloop()
#---