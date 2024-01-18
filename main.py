from tkinter import Tk, Canvas, Button, Label, PhotoImage

#Delcaring Constants
BACKGROUND_COLOR = "#B1DDC6"
TITLE = "Flashy"
WINDOW_PADDING = 50
CANVAS_WIDTH = 800
CANVAS_HEIGHT = 526
FLASHCARD_FRONT = "images/card_front.png"
FLASHCARD_BACK = "images/card_back.png"
RIGHT_BUTTON = "images/right.png"
WRONG_BUTTON = "images/wrong.png"
TITLE_FONT = ("Arial", 60, "italic")
WORD_FONT = ("Arial", 40, "bold")
LABEL_BACKGROUND = "white"
LABEL_FOREGROUND = "black"
TITLE_TEXT = "Title"
WORD_TEXT = "Word"


#Creating the window
window = Tk()
window.title(TITLE)
window.config(padx=WINDOW_PADDING, pady=WINDOW_PADDING, bg=BACKGROUND_COLOR)

#Creating the canvas
canvas = Canvas(width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)
canvas.update_idletasks()
canvas_width = canvas.winfo_width()
canvas_height = canvas.winfo_height()

#Creating the flashcard image
flashcard_image = PhotoImage(file=FLASHCARD_FRONT)

#Creating the button images
right_button_image = PhotoImage(file=RIGHT_BUTTON)
wrong_button_image = PhotoImage(file=WRONG_BUTTON)

# Creating the buttons
right_button = Button(image=right_button_image, highlightthickness=0)
wrong_button = Button(image=wrong_button_image, highlightthickness=0)

#Create the card title and word labels
card_title = Label(text=TITLE, font=TITLE_FONT, background=LABEL_BACKGROUND, fg=LABEL_FOREGROUND)
word = Label(text=WORD_TEXT, font=WORD_FONT, background=LABEL_BACKGROUND, fg=LABEL_FOREGROUND)

#Add flashcard image to the canvas and center it
canvas.create_image(canvas_width/2, canvas_height/2, image=flashcard_image)

#Add buttons to the canvas below the flashcard
right_button.grid(row=1, column=1)
wrong_button.grid(row=1, column=0)


#Add the labels to the canvas
card_title.place(x=canvas_width/2, y=canvas_height/4, anchor="center")
word.place(x=canvas_width/2, y=canvas_height/2, anchor="center")


window.mainloop()