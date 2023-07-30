from tkinter import *
#importing Image Tk allows the image to be displayed, manipulated and modified
from PIL import ImageTk, Image
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText


#creating a class
class PhysicsQuizApp:
    def __init__(self):
        self.window = Tk() #creating the window for the GUI
        self.window.title("Physics Quiz") #Titling the window
        self.window.geometry("1050x600")#setting the dimensions for the window

# Creating frames in a class
#Creating a border on the frame
#setting the colour to black, relief indicats the border style should a solid line and bd means the width of the border should be 5 pixels
        self.frame1 = Frame(self.window, bd=5, relief="solid", highlightbackground="black")
        self.frame1.config(bg="#d38cb0")#set background colour by configuring the frame
        self.frame1.pack(fill="both", expand=True)#making the frame fit to the available space by making it expand both vertically and horizontally
        
        self.frame2 = Frame(self.window, bd=5, relief="solid", highlightbackground="black")
        self.frame2.config(bg="#ce9ca7")
        self.frame2.pack(fill="both", expand=True)

        self.frame3 = Frame(self.window, bd=5, relief="solid", highlightbackground="black")
        self.frame3.config(bg="#ce9ca7")
        self.frame3.pack(fill="both", expand=True)

        self.frame4 = Frame(self.window, bd=5, relief="solid", highlightbackground="black")
        self.frame4.config(bg="#ce9ca7")
        self.frame4.pack(fill="both", expand=True)

        self.frame5 = Frame(self.window, bd=5, relief="solid", highlightbackground="black")
        self.frame5.config(bg="light pink")
        self.frame5.pack(fill="both", expand=True)

        self.frame6 = Frame(self.window, bd=5, relief="solid", highlightbackground="black")
        self.frame6.config(bg="light pink")
        self.frame6.pack(fill="both", expand=True)


#setting the current frame to 1 so that switching frames is easier to keep track of
        self.current_frame = 1
#importing background image from file directory
        self.bg_image = ImageTk.PhotoImage(file="backdrop.jpg")
# importing the bg_image into the canvas.
#The canvas is used to draw on the window and allows other widgets, text, and images to be seen.
        self.my_canvas = Canvas(self.frame1, width=920, height=620) #setting the height and width of the canvas to match the dimensions of the window
        self.my_canvas.pack(fill="both", expand=True) # Fill and True allows the canvas to fit to the available space in the window
        self.my_canvas.create_image(0, 0, anchor=NW, image=self.bg_image) # creating the image in the canvas and positioning it "north west"
# creating labels into the canvas in the main window
#Setting the font, font size and making it bold to add to the aesthetic and making it more visually appealing
        self.label = Label(self.my_canvas, text="Physics Quiz", font=("Times New Roman", 20, "underline italic bold"))
        self.label.config(bg="#e4b1cc")#modifying the background colour of the widget using the colour's hex code
        self.label.place(x=350, y=50) #placing the label 350 pixels from the left of the window and 50 pixels from the top
#creating a label for Name of users
        self.label_name = Label(self.my_canvas, text="Name:", font=("Courier New", 14, "underline bold"))
        self.label_name.place(x=200, y=145)#placing the name label 200 pixels from the left and 145 pixels from the top
        self.label_name.config(bg="#ddeeff") #modifying the background of the label
#Creating a label for age for users
        self.label_age = Label(self.my_canvas, text="Age:", font=("Courier New", 14, "underline bold"))
        self.label_age.config(bg="#ddeeff")#modifying the background of the label
        self.label_age.place(x=200, y=200)#placing the age label 200 pixels from the left and 200 pixels from the top
#creating entry boxes for user's input 
        self.Name = Entry(self.my_canvas, font=("Times New Roman", 14)) #placing the entry box in the canvas and changing the font and font size for the input
        self.Name.place(x=300, y=150)#using the place method to put the entry box 300 pixels from the left and 150 pixels from the top
# validating the input into the 'NCEA level' entry box by registering the validate entry function
#This means that the input can customly validate the user's input with the specified conditions in the validate entry function
        self.validate_ncea_level = self.window.register(self.validate_entry)
#creating an entry box user's input for age
        self.age = Entry(self.my_canvas, font=("Times New Roman", 14))
        self.age.place(x=330, y=200) # placing the entry box 330 pixels from the left and 200 pixels from the top
#creating a label for the contents in frame 2
        self.label_contents = Label(self.frame2, text="Contents", font=("Times New Roman", 20, "underline italic bold"))
        self.label_contents.config(bg="#ce9ca7") #changing the background colour of the label
        self.label_contents.pack(pady=50)#positioning the label to have a vertical padding of 50 pixels
#creating a button in the canvas and setting its state to disabled so it cannot be accessed until it is triggered
    #the enter button is set to follow the button click function where it is only enabled with the next button is clicked
        self.button = Button(self.my_canvas, text="Enter", font=("Courier New", 14), bg="#b885cc", command=self.button_click, state="disabled")
#putting the enter button in the canvas while passing it through the window so it will be displayed on the created window
        self.button_window = self.my_canvas.create_window(470, 260, anchor="center", window=self.button)
