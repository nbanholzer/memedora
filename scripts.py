import json
import MySQLdb

def up():
    db = MySQLdb.connect(host = "sql211.byethost13.com",    # your host, usually localhost
                         user = "b13_19449026",         # your username
                         passwd = "rootadmin",  # your password
                         db = "memes")        # name of the data base

    cur = db.cursor()

    cur.execute("SELECT current_meme, current_rand FROM users WHERE id = 1")
    current_meme = json.loads(curr.fetchone()[0])
    current_rand = json.loads(curr.fetchone()[1])

    new_meme = [0,0,0,0,0,0]
    yes_no = 1
    current_rand = [[1,1],[1,1,1,1],[1,1],[1,1,1],[1,1],[1,1,1]]

    for i in range (0,5) :
        if current_rand[i][current_meme[i]] <= 0.1 * (sum(current_rand[i])):
            current_rand[i][current_meme[i]] += 2 * yes_no
        else:
            current_rand[i][current_meme[i]] += 0.1 * yes_no
            if current_rand[i][current_meme[i]] <= 1:
                current_rand[i][current_meme[i]] = 1

    for i in range (0,5) :
        for i in range (0,len(current_rand[i])-1):
            if current_rand[i][j] > randint(0,sum(current_rand[i])):
                new_meme[i] = j

    current_meme = new_meme

    cur.execute("""UPDATE users
    SET current_meme = %s, current_rand = %s
    WHERE id=1;
    """, (json.dumps(current_meme), json.dumps(current_rand)))
    cur = db.cursor()
    cur.execute("SELECT current_meme, current_rand FROM users WHERE id = 1")
    current_meme = json.loads(curr.fetchone()[0])
    new_meme = current_meme
    cur.execute("SELECT link FROM images WHERE ('num' =" + str(new_meme[0]) + " AND 'content' =" + str(new_meme[1]) + " AND 'pic_text' =" + str(new_meme[2]) + " AND 'photo_comic_gif' =" + str(new_meme[3]) + " AND 'standard_original' =" + str(new_meme[4]) + " AND 'animal_people_not' = " + str(new_meme[5]) + ");")
    link = cur.fetchone()[0]

    db.close()
    return link

def down():
    db = MySQLdb.connect(host = "sql211.byethost13.com",    # your host, usually localhost
                     user = "b13_19449026",         # your username
                     passwd = "rootadmin",  # your password
                     db = "memes")        # name of the data base

    cur = db.cursor()

    cur.execute("SELECT current_meme, current_rand FROM users WHERE id = 1")
    current_meme = json.loads(curr.fetchone()[0])
    current_rand = json.loads(curr.fetchone()[1])

    new_meme = [0,0,0,0,0,0]
    yes_no = -1
    current_rand = [[1,1],[1,1,1,1],[1,1],[1,1,1],[1,1],[1,1,1]]

    for i in range (0,5) :
        if current_rand[i][current_meme[i]] <= 0.1 * (sum(current_rand[i])):
            current_rand[i][current_meme[i]] += 2 * yes_no
        else:
            current_rand[i][current_meme[i]] += 0.1 * yes_no
        if current_rand[i][current_meme[i]] <= 1:
            current_rand[i][current_meme[i]] = 1

    for i in range (0,5) :
        for i in range (0,len(current_rand[i])-1):
            if current_rand[i][j] > randint(0,sum(current_rand[i])):
                new_meme[i] = j

    current_meme = new_meme

    cur.execute("""UPDATE users
    SET current_meme = %s, current_rand = %s
    WHERE id=1;
    """, (json.dumps(current_meme), json.dumps(current_rand)))

    cur.execute("""UPDATE users
    SET current_meme = %s, current_rand = %s
    WHERE id=1;
    """, (json.dumps(current_meme), json.dumps(current_rand)))
    cur = db.cursor()
    cur.execute("SELECT current_meme, current_rand FROM users WHERE id = 1")
    current_meme = json.loads(curr.fetchone()[0])
    new_meme = current_meme
    cur.execute("SELECT link FROM images WHERE ('num' =" + str(new_meme[0]) + " AND 'content' =" + str(new_meme[1]) + " AND 'pic_text' =" + str(new_meme[2]) + " AND 'photo_comic_gif' =" + str(new_meme[3]) + " AND 'standard_original' =" + str(new_meme[4]) + " AND 'animal_people_not' = " + str(new_meme[5]) + ");")
    link = cur.fetchone()[0]
    db.close()
    return link

def reset():
    db = MySQLdb.connect(host = "sql211.byethost13.com",    # your host, usually localhost
                     user = "b13_19449026",         # your username
                     passwd = "rootadmin",  # your password
                     db = "memes")        # name of the data base

    cur = db.cursor()
    cur.execute("""UPDATE users
    SET current_rand = %s
    WHERE id=1;
    """, json.dumps([[1,1],[1,1,1,1],[1,1],[1,1,1],[1,1],[1,1,1]]))
