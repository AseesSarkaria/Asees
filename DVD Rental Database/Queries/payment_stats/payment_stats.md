
SELECT 
	b.store_id,
	date_part('year', a.payment_date) AS year,
	date_part('month', a.payment_date) AS month,
	count(*) AS purchase_volume,
	sum(a.amount) AS revenue,
	(round(((100.0 * (count(*))) / (lag(count(*)) OVER (PARTITION BY b.store_id))), 2) - (100)) AS mom_purchase_volume,
	(round(((100.0 * sum(a.amount)) / lag(sum(a.amount)) OVER (PARTITION BY b.store_id)), 2) - (100)) AS mom_revenue,
	round((((100.0 * sum(a.amount)) / lag(sum(a.amount)) OVER (PARTITION BY b.store_id)) - (((100.0 * (count(*))) / (lag(count(*)) OVER (PARTITION BY b.store_id))) - (100))), 2) AS mom_purchases_to_revenue_ratio,
	max(a.amount) AS biggest_purchase,
	min(
		CASE
			WHEN (a.amount > 0) THEN a.amount
			ELSE NULL
		END) AS smallest_purchase,
	max(a.amount) - min(
		CASE
			WHEN (a.amount > 0) THEN a.amount
			ELSE NULL
		END) AS max_min_difference,
	round(avg(a.amount), 2) AS average_purchase,
	percentile_cont((0.5)) WITHIN GROUP (ORDER BY ((a.amount))) AS median_purchase,
	(round(avg(a.amount), 2) - (percentile_cont((0.5)) WITHIN GROUP (ORDER BY ((a.amount))))) AS avg_med_difference,
	round(stddev(a.amount), 2) AS standard_deviation
FROM payment a
 JOIN staff b ON a.staff_id = b.staff_id
GROUP BY b.store_id, (date_part('year', a.payment_date)), (date_part('month', a.payment_date))
UNION ALL
SELECT 0 AS store_id,
date_part('year', payment.payment_date) AS year,
date_part('month', payment.payment_date) AS month,
count(*) AS purchase_volume,
sum(payment.amount) AS revenue,
(round(((100.0 * (count(*))) / (lag(count(*)) OVER ())), 2) - (100)) AS mom_purchase_volume,
(round(((100.0 * sum(payment.amount)) / lag(sum(payment.amount)) OVER ()), 2) - (100)) AS mom_revenue,
round((((100.0 * sum(payment.amount)) / lag(sum(payment.amount)) OVER ()) - (((100.0 * (count(*))) / (lag(count(*)) OVER ())) - (100))), 2) AS mom_purchases_to_revenue_ratio,
max(payment.amount) AS biggest_purchase,
min(
	CASE
		WHEN (payment.amount > (0)) THEN payment.amount
		ELSE NULL
	END) AS smallest_purchase,
(max(payment.amount) - min(
	CASE
		WHEN (payment.amount > (0)) THEN payment.amount
		ELSE NULL
	END)) AS max_min_difference,
round(avg(payment.amount), 2) AS average_purchase,
percentile_cont((0.5)) WITHIN GROUP (ORDER BY ((payment.amount))) AS median_purchase,
(round(avg(payment.amount), 2) - (percentile_cont((0.5)) WITHIN GROUP (ORDER BY ((payment.amount))))) AS avg_med_difference,
round(stddev(payment.amount), 2) AS standard_deviation
FROM payment
GROUP BY (date_part('year', payment.payment_date)), (date_part('month', payment.payment_date))
ORDER BY 1, 2, 3

---Output---
"store_id"	"year"	"month"	"purchase_volume"	"revenue"	"mom_purchase_volume"	"mom_revenue"	"mom_purchases_to_revenue_ratio"	"biggest_purchase"	"smallest_purchase"	"max_min_difference"	"average_purchase"	"median_purchase"	"avg_med_difference"
0	2007	2	2016	8351.84				10.99	0.99	10.00	4.14	3.99	0.14999999999999947	2.35
0	2007	3	5644	23886.56	179.96	186.00	106.04	11.99	0.99	11.00	4.23	3.99	0.2400000000000002	2.36
0	2007	4	6754	28559.46	19.67	19.56	99.90	11.99	0.99	11.00	4.23	3.99	0.2400000000000002	2.37
0	2007	5	182	514.18	-97.31	-98.20	99.11	9.98	0.99	8.99	2.83	2.99	-0.16000000000000014	2.19
1	2007	2	1016	4160.84				10.99	0.99	10.00	4.10	3.99	0.10999999999999943	2.35
1	2007	3	2817	11776.83	177.26	183.04	105.78	11.99	0.99	11.00	4.18	3.99	0.1899999999999995	2.36
1	2007	4	3364	14080.36	19.42	19.56	100.14	11.99	0.99	11.00	4.19	3.99	0.20000000000000018	2.37
1	2007	5	95	234.09	-97.18	-98.34	98.84	7.98	0.99	6.99	2.46	0.99	1.47	2.08
2	2007	2	1000	4191.00				10.99	0.99	10.00	4.19	3.99	0.20000000000000018	2.36
2	2007	3	2827	12109.73	182.70	188.95	106.25	11.99	0.99	11.00	4.28	3.99	0.29000000000000004	2.36
2	2007	4	3390	14479.10	19.92	19.57	99.65	11.99	0.99	11.00	4.27	3.99	0.27999999999999936	2.38
2	2007	5	87	280.09	-97.43	-98.07	99.37	9.98	0.99	8.99	3.22	2.99	0.22999999999999998	2.25
