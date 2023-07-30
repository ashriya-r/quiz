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
        self.frame3.config(bg="#ffd0cf")
        self.frame3.pack(fill="both", expand=True)

        self.frame4 = Frame(self.window, bd=5, relief="solid", highlightbackground="black")
        self.frame4.config(bg="#ffd0cf")
        self.frame4.pack(fill="both", expand=True)

        self.frame5 = Frame(self.window, bd=5, relief="solid", highlightbackground="black")
        self.frame5.config(bg="#ffd0cf")
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
        self.back_l3m.pack(side="left", anchor="sw", padx=(15,0), pady=15)
        

        self.back_l3w = Button(self.frame4, text="Back", font=("Gerogia", 12), command = self.back)
        self.back_l3w.pack(side="left", anchor="sw", padx=(15,0), pady=15)

        self.back_l3e = Button(self.frame5, text="Back", font=("Gerogia", 12), command = self.back)
        self.back_l3e.pack(side="left", anchor="sw", padx=(15,0), pady=15)
#binding the resizer function to frame 1 so that when the configure event is triggered, the image is resized to fit the size or position of frame1
        self.Motion_img = PhotoImage(file="Motion.png") #importing the image from the file directory
        self.small_img2 = self.Motion_img.subsample(2)#making the image smaller by sampling it down by a scale factor of 2
        self.image_label1 = Label(self.frame2, image=self.small_img2)#making the image as a label in frame2 to make it easier to position on the window
        self.image_label1.pack(side="bottom", anchor="se")#positioning the image on the bottom side and centering it 'south east' on the window

        self.Atom_img = PhotoImage(file="Atom.png")#import image from file directory
        self.small_img1 = self.Atom_img.subsample(2)#making the image smaller by scaling it down by a factor of 2
        self.image_label2 = Label(self.frame2, image=self.small_img1)#making the image as a label
        self.image_label2.place(x=15, y=15)#placing the image 15 pixels from the left and 15 pixels from the top
       
        self.mechanics_quiz()
        self.waves_quiz()
        self.electricity_and_magnetism_quiz()
        self.score = 0
        
            
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
        self.select_button = Button(self.frame2, text="Select", font=("Courier New", 14), bg="#b885cc", command=self.select_button_click)
        self.select_button.place(x=350, y=300) #placing the button 350 pixels from the left and 300 pixels from the top
#method to select an item from the list box
    def listbox_content(self, event): #takes 2 arguments self, and event
        #method is designed to handle the events related to the listbox
        selected_item = self.Physics_content.curselection() #retrieves items from the list box
        #the curselection method returns the content from the dictionary
        if selected_item: #statement checks if there was an item selected and will evaluate to true to execute the next block of code
            self.list = selected_item[0] #assigns the content of the selected item to the variable, list by retrieving the first index starting from 0
#index is a numbered label assigned to each item in the list
            #creating a method function for the select button
            #the purpose of this button is to take the user to the corresponding frame based on the item they have selected
    def select_button_click(self):
        selected_item = self.Physics_content.curselection() #retrieves items from the list box
        if selected_item: #if there is an item selected, the content will show based on what has been selected starting from index 0
            self.list = selected_item[0]
            self.selected_content = self.contents[self.list] #retrieves the items from the dictionary using the self.list variable as a key
            self.display_selected_frame(self.selected_content) #calls the method display frame to show show the selected content on
        else:# if nothing is selected and the button is clicked, and error message will show via the message box
            messagebox.showerror("Error", "Please select an item from the list.")
       #to show the selected frame without it appearing split in the window, the other frames are set to be hidden from view using the .pack_forget method     
    def display_selected_frame(self, selected_content):
        self.frame1.pack_forget()
        self.frame2.pack_forget()
        self.frame3.pack_forget()
        self.frame4.pack_forget()
        self.frame5.pack_forget()
        self.frame6.pack_forget()
        
    #creating the selected fram
        self.selected_frame = Frame(self.window, bd=5, relief="solid", highlightbackground="black")
        self.selected_frame.config(bg="#d38cb0")
        self.selected_frame.pack(fill="both", expand=True)
