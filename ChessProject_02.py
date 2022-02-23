from tkinter import *
from tkinter.ttk import *

CHESS_PIECE = ['PAWN', 'ROOK', 'KNIGHT', 'BISHOP', 'QUEEN', 'KING']
STATUS = ['ALIVE', 'DEAD']
TEAM = ['RED', 'BLACK']
Squares = []
start_window_size = "600x650"
isDrawn = False
Square_arr = {     'A1' : [100,500,150,450],
                   'A2' : [100,450,150,400],
                   'A3' : [100,400,150,350],
                   'A4' : [100,350,150,300],
                   'A5' : [100,300,150,250],
                   'A6' : [100,250,150,200],
                   'A7' : [100,200,150,150],
                   'A8' : [100,150,150,100],
                   'B1' : [150,500,200,450],
                   'B2' : [150,450,200,400],
                   'B3' : [150,400,200,350],
                   'B4' : [150,350,200,300],
                   'B5' : [150,300,200,250],
                   'B6' : [150,250,200,200],
                   'B7' : [150,200,200,150],
                   'B8' : [150,150,200,100],
                   'C1' : [200,500,250,450],
                   'C2' : [200,450,250,400],
                   'C3' : [200,400,250,350],
                   'C4' : [200,350,250,300],
                   'C5' : [200,300,250,250],
                   'C6' : [200,250,250,200],
                   'C7' : [200,200,250,150],
                   'C8' : [200,150,250,100],
                   'D1' : [250,500,300,450],
                   'D2' : [250,450,300,400],
                   'D3' : [250,400,300,350],
                   'D4' : [250,350,300,300],
                   'D5' : [250,300,300,250],
                   'D6' : [250,250,300,200],
                   'D7' : [250,200,300,150],
                   'D8' : [250,150,300,100],
                   'E1' : [300,500,350,450],
                   'E2' : [300,450,350,400],
                   'E3' : [300,400,350,350],
                   'E4' : [300,350,350,300],
                   'E5' : [300,300,350,250],
                   'E6' : [300,250,350,200],
                   'E7' : [300,200,350,150],
                   'E8' : [300,150,350,100],
                   'F1' : [350,500,400,450],
                   'F2' : [350,450,400,400],
                   'F3' : [350,400,400,350],
                   'F4' : [350,350,400,300],
                   'F5' : [350,300,400,250],
                   'F6' : [350,250,400,200],
                   'F7' : [350,200,400,150],
                   'F8' : [350,150,400,100],
                   'G1' : [400,500,450,450],
                   'G2' : [400,450,450,400],
                   'G3' : [400,400,450,350],
                   'G4' : [400,350,450,300],
                   'G5' : [400,300,450,250],
                   'G6' : [400,250,450,200],
                   'G7' : [400,200,450,150],
                   'G8' : [400,150,450,100],
                   'H1' : [450,500,500,450],
                   'H2' : [450,450,500,400],
                   'H3' : [450,400,500,350],
                   'H4' : [450,350,500,300],
                   'H5' : [450,300,500,250],
                   'H6' : [450,250,500,200],
                   'H7' : [450,200,500,150],
                   'H8' : [450,150,500,100]
                   }

class ChessPiece:
    def __init__(self, name, startingPosition, piece, status, allowedMovement, currentPosition, team):
        self.name = name
        self.startingPosition = startingPosition
        self.piece = piece
        self.status = status
        self.allowedMovement = allowedMovement
        self.currentPosition = currentPosition
        self.team = team


#class Square:
#    def __init__(self, x0, y0, x1, y1):
#        self.x0 = x0
#        self.y0 = y0
#        self.x1 = x1
#        self.y1 = y1

class Square(dict):
    def __init__(self, default=None):
        dict.__init__(self)
        self.default = default

    def __getitem__(self, key):
        try:
            return dict.__getitem__(self, key)
        except KeyError:
            return self.default



def Init_Pieces():
    squares = Square()
    P1 = ChessPiece('Pawn_01', '', CHESS_PIECE[0], STATUS[0], '', '', TEAM[0])
    P2 = ChessPiece('Pawn_02', '', CHESS_PIECE[0], STATUS[0], '', '', TEAM[0])
    P3 = ChessPiece('Pawn_03', '', CHESS_PIECE[0], STATUS[0], '', '', TEAM[0])
    P4 = ChessPiece('Pawn_04', '', CHESS_PIECE[0], STATUS[0], '', '', TEAM[0])
    P5 = ChessPiece('Pawn_05', '', CHESS_PIECE[0], STATUS[0], '', '', TEAM[0])
    P6 = ChessPiece('Pawn_06', '', CHESS_PIECE[0], STATUS[0], '', '', TEAM[0])
    P7 = ChessPiece('Pawn_07', '', CHESS_PIECE[0], STATUS[0], '', '', TEAM[0])
    P8 = ChessPiece('Pawn_08', '', CHESS_PIECE[0], STATUS[0], '', '', TEAM[0])
    R1 = ChessPiece('Rook_01', '', CHESS_PIECE[1], STATUS[0], '', '', TEAM[0])
    R2 = ChessPiece('Rook_02', '', CHESS_PIECE[2], STATUS[0], '', '', TEAM[0])
    K1 = ChessPiece('Knight_01', '', CHESS_PIECE[3], STATUS[0], '', '', TEAM[0])
    K2 = ChessPiece('Knight_02', '', CHESS_PIECE[3], STATUS[0], '', '', TEAM[0])
    B1 = ChessPiece('Bishop_01', '', CHESS_PIECE[4], STATUS[0], '', '', TEAM[0])
    B2 = ChessPiece('Bishop_02', '', CHESS_PIECE[4], STATUS[0], '', '', TEAM[0])
    Q1 = ChessPiece('Queen', '', CHESS_PIECE[5], STATUS[0], '', '', TEAM[0])
    KING1 = ChessPiece('King', '', CHESS_PIECE[6], STATUS[0], '', '', TEAM[0])

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

      #  Squares = [A1, A2, A3, A4, A5, A6, A7, A8, B1, B2, B3, B4, B5, B6, B7, B8, C1, C2, C3, C4, C5, C6, C7, C8, D1, D2, D3, D4, D5, D6, D7, D8, E1, E2, E3, E4, E5, E6, E7, E8, F1, F2, F3, F4, F5, F6, F7, F8, G1, G2, G3, G4, G5, G6, G7, G8, H1, H2, H3, H4, H5, H6, H7, H8]
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


