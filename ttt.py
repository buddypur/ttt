from tkinter import *
import tkinter.messagebox

root = Tk()
root.title("zero kaanta")

click = TRUE


def reset():
    button1.config(bg="SystemButtonFace", text=" ")
    button2.config(bg="SystemButtonFace", text=" ")
    button3.config(bg="SystemButtonFace", text=" ")
    button4.config(bg="SystemButtonFace", text=" ")
    button5.config(bg="SystemButtonFace", text=" ")
    button6.config(bg="SystemButtonFace", text=" ")
    button7.config(bg="SystemButtonFace", text=" ")
    button8.config(bg="SystemButtonFace", text=" ")
    button9.config(bg="SystemButtonFace", text=" ")


def xo(buttons):
    global click

    if (button1["text"] == "X" and button2["text"] == "X" and button3["text"] == "X" or
            button4["text"] == "X" and button5["text"] == "X" and button6["text"] == "X" or
            button7["text"] == "X" and button8["text"] == "X" and button9["text"] == "X" or
            button1["text"] == "X" and button4["text"] == "X" and button7["text"] == "X" or
            button2["text"] == "X" and button5["text"] == "X" and button8["text"] == "X" or
            button3["text"] == "X" and button6["text"] == "X" and button9["text"] == "X" or
            button1["text"] == "X" and button5["text"] == "X" and button9["text"] == "X" or
            button3["text"] == "X" and button5["text"] == "X" and button7["text"] == "X"):
        tkinter.messagebox.showinfo("winner X", "you won")

    elif (button1["text"] == "O" and button2["text"] == "O" and button3["text"] == "O" or
          button4["text"] == "O" and button5["text"] == "O" and button6["text"] == "O" or
          button7["text"] == "O" and button8["text"] == "O" and button9["text"] == "O" or
          button1["text"] == "O" and button4["text"] == "O" and button7["text"] == "O" or
          button2["text"] == "O" and button5["text"] == "O" and button8["text"] == "O" or
          button3["text"] == "O" and button6["text"] == "O" and button9["text"] == "O" or
          button1["text"] == "O" and button5["text"] == "O" and button9["text"] == "O" or
          button3["text"] == "O" and button5["text"] == "O" and button7["text"] == "O"):
        tkinter.messagebox.showinfo("winner O", "you won")

    elif buttons["text"] == " " and click == TRUE:
        buttons["text"] = "X"
        click = FALSE
        buttons.config(bg="red")
    elif buttons["text"] == " " and click == FALSE:
        buttons["text"] = "O"
        click = TRUE
        buttons.config(bg="blue")
    else:
        tkinter.messagebox.showinfo("draw", "its a draw")


buttons = StringVar()
button1 = Button(root, text=" ", height=5, width=10, font=("times 10 bold"), command=lambda: xo(button1))
button1.grid(row=0, column=0)
button2 = Button(root, text=" ", height=5, width=10, font=("times 10 bold"), command=lambda: xo(button2))
button2.grid(row=0, column=1)
button3 = Button(root, text=" ", height=5, width=10, font=("times 10 bold"), command=lambda: xo(button3))
button3.grid(row=0, column=2)
button4 = Button(root, text=" ", height=5, width=10, font=("times 10 bold"), command=lambda: xo(button4))
button4.grid(row=1, column=0)
button5 = Button(root, text=" ", height=5, width=10, font=("times 10 bold"), command=lambda: xo(button5))
button5.grid(row=1, column=1)
button6 = Button(root, text=" ", height=5, width=10, font=("times 10 bold"), command=lambda: xo(button6))
button6.grid(row=1, column=2)
button7 = Button(root, text=" ", height=5, width=10, font=("times 10 bold"), command=lambda: xo(button7))
button7.grid(row=2, column=0)
button8 = Button(root, text=" ", height=5, width=10, font=("times 10 bold"), command=lambda: xo(button8))
button8.grid(row=2, column=1)
button9 = Button(root, text=" ", height=5, width=10, font=("times 10 bold"), command=lambda: xo(button9))
button9.grid(row=2, column=2)

restart = Button(root, text="restart", width=20)
restart.grid(columnspan=3, padx=5, pady=5)
restart.config(command=reset)
quit = Button(root, text="quit", width=20, command=root.destroy)
quit.grid(columnspan=4, padx=5, pady=5)
root.mainloop()
