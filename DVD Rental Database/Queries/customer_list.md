
SELECT 
	cu.customer_id AS id,
	cu.first_name || ' ' || cu.last_name AS name,
	a.address,
	a.postal_code AS "zip code",
	a.phone,
	city.city,
	country.country,
		CASE
			WHEN cu.activebool THEN 'active'
			ELSE ''
		END AS notes,
	cu.store_id AS sid
FROM customer cu
 JOIN address a ON cu.address_id = a.address_id
 JOIN city ON a.city_id = city.city_id
 JOIN country ON city.country_id = country.country_id

--top 5 rows---
"id"	"name"	"address"	"zip code"	"phone"	"city"	"country"	"notes"	"sid"
524	"Jared Ely"	"1003 Qinhuangdao Street"	"25972"	"35533115997"	"Purwakarta"	"Indonesia"	"active"	1
1	"Mary Smith"	"1913 Hanoi Way"	"35200"	"28303384290"	"Sasebo"	"Japan"	"active"	1
2	"Patricia Johnson"	"1121 Loja Avenue"	"17886"	"838635286649"	"San Bernardino"	"United States"	"active"	1
3	"Linda Williams"	"692 Joliet Street"	"83579"	"448477190408"	"Athenai"	"Greece"	"active"	1
4	"Barbara Jones"	"1566 Inegl Manor"	"53561"	"705814003527"	"Myingyan"	"Myanmar"	"active"	2
