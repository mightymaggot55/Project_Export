from tkinter import *
from tkinter.ttk import *

TYPE = ['PAWN', 'ROOK', 'KNIGHT', 'BISHOP', 'QUEEN', 'KING']
STATUS = ['ALIVE', 'DEAD']
TEAM = ['RED', 'BLACK']
Squares = []
start_window_size = "600x650"
isDrawn = False

class ChessPiece:
    def __init__(self, name, startingPosition, type, status, allowedMovement, currentPosition, team):
        self.name = name
        self.startingPosition = startingPosition
        self.type = type
        self.status = status
        self.allowedMovement = allowedMovement
        self.currentPosition = currentPosition
        self.team = team


class Square:
    def __init__(self, x0, y0, x1, y1):
        self.x0 = x0
        self.y0 = y0
        self.x1 = x1
        self.y1 = y1


def Init_Pieces():
    squares = Square()
    P1 = ChessPiece('Pawn_01', '', TYPE[0], STATUS[0], '', '', TEAM[0])
    P2 = ChessPiece('Pawn_02', '', TYPE[0], STATUS[0], '', '', TEAM[0])
    P3 = ChessPiece('Pawn_03', '', TYPE[0], STATUS[0], '', '', TEAM[0])
    P4 = ChessPiece('Pawn_04', '', TYPE[0], STATUS[0], '', '', TEAM[0])
    P5 = ChessPiece('Pawn_05', '', TYPE[0], STATUS[0], '', '', TEAM[0])
    P6 = ChessPiece('Pawn_06', '', TYPE[0], STATUS[0], '', '', TEAM[0])
    P7 = ChessPiece('Pawn_07', '', TYPE[0], STATUS[0], '', '', TEAM[0])
    P8 = ChessPiece('Pawn_08', '', TYPE[0], STATUS[0], '', '', TEAM[0])
    R1 = ChessPiece('Rook_01', '', TYPE[1], STATUS[0], '', '', TEAM[0])
    R2 = ChessPiece('Rook_02', '', TYPE[2], STATUS[0], '', '', TEAM[0])
    K1 = ChessPiece('Knight_01', '', TYPE[3], STATUS[0], '', '', TEAM[0])
    K2 = ChessPiece('Knight_02', '', TYPE[3], STATUS[0], '', '', TEAM[0])
    B1 = ChessPiece('Bishop_01', '', TYPE[4], STATUS[0], '', '', TEAM[0])
    B2 = ChessPiece('Bishop_02', '', TYPE[4], STATUS[0], '', '', TEAM[0])
    Q1 = ChessPiece('Queen', '', TYPE[5], STATUS[0], '', '', TEAM[0])
    KING1 = ChessPiece('King', '', TYPE[6], STATUS[0], '', '', TEAM[0])

