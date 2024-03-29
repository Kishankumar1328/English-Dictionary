from tkinter import *
from PyMultiDictionary import MultiDictionary

dictionary=MultiDictionary()
root=Tk()
root.title("Word Dictionary")
root.geometry("1250x750")

def dict():
    meaning.config(text=dictionary.meaning('en',word.get())[1])
    synonym.config(text=dictionary.synonym('en',word.get()))
    antonym.config(text=dictionary.antonym('en',word.get()))

Label(root,text='Word Dictionary',font=("Arial 31 bold"),
      fg='gold').pack(pady=10)
frame=Frame(root)
Label(frame,text="Type Word:",font=("Arial 29 bold")).pack(side=LEFT)
word=Entry(frame,font=("Arial 23 bold"))
word.pack()
frame.pack(pady=10)

frame1 = Frame(root)
Label(frame1, text="Meaning: ", font=("Arial 18 bold")).pack(side=LEFT)
meaning = Label(frame1, text="", font=("Arial 18"),wraplength=1000)
meaning.pack()
frame1.pack(pady=15)

frame2 = Frame(root)
Label(frame2, text="Synonym: ", font=("Arial 18 bold")).pack(side=LEFT)
synonym = Label(frame2, text="", font=("Arial 18"), wraplength=1000)
synonym.pack()
frame2.pack(pady=15)

frame3 = Frame(root)
Label(frame3, text="Antonym: ", font=("Arial 18 bold")).pack(side=LEFT)
antonym = Label(frame3, text="", font=("Arial 18"), wraplength=1000)
antonym.pack(side=LEFT)
frame3.pack(pady=20)

Button(root,text='submit',font=("Arial 18 bold"),command=dict).pack()
root.mainloop()