#creating a label for the selected frames by retrieving the title section from the dictionary
        title_label = Label(self.selected_frame, text=self.selected_content["title"], font=("Times New Roman", 20, "underline italic bold"))
        title_label.pack(pady=50)
#creating a label for the content and retrieving it from the dictionary through the selected content variable.
        #using /n.join to creating multi line strings for the content to appear on separate lines
        content_label = Label(self.selected_frame, text="\n".join(self.selected_content["content"]), font=("Courier New", 12))
        content_label.place(x=20, y=20)
    #configuring the labels to match the background of the frame
        content_label.config(bg="#d8d8f8")
        title_label.config(bg="#d38cb0")
        self.selected_frame.config(bg="#d38cb0")
        self.window.config(width=self.selected_frame.winfo_reqwidth(), height=self.selected_frame.winfo_reqheight())
#configuring the window to match the size of the selected frame.
#this is done by using the window information and finding the relative with and height of the selected frame to match the window to
#creating a back button to go back to the contents list if users want to select a different topic
#seeting the command for the back button switch to frame 2
        backbtn = Button(self.selected_frame, text="Back", command=self.switch_to_frame2, font=("Times New Roman", 14))
        backbtn.pack(side="left", anchor="sw", padx=(15,0), pady=15)
        self.switch_frames(self.selected_frame)

        self.scrolled_box = ScrolledText(self.selected_frame, font=("Times new roman", 14), width=100, height=15)
        self.scrolled_box.place(x=80, y=200)
        self.scrolled_box.config(bg="#f2dde7")

        quizbtn = Button(self.selected_frame, text = "Take the Quiz!", command =self.switch_to_quiz, font=("Helevatica", 12, "bold") )
        quizbtn.pack(side="right", anchor="se", padx=(20), pady=15)
        quizbtn.config(bg="#ffd1dc")

        if self.selected_content["title"] == "Level 3: Mechanics":
            mechanics_notes_title = Label(self.selected_frame, text = "Mechanics Notes", font=("Georgia", 14, "bold underline"))
            mechanics_notes_title.place(x=630, y=140)
            mechanics_notes_title.config(bg="#8cd3af")
            mechanics_notes = [
                """ Things to remember in Mechanics:

 1. Most equations are only used once so highlight an equation once you have used it

 2. The formulae on the equation sheet are in order: linear motion(2 rows), angular motion (4 rows),
     forces - gravitational and centripedal(1 row), SHM(3 rows)

 3. A reference circle is a circle and a phasor is a vector that rotates anticlockwise inside it

 4.The centre of mass of a system remains at rest or moving at a constant velocity providing the system remains an
     isolated system (Newton's first law)

 5.'Show that' means state the equation you need to use, write it again with the numbers inserted and then check the
    answer matches the question

 6. Leave any derivations (calculus stuff) until last

 7. Remember the conservation laws: Momentum and angular momentum are conserved unless an external force or external torque acts

 8. p = F x t is rarely used but F = p/t is. Practice rearranging the formula to F = p/t.

 9. Any constants you need are given to you

 10. Label arrows and all diagrams
"""
                ]

            for note in mechanics_notes:
                self.scrolled_box.insert("end", note + "\n")
            self.scrolled_box.config(state="disabled")

        if self.selected_content["title"] == "Level 3: Waves":
            waves_notes_title = Label(self.selected_frame, text="Waves Notes", font=("Georgia", 16, "bold underline"))
            waves_notes_title.place(x=630, y=140)
            waves_notes_title.config(bg="#8cd3af")

            waves_notes = [
                """ Things to remember in Waves:

 1. The Doppler Effect is not symmetrical and is only observed when there is a relative motion between the observer and the source.

 2. Draw standing waves travelling in one direction in blue and waves travelling in the other in black to make it clear

 3. Closed pipes - you can't get even harmonis e,g, 2nd and 4th - because there is a node and antinode

 4. The fundamental is the simplest standing wave pattern (least number of A or AN)

 5. Node is no displacement and Antinode is maximum displacement

 6. Diffraction splits white light into a spectrum because it's a mixture of wavelength's EXCEPT for the central maxima. Red is diffracted most of
     visible light

 7. Strings with transverse waves (fixed at both ends) count the antinodes

 8. Open pipes with longitudinal waves count nodes

 9. Write done the Beat formula (fb = f1 - f2), as soon as you are allowed to because it might not be given on the formula sheet

 10. You will probably use most of thre equations more than once. Any constants you need will be given to you.
"""
                ]

            for note in waves_notes:
                self.scrolled_box.insert("end", note + "\n")
            self.scrolled_box.config(state="disabled")

        if self.selected_content["title"] == "Level 3: Electricty & Magnetism":
            lvl3em = Label(self.selected_frame, text="Electricity and Magnetism Notes", font=("Georgia", 14, "bold underline"))
            lvl3em.place(x=510, y=140)
            lvl3em.config(bg="#8cd3af")

            lvl3electricity = [
                """ Things to remember in Electricity and Magnetism

 1. Capacitors block low frequency and inductors block high frequency

 2. A phasor diagram is like a vector diagram - it doesn't have to be used in a reference circle

 3. Z(Impendance) = R 'at resonance' (when f = f0) and then I is the maximum value

 4. Xc and X l are 180 degrees out of phase

 5. Kirchoff's laws - sum of voltages in a loop are zero (law of conservation of energy)
     current entering a junction = current leaving a junction(law of conservation of charge)

 6. In the impedance question, remember R is resistance, Xc reactance of the capacitor and Xl reactance of the inductor

 7. You might need to us Ct = C1 + C2 for adding capacitors in parallel, 1/Ct = 1/C1 + 1/C2 is for adding capacitors
     in series (they are insulators and therefore the opposite to resistors)

 8. Remember the basic electricity rules (in series, I is the same but V splits; in a parallel circuit, I splits and
      V is the same)
      You might need to use Rt = R1 +R2... for adding resistors in series and 1/Rt = 1/R1 + 1/R2 for adding
      resistors in parallel

 9. Most equations are only used once so highlight the equation once you have used it

 10. Ir is the lost volts (more lost volts the hotter the battery is and the more inadequate it becomes)
"""
                ]

            for note in lvl3electricity:
                self.scrolled_box.insert("end", note + "\n")
            self.scrolled_box.config(state="disabled")
           
