import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk  # Required to load non-PNG images in Tkinter

def menu(year):
    chinese_zodiac = {
        (1992, 1980, 2004): "Monkey",
        (1993, 1981, 2005): "Rooster",
        (1994, 1982, 1970): "Dog",
        (1995, 1971, 1983): "Boar",
        (1996, 1984, 1972): "Rat",
        (1997, 1985, 1973): "Ox",
        (1998, 1986, 1974): "Tiger",
        (1975, 1999, 1987): "Rabbit",
        (1976, 2000, 1988): "Dragon",
        (1977, 2001, 1989): "Snake",
        (2002, 1978, 1990): "Horse",
        (2003, 1979, 1991): "Ram"
    }

    for years, animal in chinese_zodiac.items():
        if year in years:
            return f"You were born in the Year of the {animal}."
    return ""

def birth_info(month, day):
    birth_details = {
        1: ("January", "Garnet", "Capricorn" if day <= 19 else "Aquarius"),
        2: ("February", "Amethyst", "Aquarius" if day <= 18 else "Pisces"),
        3: ("March", "Aquamarine or Bloodstone", "Pisces" if day <= 20 else "Aries"),
        4: ("April", "Diamond", "Aries" if day <= 19 else "Taurus"),
        5: ("May", "Emerald", "Taurus" if day <= 20 else "Gemini"),
        6: ("June", "Pearl, Alexandrite or Moonstone", "Gemini" if day <= 20 else "Cancer"),
        7: ("July", "Ruby", "Cancer" if day <= 22 else "Leo"),
        8: ("August", "Peridot or Sardonyx", "Leo" if day <= 22 else "Virgo"),
        9: ("September", "Sapphire", "Virgo" if day <= 22 else "Libra"),
        10: ("October", "Opal or Tourmaline", "Libra" if day <= 22 else "Scorpio"),
        11: ("November", "Topaz", "Scorpio" if day <= 21 else "Sagittarius"),
        12: ("December", "Turquoise or Zircon", "Sagittarius" if day <= 21 else "Capricorn")
    }

    if month in birth_details:
        month_name, birthstone, zodiac_sign = birth_details[month]
        return f"You were born in {month_name}.\nYour Birthstone is {birthstone}.\nYour Zodiac sign is {zodiac_sign}."
    else:
        return "Invalid month entered."

def calculate_birth_details():
    try:
        year = int(year_entry.get())
        month = int(month_entry.get())
        day = int(day_entry.get())
        
        if year < 1970 or year > 2005:
            messagebox.showerror("Error", "Year must be between 1970 and 2005.")
            return
        if month < 1 or month > 12:
            messagebox.showerror("Error", "Month must be between 1 and 12.")
            return
        if day < 1 or day > (30 if month in [4, 6, 9, 11] else 29 if month == 2 else 31):
            messagebox.showerror("Error", f"Day must be valid for the given month.")
            return

        chinese_zodiac_result = menu(year)
        birth_info_result = birth_info(month, day)
        
        result_text = f"Date of Birth: {month}-{day}-{year}\n{chinese_zodiac_result}\n{birth_info_result}"
        result_label.config(text=result_text)

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers for year, month, and day.")

# Setting up the GUI
app = tk.Tk()
app.title("Birth Details Application")
app.geometry("400x300")

# Load the background image
bg_image = Image.open("background.png")  # Replace with the path to your background image
bg_image = bg_image.resize((400, 300), Image.LANCZOS)
bg_photo = ImageTk.PhotoImage(bg_image)

# Place the background image in a label
bg_label = tk.Label(app, image=bg_photo)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# Adding input fields and labels with a semi-transparent background
tk.Label(app, text="Enter Year (1970-2005):", bg="lightgrey", font=("Arial", 10)).place(x=20, y=40)
year_entry = tk.Entry(app)
year_entry.place(x=200, y=40)

tk.Label(app, text="Enter Month (1-12):", bg="lightgrey", font=("Arial", 10)).place(x=20, y=80)
month_entry = tk.Entry(app)
month_entry.place(x=200, y=80)

tk.Label(app, text="Enter Day:", bg="lightgrey", font=("Arial", 10)).place(x=20, y=120)
day_entry = tk.Entry(app)
day_entry.place(x=200, y=120)

calculate_button = tk.Button(app, text="Calculate Birth Details", command=calculate_birth_details)
calculate_button.place(x=140, y=160)

result_label = tk.Label(app, text="", justify="left", wraplength=300, bg="White", font=("Arial", 9))
result_label.place(x=20, y=200)

app.mainloop()
