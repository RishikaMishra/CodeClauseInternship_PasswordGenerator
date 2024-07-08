import tkinter as tk
from PIL import Image
import random
import string

def generate_password(length, use_numbers=True, use_symbols=True):
    # Define character sets
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    # Initialize the pool of characters
    pool = lowercase_letters + uppercase_letters
    if use_numbers:
        pool += digits
    if use_symbols:
        pool += symbols

    # Generate the password
    password = ''.join(random.choice(pool) for _ in range(length))
    return password

def generate_button_clicked():
    password_length = int(length_entry.get())
    include_numbers = numbers_var.get()
    include_symbols = symbols_var.get()

    generated_password = generate_password(password_length, include_numbers, include_symbols)
    result_label.config(text=f"Generated password: {generated_password}")


# Create the main window
root = tk.Tk()
root.title("Password Generator")
root.geometry('1500x800')

# Styling and layout improvements
root.configure(bg="light pink")  # Set background color
canvas = tk.Canvas(root, width=1500, height=70, bg="Light Blue")
canvas.create_text(750, 30, text=" GENERATE YOUR PASSWORD.. ", fill="Navy Blue", font='Algerian 28 bold')
canvas.pack()

#image
#image = Image.open('C:/Users/Rishika/PycharmProjects/password_generator/password.png')
image = tk.PhotoImage(file='C:/Users/Rishika/PycharmProjects/password_generator/password.png')

# Create a label to display the image
image_label = tk.Label(root, image=image, bg="Light pink")
image_label.place(x=50, y=180)


# Widgets
length_label = tk.Label(root, text="Password Length:", bg="Light pink", font='Calibri 14')
length_entry = tk.Entry(root, width=35, bg="White")
Alpha_numbers_var = tk.BooleanVar(value=True)
Alpha_numbers_checkbox = tk.Checkbutton(root, text="Include Alphanumerics (from A,a to Z,z and 0 to 9)", font='Calibri 14', variable=Alpha_numbers_var, bg="Light pink")
numbers_var = tk.BooleanVar(value=True)
numbers_checkbox = tk.Checkbutton(root, text="Include Numbers (from 0 to 9)", font='Calibri 14', variable=numbers_var, bg="Light pink")
symbols_var = tk.BooleanVar(value=True)
symbols_checkbox = tk.Checkbutton(root, text="Include Symbols (Special characters @,$...)", font='Calibri 14', variable=symbols_var, bg="Light pink")
generate_button = tk.Button(root, height=1, width=20, text="Generate Password", font='Calibri 14', command=generate_button_clicked, bg="pink")
result_label = tk.Label(root, text="", bg="Light pink", font='Calibri 12')


# Layout
length_label.place(x=450, y=250)
length_entry.place(x=620, y=255)
Alpha_numbers_checkbox.place(x=450, y=300)
numbers_checkbox.place(x=450, y=330)
symbols_checkbox.place(x=450, y=360)
generate_button.place(x=450, y=410)
result_label.place(x=550, y=485)

root.mainloop()
