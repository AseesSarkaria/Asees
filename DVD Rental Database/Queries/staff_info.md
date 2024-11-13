SELECT 
	s.staff_id AS id,
    s.first_name || ' ' || s.last_name AS name,
    a.address,
    a.postal_code AS "zip code",
    a.phone,
    city.city,
    country.country,
    s.store_id
FROM staff s
 JOIN address a ON s.address_id = a.address_id
 JOIN city ON a.city_id = city.city_id
 JOIN country ON city.country_id = country.country_id

 ---Output---
 "id"	"name"	"address"	"zip code"	"phone"	"city"	"country"	"store_id"
1	"Mike Hillyer"	"23 Workhaven Lane"		"14033335568"	"Lethbridge"	"Canada"	1
2	"Jon Stephens"	"1411 Lillydale Drive"		"6172235589"	"Woodridge"	"Australia"	2
