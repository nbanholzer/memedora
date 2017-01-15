import MySQLdb

db = MySQLdb.connect(host = "sql211.byethost13.com",    # your host, usually localhost
                     user = "b13_19449026",         # your username
                     passwd = "rootadmin",  # your password
                     db = "memes")        # name of the data base

# you must create a Cursor object. It will let
#  you execute all the queries you need
cur = db.cursor()

# Use all the SQL you like
cur.execute("SELECT * FROM images")

# print all the first cell of all the rows
for row in cur.fetchall():
    print row[0]

db.close()


#[num,content,pic_text,photo_comic_gif,standard_original,animal_people_not]


current_meme = [1,3,1,2,1,2]
new_meme = [0,0,0,0,0,0]
yes_no = 1
current_rand = [[1,1],[1,1,1,1],[1,1],[1,1,1],[1,1],[1,1,1]]

for i in range (0,5) :
    if current_rand[i][current_meme[i]] <= 0.1 * (sum(current_rand[i])):
        current_rand[i][current_meme[i]] += 2 * yes_no
    else :
        current_rand[i][current_meme[i]] += 0.1 * yes_no
    if current_rand[i][current_meme[i]] <= 1:
        current_rand[i][current_meme[i]] = 1



for i in range (0,5) :
   for i in range (0,len(current_rand[i])-1):
     if current_rand[i][j] > randint(0,sum(current_rand[i])):
        new_meme[i] = j


current_meme= new_meme