#setting the next button to false to keep trach of whether or not it has been clicked
    #creating the next button
#my canvas is the parent widget to where the button will be placed
#the command allows to specify the function being called when the button is clicked.

        self.nextbtn_clicked = False
        self.next_button = Button(self.my_canvas, text="Next", font=("Courier New", 14), bg="#b885cc", command=lambda: [self.validate_entry(), self.enable_enter_button()])
        self.next_button.place(x=350, y=243)
        """
by making the command=lambda, multiple functions can be executed and perfom more complex
operations when the button is clicked such as validate the entry of the input in the entry boxes while
simultaneously enabling the enter button
"""
#adding another back button to the second frame so the user can switch between the main window and frame2
#the go back function is called through command to switch between the frames
        self.back_button = Button(self.frame2, text="Back", command=self.go_back, font=("Courier New", 14))
#using the pack method to position the button on the left side, anchoring it 'south west', and with a horizontal padding of 15, and a vertical padding of 15
        self.back_button.pack(side="left", anchor="sw", padx=(15, 0), pady=15)
        self.frame1.bind('<Configure>', self.resizer)
########################## Creating back buttons for each frame ###############################
        self.back_l3m = Button(self.frame3, text="Back", font=("Gerogia", 12), command=self.back)
        self.back_l3m.pack(side="left", anchor="sw", padx=(15, 0), pady=15)
        

        self.back_l3w = Button(self.frame4, text="Back", font=("Gerogia", 12), command = self.back)
        self.back_l3w.pack(side="left", anchor="sw", padx=(15, 0), pady=15)

        self.back_l3e = Button(self.frame5, text="Back", font=("Gerogia", 12), command = self.back)
        self.back_l3e.pack(side="left", anchor="sw", padx=(15, 0), pady=15)
#binding the resizer function to frame 1 so that when the configure event is triggered, the image is resized to fit the size or position of frame1
        self.Motion_img = PhotoImage(file="Motion.png") #importing the image from the file directory
        self.small_img2 = self.Motion_img.subsample(2)#making the image smaller by sampling it down by a scale factor of 2
        self.image_label1 = Label(self.frame2, image=self.small_img2)#making the image as a label in frame2 to make it easier to position on the window
        self.image_label1.pack(side="bottom", anchor="se")#positioning the image on the bottom side and centering it 'south east' on the window

        self.Atom_img = PhotoImage(file="Atom.png")#import image from file directory
        self.small_img1 = self.Atom_img.subsample(2)#making the image smaller by scaling it down by a factor of 2
        self.image_label2 = Label(self.frame2, image=self.small_img1)#making the image as a label
        self.image_label2.place(x=15, y=15)#placing the image 15 pixels from the left and 15 pixels from the top

    def back(self):
            if self.selected_frame:
                if self.frame3:
                    self.switch_frames(self.selected_frame)
                elif self.frame4:
                    self.switch_frames(self.selected_frame)
                elif self.frame5:
                    self.switch_frames(self.selected_frame)

    def resizer(self, size): #e represents the resize event that triggers the function
        bg = Image.open("backdrop.jpg")#setting the bg_image as global so it can be accessed from all functions
        #BICUBIC is a method to resize the image by scaling it so that it fits the window without blurring
        resized_bg = bg.resize((size.width, size.height), Image.BICUBIC)#resizing the image
        #size.width and size.height references the data of the canvas to resize the image to fit the canvas
        self.bg_image = ImageTk.PhotoImage(resized_bg)#recall the previous image in its resized form
        self.my_canvas.configure(width=self.window.winfo_width(), height=self.window.winfo_height())
        #Configuring the canvas allows the background image to resize to fit the maximum size of the window.
    #Using window.winfo allows Python to identify the window information and fit the background image accordingly.
        self.my_canvas.create_image(0, 0, image=self.bg_image, anchor="nw") #Place the resized image into the canvas and aligning it "north west" in the window
#defining the button_click function so that when the 'next' button is clicked, it will switch frames to the next frame

    def button_click(self):
        self.current_frame += 1 #allows the function to be called in a sequential order
        #when this function is used, it adds 1 to the current frame
        if self.current_frame == 2: #if the current frame is 2, switch to frame2 and so on
            #the if and elif statements check the value for the current frames and switches the frames accordingly
            self.switch_frames(self.frame2)
        elif self.current_frame == 3:
            self.switch_frames(self.frame3)
        elif self.current_frame == 4:
            self.switch_frames(self.frame4)
        elif self.current_frame == 5:
            self.switch_frames(self.frame5)
        elif self.current_frame == 6:
            self.switch_frames(self.frame6)
            
    def switch_frames(self, frame=None):
        self.frame1.pack_forget() #the switch frames method handles the display of the frames in the GUI
        self.frame2.pack_forget() #.pack_forget is the method used to to hide the frames from view and can be shown later
        self.frame3.pack_forget()#the purpose of this is so that when switching frames, the frames aren't split in the window
        self.frame4.pack_forget()
        self.frame5.pack_forget()
        self.frame6.pack_forget()
        if frame:# if no arugment for frame is passed, it will default to none and all the frames will be hidden
            #passing the arugment for a specific frame allows that frame to be shown to fit the window by using fill="both" and expand=true
            frame.pack(fill="both", expand=True)

