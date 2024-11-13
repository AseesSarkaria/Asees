SELECT film.film_id AS fid,
    film.title,
    film.description,
    category.name AS category,
    film.rental_rate AS price,
    film.length,
    film.rating,
    group_concat((((upper(substring((actor.first_name), 1, 1)) || lower(substring((actor.first_name), 2))) || upper(substring((actor.last_name), 1, 1))) || lower(substring((actor.last_name), 2)))) AS actors
FROM category
 LEFT JOIN film_category ON category.category_id = film_category.category_id
 LEFT JOIN film ON film_category.film_id = film.film_id
 JOIN film_actor ON film.film_id = film_actor.film_id
 JOIN actor ON film_actor.actor_id = actor.actor_id
GROUP BY film.film_id, film.title, film.description, category.name, film.rental_rate, film.length, film.rating

---top 5 movies---
"fid"	"title"	"description"	"category"	"price"	"length"	"rating"	"actors"
730	"Ridgemont Submarine"	"A Unbelieveable Drama of a Waitress And a Composer who must Sink a Mad Cow in Ancient Japan"	"New"	0.99	46	"PG-13"	"JohnnyLollobrigida, JulianneDench, WhoopiHurt, MichaelBolger, JuliaFawcett"
892	"Titanic Boondock"	"A Brilliant Reflection of a Feminist And a Dog who must Fight a Boy in A Baloon Factory"	"Animation"	4.99	104	"R"	"BetteNicholson, DanHarris, PenelopeCronyn, WarrenNolte, JulianneDench, EwanGooding, JayneNolte, GeoffreyHeston, WillWilson, OlympiaPfeiffer, MatthewCarrey, MaryKeitel"
286	"Enough Raging"	"A Astounding Character Study of a Boat And a Secret Agent who must Find a Mad Cow in The Sahara Desert"	"Travel"	2.99	158	"NC-17"	"JohnnyLollobrigida, SandraPeck, SeanWilliams, JulianneDench, KevinGarland, RichardPenn, AlGarland, MatthewCarrey, MichaelBolger"
857	"Strictly Scarface"	"A Touching Reflection of a Crocodile And a Dog who must Chase a Hunter in An Abandoned Fun House"	"Comedy"	2.99	144	"PG-13"	"GregChaplin, DarylCrawford, WhoopiHurt, AlanDreyfuss"
593	"Monterey Labyrinth"	"A Awe-Inspiring Drama of a Monkey And a Composer who must Escape a Feminist in A U-Boat"	"Horror"	0.99	158	"G"	"KarlBerry, JuliaMcqueen, DanHarris, JulianneDench, FayWood, RockDukakis"
