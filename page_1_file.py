import tkinter as tk
import tkmacosx as tkm

#####################################
#  Page 1                           #
#   1.  Input Template Frame        #
#####################################

####################
#   Page 1 Frame   #
####################

class page_1_frame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # create the canvas to place objects in
        canvas = tk.Canvas(self, width = 500, height = 500)
        canvas.pack(fill = "both")
        canvas.create_image(0, 0, image = controller.bg, anchor = "nw")
        
        # creating the text on the canvas
        canvas.create_text(250, 40, text = "Page 1", font = controller.title_font, fill = "white")
        canvas.create_text(250, 70, text = "Select one of the Options below:", font = controller.sub_font, fill = "white")

        # creating the buttons
        input_frame_button = tkm.Button(self, text = "Input Template", bg = controller.button_colour, fg = "white", highlightthickness = 3, command = lambda: controller.add_display_frame(input_frame))
        input_frame_button.config(highlightbackground = "white", highlightcolor = "white")
        back_button = tkm.Button(self, text = "Back to Start Page", bg = controller.button_colour, fg = "white", highlightthickness = 3, command = lambda: controller.display_frame("start_frame"))
        back_button.config(highlightbackground = "white", highlightcolor = "white")

        # placing the buttons onto the canvas
        creation_button_canvas = canvas.create_window(250, 120, anchor = "center", window = input_frame_button)
        back_button_canvas = canvas.create_window(250, 160, anchor = "center", window = back_button)

##############################################
# Page 1 -- (1) Input Template Frame         #
##############################################