#defining the go back function so that when the back button is clicked, it will go back to the previous frame
    def go_back(self):
        self.current_frame -= 1 #setting the decrement to 1 so that when switching frames, it goes back by 1 each time
        #when the function is used, it subtracts 1 from the current frame
        if self.current_frame == 1:
            #The if and elif statements checks the value of the current frame and switches frames accordingly
            #Example, if the current frame is 4, it will display frame4 
            self.switch_frames(self.frame1)
        elif self.current_frame == 2:
            self.switch_frames(self.frame2)
        elif self.current_frame == 3:
            self.switch_frames(self.frame3)
        elif self.current_frame == 4:
            self.switch_frames(self.frame4)
        elif self.current_frame == 5:
            self.switch_frames(self.frame5)
        elif self.current_frame == 6:
            self.switch_frames(self.frame6)

#defining a method to validate the input into the entry boxes by creating conditions for what each box should have
    def validate_entry(self):
        # .get allows the data to be retrieved from the entry box widgets to validate if it satisfies the below conditions
        name = self.Name.get()
        age = self.age.get()
#creating conditions
#if the user doesn't enter anything in the entry boxes and try to click the button, an error message will come up
        if not name or not age:
            messagebox.showerror("Error", "Please enter values in all fields to continue")
        elif not name.isalpha():
#if the entry box for name contains a value that is not alphabetic, it will show an error message    
            messagebox.showerror("Error", "Please enter only alphabetic characters for the Name field")
        elif not age.isdigit():
            messagebox.showerror("Error", "Please enter a valid positive integer for age")
        elif int(age) < 16:
#if the age is not greater than 16, it will show an error message            
            messagebox.showerror("Error", " Sorry, you must be 16 or older :(")
        else:
#if the conditions are satified and the required input is in each box a success message will show
            messagebox.showinfo("Success", "Please press Enter to continue :)")
            self.button.config(state="normal")
#it allows the user to interact with the program more efficiently
#defining the function to enable the enter button, after the next button is clicked
    def enable_enter_button(self):
        if self.nextbtn_clicked:  #If the next button is clicked, enable the enter button by setting its state as normal
            self.button.config(state="normal") #setting the state to normal so it executes the function when it is triggered
#creating a list box
    def create_listbox(self):
# Define the contents using dictionaries
#square brackets used to define the list of items as well as organise each items by creating new lists based on the existing lists
#Curly brackets are used to store the data into the dictonary
        self.contents = [
            {
                "title": "Level 3: Mechanics", #fourth list with level 3 mechanics content
                "content": [
                    " - Transitional Motion",
                    " - Circular Motion",
                    " - Rotational Motion",
                    " - Simple Harmonic Motion"
                    ]
                },
            {
                "title": "Level 3: Waves", #fifth list with level 3 waves content
                "content": [
                    " - Diffraction & Interference",
                    " - Standing Waves",
                    " - Harmonics",
                    " - Resonance & Beats",
                    " - The Doppler Effect"
                    ]
                },
            {
                "title": "Level 3: Electricty & Magnetism", #sixth list with level 3 electricity and magnetism content
                "content": [
                    " - Altering Current",
                    " - Electromagnetic Induction",
                    " - Capacitance",
                    " - DC Circuits & AC Circuits"
                    ]
                }
            ]
        #creating the list box
        self.Physics_content =Listbox(self.frame2, font=("Times New Roman", 14, "bold"), width=40, height=8)
        self.Physics_content.place(x=350, y=100)
        
        # Insert content into the Listbox widget
        #for each of the content in the contents dictonary, insert the title (level 3/Level2 mechanics, waves, and Electricy and magnetism)
#at the end of the phyiscs_content listbox widget
        for content in self.contents:
            self.Physics_content.insert(END, content["title"])
          #<<>> represents a virtual event and not a real event like a button click 
        self.Physics_content.bind("<<ListboxSelect>>", self.listbox_content)
#self.physics content is the variable that is being binded to the listbox. Binding is a method used to bind the event
# when the something is selected from the listbox, the bind method helps call the method function 'listbox_content"
        #creating a 'select' button in the second frame o take a command and move to the selected frame corresponding to the topic in the list
        self.select_button = Button(self.frame2, text="Select", font=("Courier New", 14), bg="#b885cc")
        self.select_button.place(x=350, y=300) #placing the button
    def listbox_content(self, event): #takes 2 arguments self, and event
        #method is designed to handle the events related to the listbox
        selected_item = self.Physics_content.curselection() #retrieves items from the list box
        #the curselection method returns the content from the dictionary
        if selected_item: #statement checks if there was an item selected and will evaluate to true to execute the next block of code
            self.list = selected_item[0] #assigns the content of the selected item to the variable, list by retrieving the first index starting from 0
#index is a numbered label assigned to each item in the list
app = PhysicsQuizApp()
app.create_listbox()