#creating a method to switch the frame to frame 2 by using the back button
    def switch_to_frame2(self):
        if self.selected_frame: #keeps track of which frame is shown; if statement checks if the selected frame is not none
            self.selected_frame.pack_forget()#using pack_forget method to hide the selected frame from view so that the next frame can be shown
            self.switch_frames(self.frame2)#switching the frames to show frame2

    def switch_to_quiz(self):
        if self.selected_frame:
            self.selected_frame.pack_forget()    
            if self.selected_content["title"] == "Level 3: Mechanics":
                self.switch_frames(self.frame3)
                self.frame3.pack(fill="both", expand=True)

            elif self.selected_content["title"] == "Level 3: Waves":
                self.switch_frames(self.frame4)
                self.frame4.pack(fill="both", expand=True)

            elif self.selected_content["title"] == "Level 3: Electricty & Magnetism":
                self.switch_frames(self.frame5)
                self.frame5.pack(fill="both", expand=True)
    def mechanics_quiz(self):
        self.questions = [
            """ Two astronauts, Sylvia and Sam, are on a mission to another planet. During their journey they are
                doing a "spacewalk" outside their spaceship. At one time they are moving freely. They collide and
                stick together. Calculate the distance between Sam and the centre of mass of the system when he
                and Sylvia are 4.80 m apart. """,

            """ When the spaceship reaches the planet, the spaceship goes into orbit around the planet with a
              period of 5.46 x 10^3s, and at a height of 351km above the surface. Assume the orbit is circular. The
              planet has a radius of 5220km.
              Calculate the mass of the planet """,

            """ Jay is enjoying a swing at the playground. Jay moves to a new swing that is a tyre hanging vertically
               on a single chain. The system is a conical pendulum. Jay travels 2.6m/s around a circle of radius
               0.411m. The total mass of Jay and the swing is 70.0kg. Assume friction and the mass of the supporting
               chain are negligible. Calculate the tension in the chains supporting the swing and the angle of the chain
               from vertical """,

            """ A solid cylinder and a hollow cylinder of the same shape and mass are rolled down a slope.
               The hollow cylinder has a radius of 0.058m. It rolls down the slope and reachers a speed of 0.250m/s
               at the bottome. The rotational inertia of the hollow cylinder is 0.140kgm^2. Calculate the rotational
               kinetic energy of the hollow cylinder at the bottom of the slope.""",

            """ Serena swings from end A to end B with an amplitude of 1.50m and a period of 3.50s. Using a
               reference circle, calculate the velocity of Serena and the swing when she is 0.500m from
               end B."""
        ]

        self.options = [
            ["2.28m", "2.37m", "3.25m", "1.28m"],
            ["3.43 x 10^23kg", "3.57 x 10^24kg", "4.21 x 10^23kg", "3.43 x 10^24kg"],
            ["tension = 1450N, angle = 50.23 degrees", "tension = 1350N, angle = 59.34 degrees",
            "tension = 1290N, angle = 59.41 degrees", "tension = 1375N, angle = 44.79 degrees"],
            ["1.30J", "1.75J", "1.47J", "2.19J"],
            ["3.01m/s", "2.01m/s", "2.47m/s", "3.19m/s"]
        ]

        self.answers = [0, 3, 1, 0, 1]
        self.current_question = 0

        self.selected_option = IntVar()

        self.question_label = Label(self.frame3, text=self.questions[self.current_question], font=("Georgia",12), justify="center")
        self.question_label.place(x=100, y=20)
        self.question_label.config(bg="#ffd0cf")
        y_offset = 120

        for i, option in enumerate(self.options[self.current_question]):
            Radiobutton(self.frame3, text=option, variable=self.selected_option, value=i, bg="#ffd0cf").place(x=120, y=y_offset )
            y_offset += 30

        self.submit_button = Button(self.frame3, text="submit", command=self.check_answer, font=("Times New Roman", 12, "bold"))
        self.submit_button.pack(side="right", anchor="se")
        self.submit_button.config(bg="#cca6d9")


    def check_answer(self):
        user_answer = self.selected_option.get()
        correct_answer = self.answers[self.current_question]

        if user_answer == correct_answer:
            self.score += 1
            messagebox.showinfo("Result", "Correct Answer :)")
        else:
            messagebox.showinfo("Result", "Incorrect answer :(")
        self.next_question()
    def next_question(self):
        if self.current_question < len(self.questions) - 1:
            self.current_question += 1
            self.question_label.config(text=self.questions[self.current_question])

            for widget in self.frame3.winfo_children():
                    if isinstance(widget, Radiobutton):
                            widget.destroy()
            height = self.question_label.winfo_reqheight()
            num_options = len(self.options[self.current_question])
            y_offset = height + 10

            for i, option in enumerate(self.options[self.current_question]):
              Radiobutton(self.frame3, text=option, variable=self.selected_option, value=i, bg="#ffd0cf").place(x=120, y=y_offset)
              y_offset += 30

            self.submit_button.pack()
        else:
            final_score_message = f"Quiz complete \nYour score: {self.score} out of 5"
            messagebox.showinfo("Result", final_score_message)
            self.window.destroy()
