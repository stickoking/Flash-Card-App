from tkinter import Tk, Canvas, Button, PhotoImage
from classes.flashcard import Flashcard

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
TITLE_FONT = ("Arial", 40, "italic")
WORD_FONT = ("Arial", 60, "bold")
LABEL_BACKGROUND = "white"
LABEL_FOREGROUND = "black"

def retrieve_word():
    flashcard.get_random_word()
    canvas.itemconfig(canvas_image, image=flashcard_front_image)
    canvas.itemconfig(canvas_title, text="French")
    canvas.itemconfig(canvas_word, text=flashcard.random_word["French"])

def flip_card():
    canvas.itemconfig(canvas_image, image=flashcard_back_image)
    canvas.itemconfig(canvas_title, text="English")
    canvas.itemconfig(canvas_word, text=flashcard.random_word["English"])
    window.after(3000, flip_card)

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

#Creating the flashcard data from classes/flashcard.py
flashcard = Flashcard()

#Creating the flashcard image
flashcard_front_image = PhotoImage(file=FLASHCARD_FRONT)
flashcard_back_image = PhotoImage(file=FLASHCARD_BACK)

#Creating the button images
right_button_image = PhotoImage(file=RIGHT_BUTTON)
wrong_button_image = PhotoImage(file=WRONG_BUTTON)

# Creating the buttons
right_button = Button(image=right_button_image, highlightthickness=0 , command=retrieve_word)
wrong_button = Button(image=wrong_button_image, highlightthickness=0, command=flip_card)

#Add flashcard image to the canvas and center it
canvas_image = canvas.create_image(canvas_width/2, canvas_height/2, image=flashcard_front_image)
canvas_title = canvas.create_text(canvas_width/2, canvas_height/4, text="French", font=TITLE_FONT, fill=LABEL_FOREGROUND)
canvas_word = canvas.create_text(canvas_width/2, canvas_height/2, text=flashcard.random_word["French"], font=WORD_FONT, fill=LABEL_FOREGROUND)

#Add buttons to the canvas below the flashcard
right_button.grid(row=1, column=1)
wrong_button.grid(row=1, column=0)

#After 3000ms, change the flashcard image to the back of the card continue to do so every 3000ms
window.after(3000, flip_card)

window.mainloop()