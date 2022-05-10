import sqlite3

conn = sqlite3.connect("movies_ranking.sqlite")
c=conn.cursor()

c.execute("SELECT * FROM movies WHERE Genre='Comedy'") #ვირჩევ მხოლოდ ისეთ ფილმებს რომლის ჟანრიც კომედიაა
a=c.fetchall() #ყველა შესაძლო ვარიანტი
for x in a:
    print(x)
movie1= ('Dark knight', 'Drama','DC', 200, 2014) #ერთერთი ფილმი თავისი აღწერით
c.execute('INSERT INTO movies(Film,Genre,LeadStudio,WorldWideGross,Year) VALUES(?,?,?,?,?)', movie1) #ვამატებთ ამ ფილმს movies ში

c.execute("UPDATE movies SET Genre='Comedy' where film='Dark knight'")

c.execute("DELETE From movies WHERE ID=78")









conn.close()