#################################Creating Waves quiz#################################################
    def waves_quiz(self):
        self.wavesquestions = [
            """ Mike and Kate are on a tramping trip and are crossing a suspension bridge. They realise that by
                   jumping up and down in a particular way. they can set up a standing wave in the bridge. The
                   bridge is 24.0m long. The bridge oscillates at the fundamental frequency mode with a period
                   of 1.80s. Calculate the speed of the waves.""",

            """ Some police forces have used whistles that have two chambers of different lengths where one
                side of the chamber is longer than the other. The fundamental frequencies for the two chambers
                are 2136 Hz, and 1904 Hz. The speed of sound in air is 343 m/2. Calculate the length of the longer
                chamber""",

            """ A tourist is watching a ferry boat coming towards her. The speed of the ferry is 5.50m/s.
                The ferry sounds its horn, producing a not of frequency 95.0 Hz. The speed of sound in the
                air over the water is 3.50 x 10^2m/2. Calculate the frequency of the note that the tourist hears.""",

            """ Moana is doing an expierment in the laboratory. She shines a laser beam at a double slit and
                  observes an interference pattern on a screen. Moana measures the distance between the adjacent
                  bright spots (maxima) and finds they are 0.0100m apart. The slits are 1.28 x 10^-4m apart.
                  The screen is 2.10m from the slits. Moana replaces the double slit with a diffraction grating
                  in the same position. The diffraction grating has 500 lines per mm. Calculate the angle between
                  the central antinodal line and the first antinodal line.""",

            """ James and Tara take two portable speakers out on the school field and place them 1.25m apart
                They send a signal via their computer to play a frequency of 2.50 x 10^3 Hz out of both speakers
                at the same time. They walk along a line parallel to the speakers, 20.0m away. They notice
                a regular series of quiet and loud spots along the line and decide to investigate them.
                James stands along the central line and Tara stands on the first adjacent lout spot along the line.
                Calculate the angle, that Tara makes with the central line."""
        ]

        self.choices = [
            ["28.5m/s", "26.7m/s", "26.4m/s", "21.8m/s"],
            ["0.045m", "0.069m", "0.052m", "0.049m"],
            ["67.4Hz", "89.5Hz", "96.5Hz", "91.2Hz"],
            ["17.5 degrees", "18.1 degrees", "17.2 degrees", "20.6 degrees"],
            ["8.27 degrees", "6.21 degrees", "4.91 degrees", "6.27 degrees"]
        ]

        self.answers1 = [1, 0, 2, 0, 3]
        self.current_question1 = 0

        self.selected_options1 = IntVar()

        self.question_labels = Label(self.frame4, text=self.wavesquestions[self.current_question1], font=("Georgia",12), justify="center")
        self.question_labels.place(x=120, y=10)
        self.question_labels.config(bg="#ffd0cf")
        y_offset = 130

        for i, option in enumerate(self.choices[self.current_question1]):
            Radiobutton(self.frame4, text=option, variable=self.selected_options1, value=i, bg="#ffd0cf").place(x=120, y=y_offset )
            y_offset += 40

        self.submit_button1 = Button(self.frame4, text="Submit", command=self.check_answers, font=("Times New Roman", 12, "bold"))
        self.submit_button1.pack(side="right", anchor="se")
        self.submit_button1.config(bg="#cca6d9")


    def check_answers(self):
        user_answers = self.selected_options1.get()
        correct_answers = self.answers1[self.current_question1]

        if user_answers == correct_answers:
            self.score +=1
            messagebox.showinfo("Result", "Correct Answer :)")
        else:
            messagebox.showinfo("Result", "Incorrect answer :(")
        self.next_questions()

    def next_questions(self):
        if self.current_question1 < len(self.wavesquestions) - 1:
            self.current_question1 += 1
            self.question_labels.config(text=self.wavesquestions[self.current_question1])

            for widget in self.frame4.winfo_children():
                    if isinstance(widget, Radiobutton):
                            widget.destroy()
            height1 = self.question_labels.winfo_reqheight()
            num_choices= len(self.choices[self.current_question1])
            y_offset = height1 + 20

            for i, option in enumerate(self.choices[self.current_question1]):
              Radiobutton(self.frame4, text=option, variable=self.selected_options1, value=i, bg="#ffd0cf").place(x=120, y=y_offset)
              y_offset += 40

            self.submit_button1.pack()
        else:
            final_score = f"Quiz Complete! \n Your score: {self.score} out of 5"
            messagebox.showinfo("Result", final_score)
            self.window.destroy()
