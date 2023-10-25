import pyperclip as clipboard
from tkinter import *
from tkinter.ttk import *

conf_file='personalClipboard/conf/options_conf.conf'
my_row=0

def copiar(data):
    clipboard.copy(data)
    print("Texto copiado: "+data)

with open(conf_file,'r') as lc:
    height=len(lc.readlines()*40)

window = Tk()
window.title("Personal MultiClipboard")
window.geometry("200x"+str(height))
window.resizable(0,0)

with open(conf_file,'r') as a:
    lines=a.readlines()
    lines_count=len(a.readlines())
    for l in lines:
        l = l.rstrip('\n')
        conf=l.split(';')
        tag=conf[0]
        text=conf[1]
        print("text:"+text)
        style = Style()
        style.configure('TButton', font =
                       ('calibri', 12, 'bold'),
                            borderwidth = '1')
        style.map('TButton', foreground = [('active', '!disabled', 'green')],
                             background = [('active', 'black')])
        
        button = Button(window, text=tag, command=lambda text=text: copiar(text))
        button.grid(row = my_row, column = 0, padx=40, pady=5)
        my_row+=1

window.mainloop()
