from tkinter import *

window = Tk()
window.geometry('720x480')
window.title('gestion de stock')
window.config(background='#8d8d8d')
#window['bg'] = '#8d8d8d'
#window.resizable(height=False,width=False)
window.minsize(480, 360)
window.iconbitmap('ps.ico')

frame = Frame(window, bg='#8d8d8d')

label_title = Label(frame, text='PlayStation Store', font=('helvetica', 40), bg='#8d8d8d')
label_title.pack()
label_subtitle = Label(frame, text='Gestion du stock', font=('helvetica', 25), bg='#8d8d8d')
label_subtitle.pack()

console_button = Button(frame, text='Consoles', font=('Helvetica', 25), bg='#8d8d8d')
console_button.pack(pady=15, fill=X)
accessories_button = Button(frame, text='Accessoires', font=('Helvetica', 25), bg='#8d8d8d')
accessories_button.pack(pady=15, fill=X)
games_button = Button(frame, text='Jeux', font=('Helvetica', 25), bg='#8d8d8d')
games_button.pack(pady=15, fill=X)

frame.pack(expand=YES)

#frame_category = Frame(window, bg='#8d8d8d')


#frame_category.pack()


window.mainloop()
