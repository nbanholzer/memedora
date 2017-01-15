import json
import MySQLdb

db = MySQLdb.connect(host = "sql211.byethost13.com",    # your host, usually localhost
                     user = "b13_19449026",         # your username
                     passwd = "rootadmin",  # your password
                     db = "memes")        # name of the data base

cur = db.cursor()
cur.execute("SELECT current_meme, current_rand FROM users WHERE id = 1")
current_meme = json.loads(curr.fetchone()[0])
new_meme = current_meme
cur.execute("SELECT link FROM images WHERE ('num' =" + str(new_meme[0]) + " AND 'content' =" + str(new_meme[1]) + " AND 'pic_text' =" + str(new_meme[2]) + " AND 'photo_comic_gif' =" + str(new_meme[3]) + " AND 'standard_original' =" + str(new_meme[4]) + " AND 'animal_people_not' = " + str(new_meme[5]) + ");")
link = cur.fetchone()[0]

db.close()
