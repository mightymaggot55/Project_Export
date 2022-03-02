from tkinter import StringVar, Label, Entry, Button, Tk, Frame
LOGIN_WINDOW_SIZE = '400x400'
MAIN_WINDOW_SIZE = '600x600'
from os import read, write

def read_authentication(_file, _username, _password):
    path = 'Project1/Authentication Names'
    file = open(path, 'r')
    lines = file.readline()
    for line in lines:
        u_input = str.split(',')
        username = u_input[0]
        password = u_input[1]
        if _username == username & _password == password:
            print('Credentials Verified')
            return True
        else:
            print('Invalid Credentials')
            return False


def Write_File():
    pass

def Authenticate():
    read_file()

def Hash_Password():
    pass

