from tkinter import StringVar, Label, Entry, Button, Tk, Frame
import Functionality as func
LOGIN_WINDOW_SIZE = '400x400'
MAIN_WINDOW_SIZE = '600x600'
Authenticated = False

class GUI:
    def __init__(**kwargs):
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
        _button = Button(**kwargs)
        _button.pack()

    @staticmethod
    def Init_Label(**kwargs):
        _label = Label(**kwargs)
        _label.pack()

    @staticmethod
    def Init_TextBox(**kwargs):
        _textbox = Entry(**kwargs)
        _textbox.pack()


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
        print('Submitted')
        verify = func.read_authentication(self.username_var.get(), self.password_var.get())
        if verify:
            print('Login Verified')
        else:
            print('Login Rejected. Try Again')


def Init_Login_GUI_1():
    login_win = Tk()
    frame = Frame(login_win)
    frame.pack()
    login_GUI = Login_GUI_02()
    login_GUI.Init_GUI('600x600', 'Login Test')
    login_GUI.GUI_Components()

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


    def submit_details(self):
        print('Submitted')
        print("First Name: %s\nLast Name: %s" % (self.username_var.get(), self.password_var.get()))

class GUI:
    def __init__(**kwargs):
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
        _button = Button(**kwargs)
        _button.pack()

    @staticmethod
    def Init_Label(**kwargs):
        _label = Label(**kwargs)
        _label.pack()

    @staticmethod
    def Init_TextBox(**kwargs):
        _textbox = Entry(**kwargs)
        _textbox.pack()


if __name__ == '__main__': main()