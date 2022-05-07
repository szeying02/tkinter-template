import tkinter as tk
from tkinter import ttk
import tkmacosx as tkm

#########################################
#  Page 2                               #
#   1.  Display Table of Results Frame  #
#   2.  Search Table Results Frame      #
#########################################

####################
#   Page 2 Frame   #
####################

class page_2_frame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # create the canvas to place objects in
        canvas = tk.Canvas(self, width = 500, height = 500)
        canvas.pack(fill = "both")
        canvas.create_image(500, 0, image = controller.bg, anchor = "ne")

        # creating the text on the canvas
        canvas.create_text(250, 40, text = "Page 2", font = controller.title_font, fill = "white")
        canvas.create_text(250, 70, text = "Select one of the Options below:", font=controller.sub_font, fill="white")
        
        # creating the buttons
        display_results_button = tkm.Button(self, text = "Display Table of Results Template", bg = controller.button_colour, fg = "white", highlightthickness = 3, command = lambda: controller.add_display_frame(display_results_frame))
        display_results_button.config(highlightbackground = "white", highlightcolor = "white")
        search_button = tkm.Button(self, text = "Search Table Results Template", bg = controller.button_colour, fg = "white", highlightthickness = 3, command = lambda: controller.add_display_frame(search_frame))
        search_button.config(highlightbackground = "white", highlightcolor = "white")
        back_button = tkm.Button(self, text = "Back to Start Page", bg = controller.button_colour, fg = "white", highlightthickness = 3, command = lambda: controller.display_frame("start_frame"))
        back_button.config(highlightbackground = "white", highlightcolor = "white")
        
        # placing the buttons onto the canvas
        display_results_button_canvas = canvas.create_window(250, 120, anchor = "center", window = display_results_button)
        search_button_canvas = canvas.create_window(250, 160, anchor = "center", window = search_button)
        back_button_canvas = canvas.create_window(250, 200, anchor = "center", window = back_button)
        
##################################################
# Page 2 -- (1) Display Table of Results Frame   #
# Directly display desired results in a table    #
##################################################

class display_results_frame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label_img = tk.Label(self, image = controller.bg)
        label_img.place(x = 0, y = 0, relwidth = 1, relheight = 1)
        self.results_window()

    def get_results(self):
        """gets all desired results from the database"""
        results = []
        # conduct your own search in your database and input it into results using the input_text keyed in previously
        # the example below assumes a total of 3 fields to be displayed in the results table
        # each search result is stored in a tuple of the 3 fields: ("1", "2", "3") and appended to results
        results = [("01", "This is a Long Text", "Short"), ("02", "Another Long Test", "Text"), ("03", "Third Long Test", "Here")]
        return results

    def results_window(self):
        """pop-up the table window"""
                
        # create new small window on top of existing window
        window = tk.Toplevel()
        
        # restricting the size of the window
        window.minsize(width = 540, height = 320)
        window.maxsize(width = 540, height = 320)
        
        window.title("Display Results")
        
        # setting the background colour of window
        window.configure(bg = self.controller.results_colour)

        # create and place the header
        header = tk.Label(window, text = "Report", font = self.controller.title_font, bg = self.controller.results_colour, fg = "white")
        header.grid(row = 0, column = 0, columnspan = 2, pady = 5)

        # creating the table -- tree
        cols = ("id", "long_text", "short_text")
        tree = ttk.Treeview(window, columns = cols, show = "headings")
        tree.column("# 1", anchor = "center", stretch = "no", width = 115)
        tree.heading("id", text = "ID")
        tree.column("# 2", stretch = "no", width = 280)
        tree.heading("long_text", text = "Long Text")
        tree.column("# 3", stretch = "no", width = 125)
        tree.heading("short_text", text = "Short Text")

        results = self.get_results()

        # input results into the table
        for result in results:
            tree.insert('', tk.END, values=result)
        
        # place the table
        tree.grid(row = 1, column = 0, sticky = "nsew")

        # place a scorll bar to the right of the table
        scrollbar = ttk.Scrollbar(window, orient = tk.VERTICAL, command = tree.yview)
        tree.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=1, column=1, sticky="ns")

       # create and place the button
        back_button = tkm.Button(window, text="Back", command = lambda: self.revert_window(window), bg = self.controller.button_colour, fg = "white", highlightthickness = 3)
        back_button.config(highlightbackground = "white", highlightcolor = "white")
        back_button.grid(row = 2, column = 0, columnspan = 2, pady = 6)

    def revert_window(self, window):
        window.destroy()
        return self.controller.display_frame("page_2_frame")

