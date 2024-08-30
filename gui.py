from tkinter import *
from tkinter import filedialog
import customtkinter as ctk
from pdf_unlock import main

def path_button_click():
    root.file_path = filedialog.askopenfilename(filetypes=[('PDF Files', '*.pdf')])
    if root.file_path:
        file_name = root.file_path.split('/')
        path_label.configure(text='Selected file: ' + file_name[-1])
    
def convert_button_click():
   result = main(path=root.file_path, password=table_entry.get())
   result_label = ctk.CTkLabel(master=root,text=result,font=('Arial',15),bg_color='transparent')
   result_label.place(relx = 0.3, y = 200, anchor=NW)

# MAIN WINDOW
root = ctk.CTk()
root.title('PDF-Unlocker')
root.geometry('400x250')
root.resizable(False, False)

root.file_path = ''

browse_button = ctk.CTkButton(master=root,text='Select PDF', command=path_button_click)
browse_button.place(relx=0.3,y=20,anchor=NW)

path_label = ctk.CTkLabel(master=root, text="", font=('Arial', 15))
path_label.place(relx=0.2,y=60,anchor=NW)

table_entry = ctk.CTkEntry(master=root,
                           placeholder_text="Password...",
                           width=200,
                           height=30,
                           state='normal')
table_entry.place(relx=0.2,y=100,anchor=NW) 

convert_button = ctk.CTkButton(master=root, text='Unlock',command=convert_button_click)
convert_button.place(relx=0.3, y=160, anchor=NW)

root.mainloop()