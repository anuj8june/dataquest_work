## 4. Querying a normalized database ##

query = "select ceremonies.year,nominations.movie from nominations inner join ceremonies on nominations.ceremony_id == ceremonies.id where nominations.nominee == 'Natalie Portman' "
portman_movies = conn.execute(query).fetchall()
print(portman_movies)

## 7. Join table ##

query = "select * from movies_actors limit 5"
five_join_table = conn.execute(query).fetchall()
print(five_join_table)

query = "select * from actors limit 5"
five_actors = conn.execute(query).fetchall()
print(five_actors)

query = "select * from movies limit 5"
five_movies = conn.execute(query).fetchall()
print(five_movies)

## 9. Querying a many-to-many relation ##

query = '''select actors.actor,movies.movie from movies inner join movies_actors on movies.id == movies_actors.movie_id inner join actors on movies_actors.actor_id == actors.id where movies.movie = "The King's Speech"; '''
kings_actors = conn.execute(query).fetchall()
print(kings_actors)

## 10. Practice: querying a many-to-many relation ##

query = '''select movies.movie,actors.actor from movies inner join movies_actors on movies.id == movies_actors.movie_id inner join actors on movies_actors.actor_id == actors.id where actors.actor = "Natalie Portman"; '''
portman_joins = conn.execute(query).fetchall()
print(portman_joins)