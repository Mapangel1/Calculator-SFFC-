import tkinter as tk
root = tk.Tk()
root.title("FFC")
root.geometry("400x560")
#UI
Output = tk.Text(root, width=48, height=5)
def number_symbols(value):
    Output.insert(tk.END, value)
def clear_button():
    Output.delete("1.0", "end-1c")
def clear_last_number():
    Output.get("1.0", tk.END)
    Output.delete("end-2c", tk.END)
def equal():
    try:
        expression = Output.get("1.0", "end-1c")
        
        tokens = []
        num = ""
        for char in expression:
            if char.isdigit() or char == ".":
                num += char  
            else:
                if num != "":
                    tokens.append(float(num))  
                    num = ""
                if char in "+-*/":
                    tokens.append(char)        
        if num != "":
            tokens.append(float(num))       

    
        i = 0
        while i < len(tokens):
            if tokens[i] == "*":
                tokens[i-1] = tokens[i-1] * tokens[i+1]
                del tokens[i:i+2]  
                i -= 1
            elif tokens[i] == "/":
                try:
                    tokens[i-1] = tokens[i-1] / tokens[i+1]
                except ZeroDivisionError:
                    Output.config(state=tk.NORMAL)
                    Output.delete("1.0", "end-1c")
                    Output.insert(tk.END, "Error: Division by 0")
                    return
                del tokens[i:i+2]
                i -= 1
            else:
                i += 1

    
        i = 0
        while i < len(tokens):
            if tokens[i] == "+":
                tokens[i-1] = tokens[i-1] + tokens[i+1]
                del tokens[i:i+2]
                i -= 1
            elif tokens[i] == "-":
                tokens[i-1] = tokens[i-1] - tokens[i+1]
                del tokens[i:i+2]
                i -= 1
            else:
                i += 1

        result = tokens[0]  

    
        Output.config(state=tk.NORMAL)
        Output.delete("1.0", "end-1c")
        Output.insert(tk.END, str(result))
    except TypeError:
        input("You cannot put letters or multiple symbols silly ")
        pass
Button_1 = tk.Button(root, text="1", width=17, height=3, command=lambda: number_symbols("1"))
Button_2 = tk.Button(root, text="2", width=15, height=3, command=lambda: number_symbols("2"))
Button_3 = tk.Button(root, text="3", width=12, height=3, command=lambda: number_symbols("3"))
Button_4 = tk.Button(root, text="4", width=17, height=3, command=lambda: number_symbols("4"))
Button_5 = tk.Button(root, text="5", width=15, height=3, command=lambda: number_symbols("5"))
Button_6 = tk.Button(root, text="6", width=12, height=3, command=lambda: number_symbols("6"))
Button_7 = tk.Button(root, text="7", width=17, height=3, command=lambda: number_symbols("7"))
Button_8 = tk.Button(root, text="8", width=15, height=3, command=lambda: number_symbols("8"))
Button_9 = tk.Button(root, text="9", width=12, height=3, command=lambda: number_symbols("9"))
Button_0 = tk.Button(root, text="0", width=15, height=3, command=lambda: number_symbols("0"))
Button_Period = tk.Button(root, text=".", width=12, height=3, command=lambda: number_symbols("."))
Button_Negative = tk.Button(root, text="+/-", width=17, height=3, command=lambda: number_symbols("-"))
Button_Add = tk.Button(root, text="+", width=17, height=3, font=("Arial", 9), command=lambda: number_symbols("+"))
Button_Subtract = tk.Button(root, text="-", width=15, height=3, font=("Arial", 9), command=lambda: number_symbols("-"))
Button_Multiply = tk.Button(root, text="x", width=12, height=3, font=("Arial", 9), command=lambda: number_symbols("*"))
Button_Divide = tk.Button(root, text="/", width=17, height=3, font=("Arial", 9), command=lambda: number_symbols("/"))
Button_CE = tk.Button(root, text="CE", width=15, height=3, command=clear_button)
Button_C = tk.Button(root, text="C", width=12,height=3, command=clear_last_number)
Button_Equal = tk.Button(root, text="=", width=54, height=3, command=equal)
Button_1.place(x=10,y=435)
Button_2.place(x=160,y=435)
Button_3.place(x=300,y=435)
Button_4.place(x=10,y=370)
Button_5.place(x=160,y=370)
Button_6.place(x=300,y=370)
Button_7.place(x=10,y=305)
Button_8.place(x=160,y=305)
Button_9.place(x=300,y=305)
Button_0.place(x=160,y=500)
Button_Period.place(x=300,y=500)
Button_Negative.place(x=10,y=500)
Button_Add.place(x=10,y=240)
Button_Subtract.place(x=160,y=240)
Button_Multiply.place(x=300,y=240)
Button_Divide.place(x=10,y=175)
Button_CE.place(x=160,y=175)
Button_C.place(x=300,y=175)
Button_Equal.place(x=10,y=115)
Output.pack()
root.mainloop()