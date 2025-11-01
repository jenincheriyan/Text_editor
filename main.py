from tkinter import filedialog, messagebox
import tkinter as tk
filename = None


root = tk.Tk()
root.title("Jenin's Editor")
root.geometry("500x500")

text_area= tk.Text(root, wrap="word", undo=True)
text_area.pack(expand=True, fill="both")

def newFile():
    global filename
    filename="untitled"
    text_area.delete(1.0, tk.END)

def saveFile():
    global filename
    t= text_area.get(1.0,tk.END)
    f= open(filename, 'w')
    f.write(t)
    f.close()
def saveAs():
    f= filedialog.asksaveasfile(mode='w', defaultextension='.txt')
    t = text_area.get(1.0, tk.END)
    try:
        f.write(t.rstrip())
    except:
        tk.showerror(title="Oops!", message="Unable to save file.")

def openFile():
    f=filedialog.askopenfile(mode='r')
    t=f.read()
    text_area.delete(1.0, tk.END)
    text_area.insert(1.0, t)
    f.close()

menubar=tk.Menu(root)
filemenu=tk.Menu(menubar)
filemenu.add_command(label="NEW", command=newFile)
filemenu.add_command(label="OPEN", command=openFile)
filemenu.add_command(label="SAVE", command=saveFile)
filemenu.add_command(label="SAVE AS", command=saveAs)

filemenu.add_separator()
filemenu.add_command(label="QUIT", command=root.quit)
menubar.add_cascade(label="file",menu=filemenu)

root.config(menu=menubar)
root.mainloop()


