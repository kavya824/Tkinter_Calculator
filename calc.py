import tkinter as tk 
"""Imports Tkinter module ----- tk is an alias for  easy access """

#button click handler
def press(v):
    entry.insert(tk.END, v)
    '''Called when a number or operator button is clicked 
      inserts the pressed value at the end of entry widget'''
      
def clear():
    entry.delete(0, tk.END)
    '''Clears the calculator screen
    Deletes all charcters from index 0 to END'''
    
def calc():
    try:
        result = eval(entry.get())
        '''entry.get() retrives the expression (eg - 5+3)
        eval() evaluates the stringg as a python expression'''
        
        entry.delete(0, tk.END)   # clears the screen 
        entry.intsert(0, result)   #displays the result
        
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Invalid expression")
        '''Handles invalid expressions (eg- 5++)
         Display appropriate message instead of crashing'''
         
#main window creation
root = tk.Tk()  #creates the main application window 
root.title("Calculator") # sets window title
root.configure(bg= "#1e1e1e") # sets background color
root.resizable(False, False) # disables resizing of window

#entry widget (display screen)
entry = tk.Entry(   
    root,
    font = ("arial", 20),
    bg = "#2d2d2d",
    fg = "white",
    bd = 0,
    justify="right"
     )
'''Text input field
   Acts as calculator display
   Righht-aligned for better calculator look'''
   
entry.grid(row=0, column=0, columnspan=4, padx=12, pady=12, ipady=10)
'''Places entry at top
columnspan=4 makes it streach across 4 columns'''

#Button labels
buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "=", "+",]

'''representt calculator buttons
stored in list to reduce repetitive code'''

#dynamic button creation
r=1
c=0
'''Rows and column counters for grid layout'''
for b in buttons:
    cmd = calc if b =="=" else lambda x=b: press(x)
    '''if button is "=' call  calc()
    otherwise, call press() with the button value
    lambda x=b prevents late binding issue'''
    
    
    tk.Button(
        root,
        text=b,
        command=cmd,    # these 3 lines creates  abutton widget
        font=("calibari", 14),
        width=5,
        height=2,
        bg= "orange" if b in "=-*/" else "black",
        fg = "white",
        bd=0
    ).grid(row=r, column=c, padx=6, pady=6)
    c+=1
    if c==4:
        r+=1
        c=0
        '''moves to next row after 4 buttons'''
        
#clear button
tk.Button(
    root,
    text="C",
    command=clear,
    font=("Calibri",14),
    bg="grey",
    bd=0,
    width=22,
    height=2
).grid(row=r, column=0, columnspan=4,pady=8)

root.mainloop()
'''keeps the window running
listen for user interactions'''
