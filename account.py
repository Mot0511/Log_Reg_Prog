from tkinter import *
from tkinter.ttk import Button
from tkinter.ttk import Entry
from tkinter import ttk
from signUp import *
from tkinter import filedialog
import sqlite3 as sq
import sys


def connect(dbname):
    with sq.connect(f'{dbname}.db') as db:
        cur = db.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS users (
                    name TEXT NOT NULL,
                    img BLOB NOT NULL
                    )""")
        return cur


def get_image(n):
    try:
        with open(n, "rb") as f:
            return f.read()
    except IOError as e:
        print(e)
        return False

def upload():
    path = filedialog.askopenfilename(initialdir='/', title='Open image', filetypes=(('Images', '*.png'), ('All files', '*.*'))) # получение пути к картинке
    img = get_image(path) # получение картинки
    with sq.connect('firstdb.db') as db:
        cur = db.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS images (
            name TEXT NOT NULL,
            img BLOB NOT NULL
            )""")
        if img:
            binary = sq.Binary(img) # преобразование в бинарный вид


        cur.execute(f"INSERT INTO images VALUES (?, ?)", (log, binary)) # выгрузка в бд
        if cur:
            messagebox.showinfo('Данные добавлены в базу данных', 'Данные добавлены в базу данных')
        else:
            messagebox.showerror('Ошибка при добавлении данных в базу', 'Ошибка при добавлении данных в базу')

def show_users():
    with sq.connect('firstdb.db') as db:
        cur = db.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS users (
                    name TEXT NOT NULL,
                    img BLOB NOT NULL
                    )""")

        cur.execute("SELECT * FROM users")
        fa = cur.fetchall()
        users = ''
        for i in fa:
            users += i[0] + ' '


        listbox.configure(text=users)

def show_count():
    cur = connect('firstdb')
    user = user_count.get()
    cur.execute("SELECT count(login) as count FROM images WHERE login == ?", (user))
    count.configure(text=cur.fetchone()[0])

def in_account(login):
    global log
    log = login
    acc_win = Tk()
    acc_win.title("Аккаунт пользователя")
    acc_win.geometry("360x500")

    tab = ttk.Notebook(acc_win)
    logIn = ttk.Frame(tab)
    SignUp = ttk.Frame(tab)
    tab.add(logIn, text="Личный кабинет")
    tab.add(SignUp, text="Настройки")

    l_login = Label(logIn, text=f"Аккаунт пользователя: {log}", font=("Arial Bold", 15))
    l_login.grid(column=0, row=0)

    upload_bt = Button(logIn, text='Загрузить картинку', command=upload)
    upload_bt.grid(column=0, row=1)
    upload_bt = Button(logIn, text='Показать всех пользователей', command=show_users)
    upload_bt.grid(column=0, row=2)


    global listbox
    listbox = Label(logIn, text='')
    listbox.grid(column=0, row=3)

    global user_count
    user_count = Entry(logIn)
    user_count.grid(column=0, row=4)
    upload_bt = Button(logIn, text='Вывести кол-во картинок у этого пользователя', command=show_count)
    upload_bt.grid(column=0, row=5)
    global count
    count = Label(logIn, text='')
    count.grid(column=0, row=6)

    tab.pack(expand=1, fill='both')
    acc_win.mainloop()