import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

def open_file():
    #opening a file for editing
    file = askopenfilename(filetypes = [("Text Files" , "*.txt"), ("All Files", "*.*")])
    if not file:
        return
    text1.delete("1.0", tk.END)
    
    with open(file, mode = "r", encoding = "utf-8") as input_file:
        text = input_file.read()
        text1.insert(tk.END, text)
    window.title(f'Text Editor - {file}')
        

def save_file():
    #Saving the file to a new file
    file = asksaveasfilename(defaultextension = ".txt", filetypes = [("Text Files" , "*.txt"), ("All Files", "*.*")])
    if not file:
        return
    with open(file, mode = "w", encoding = "utf-8") as output_file:
        text = text1.get("1.0", tk.END)
        output_file.write(text)
    window.title(f'Text Editor - {file}')
    

window = tk.Tk()
window.title("Text Editor")
text1 = tk.Text()
text1.pack(fill = tk.BOTH, side = tk.RIGHT, expand = True)
frame = tk.Frame(relief = tk.RAISED, bd = 2) #gives the button's a raisen look
    #frame is used to group widgets, give them padding and border effect using relief.
btn_save = tk.Button(text = "Save", master = frame, command = save_file )
btn_save.grid(row = 0, column = 0, padx = 5, pady = 5)
btn_open = tk.Button(text = "Open", master = frame, command = open_file)
btn_open.grid(row = 1, column = 0, padx = 5)
frame.pack()
    #frame.grid(row = 0, column = 0)
    #when using grid or pack, remember you can't use the other within the same block being managed by the other
    
window.mainloop()

