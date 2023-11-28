from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
import os
root=Tk()
root.title("NotePad")

open_img=ImageTk.PhotoImage(Image.open("open.png"))
exit_img=ImageTk.PhotoImage(Image.open("exit.jpg"))
save_img=ImageTk.PhotoImage(Image.open("save.png"))

label_file_name=Label(root, text="File Name")
label_file_name.place(relx=0.28, rely=0.03)

input_file_name=Entry(root)
input_file_name.place(relx=0.46, rely=0.03)

my_text=Text(root, width=35 , height=80)
my_text.place(relx=0.5 , rely=0.55 , anchor=CENTER)

name=""
def openFile():
    global name
    my_text.delete(1.0, END)
    input_file_name.delete(0,END)
    text_file=filedialog.askopenfilename(title="Open Text File", filetypes=(("Text Files", ".txt"),))
    print(text_file)
    name= os.path.basename(text_file)
    formated_name = name.split(".")[0]
    input_file_name.insert(END, formated_name)
    root.title(formated_name)
    text_file=open(name,"r")
    paragraph=text_file.read()
    my_text.insert(END, paragraph)
    text_file.close()
def closeWindow():
    root.destroy()
def save():
    input_name=input_file_name.get()
    file=open(input_name+".txt")
    data=my_text.get(1.0, END)
    print(data)
    file.write(data)
    input_file_name.delete(0, END)
    my_text.delete(1.0, END)
    messagebox.showinfo("Update", "Success")
open_button=Button(root, image=open_img, text="Open File", command=openFile)
open_button.place(relx=0.05, rely=0.03, anchor=CENTER)
save_button=Button(root, image=save_img, text="Save File", command=save)
save_button.place(relx=0.11, rely=0.03, anchor=CENTER)
exit_button=Button(root, image=exit_img, text="Exit File", command=closeWindow)
exit_button.place(relx=0.17, rely=0.03, anchor=CENTER)
root.mainloop()

