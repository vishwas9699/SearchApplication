from tkinter import *
from tkinter import font
from tkinter.scrolledtext import ScrolledText
import wikipedia as wiki
from tkinter.messagebox import askokcancel
import threading


def call_for_search(*args):
    x= threading.Thread(target=search)
    x.start()

def call_back_for_root():
    if askokcancel("App Says","Do you really want to exit"):
        root.quit()

def copy_data(*args):
    data=text.get('0.0',END)
    root.clipboard_clear()
    root.clipboard_append(data)

root = Tk()
root.title("Search Application")
root.geometry("320x480")
root.protocol("WM_DELETE_WINDOW",call_back_for_root)
root.configure(bg="white")

def call_for_search():
    x= threading.Thread(target=search)
    x.start()

def call_back_for_root():
    if askokcancel("App Says","Do you really want to exit"):
        root.quit()

def search():
    global lang_dict
    val=lang.get()
    search_data=ent.get()
    ent.set("")
    text.delete('0.0',END)
    text.insert('0.0',"Searching for : {}".format(search_data))
    try:
        wiki.set_lang(lang_dict[val])
        data=wiki.summary(search_data,sentences=4)
    except Exception as e:
        data = e

    text.delete('0.0',END)
    text.insert('0.0',data)
    srch_lbl["text"]="Searching for : {}".format(search_data)

ent =StringVar()
lang =StringVar()
lang_dict = {'English':'en','Kannada':'kn','Hindi':'hi','French':'fr','German':'de','Arabic':'ar'}

search_ent=Entry(root,width=21,font=('arial',14),bd=2,relief=RIDGE,textvariable=ent)
search_ent.place(x=15,y=20)

img = PhotoImage(file="SearchButton.png")
search_btn=Button(root,bd=2,image=img,relief=GROOVE,command=call_for_search)
search_btn.bind('<Return>',call_for_search)
search_btn.place(x=250,y=20)

srch_lbl=Label(root,text='Searching results for : ',font=("arial",12,'bold'),bg='white')
srch_lbl.place(x=15,y=70)

text=ScrolledText(root,font=('times',12),relief=SUNKEN,bd=4,wrap=WORD)
text.bind("<Double-1>",copy_data())
text.place(x=15,y=100,height=300,width=300)


lang_list=['English','Kannada','Hindi','French','German','Arabic']
lang.set(lang_list[0])

language=OptionMenu(root,lang,*lang_list)
language.place(x=10,y=420)

clear_btn = Button(root,text="Clear",font=('arial',10,"bold"),width=10,command=lambda:text.delete("0.0",END))
clear_btn.place(x=100,y=420)

exit_btn= Button(root,text="Exit",font=('arial',10,"bold"),width=10,command=root.quit)
exit_btn.place(x=210,y=420)


root.mainloop()