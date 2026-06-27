
import tkinter as tk
from tkinter import ttk
import requests
import pyperclip


base_url = "https://api.chucknorris.io/jokes/random"


def generate_joke():
    response = requests.get(base_url)
    response_json = response.json()
    joke = response_json["value"]

    joke_var.set(joke)


def generate_by_category():
    category_name = category_var.get()

    search_param = {"category": category_name}

    # requests automatically uses: .../jokes/random?category=food
    response = requests.get(base_url, params=search_param)

    response_json = response.json()
    joke = response_json["value"]

    joke_var.set(joke)


def copy_joke():
    joke = joke_var.get()
    pyperclip.copy(joke)


# ui and variable setup
root = tk.Tk()
root.title("Chuck Norris Jokes")

joke_var = tk.StringVar(value="Click the button to generate a new joke!")
category_var = tk.StringVar()

# UI framing
input_frame = ttk.Frame(root)
input_frame.grid(row=0, column=0)

separator = ttk.Separator(root)
separator.grid(row=1, column=0, sticky=tk.EW)

output_frame = ttk.Frame(root)
output_frame.grid(row=2, column=0)

# input frame
heading_label = ttk.Label(input_frame, text="Chuck Norris Jokes", font=("Arial", 16))
heading_label.grid(row=0, column=0, padx=5, pady=(10, 3), columnspan=3)

generate_button = ttk.Button(input_frame, text=">>> Random Joke <<<", command=generate_joke)
generate_button.grid(row=1, column=0, ipadx=5, ipady=5, padx=3, pady=3, columnspan=3)

category_label = ttk.Label(input_frame, text="Or select from category:", font=("Arial", 13))
category_label.grid(row=2, column=0, padx=5, pady=(15, 5), columnspan=3)

# radiobutton setup
rb_option1 = ttk.Radiobutton(input_frame,
                             text="Food",
                             variable=category_var,
                             value="food",
                             command=generate_by_category)
rb_option1.grid(row=3, column=0, padx=3, pady=5)

rb_option2 = ttk.Radiobutton(input_frame,
                             text="Science",
                             variable=category_var,
                             value="science",
                             command=generate_by_category)
rb_option2.grid(row=3, column=1, padx=3, pady=5)

rb_option3 = ttk.Radiobutton(input_frame,
                             text="Sport",
                             variable=category_var,
                             value="sport",
                             command=generate_by_category)
rb_option3.grid(row=3, column=2, padx=3, pady=5)

# output frame
joke_label = ttk.Label(output_frame, textvariable=joke_var, font=("Arial", 9))
joke_label.grid(row=0, column=0, ipadx=10, ipady=10, padx=5, pady=5)

copy_button = ttk.Button(output_frame, text="Copy!", command=copy_joke)
copy_button.grid(row=1, column=0, padx=5, pady=(2, 9))


if __name__ == "__main__":
    root.mainloop()