####################################################################
# Page 2 -- (2) Search Table Results Frame                         #
# Search the databse based on a field before displaying results    #
####################################################################

class search_frame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # create the canvas to place objects in
        canvas = tk.Canvas(self, width = 500, height = 500)
        canvas.pack(fill = "both")
        canvas.create_image(250, 0, image = controller.bg_sub, anchor = "n")

        # creating the text on the canvas
        canvas.create_text(250, 40, text = "Search Template", font = controller.title_font, fill = "white", anchor = "center")
        canvas.create_text(50, 90, text = "Search Field", font = controller.regular_font, anchor="w", fill = "white")

        # creating input box -- to input the field to search
        search_field_entry = tk.Entry(self)

        # assigning the input text box to a class attribute for future retrievals
        self.search_field = search_field_entry

        # button creation
        search_button = tkm.Button(self, text = "Search", command = self.results_window, bg = controller.button_colour, fg = "white", highlightthickness = 3)
        search_button.config(highlightbackground = "white", highlightcolor = "white")
        back_button = tkm.Button(self, text = "Back to Page 2", command = lambda: controller.display_frame("page_2_frame"), bg = controller.button_colour, fg = "white", highlightthickness = 3)
        back_button.config(highlightbackground = "white", highlightcolor = "white")
        
        # placing the input box and buttons onto the canvas
        search_field_entry_canvas = canvas.create_window(280, 90, anchor = "center", window = search_field_entry)
        search_button_canvas = canvas.create_window(50, 130, anchor = "w", window = search_button)
        back_button_canvas = canvas.create_window(450, 130, anchor = "e", window = back_button)

    def get_search_field(self):
        """get the text keyed into the search field"""
        return self.search_field.get()

    def get_search_results(self):
        """gets the search result from the database"""
        input_text = self.get_search_field()
        results = []
        # conduct your own search in your database and input it into results using the input_text keyed in previously
        # the example below assumes a total of 3 fields to be displayed in the results table
        # each search result is stored in a tuple of the 3 fields: ("1", "2", "3") and appended to results
        results = [("01", "This is a Long Text", "Short"), ("02", "Another Long Test", "Text"), ("03", "Third Long Test", "Here")]
        return results

    def results_window(self):
        """pop-up the tabled results in a new window"""
        
        # create new small window on top of existing window
        window = tk.Toplevel()
        
        # restricting the size of the window
        window.minsize(width = 540, height = 320)
        window.maxsize(width = 540, height = 320)
        
        window.title("Search Results")

        # setting the background colour of window
        window.configure(bg = self.controller.results_colour)

        # create and place the header
        header = tk.Label(window, text="Search Results", font = self.controller.title_font, bg = self.controller.results_colour, fg = "white")
        header.grid(row = 0, column = 0, columnspan = 2, pady = 5)

        # creating the table -- tree
        cols = ("id", "long_text", "short_text")
        tree = ttk.Treeview(window, columns = cols, show = "headings")
        tree.column("# 1", anchor = "center", stretch = "no", width = 115)
        tree.heading("id", text = "ID")
        tree.column("# 2", stretch = "no", width = 280)
        tree.heading("long_text", text = "Long Text")
        tree.column("# 3", stretch = "no", width = 125)
        tree.heading("short_text", text = "Short Text")

        results = self.get_search_results()

        # input results into the table
        for result in results:
            tree.insert('', tk.END, values = result)
        
        # place the header
        tree.grid(row = 1, column = 0, sticky = "nsew")

        # place a scorll bar to the right of the table
        scrollbar = ttk.Scrollbar(window, orient = tk.VERTICAL, command = tree.yview)
        tree.configure(yscroll = scrollbar.set)
        scrollbar.grid(row = 1, column = 1, sticky = "ns")
       
       # create and place the button
        back_button = tkm.Button(window, text = "Back", command = window.destroy, bg = self.controller.button_colour, fg = "white", highlightthickness = 3)
        back_button.config(highlightbackground = "white", highlightcolor = "white")
        back_button.grid(row = 2, column = 0, columnspan = 2, pady = 6)
