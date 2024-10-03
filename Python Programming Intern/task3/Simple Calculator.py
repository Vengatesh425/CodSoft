import tkinter as tk

def button_click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(value))

def clear_display():
    entry.delete(0, tk.END)

def calculate():
    try:
        expr = entry.get()
        if "+" in expr:
            num1,num2 = map(float,expr.split("+"))
            result = num1 + num2 if '.' in expr else int(num1 + num2)
        elif "-" in expr:
            num1,num2 = map(float,expr.split("-"))
            result = num1 - num2 if '.' in expr else int(num1 - num2)
        elif "*" in expr:
            num1,num2 = map(float,expr.split("*"))
            result = num1 * num2 if '.' in expr else int(num1 * num2)
        elif "/" in expr:
            num1,num2 = map(float,expr.split("/"))
            result = num1 / num2 if num2 != 0 else "Zero Division Error"
            
        else:
            result = "Invalid input value"
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
        
    except ValueError:
        entry.delete(0, tk.END)
        entry.insert(0, "Invalid input")

root = tk.Tk()
root.title("Simple Calculator")

entry = tk.Entry(root,width=16,font=('Arial',24),bd=8,insertwidth=5,borderwidth=10)
entry.grid(row=0,column=0,columnspan=4)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'  
]

for i, button in enumerate(buttons):
    if button == '=':
        action= calculate
    else:
        action= lambda b=button: button_click(b)
        
    tk.Button(root,text=button,padx=20,pady=20,font=('Arial',18),bd=8,command=action).grid(row=(i//4)+1,column=i%4)

tk.Button(root,text='C',padx=20,pady=20,font=('Arial',18),bd=8,command=clear_display).grid(row=5,column=0)

root.mainloop()
