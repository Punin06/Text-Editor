import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

#function to open file
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
        
#function to save file
def save_file():
    #Saving the file to a new file
    file = asksaveasfilename(defaultextension = ".txt", filetypes = [("Text Files" , "*.txt"), ("All Files", "*.*")])
    if not file:
        return
    with open(file, mode = "w", encoding = "utf-8") as output_file:
        text = text1.get("1.0", tk.END)
        output_file.write(text)
    window.title(f'Text Editor - {file}')
    
#Creating window
window = tk.Tk()
#Setting title to Text Editor
window.title("Text Editor")
#Creating the text widget and storing it in text1 to access and adding it to the window via pack.
text1 = tk.Text()
text1.pack(fill = tk.BOTH, side = tk.RIGHT, expand = True)
#Creating frame to store buttons.
frame = tk.Frame(relief = tk.RAISED, bd = 2) 
#Creating a save button and and open button, and then adding them to the window
btn_save = tk.Button(text = "Save", master = frame, command = save_file )
btn_save.grid(row = 0, column = 0, padx = 5, pady = 5)
btn_open = tk.Button(text = "Open", master = frame, command = open_file)
btn_open.grid(row = 1, column = 0, padx = 5)
frame.pack()
    
window.mainloop()

