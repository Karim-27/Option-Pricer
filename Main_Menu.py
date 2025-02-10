import tkinter as tk
from Black_Scholes import black_scholes 

# Main Menu Window
root = tk.Tk()
root.title("Option Pricing")
root.geometry("400x300")

# Welcome Label
welcome_label = tk.Label(root, text="Welcome to the Options Calculator", font=("Arial", 14))
welcome_label.pack(pady=20)

# Button to Open Black-Scholes Window
def run_black_scholes():
    black_scholes()

black_scholes_button = tk.Button(root, text="Black-Scholes Calculator", font=("Arial", 12), command=run_black_scholes)
black_scholes_button.pack(pady=10)

root.mainloop()  # Main event loop