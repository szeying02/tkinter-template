import tkinter as tk
import tkmacosx as tkm
from tkinter import font as tkfont
from PIL import ImageTk, Image, ImageOps

from page_1_file import *
from page_2_file import *

class window(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # setting up the default fonts that will be used across all pages
        self.title_font = tkfont.Font(family = "Helvetica", size = 24, weight = "bold")
        self.sub_font = tkfont.Font(family = "Helvetica", size = 16, weight = "bold")
        self.regular_font = tkfont.Font(family = "Helvetica", size = 14)
        self.italic_font = tkfont.Font(family = "Helvetica", size = 14, slant = "italic")

        # setting up the default colours that will be used across all pages
        self.success_colour = "#436b5d"
        self.error_colour = "#7d2338"
        self.confirmation_colour = "#434d6b"
        self.button_colour = "#2F4F4F"
        self.results_colour = "#434d6b"
        
        # setting up the default backgrounds images that will be used across all pages
        self.bg = ImageTk.PhotoImage(Image.open("assets/bg_main.jpg"))
        bg_sub_img = Image.open("assets/bg_sub.jpg")
        bg_sub_img = ImageOps.mirror(bg_sub_img.resize((879, 595), Image.ANTIALIAS))
        self.bg_sub =  ImageTk.PhotoImage(bg_sub_img)
        
        # the container is where we'll stack a bunch of frames on top of each other
        # to display a particular frame, it needs to be raised above the rest
        container = tk.Frame(self)
        self.container = container
        container.pack(side = "top", fill = "both", expand = True)
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)

        # store all frames in a dictionary
        self.frames = {}
        
        # add and display the first frame / start page
        self.add_display_frame(start_frame)
        
    def add_frame(self, frame_class):
        """add a frame for the given frame"""
        frame_name = frame_class.__name__
        frame = frame_class(parent = self.container, controller = self)
        self.frames[frame_name] = frame
        frame.grid(row = 0, column = 0, sticky = "nsew")

    def display_frame(self, frame_name):
        """show a frame for the given frame name"""
        frame = self.frames[frame_name]
        frame.tkraise()

    def add_display_frame(self, frame_class):
        """add and display a frame for a given frame"""
        self.add_frame(frame_class)
        frame_name = frame_class.__name__
        self.display_frame(frame_name)

# Start Page Frame
class start_frame(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # create the canvas to place objects in
        canvas = tk.Canvas(self, width = 500, height = 500)
        canvas.pack(fill = "both")
        canvas.create_image(500, 0, image = controller.bg, anchor = "n")
        
        # creating the text on the canvas
        canvas.create_text(250, 40, text = "tkinter template", font = controller.title_font, fill = "white")

        # creating the buttons
        page_1_button = tkm.Button(self, text = "Page 1", bg = "#2F4F4F", fg = "white", highlightthickness=3, command=lambda: controller.add_display_frame(page_1_frame))
        page_1_button.config(highlightbackground = "#FFFFFF", highlightcolor = "#FFFFFF")
        page_2_button = tkm.Button(self, text ="Page 2", bg = "#2F4F4F", fg = "white", highlightthickness=3, command=lambda: controller.add_display_frame(page_2_frame))
        page_2_button.config(highlightbackground = "#FFFFFF", highlightcolor = "#FFFFFF")

        # placing the buttons onto the canvas
        page_1_button_canvas = canvas.create_window(250, 120, anchor = "center", window = page_1_button)
        page_2_button_canvas = canvas.create_window(250, 170, anchor = "center", window = page_2_button)


root = window()
root.title("tkinter template")

# fixing the size of the gui window
root.minsize(width = 500, height = 500)
root.maxsize(width = 500, height = 500)
root.mainloop()
