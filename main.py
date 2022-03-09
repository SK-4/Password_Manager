from gc import callbacks
from tkinter import *
from tkinter import messagebox
from random import choice,randint,shuffle,random
import pyperclip
import json

#Password Generator
def generate():
    MAX_LEN = 12
    # maximum length of password needed
    # this can be changed to suit your password length
    # declare arrays of the character that we need in out password
    # Represented as chars to enable easy string concatenation
    DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                        'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                        'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                        'z']

    UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                        'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q',
                        'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                        'Z']

    SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>','*', '(', ')', '<']
    pass_letter=[choice(LOCASE_CHARACTERS) for  _ in range(randint(3,4))]
    pass_Letter=[choice(UPCASE_CHARACTERS) for  _ in range(randint(2,4))]
    pass_digits=[choice(DIGITS) for  _ in range(randint(1,2))]
    pass_digits=[choice(SYMBOLS) for  _ in range(randint(1,2))]

    pass_list=pass_letter+pass_Letter+pass_digits
    shuffle(pass_list)

    passw = "".join(pass_list)
    
    pass_entry.insert(0,passw)
    pyperclip.copy(passw)
#Save Password
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = pass_entry.get()
    new_data= {
        website:{
            "Email": email,
            "Password": password
        }
    }
    if len(website)==0 or len(password)==0:
        messagebox.showerror(title="Error",message="Please dont leave any field empty")
    else:
        try:
            with open("data.json","r") as data_file:
                #reading old data
                data=json.load(data_file)
        except FileNotFoundError:
            with open("data.json","w") as data_file:
                json.dump(new_data,data_file,indent=2)
        else:
            #updating old data into new data
            data.update(new_data)

            with open("data.json",'w') as data_file:    
            #saving updated data
                json.dump(data,data_file,indent=2)
        finally:
                website_entry.delete(0,END)
                pass_entry.delete(0,END)
                messagebox.showinfo(title="SAVED",message=f"{website} added to database")

#Search option 
def find_():
    website = website_entry.get().title()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
            messagebox.showerror(title="ERROR",message='No Data Found')
    else:
        if website in data:
            email = data[website]["Email"]
            password = data[website]["Password"]
            messagebox.showinfo(title=website,message=f"Email:{email}\nPassword:{password}")
        
        else:
            messagebox.showerror(title="Error",message="No Data found in Database")

#UI SETUP
window=Tk()
window.title("Password Manager")
window.config(padx=20,pady=20)

canvas=Canvas(width=300,height=300)
img=PhotoImage(file="logo.png")
canvas.create_image(170,150,image=img)
canvas.grid(column=1,row=0)

website_label=Label(text="Website")
website_label.grid(row=1,column=0)
email_label=Label(text="Email/Username")
email_label.grid(row=2,column=0)
pass_label=Label(text="Password")
pass_label.grid(row=3,column=0)

website_entry=Entry(width=30)
website_entry.grid(row=1,column=1,columnspan=2)
website_entry.focus()
email_entry=Entry(width=30)
email_entry.grid(row=2,column=1,columnspan=2)
email_entry.insert(0,"sohamkshirsagar7@gmail.com")
pass_entry=Entry(width=12)
pass_entry.grid(row=3,column=1)

#generate generate_buttons
generate_buttons=Button(text="Generate Password",command=generate)
generate_buttons.grid(row=3,column=2)
search_button=Button(text="Search",command=find_,width=14)
search_button.grid(row=1,column=2)
add_button=Button(text="ADD",width=26,command=save)
add_button.grid(row=4,column=1,columnspan=2)

window.mainloop()