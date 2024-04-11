-- Q12) Analyze the cumulative revenue generated over time.
select order_date, sum(revenue) over (order by order_date) as cumulative_revenue 
from
(SELECT 
    c.order_date, SUM(quantity * price) AS revenue
FROM
    order_details a
        INNER JOIN
    pizzas b ON a.pizza_id = b.pizza_id
        INNER JOIN
    orders c ON c.order_id = a.order_id
    group by order_date) as sales;