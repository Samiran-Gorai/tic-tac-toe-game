
import random 
import tkinter 
from tkinter import *
from functools import partial
from tkinter import messagebox 

sign = 0
 
global board 
board = [[" " for x in range(3)] for y in range(3)] 
  
def winner(b, l): 
    return ((b[0][0] == l and b[0][1] == l and b[0][2] == l) or
            (b[1][0] == l and b[1][1] == l and b[1][2] == l) or
            (b[2][0] == l and b[2][1] == l and b[2][2] == l) or
            (b[0][0] == l and b[1][0] == l and b[2][0] == l) or
            (b[0][1] == l and b[1][1] == l and b[2][1] == l) or
            (b[0][2] == l and b[1][2] == l and b[2][2] == l) or
            (b[0][0] == l and b[1][1] == l and b[2][2] == l) or
            (b[0][2] == l and b[1][1] == l and b[2][0] == l)) 
  

def gameboard_pl(game_board, l1, l2): 
    global button 
    button = [] 
    for i in range(3): 
        m = 3+i 
        button.append(i) 
        button[i] = [] 
        for j in range(3): 
            n = j 
            button[i].append(j) 
            get_t = partial(get_text, i, j, game_board, l1, l2) 
            button[i][j] = Button( 
                game_board, bd=5, command=get_t, height=4, width=8) 
            button[i][j].grid(row=m, column=n) 
    game_board.mainloop() 
  
def get_text(i, j, gb, l1, l2): 
    global sign 
    if board[i][j] == ' ': 
        if sign % 2 == 0: 
            l1.config(state=DISABLED) 
            l2.config(state=ACTIVE) 
            board[i][j] = "X"
        else: 
            l2.config(state=DISABLED) 
            l1.config(state=ACTIVE) 
            board[i][j] = "O"
        sign += 1
        button[i][j].config(text=board[i][j]) 
    if winner(board, "X"): 
        gb.destroy() 
        box = messagebox.showinfo("Winner", "Player 1 won the match")
    elif winner(board, "O"): 
        gb.destroy()
        box = messagebox.showinfo("Winner", "Player 2 won the match")
    elif(isfull()): 
        gb.destroy() 
        box = messagebox.showinfo("Tie Game", "Tie Game") 
  
def isfree(i, j): 
    return board[i][j] == " "

def isfull(): 
    flag = True
    for i in board: 
        if(i.count(' ') > 0): 
            flag = False
    return flag 

def withplayer(game_board): 
    game_board.destroy() 
    game_board = Tk() 
    game_board.title("Tic Tac Toe") 
    l1 = Button(game_board, text = "Player 1 : X", width = 10) 
      
    l1.grid(row = 1, column = 1) 
    l2 = Button(game_board, text = "Player 2 : O",  
                width = 10, state = DISABLED) 
      
    l2.grid(row = 2, column = 1) 
    gameboard_pl(game_board, l1, l2)

def play(): 
    menu = Tk() 
    menu.geometry("300x300")
    menu.title("Tic Tac Toe") 
    wpl = partial(withplayer, menu) 
      
    head = Button(menu, text = "---Welcome to tic-tac-toe---",    
                  fg = "red",width= 500) 
      
    B1 = Button(menu, text = "2 Player Mode", command = wpl, activeforeground = 'red', 
                activebackground = "blue", bg = "yellow", fg = "blue", 
                width = 500, bd = 5) 
      
    B2 = Button(menu, text = "Exit", command = menu.quit, activeforeground = 'red', 
                activebackground = "yellow", bg = "green", fg = "yellow", 
                width = 500, bd = 5) 
    head.pack(side = 'top') 
    B1.pack(side = 'top') 
    B2.pack(side = 'top') 
    menu.mainloop() 

play() 
