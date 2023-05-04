from tkinter import *

master = Tk()
master.geometry('720x480')
master.title('PlayStation gestion de stock')
master.config(background='#8d8d8d')
#master['bg'] = '#8d8d8d'
#master.resizable(height=False,width=False)
master.minsize(480, 360)
master.iconbitmap('ps.ico')

def console_window():
    new_window = Toplevel(master)
    new_window.title('Consoles')
    new_window.geometry('720x480')
    new_window.iconbitmap('ps.ico')

def accessories_window():
    new_window = Toplevel(master)
    new_window.title('Accessoires')
    new_window.geometry('720x480')
    new_window.iconbitmap('ps.ico')

def games_window():
    new_window = Toplevel(master)
    new_window.title('Jeux')
    new_window.geometry('720x480')
    new_window.iconbitmap('ps.ico')



frame = Frame(master, bg='#8d8d8d')

label_title = Label(frame, text='PlayStation Store', font=('helvetica', 40), bg='#8d8d8d')
label_title.pack()
label_subtitle = Label(frame, text='Gestion du stock', font=('helvetica', 25), bg='#8d8d8d')
label_subtitle.pack()

console_button = Button(frame, text='Consoles', font=('Helvetica', 25), bg='#8d8d8d', command=console_window)
console_button.pack(pady=15, fill=X)
accessories_button = Button(frame, text='Accessoires', font=('Helvetica', 25), bg='#8d8d8d', command=accessories_window)
accessories_button.pack(pady=15, fill=X)
games_button = Button(frame, text='Jeux', font=('Helvetica', 25), bg='#8d8d8d', command=games_window)
games_button.pack(pady=15, fill=X)

frame.pack(expand=YES)

#frame_category = Frame(window, bg='#8d8d8d')


#frame_category.pack()


master.mainloop()
