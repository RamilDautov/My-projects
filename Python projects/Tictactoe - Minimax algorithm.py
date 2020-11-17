from tkinter import *
import tkinter.messagebox
import math
from sys import exit
tk = Tk()
tk.title("Tic Tac Toe")

bclick = True
flag = 0

scores = {
    "X": -1,
    "O": 1,
    "Tie": 0
}

def disableButton():
    button1.configure(state=DISABLED)
    button2.configure(state=DISABLED)
    button3.configure(state=DISABLED)
    button4.configure(state=DISABLED)
    button5.configure(state=DISABLED)
    button6.configure(state=DISABLED)
    button7.configure(state=DISABLED)
    button8.configure(state=DISABLED)
    button9.configure(state=DISABLED)



def btnClick(buttons):
    global bclick, flag
    if buttons["text"] == " " and bclick == True:
        buttons["text"] = "X"
        bclick = False
        checkForWin()
        flag += 1
        aIturn()
        checkForWin()
        flag += 1
    else:
        tkinter.messagebox.showinfo("Tic-Tac-Toe", "Button already Clicked!")


def aIturn():
    global bclick, flag
    a = [button1, button2, button3, button4, button5, button6, button7, button8, button9]
    c = [[button1["text"], button2["text"], button3["text"]],
         [button4["text"], button5["text"], button6["text"]],
         [button7["text"], button8["text"], button9["text"]]]
    bestScore = -math.inf
    for i in range(0, 3):
        for j in range(0, 3):
            if c[i][j] == " ":
                c[i][j] = "O"
                score = minimax(c, 0, False)
                c[i][j] = " "
                if score > bestScore:
                    bestScore = score
                    bestMove = [i, j]
    a[3*bestMove[0]+bestMove[1]]["text"] = "O"
    bclick = True


