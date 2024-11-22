```sql
SELECT 
    film.film_id AS fid,
    film.title,
    film.description,
    category.name AS category,
    film.rental_rate AS price,
    film.length,
    film.rating,
    group_concat(actor.first_name || ' ' || actor.last_name) AS actors
FROM category
 LEFT JOIN film_category ON category.category_id = film_category.category_id
 LEFT JOIN film ON film_category.film_id = film.film_id
 JOIN film_actor ON film.film_id = film_actor.film_id
 JOIN actor ON film_actor.actor_id = actor.actor_id
GROUP BY film.film_id, film.title, film.description, category.name, film.rental_rate, film.length, film.rating
```
```text
---top 5 rows---
"fid"	"title"	"description"	"category"	"price"	"length"	"rating"	"actors"
730	"Ridgemont Submarine"	"A Unbelieveable Drama of a Waitress And a Composer who must Sink a Mad Cow in Ancient Japan"	"New"	0.99	46	"PG-13"	"Johnny Lollobrigida, Julianne Dench, Whoopi Hurt, Michael Bolger, Julia Fawcett"
892	"Titanic Boondock"	"A Brilliant Reflection of a Feminist And a Dog who must Fight a Boy in A Baloon Factory"	"Animation"	4.99	104	"R"	"Bette Nicholson, Dan Harris, Penelope Cronyn, Warren Nolte, Julianne Dench, Ewan Gooding, Jayne Nolte, Geoffrey Heston, Will Wilson, Olympia Pfeiffer, Matthew Carrey, Mary Keitel"
286	"Enough Raging"	"A Astounding Character Study of a Boat And a Secret Agent who must Find a Mad Cow in The Sahara Desert"	"Travel"	2.99	158	"NC-17"	"Johnny Lollobrigida, Sandra Peck, Sean Williams, Julianne Dench, Kevin Garland, Richard Penn, Al Garland, Matthew Carrey, Michael Bolger"
857	"Strictly Scarface"	"A Touching Reflection of a Crocodile And a Dog who must Chase a Hunter in An Abandoned Fun House"	"Comedy"	2.99	144	"PG-13"	"Greg Chaplin, Daryl Crawford, Whoopi Hurt, Alan Dreyfuss"
593	"Monterey Labyrinth"	"A Awe-Inspiring Drama of a Monkey And a Composer who must Escape a Feminist in A U-Boat"	"Horror"	0.99	158	"G"	"Karl Berry, Julia Mcqueen, Dan Harris, Julianne Dench, Fay Wood, Rock Dukakis"
