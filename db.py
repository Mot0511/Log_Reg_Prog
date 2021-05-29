import sqlite3 as sq


def read_img(n):
    try:
        with open(n, "rb") as f:
            return f.read()
    except IOError as e:
        print(e)
        return False


with sq.connect("firstdb.db") as con:
    cur = con.cursor()

    cur.execute("""CREATE TABLE IF NOT EXISTS user (
    name TEXT NOT NULL,
    img BLOB NOT NULL
    )""")

    img = read_img("D:/img.png")
    binary = sq.Binary(img)


    cur.execute(f"INSERT INTO user VALUES ('name', '{binary}')")

    cur.execute("SELECT * FROM user LIMIT 1, 3")
    print(cur.fetchall())