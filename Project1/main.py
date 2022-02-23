from tkinter import StringVar, Label, Entry, Button, Tk, Frame
LOGIN_WINDOW_SIZE = '400x400'
MAIN_WINDOW_SIZE = '600x600'
from os import read, write

def main():
    #Init_Login_GUI()
    Init_CallLog_GUI()
    #Init_Login_GUI_1()
    #Hash_Password()
    #Encrypt()
    #Authenticate()
    #Init_CallLog_Window()

def Init_CallLog_GUI():
    _gui = CallLog_GUI()
    _gui.Init_Window()


def Init_Login_GUI():
    login_win = Tk()
    frame = Frame(login_win)
    frame.pack()
    gui = Login_GUI()
    gui.create_input_boxes(frame)
    gui.create_login_window(login_win)

def Init_Login_GUI_1():
    login_win = Tk()
    frame = Frame(login_win)
    frame.pack()
    login_GUI = Login_GUI_02()
    login_GUI.Init_GUI('600x600', 'Login Test')
    login_GUI.GUI_Components()


class Login_GUI:
    def __init__(self):
        self.username_var = StringVar()
        self.password_var = StringVar()

    def create_input_boxes(self, frame):
        username_label = Label(frame, text="Username")
        username_input = Entry(frame, width=40, textvariable=self.username_var)
        password_label = Label(frame, text="Password")
        password_input = Entry(frame, width=40, textvariable=self.password_var)
        input_button = Button(frame, text="Submit", width="34", command=lambda: self.submit_details())
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

    def submit_details(self):
        print('Submitted')
        print("First Name: %s\nLast Name: %s" % (self.username_var.get(), self.password_var.get()))



#______________________________________________________________________________


class GUI:
    def __init__(*args):
        print()

    @staticmethod
    def Init_GUI(win_size, title):
        GUI_window = Tk()
        frame = Frame(GUI_window)
        GUI_window.geometry(win_size)
        GUI_window.title(title)

    @staticmethod
    def Init_Components(**kwargs):
       pass

    @staticmethod
    def Init_Button(**kwargs):
        _button = Button(kwargs)
        _button.pack()

    @staticmethod
    def Init_Label(**kwargs):
        _label = Label(kwargs)
        _label.pack()

    @staticmethod
    def Init_TextBox(**kwargs):
        _textbox = Entry(kwargs)
        _textbox.pack()

#_____________________________________________________________________


class Login_GUI_02(GUI):
    def __init__(self):
        super().__init__()
        self.username_var = StringVar()
        self.password_var = StringVar()


    def GUI_Components(self):
        self.Init_GUI('800x800', 'Login Page')
        self.Init_Label(text='TEST', width=40, height=10)

        self.Init_Button(text='button', width=40, height=10)
        self.Init_Button(text='Submit', width=34, command=lambda: self.submit_details())

        self.Init_TextBox(width=40, height=10, textvarible=self.password_var)
        self.Init_TextBox(width=40, height=10, textvariable=self.username_var)

    def submit(self):
        print(self.username_var, self.password_var)
        pass

    @staticmethod
    def call_log_window(login_window):
        login_window.geometry(LOGIN_WINDOW_SIZE)
        login_window.title("Login Page")
        login_window.mainloop()

    def submit_details(self):
        print('Submitted')
        print("First Name: %s\nLast Name: %s" % (self.username_var.get(), self.password_var.get()))



#_____________________________________________________________________________



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




def read_file():
    path = 'C:/Project1/Authentication Names'
    file = open('Authentication Names.txt', 'r')
    lines = file.readline()
    for line in lines:
        if line == '':
            break



def Encrypt():
    pass

def Authenticate():
    read_file()

def Hash_Password():
    pass

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



if __name__ == '__main__': main()

