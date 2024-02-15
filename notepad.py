    # Date - 09/02/2023


import tkinter as tk
from tkinter import messagebox, filedialog

root = tk.Tk()
root.geometry("940x470")
root.title("Notepad")
root.resizable(False, False)


# functionality
def new():
        interface = tk.Toplevel(root)
        interface.geometry("940x470")
        interface.minsize(940, 470)
        interface.title("Notepad")
        interface.resizable(False, False)


        # Creating a Menu widget and placing it in the root window
        menu_Bar = tk.Menu(interface)
        interface.config(menu=menu_Bar)

        file_menu = tk.Menu(menu_Bar, tearoff=0)

        menu_Bar.add_cascade(menu=file_menu, label="File")
        file_menu.add_command(label="New", command= new)
        file_menu.add_command(label="Open", command= open)
        file_menu.add_command(label="Save as", command= save_as)


        # Creating a Text widget and placing it in the root window
        text = tk.Text(interface, wrap="word", font= ("Open Sans", 11, ))
        text.pack(fill="both", expand=True)


        # Creating a Scrollbar widget and associating it with the Text widget
        scrollbar = tk.Scrollbar(text, command=text.yview)
        text.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side="right", fill="y")
    
def open():
        opn = filedialog.askopenfile(mode= "r")
        
        if opn:
            file_name = opn.name
            content = opn.read()
            text.delete("1.0", "end")
            text.insert("1.0", content)
            root.title(file_name)

def save_as():

    file = filedialog.asksaveasfile(mode='w', defaultextension=".txt")
    if file:
        text_content = text.get("1.0", "end-1c")
        file.write(text_content)
        file.close()

    









# Creating a Menu widget and placing it in the root window
menu_Bar = tk.Menu(root)
root.config(menu=menu_Bar)

file_menu = tk.Menu(menu_Bar, tearoff=0)

menu_Bar.add_cascade(menu=file_menu, label="File")
file_menu.add_command(label="New", command= new)
file_menu.add_command(label="Open", command= open)
file_menu.add_command(label="Save as", command= save_as)


# Creating a Text widget and placing it in the root window
text = tk.Text(root, wrap="word", font= ("Open Sans", 11, ))
text.pack(fill="both", expand=True)


# Creating a Scrollbar widget and associating it with the Text widget
scrollbar = tk.Scrollbar(text, command=text.yview)
text.configure(yscrollcommand=scrollbar.set)
scrollbar.pack(side="right", fill="y")


root.mainloop()