class GUI:
    def __init__(self, master_win):
        self.InitGUI(master_win)

    def InitGUI(self, master_win):
        self.master_win = master_win
        self.master_win.title = 'Chess'

        self.clickButtonLabel = Label(master_win, text="Click the button to start")
        self.clickButtonLabel.pack()
        self.startButton = Button(master_win, text='Start Game', command=lambda: self.DrawBoard(master_win))
        self.startButton.pack()

    def DrawBoard(self, master_win):
        #Draws Board and all the squares (can be condensed into a for loop)
        canvas = Canvas()
        canvas.create_rectangle(100,500,500,100) #Outside Board
        A8 = Square(100,150,150,100)
        A7 = Square(100,200,150,150)
        A6 = Square(100,250,150,200)
        A5 = Square(100,300,150,250)
        A4 = Square(100,350,150,300)
        A3 = Square(100,400,150,350)
        A2 = Square(100,450,150,400)
        A1 = Square(100,500,150,450)
        B8 = Square(150,150,200,100)
        B7 = Square(150,200,200,150)
        B6 = Square(150,250,200,200)
        B5 = Square(150,300,200,250)
        B4 = Square(150,350,200,300)
        B3 = Square(150,400,200,350)
        B2 = Square(150,450,200,400)
        B1 = Square(150,500,200,450)
        C8 = Square(200,150,250,100)
        C7 = Square(200,200,250,150)
        C6 = Square(200,250,250,200)
        C5 = Square(200,300,250,250)
        C4 = Square(200,350,250,300)
        C3 = Square(200,400,250,350)
        C2 = Square(200,450,250,400)
        C1 = Square(200,500,250,450)
        D8 = Square(250,150,300,100)
        D7 = Square(250,200,300,150)
        D6 = Square(250,250,300,200)
        D5 = Square(250,300,300,250)
        D4 = Square(250,350,300,300)
        D3 = Square(250,400,300,350)
        D2 = Square(250,450,300,400)
        D1 = Square(250,500,300,450)
        E8 = Square(300,150,350,100)
        E7 = Square(300,200,350,150)
        E6 = Square(300,250,350,200)
        E5 = Square(300,300,350,250)
        E4 = Square(300,350,350,300)
        E3 = Square(300,400,350,350)
        E2 = Square(300,450,350,400)
        E1 = Square(300,500,350,450)
        F8 = Square(350,150,400,100)
        F7 = Square(350,200,400,150)
        F6 = Square(350,250,400,200)
        F5 = Square(350,300,400,250)
        F4 = Square(350,350,400,300)
        F3 = Square(350,400,400,350)
        F2 = Square(350,450,400,400)
        F1 = Square(350,500,400,450)
        G8 = Square(400,150,450,100)
        G7 = Square(400,200,450,150)
        G6 = Square(400,250,450,200)
        G5 = Square(400,300,450,250)
        G4 = Square(400,350,450,300)
        G3 = Square(400,400,450,350)
        G2 = Square(400,450,450,400)
        G1 = Square(400,500,450,450)
        H8 = Square(450,150,500,100)
        H7 = Square(450,200,500,150)
        H6 = Square(450,250,500,200)
        H5 = Square(450,300,500,250)
        H4 = Square(450,350,500,300)
        H3 = Square(450,400,500,350)
        H2 = Square(450,450,500,400)
        H1 = Square(450,500,500,450)
        Squares = [A1, A2, A3, A4, A5, A6, A7, A8, B1, B2, B3, B4, B5, B6, B7, B8, C1, C2, C3, C4, C5, C6, C7, C8, D1, D2, D3, D4, D5, D6, D7, D8, E1, E2, E3, E4, E5, R6, E7, E8, F1, F2, F3, F4, F5, F6, F7, F8, G1, G2, G3, G4, G5, G6, G7, G8, H1, H2, H3, H4, H5, H6, H7, H8]
        print(Squares)
        A_Label = Label(canvas, text='A').place(x=120, y=70)
        eight_Label = Label(canvas, text='8').place(x=80, y=120)
        canvas.create_rectangle(100,150,150,100)          #A8
        canvas.create_rectangle(100,200,150,150)          #A7
        canvas.create_rectangle(100,250,150,200)          #A6
        canvas.create_rectangle(100,300,150,250)          #A5
        canvas.create_rectangle(100,350,150,300)          #A4
        canvas.create_rectangle(100,400,150,350)          #A3
        canvas.create_rectangle(100,450,150,400)          #A2
        canvas.create_rectangle(100,500,150,450)          #A1

        B_Label = Label(canvas, text='B').place(x=170, y=70)
        seven_Label = Label(canvas, text='7').place(x=80, y=170)
        canvas.create_rectangle(150,150,200,100)          #B8
        canvas.create_rectangle(150,200,200,150)          #B7
        canvas.create_rectangle(150,250,200,200)          #B6
        canvas.create_rectangle(150,300,200,250)          #B5
        canvas.create_rectangle(150,350,200,300)          #B4
        canvas.create_rectangle(150,400,200,350)          #B3
        canvas.create_rectangle(150,450,200,400)          #B2
        canvas.create_rectangle(150,500,200,450)          #B1

        C_Label = Label(canvas, text='C').place(x=220, y=70)
        six_Label = Label(canvas, text='6').place(x=80, y=220)
        canvas.create_rectangle(200,150,250,100)          #C8
        canvas.create_rectangle(200,200,250,150)          #C7
        canvas.create_rectangle(200,250,250,200)          #C6
        canvas.create_rectangle(200,300,250,250)          #C5
        canvas.create_rectangle(200,350,250,300)          #C4
        canvas.create_rectangle(200,400,250,350)          #C3
        canvas.create_rectangle(200,450,250,400)          #C2
        canvas.create_rectangle(200,500,250,450)          #C1

        D_Label = Label(canvas, text='D').place(x=270, y=70)
        five_Label = Label(canvas, text='5').place(x=80, y=270)
        canvas.create_rectangle(250,150,300,100)          #D8
        canvas.create_rectangle(250,200,300,150)          #D7
        canvas.create_rectangle(250,250,300,200)          #D6
        canvas.create_rectangle(250,300,300,250)          #D5
        canvas.create_rectangle(250,350,300,300)          #D4
        canvas.create_rectangle(250,400,300,350)          #D3
        canvas.create_rectangle(250,450,300,400)          #D2
        canvas.create_rectangle(250,500,300,450)          #D1

        E_Label = Label(canvas, text='E').place(x=320, y=70)
        four_Label = Label(canvas, text='4').place(x=80, y=320)
        canvas.create_rectangle(300,150,350,100)          #E8
        canvas.create_rectangle(300,200,350,150)          #E7
        canvas.create_rectangle(300,250,350,200)          #E6
        canvas.create_rectangle(300,300,350,250)          #E5
        canvas.create_rectangle(300,350,350,300)          #E4
        canvas.create_rectangle(300,400,350,350)          #E3
        canvas.create_rectangle(300,450,350,400)          #E2
        canvas.create_rectangle(300,500,350,450)          #E1

        F_Label = Label(canvas, text='F').place(x=370, y=70)
        three_Label = Label(canvas, text='3').place(x=80, y=370)
        canvas.create_rectangle(350,150,400,100)          #F8
        canvas.create_rectangle(350,200,400,150)          #F7
        canvas.create_rectangle(350,250,400,200)          #F6
        canvas.create_rectangle(350,300,400,250)          #F5
        canvas.create_rectangle(350,350,400,300)          #F4
        canvas.create_rectangle(350,400,400,350)          #F3
        canvas.create_rectangle(350,450,400,400)          #F2
        canvas.create_rectangle(350,500,400,450)          #F1

        G_Label = Label(canvas, text='G').place(x=420, y=70)
        two_Label = Label(canvas, text='2').place(x=80, y=420)
        canvas.create_rectangle(400,150,450,100)       #G8
        canvas.create_rectangle(400,200,450,150)          #G7
        canvas.create_rectangle(400,250,450,200)          #G6
        canvas.create_rectangle(400,300,450,250)          #G5
        canvas.create_rectangle(400,350,450,300)          #G4
        canvas.create_rectangle(400,400,450,350)          #G3
        canvas.create_rectangle(400,450,450,400)          #G2
        canvas.create_rectangle(400,500,450,450)          #G1

        H_Label = Label(canvas, text='H').place(x=470, y=70)
        one_Label = Label(canvas, text='1').place(x=80, y=470)
        canvas.create_rectangle(450,150,500,100)       #H8
        canvas.create_rectangle(450,200,500,150)          #H7
        canvas.create_rectangle(450,250,500,200)          #H6
        canvas.create_rectangle(450,300,500,250)          #H5
        canvas.create_rectangle(450,350,500,300)          #H4
        canvas.create_rectangle(450,400,500,350)          #H3
        canvas.create_rectangle(450,450,500,400)          #H2
        canvas.create_rectangle(450,500,500,450)          #H1
        canvas.pack(fill=BOTH, expand=1)

def onClick(event):
    x, y = event.x, event.y
    print('{}, {}'.format(x, y))

def Start():
    mainWindow = Tk()
    mainWindow.geometry(start_window_size)
    my_gui = GUI(mainWindow)
    mainWindow.bind('<Motion>', onClick)
    mainWindow.mainloop()

def main():
    Start()

if __name__ == '__main__': main()

