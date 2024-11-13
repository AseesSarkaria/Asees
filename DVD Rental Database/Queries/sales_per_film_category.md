SELECT 
	c.name AS category,
    sum(p.amount) AS total_sales
FROM payment p
 JOIN rental r ON p.rental_id = r.rental_id
 JOIN inventory i ON r.inventory_id = i.inventory_id
 JOIN film f ON i.film_id = f.film_id
 JOIN film_category fc ON f.film_id = fc.film_id
 JOIN category c ON fc.category_id = c.category_id
GROUP BY c.name
ORDER BY sum(p.amount) DESC

---Output---
"category"	"total_sales"
"Sports"	4892.19
"Sci-Fi"	4336.01
"Animation"	4245.31
"Drama"	4118.46
"Comedy"	4002.48
"New"	3966.38
"Action"	3951.84
"Foreign"	3934.47
"Games"	3922.18
"Family"	3830.15
"Documentary"	3749.65
"Horror"	3401.27
"Classics"	3353.38
"Children"	3309.39
"Travel"	3227.36
"Music"	3071.52
