import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x400")
root.resizable(False, False)

# Entry field to display expression
expression = ""
input_text = tk.StringVar()

# Function to update expression
def press(num):
    global expression
    expression += str(num)
    input_text.set(expression)

# Function to evaluate final expression
def equalpress():
    try:
        global expression
        total = str(eval(expression))
        input_text.set(total)
        expression = total
    except:
        input_text.set("Error")
        expression = ""

# Function to clear the input field
def clear():
    global expression
    expression = ""
    input_text.set("")

# Entry box
entry = tk.Entry(root, textvariable=input_text, font=('Arial', 20, 'bold'), bd=10, insertwidth=2, width=14, borderwidth=4, relief='ridge', justify='right')
entry.grid(row=0, column=0, columnspan=4, pady=10)

# Button layout
buttons = [
    ('7',1,0), ('8',1,1), ('9',1,2), ('/',1,3),
    ('4',2,0), ('5',2,1), ('6',2,2), ('*',2,3),
    ('1',3,0), ('2',3,1), ('3',3,2), ('-',3,3),
    ('0',4,0), ('.',4,1), ('+',4,2), ('=',4,3),
]

# Add buttons to window
for (text, row, col) in buttons:
    if text == '=':
        tk.Button(root, text=text, padx=20, pady=20, font=('Arial', 18, 'bold'),
                  bg='lightgreen', command=equalpress).grid(row=row, column=col, sticky="nsew")
    else:
        tk.Button(root, text=text, padx=20, pady=20, font=('Arial', 18, 'bold'),
                  command=lambda t=text: press(t)).grid(row=row, column=col, sticky="nsew")

# Clear button
tk.Button(root, text='C', padx=20, pady=20, font=('Arial', 18, 'bold'),
          bg='tomato', command=clear).grid(row=5, column=0, columnspan=4, sticky="nsew")

# Configure grid layout
for i in range(6):
    root.grid_rowconfigure(i, weight=1)
for i in range(4):
    root.grid_columnconfigure(i, weight=1)

# Run the main loop
root.mainloop()