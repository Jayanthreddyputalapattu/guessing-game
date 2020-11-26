import tkinter
import random



computer_guess = random.randint(1,100)


def check():
    user_guess = int(txt_guess.get())


    if user_guess < computer_guess:
        msg = "Higher!"
    elif user_guess > computer_guess:
        msg = "Lower!"
    elif user_guess == computer_guess:
        msg = "You Win!"
    else:
        msg = "Someting went wrong...."

    lbl_result["text"] = msg

    txt_guess.delete(0,5)

def reset():
    global computer_guess
    computer_guess = random.randint(1,100)
    lbl_result["text"] = "Game Reset Guess again!"

root = tkinter.Tk()

root.configure(bg="white")

root.title("Guessing Game")

root.geometry("300x80")



lbl_title = tkinter.Label(root,text="Welcome to the Guessing Game!",bg="white")
lbl_title.pack()

lbl_result = tkinter.Label(root,text="Good Luck!",bg="white")
lbl_result.pack()

btn_check = tkinter.Button(root,text="Check",fg="green",command=check,bg="white")
btn_check.pack(side="left")

btn_Reset = tkinter.Button(root,text="Reset",fg="red",command=reset,bg="white")
btn_Reset.pack(side="right")

txt_guess = tkinter.Entry(root,width=3)
txt_guess.pack()









root.mainloop()
root.destroy()
