from tkinter import StringVar, Label, Entry, Button, Tk, Frame
LOGIN_WINDOW_SIZE = '400x400'
MAIN_WINDOW_SIZE = '600x600'


class CallLog_GUI:
    def __init__(self):
        pass

    def Init_Window(self):
        callLog_window = Tk()
        frame = Frame(callLog_window)
        callLog_window.geometry(MAIN_WINDOW_SIZE)
        callLog_window.title('Call Log System')
        self.Init_Components()
        self.Init_GUI(callLog_window)


    def Init_Components(self):
        _label01 = Label(text='Ticket Search', width=15).grid(row=1, column=0)
        _entry01 = Entry(width=30).grid(row=0, column=0)
        _button01 = Button(text='View Current', width= 20, height=5, command=lambda: self.Current_Tickets())
        _button02 = Button(text='Raise a Ticket', width= 20, height=5, command=lambda: self.Raise_Ticket())
        _button03 = Button(text='Search Ticket', width= 10,height=0, command=lambda: self.Search_Tickets()).grid(row=0, column=1)

    @staticmethod
    def call_log_window(login_window):
        login_window.geometry(LOGIN_WINDOW_SIZE)
        login_window.title("Login Page")
        login_window.mainloop()

    @staticmethod
    def Init_GUI(gui_window):
        gui_window.mainloop()

    def Raise_Ticket(self):
        print('Raise Ticket')
        pass

    def Current_Tickets(self):
        print('View Tickets')
        pass

    def Search_Tickets(self):
        print('Search Tickets')
        pass
