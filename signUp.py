from tkinter import *
from tkinter.ttk import Button
from tkinter.ttk import Entry
import os
from tkinter import messagebox
import hashlib
import sqlite3 as sq

def reg_form(SignUp):

    label = Label(SignUp, text="Регистрация", font=("Arial Bold", 25))
    label.grid(column=0, row=0)

    login_l = Label(SignUp, text="Логин:", font=("Arial Bold", 10))
    login_l.grid(column=0, row=1)

    login = Entry(SignUp, width=50)
    login.grid(column=0, row=2)

    pass_l = Label(SignUp, text="Пароль:", font=("Arial Bold", 10))
    pass_l.grid(column=0, row=3)

    password = Entry(SignUp, width=50)
    password.grid(column=0, row=4)

    r_pass_l = Label(SignUp, text="Повторите пароль:", font=("Arial Bold", 10))
    r_pass_l.grid(column=0, row=5)

    r_pass = Entry(SignUp, width=50)
    r_pass.grid(column=0, row=6)


    def reg():
        login_text = "{}".format(login.get())
        nh_password_text = "{}".format(password.get())
        r_pass_l_text = "{}".format(r_pass.get())

        if nh_password_text == r_pass_l_text:
            with sq.connect("firstdb.db") as con:
                cur = con.cursor()
                cur.execute("""CREATE TABLE IF NOT EXISTS users (
                    login TEXT NOT NULL,
                    password TEXT NOT NULL
                    )""")

                cur.execute('INSERT INTO users VALUES (?, ?)', (login_text, r_pass_l_text))
                print('Вы зарегистрированы')
                messagebox.showinfo('Вы зарегистрированы', 'Вы зарегистрированы')

        else:
            print('Пароли не совпадают')

    reg_bt = Button(SignUp, text="Зарегистрировться", width=45, command=reg)
    reg_bt.grid(column=0, row=7)