#########################Create electricity and magnetism quiz##############################
    def electricity_and_magnetism_quiz (self):
        self.magnetismquestions = [
            [
                """ Jess is investigating a torch to find out the characteristics of the battery and the lamp. The torch uses
                 a filament lamp. The filament is a long coil of fine wire that heats up and glows when it carries sufficient
                 current. For the purposes of calculation, assume that the resistance of the filament remains constant.
                 Calculate the current that travels through the battery if a second identical lamp is connected in parallel
                 with the first lamp. """
            ],
            [
                """ Inductive loops are also used to sense the presence of cars. Inductive loops are wire coils embedded
                 into the surface of the road and are powered by an AC supply of known voltage and frequency. One
                 particular inductive loop has a 4.00 ohm resistance and is powered by a 24.0Vrms, 1.20 x 10^2 Hz
                 AC power supply. The loop is 1.60m x 0.600m rectangular shape, with the coils of wire. The strength
                 of the magnetic field inside the loop is 0.0413T. Calculate the maximum magnetic flux in each of the
                 three coils of wire if the inductive loop."""
            ],
            [
                """ Casey is using an electromagnet that has an inductance of 4.50 x 10^-1 H and a resistance of 2.00 Ohms.
                Casey connects it to a 12.0V DC battery with an internal resistance of 0.0900 ohms. Determine
                the current through the electromagnet a few minutes after the switch is closed."""
            ],
            [
                """ Transformers can be used to increase or decrease the size of an AC voltage. Jake has a transformer
                  that is designed to convert 240V into 12.0V. The secondary coil has 40 turns. Calculate the number
                of turns on the primary coil. """
            ],
            [
                """ Kate is experimenting with LCR circuits. She uses a signal generator and connects an inductor,
                  a 1.00 x 10^-4F capacitor and a lamp to act as a resistor, all in series. Kate adjusts the frequency
                  of the signal generator until the lamp glows brightly. The lamp is brightest at a particular
                  frequency called the resonant frequency. Kate observes that the resonante frequency is
                  2.10 x 10^2Hz. By first showing that the reactance of the capacitor is 7.58 ohms, calculate
                  the inductance of the inductor."""
            ]
        ]

        self.choice = [
            ["1.59A", "1.43A", "1.36A", "1.72A"],
            ["0.0496Wb", "0.0583Wb", "0.0451Wb", "0.0396Wb"],
            ["5.71A", "4.97A", "5.74A", "5.01A"],
            ["750 turns", "540 turns", "808 turns", "800 turns"],
            ["5.74 x 10^-2", "5.47 x 10^-3", "5.74 x 10^-3", "5.75 x 10^-2"]
        ]

        self.answers2 = [1, 3, 2, 3, 2]

        self.current_question2 = 0

        self.selected_options2 = IntVar()

        self.question_labels1 = Label(self.frame5, text=self.magnetismquestions[self.current_question2], font=("Georgia",12), justify="center")
        self.question_labels1.place(x=120, y=10)
        self.question_labels1.config(bg="#ffd0cf")
        y_offset = 130

        for i, option in enumerate(self.choice[self.current_question2]):
            Radiobutton(self.frame5, text=option, variable=self.selected_options2, value=i, bg="#ffd0cf").place(x=120, y=y_offset )
            y_offset += 40

        self.submit_button2 = Button(self.frame5, text="Submit", command=self.check_answers1, font=("Times New Roman", 12, "bold"))
        self.submit_button2.pack(side="right", anchor="se")
        self.submit_button2.config(bg="#cca6d9")


    def check_answers1(self):
        user_answers1 = self.selected_options2.get()
        correct_answers1 = self.answers2[self.current_question2]

        if user_answers1 == correct_answers1:
            self.score += 1
            messagebox.showinfo("Result", "Correct Answer :)")
        else:
            messagebox.showinfo("Result", "Incorrect answer :(")
        self.next_questions1()

    def next_questions1(self):
        if self.current_question2 < len(self.magnetismquestions) - 1:
            self.current_question2 += 1
            self.question_labels1.config(text=self.magnetismquestions[self.current_question2])

            for widget in self.frame5.winfo_children():
                    if isinstance(widget, Radiobutton):
                            widget.destroy()
            height2 = self.question_labels1.winfo_reqheight()
            num_choice= len(self.choice[self.current_question2])
            y_offset = height2 + 20

            for i, option in enumerate(self.choice[self.current_question2]):
              Radiobutton(self.frame5, text=option, variable=self.selected_options2, value=i, bg="#ffd0cf").place(x=120, y=y_offset)
              y_offset += 40

            self.submit_button2.pack()
        else:
            final_score1 = f"Quiz Complete! \n Your score: {self.score} out of 5"
            messagebox.showinfo("Result", final_score1)
            self.window.destroy()

app = PhysicsQuizApp()
app.create_listbox()
app.window.mainloop()