def minimax(board, depth, isMaximizing):
    result = checkWinner(board, depth)
    if result is not None:
        score = scores[result]
        return score

    if isMaximizing:
        bestScore = -math.inf
        for i in range(0, 3):
            for j in range(0, 3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    score = minimax(board, depth + 1, False)
                    board[i][j] = " "
                    if score > bestScore:
                        bestScore = score
        return bestScore
    else:
        bestScore = math.inf
        for i in range(0, 3):
            for j in range(0, 3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    score = minimax(board, depth + 1, True)
                    board[i][j] = " "
                    if score < bestScore:
                        bestScore = score
        return bestScore



def checkForWin():
    if (button1['text'] == 'X' and button2['text'] == 'X' and button3['text'] == 'X' or
        button4['text'] == 'X' and button5['text'] == 'X' and button6['text'] == 'X' or
        button7['text'] == 'X' and button8['text'] == 'X' and button9['text'] == 'X' or
        button1['text'] == 'X' and button5['text'] == 'X' and button9['text'] == 'X' or
        button3['text'] == 'X' and button5['text'] == 'X' and button7['text'] == 'X' or
        button1['text'] == 'X' and button4['text'] == 'X' and button7['text'] == 'X' or
        button2['text'] == 'X' and button5['text'] == 'X' and button8['text'] == 'X' or
        button3['text'] == 'X' and button6['text'] == 'X' and button9['text'] == 'X'):
        disableButton()
        tkinter.messagebox.showinfo("Tic-Tac-Toe", "You won!")
        exit(0)

    elif(flag == 8):
        tkinter.messagebox.showinfo("Tic-Tac-Toe", "It is a Tie")
        exit(0)

    elif (button1['text'] == 'O' and button2['text'] == 'O' and button3['text'] == 'O' or
          button4['text'] == 'O' and button5['text'] == 'O' and button6['text'] == 'O' or
          button7['text'] == 'O' and button8['text'] == 'O' and button9['text'] == 'O' or
          button1['text'] == 'O' and button5['text'] == 'O' and button9['text'] == 'O' or
          button3['text'] == 'O' and button5['text'] == 'O' and button7['text'] == 'O' or
          button1['text'] == 'O' and button4['text'] == 'O' and button7['text'] == 'O' or
          button2['text'] == 'O' and button5['text'] == 'O' and button8['text'] == 'O' or
          button3['text'] == 'O' and button6['text'] == 'O' and button9['text'] == 'O'):
        disableButton()
        tkinter.messagebox.showinfo("Tic-Tac-Toe", "You are loser!")
        exit(0)

def checkWinner(board, depth):
    global flag
    if (board[0][0] == 'X' and board[0][1] == 'X' and board[0][2] == 'X' or
        board[1][0] == 'X' and board[1][1] == 'X' and board[1][2] == 'X' or
        board[2][0] == 'X' and board[2][1] == 'X' and board[2][2] == 'X' or
        board[0][0] == 'X' and board[1][1] == 'X' and board[2][2] == 'X' or
        board[0][2] == 'X' and board[1][1] == 'X' and board[2][0] == 'X' or
        board[0][0] == 'X' and board[1][0] == 'X' and board[2][0] == 'X' or
        board[0][1] == 'X' and board[1][1] == 'X' and board[2][1] == 'X' or
        board[0][2] == 'X' and board[1][2] == 'X' and board[2][2] == 'X'):
        return "X"

    elif(depth + flag == 8):
        return "Tie"

    elif (board[0][0] == 'O' and board[0][1] == 'O' and board[0][2] == 'O' or
        board[1][0] == 'O' and board[1][1] == 'O' and board[1][2] == 'O' or
        board[2][0] == 'O' and board[2][1] == 'O' and board[2][2] == 'O' or
        board[0][0] == 'O' and board[1][1] == 'O' and board[2][2] == 'O' or
        board[0][2] == 'O' and board[1][1] == 'O' and board[2][0] == 'O' or
        board[0][0] == 'O' and board[1][0] == 'O' and board[2][0] == 'O' or
        board[0][1] == 'O' and board[1][1] == 'O' and board[2][1] == 'O' or
        board[0][2] == 'O' and board[1][2] == 'O' and board[2][2] == 'O'):
        return "O"
    else:
        return None

buttons = StringVar()


button1 = Button(tk, text=" ", font='Times 20 bold', bg='gray', fg='white', height=4, width=8, command=lambda: btnClick(button1))
button1.grid(row=3, column=0)

button2 = Button(tk, text=' ', font='Times 20 bold', bg='gray', fg='white', height=4, width=8, command=lambda: btnClick(button2))
button2.grid(row=3, column=1)

button3 = Button(tk, text=' ', font='Times 20 bold', bg='gray', fg='white', height=4, width=8, command=lambda: btnClick(button3))
button3.grid(row=3, column=2)

button4 = Button(tk, text=' ', font='Times 20 bold', bg='gray', fg='white', height=4, width=8, command=lambda: btnClick(button4))
button4.grid(row=4, column=0)

button5 = Button(tk, text=' ', font='Times 20 bold', bg='gray', fg='white', height=4, width=8, command=lambda: btnClick(button5))
button5.grid(row=4, column=1)

button6 = Button(tk, text=' ', font='Times 20 bold', bg='gray', fg='white', height=4, width=8, command=lambda: btnClick(button6))
button6.grid(row=4, column=2)

button7 = Button(tk, text=' ', font='Times 20 bold', bg='gray', fg='white', height=4, width=8, command=lambda: btnClick(button7))
button7.grid(row=5, column=0)

button8 = Button(tk, text=' ', font='Times 20 bold', bg='gray', fg='white', height=4, width=8, command=lambda: btnClick(button8))
button8.grid(row=5, column=1)

button9 = Button(tk, text=' ', font='Times 20 bold', bg='gray', fg='white', height=4, width=8, command=lambda: btnClick(button9))
button9.grid(row=5, column=2)

tk.mainloop()
