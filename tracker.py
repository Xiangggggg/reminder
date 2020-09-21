from tkinter import *
from tkinter import ttk
from tkinter import messagebox

# Uses tkinter library
root = Tk() 
root.attributes("-topmost", True) # Always keeps the notifications on top
Label(root, text="Hello! How much time would you like before we remind you? (Minutes>=0 please)").pack()
mins = Text(root, width=40, height=1) # User input
mins.pack() # .pack() used for formatting
button = ttk.Button(root, text='Enter') # Enter button
button.pack()

# Timeup function for warning
def timeup(): 
    messagebox.showinfo(title='Timeout', message='Time is up, take a break!')
    root.deiconify() # Repops up the root window

# Asynchronous function for reminder popup
def reminder():
    mins_value = mins.get('1.0', '1.end') # Stores user input
    try: # makes sure mins_value is valid num >= 0
        mins_value = float(mins_value)
        if mins_value >= 0: # User input float validation
            messagebox.showinfo("Success!","We will remind you every "+str(mins_value)+" min(s)!")
            root.withdraw() # Hides root window
            root.after(int(mins_value * 60000), timeup) 
        else:
            messagebox.showinfo("Error","Invalid input.")
    except ValueError:
        messagebox.showinfo("Error","Invalid input.")

button.config(command=reminder) # callback function

root.mainloop()


