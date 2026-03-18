from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("csk login page")
root.iconbitmap("champion.ico")

root.geometry('1000x1000+0+0')
root.configure(background="#E1F109")

# image
img = Image.open('csk.png')
resize_img = img.resize((300,250))
img = ImageTk.PhotoImage(resize_img)

img_label = Label(root,image = img)
img_label.pack(pady=20,padx=20)

# text label
text_label = Label(root,text="CSK",font=('Arial', 40,'bold'),bg="#DEFA0D",fg='black')
text_label.pack(pady=10,padx=10)

symbol_label = Label(root,text="⭐⭐⭐⭐⭐",font=('Arial', 30,'bold'),bg="#F0F4F3",fg='goldenrod')
symbol_label.pack(pady=10,padx=10)

email_label = Label(root,text="Email",font=('Arial', 30,'bold'),bg="#ECEAF0",fg='black')
email_label.pack(pady=(10,5))

email_entry = Entry(root,font=('Arial', 30,'bold'),fg='black',bg='white')
email_entry.pack(pady=(5,10))

password_label = Label(root,text="Password",font=('Arial', 30,'bold'),bg="#F0F4F3",fg='black')
password_label.pack(pady=(20,5))

password_entry = Entry(root,font=('Arial', 30,'bold'),fg='black',bg='white',show='*')
password_entry.pack(pady=(5,10))

login_btn = Button(root,text="Login",font=('Arial', 30,'bold'),bg="#DFEAE6",fg='black')
login_btn.pack(pady=(5,10))

root.mainloop()