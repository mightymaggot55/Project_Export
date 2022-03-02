from tkinter import StringVar, Label, Entry, Button, Tk, Frame
LOGIN_WINDOW_SIZE = '400x400'
MAIN_WINDOW_SIZE = '600x400'
from os import read, write
Login_File = r'/Authentication Names'

def Init_Login_GUI():
    login_win = Tk()
    frame = Frame(login_win)
    frame.pack()
    gui = Login_GUI()
    gui.create_input_boxes(frame)
    gui.create_login_window(login_win)

def Init_CallLog_GUI():
    _gui = CallLog_GUI()
    _gui.Init_Window()


def Encrypt():
    pass

def read_authentication(_file, _username, _password):
    with open(_file, 'r'):
        lines = _file.read()
        for line in lines:
            u_input = line.split(',')
            username = u_input[0]
            password = u_input[1]
            if _username == username & _password == password:
                print('Credentials Verified')
                return True
            else:
                print('Invalid Credentials')
                return False


class Ticket:
    def __init__(self, user, department, email, issue_summary, issue_description, date, status, assigned):
        self.user = user
        self.department = department
        self.email = email
        self.issue_summary = issue_summary
        self.issue_description = issue_description
        self.date = date
        self.status = status
        self.assigned = assigned

class Login_GUI:
    def __init__(self):
        self.username_var = StringVar()
        self.password_var = StringVar()

    def create_input_boxes(self, frame):
        username_label = Label(frame, text="Username")
        username_input = Entry(frame, width=40, textvariable=self.username_var)
        password_label = Label(frame, text="Password")
        password_input = Entry(frame, width=40, textvariable=self.password_var)
        input_button = Button(frame, text="Submit", width="34", command=lambda: self.Authenticate())
        username_label.pack()
        username_input.pack()
        password_label.pack()
        password_input.pack()
        input_button.pack()

    @staticmethod
    def create_login_window(login_window):
        login_window.geometry(LOGIN_WINDOW_SIZE)
        login_window.title("Login Page")
        login_window.mainloop()

    def Authenticate(self):
        pass


def Write_File():
    pass



def Hash_Password():
    pass

class CallLog_GUI:
    def __init__(self):
        pass

    def Init_Window(self):
        callLog_window = Tk()
        frame = Frame(callLog_window)
        callLog_window.geometry(MAIN_WINDOW_SIZE)
        callLog_window.title('Call Log System')
        callLog_window.columnconfigure(4, weight=2)


        self.Init_Components()
        self.Init_GUI(callLog_window)


    def Init_Components(self):
        _label01 = Label(text='Ticket Search', width=15).grid(column=0, row=4)
        _entry01 = Entry(width=30).grid(column=1, row=4)
        _button01 = Button(text='View Current', width= 20, height=0, command=lambda: self.Current_Tickets(), borderwidth=3).grid(column=0, row=0)
        _button02 = Button(text='Raise a Ticket', width= 20, height=0, command=lambda: self.Raise_Ticket(), borderwidth=3).grid(column=0, row=1)
        _button03 = Button(text='Search Ticket', width= 10,height=0, command=lambda: self.Search_Tickets(), borderwidth=3).grid(column=4, row=4)

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



def main():
    #Init_Login_GUI()
    Init_CallLog_GUI()

if __name__ == '__main__': main()