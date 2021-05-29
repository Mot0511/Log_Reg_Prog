from tkinter import *
from tkinter.ttk import Button
from tkinter.ttk import Entry
from tkinter import ttk
from signUp import *
from account import *


win = Tk()
win.title("Войти/Зарегистрировться")
win.geometry("360x500")


tab = ttk.Notebook(win)
logIn = ttk.Frame(tab)
SignUp = ttk.Frame(tab)
tab.add(logIn, text="Войти")
tab.add(SignUp, text="Зарегистрировться")

#log in code
label = Label(logIn, text="Авторизация", font=("Arial Bold", 25))
label.grid(column=0, row=0)

login_l = Label(logIn, text="Логин:", font=("Arial Bold", 10))
login_l.grid(column=0, row=1)

login = Entry(logIn, width=50)
login.grid(column=0, row=2)

pass_l = Label(logIn, text="Пароль:", font=("Arial Bold", 10))
pass_l.grid(column=0, row=3)

password = Entry(logIn, width=50)
password.grid(column=0, row=4)

def login_func():
    login_text = "{}".format(login.get())
    nh_password_text = "{}".format(password.get())

    with sq.connect("firstdb.db") as con:
        cur = con.cursor()

        cur.execute(f"SELECT login, password FROM users WHERE login == '{login_text}'")
        if cur:
            if cur.fetchone()[1] == nh_password_text:
                # print('Вы вошли')
                # messagebox.showinfo('Вы вошли', 'Вы вошли')
                in_account(login_text)

            else:
                messagebox.showerror('Ошибка при входе', 'Ошибка при входе')

        else:
            print('Такой пользователь не найден')


bt = Button(logIn, text="Войти", width=45, command=login_func)
bt.grid(column=0, row=5)


#sign up code
reg_form(SignUp)

tab.pack(expand=1, fill='both')
win.mainloop()
