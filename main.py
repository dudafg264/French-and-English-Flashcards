BACKGROUND_COLOR = "#B1DDC6"

from tkinter import *
import pandas
import random

word_number = random.randint(0, 101)

words_data_frame = pandas.read_csv("./data/french_words.csv")
words_dict = words_data_frame.to_dict()
words_to_learn = pandas.read_csv("./data/words_to_learn.csv")

def translation():
    global word_number
    # English Translation
    canvas.itemconfig(image, image=card_back)
    canvas.itemconfig(language_text, text="English", fill="white")
    canvas.itemconfig(word_label, text=words_to_learn["English"][word_number], fill="white")
    window.after(2000, new_french_word)

def new_french_word():
    global word_number
    canvas.itemconfig(image, image=card_front)
    word_number = random.randint(0, 101)
    new_word = words_to_learn["French"][word_number]
    canvas.itemconfig(language_text, text="French", fill="black")
    canvas.itemconfig(word_label, text=new_word, fill="black")

def know_word():
    words_to_learn_updated = words_to_learn.drop(index=word_number)
    words_to_learn_updated.to_csv("./data/words_to_learn.csv", index=False)
    translation()


window = Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, highlightthickness=0, background=BACKGROUND_COLOR)
card_back = PhotoImage(file="./images/card_back.png")
card_front = PhotoImage(file="./images/card_front.png")
image = canvas.create_image(400, 263, image=card_front)
language_text = canvas.create_text(390, 150, text="French", fill="black", font=("Ariel", 20, "italic"))
word_label = canvas.create_text(390, 250, text=words_to_learn["French"][word_number], fill="black", font=("Ariel", 40, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

my_image_v = PhotoImage(file="./images/right.png")
button_v = Button(image=my_image_v, highlightthickness=0, command=know_word)
button_v.grid(column=1, row=1)

my_image_x = PhotoImage(file="./images/wrong.png")
button_x = Button(image=my_image_x, highlightthickness=0, command=translation)
button_x.grid(column=0, row=1)


window.mainloop()