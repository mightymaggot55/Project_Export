from tkinter import *
BASE_WINDOW_SIZE = '600x600'
name_var = ""
password_var = ""

class GUI:
    def __init__(self, window):
        self.window = window

    def show_entry_fields(self, user, password):

        print("First Name: %s\nLast Name: %s" % (user, password))


    def create_input_boxes(self, window, frame):
        username_input = StringVar
        password_input = StringVar
        username_label = Label(frame, text="Username")
        username_input = Entry(frame, width=40, textvariable=username_input)
        password_label = Label(frame, text="Password")
        password_input = Entry(frame, width=40, textvariable=password_input)
        input_button = Button(frame, text="Submit", width="34", command=lambda: self.show_entry_fields())

        username_label.pack()
        username_input.pack()
        password_label.pack()
        password_input.pack()
        input_button.pack()

def create_input_boxes(window, frame):
    gui = GUI(window)
    gui.create_input_boxes(window, frame)
    gui.show_entry_fields()

def create_main_window(window, frame):
    window.geometry(BASE_WINDOW_SIZE)
    window.title("Login Page")
    window.mainloop()

def Initalise_Login_GUI():
    root = Tk()
    frame = Frame(root)

    frame.pack()
    create_input_boxes(root, frame)
    create_main_window(root, frame)

def Authenticate():
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



def main():
    Initalise_Login_GUI()
    Authenticate()
    print(name_var, password_var)
if __name__ == '__main__':
    main()