class input_frame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # create the canvas to place objects in
        canvas = tk.Canvas(self, width = 500, height = 500)
        canvas.pack(fill = "both")
        canvas.create_image(-100, -77, image = controller.bg_sub, anchor = "nw")
        
        # creating the header & sub-header texts
        canvas.create_text(250, 40, text = "Membership Creation", font = controller.title_font, fill = "white")
        canvas.create_text(250, 70, text = "To Create Member, Please Enter Requested Information Below:", font=controller.sub_font, fill = "white")

        # creating the texts on the canvas
        canvas.create_text(50, 110, text = "Input 1", font = controller.regular_font, anchor = "w", fill = "white")
        canvas.create_text(50, 140, text = "Input 2", font = controller.regular_font, anchor = "w", fill = "white")
        canvas.create_text(50, 170, text = "Input 3", font = controller.regular_font, anchor = "w", fill = "white")
        canvas.create_text(50, 200, text = "Input 4", font = controller.regular_font, anchor = "w", fill = "white")
        canvas.create_text(50, 230, text = "Input 5", font = controller.regular_font, anchor = "w", fill = "white")
        
        # creating input boxes
        input1_entry = tk.Entry(self)
        input2_entry = tk.Entry(self)
        input3_entry = tk.Entry(self)
        input4_entry = tk.Entry(self)
        input5_entry = tk.Entry(self)

        # assigning the input text boxes to class attribute for future retrievals
        self.input1 = input1_entry
        self.input2 = input2_entry
        self.input3 = input3_entry
        self.input4 = input4_entry
        self.input5 = input5_entry

        # button creation
        confirmation_button = tkm.Button(self, text="Confirm", bg=controller.button_colour, fg="white", highlightthickness=3, command=self.confirmation_popup_window)
        confirmation_button.config(highlightbackground = "white", highlightcolor= "white")
        back_button = tkm.Button(self, text="Back to Page 1", bg=controller.button_colour, fg="white", highlightthickness=3, command=lambda: controller.display_frame("page_1_frame"))
        back_button.config(highlightbackground = "white", highlightcolor= "white")

        # placing the input boxes and buttons onto the canvas
        input1_entry_canvas = canvas.create_window(220, 110, anchor = "center", window = input1_entry)
        input2_entry_canvas = canvas.create_window(220, 140, anchor = "center", window = input2_entry)
        input3_entry_canvas = canvas.create_window(220, 170, anchor = "center", window = input3_entry)
        input4_entryy_canvas = canvas.create_window(220, 200, anchor = "center", window = input4_entry)
        input5_entry_canvas = canvas.create_window(220, 230, anchor = "center", window = input5_entry)
        confirmation_button_canvas = canvas.create_window(50, 270, anchor = "w", window = confirmation_button)
        back_button_canvas = canvas.create_window(450, 270, anchor = "e", window = back_button)

    def get_inputs(self):
        """get inputs from the input boxes"""
        input1_text = self.input1.get()
        input2_text = self.input2.get()
        input3_text = self.input3.get()
        input4_text = self.input4.get()
        input5_text = self.input5.get()
        return (input1_text, input2_text, input3_text, input4_text, input5_text)
    
    def confirmation_popup_window(self):
        # create new small window on top of existing window
        window = tk.Toplevel()
        
        # restricting the size of the window
        window.minsize(width = 400, height = 400)
        window.maxsize(width = 400, height = 400)

        # create the canvas to place objects in
        canvas = tk.Canvas(window, width = 400, height = 400, bg = self.controller.confirmation_colour)
        canvas.pack(fill = "both")

        # creating the text on the canvas
        canvas.create_text(200, 30, text = "Please Confirm Details to Be Correct:", font=self.controller.sub_font, fill="white")

        # obtain the inputs from the input boxes
        input1_text, input2_text, input3_text, input4_text, input5_text = self.get_inputs()

        # creating the text on the canvas
        canvas.create_text(20, 70, text = "Input 1", font = self.controller.regular_font, anchor = "w", fill = "white")
        canvas.create_text(20, 100, text = "Input 2", font = self.controller.regular_font, anchor = "w", fill = "white")
        canvas.create_text(20, 130, text = "Input 3", font = self.controller.regular_font, anchor = "w", fill = "white")
        canvas.create_text(20, 160, text = "Input 4", font = self.controller.regular_font, anchor = "w", fill = "white")
        canvas.create_text(20, 190, text = "Input 5", font = self.controller.regular_font, anchor = "w", fill = "white")
        
        canvas.create_text(120, 70, text = input1_text, font = self.controller.regular_font, anchor = "w", fill = "white")
        canvas.create_text(120, 100, text = input2_text, font = self.controller.regular_font, anchor = "w", fill = "white")
        canvas.create_text(120, 130, text = input3_text, font = self.controller.regular_font, anchor = "w", fill = "white")
        canvas.create_text(120, 160, text = input4_text, font = self.controller.regular_font, anchor = "w", fill = "white")
        canvas.create_text(120, 190, text = input5_text, font = self.controller.regular_font, anchor = "w", fill = "white")
        
                # placing the buttons onto the canvas
        proceed_button = tkm.Button(window, text = "Proceed", command = lambda: self.check_valid_inputs(window), bg = self.controller.button_colour, fg = "white", highlightthickness = 3)
        proceed_button.config(highlightbackground = "white", highlightcolor= "white")
        message_button = tkm.Button(window, text = "Back", command = window.destroy, bg = self.controller.button_colour, fg = "white", highlightthickness = 3)
        message_button.config(highlightbackground = "white", highlightcolor= "white")
        proceed_button_canvas = canvas.create_window(20, 230, anchor = "w", window = proceed_button)
        message_button_canvas = canvas.create_window(380, 230, anchor = "e", window = message_button)

    def check_valid_inputs(self, window):
        """checks whether the inputs are valid before popping up the success window (if inputs are valid) or error window (inputs are invalid)"""
        valid = True # setting valid as true for the default here
        
        # destroy the confirmation window
        window.destroy()
        if valid:
            return self.success_popup_window()
        else:
            return self.error_popup_window()

    def success_popup_window(self):
        """pop-up the success window"""
        # create new small window on top of existing window
        window = tk.Toplevel()

        # restricting the size of the window
        window.minsize(width = 300,height = 300)
        window.maxsize(width = 300,height = 300)

        window.title("Success!")
        
        # setting the background colour of window
        window.configure(bg=self.controller.success_colour)

        # adding text & button
        success_label = tk.Label(window, text = "Success!", font = self.controller.title_font, bg = self.controller.success_colour, fg = "white")
        message_label = tk.Label(window, text = "All inputs are valid", font = self.controller.regular_font, bg = self.controller.success_colour, fg = "white")
        message_button = tkm.Button(window, text="Back", command = window.destroy, bg = self.controller.button_colour, fg = "white", highlightthickness = 3)
        message_button.config(highlightbackground = "white", highlightcolor = "white")

        #placing text & button
        success_label.pack(pady = 5)
        message_label.pack(pady = 5)
        message_button.pack()

    def error_popup_window(self):
        """pop-up the error window"""
        # create new small window on top of existing window
        window = tk.Toplevel()

        # restricting the size of the window
        window.minsize(width = 300, height = 300)
        window.maxsize(width = 300, height = 300)
        
        window.title("Error!")

        # setting the background colour of window
        window.configure(bg=self.controller.error_colour)
        
        # adding text & button
        error_label = tk.Label(window, text = "Error!", font = self.controller.title_font, bg = self.controller.error_colour, fg = "white")
        message_label = tk.Label(window, text = "One or more inputs are invalid", wraplength = 280, justify = "center", font=self.controller.regular_font, bg = self.controller.error_colour, fg = "white")
        message_button = tkm.Button(window, text = "Back", command = window.destroy, bg = self.controller.button_colour, fg = "white", highlightthickness = 3)
        message_button.config(highlightbackground = "white", highlightcolor = "white")

        #placing text & button
        error_label.pack(pady = 5)
        message_label.pack(pady = 5)
        message_button.pack()
