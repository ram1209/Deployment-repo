import sqlite3


con=sqlite3.connect('data.db')

cursor=con.cursor()


#create_table="create table Users (id int,username text,password text)"
create_table="create table Users (id int,username text,password text)
#
# #user=(1,'jose','asdf')
#
users=[
     (1,'ram','asfg'),
     (2,'raghu','gyui')
     ]
#
 #cursor.execute(create_table)

#
cursor.execute(create_table)
insert_query="insert into users values(?,?,?)"
#
cursor.executemany(insert_query,users)

select_query="select * from users"
cursor.execute(select_query)
print("row")
for row in cursor:
    print(row)

con.commit()
con.close()
