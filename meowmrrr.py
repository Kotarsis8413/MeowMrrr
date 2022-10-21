from tkinter import *
def wait(timewait, waittext):
    import time
    print(waittext + str(timewait))
    time.sleep(timewait)
def close(closelog):
    import sys
    sys.exit('programm closed, reason: ' + closelog)
def log(text):
    print(text)

class f:
    def read(filename):
        fileopen = open(filename, 'r')
        log(fileopen.read())
        fileopen.close()
    def edit(filename, content):
        fileopen = open(filename, 'w')
        fileopen.write(content)
        fileopen.close()

filee = f

class message:
    def info(contents, messages):
        from tkinter import messagebox
        messagebox.showinfo(contents, message=messages)
    def warning(contents, messages):
        from tkinter import messagebox
        messagebox.showwarning(contents, message=messages)
    def error(contents, messages):
        from tkinter import messagebox
        messagebox.showerror(contents, message=messages)
class welcome:
    def default(programm_name, message, contents):
        from tkinter import messagebox
        messagebox.showinfo(contents, message='welcome to the ' + programm_name + ', ' + message)
    def interface(programm_name, message, contents, size, color, fontsize):
        root = Tk()
        root.title(contents)
        root.geometry(size)
        root['bg'] = color
        info = 'welcome to the ' + programm_name + ', ' + message
        Label(root, text=info, bg=color, font="Arial " + fontsize).pack()
        Button(root, text='close', bg=color, font="Arial " + fontsize, command=lambda: root.destroy()).pack()
        root.mainloop()







