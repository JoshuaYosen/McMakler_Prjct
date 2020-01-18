

/* Question 1 */
With orders (id, number, country, customer_id) As
(
  Values(1, 'O-1', 'DE', 1),
  (4, 'O-2', 'AT', 2),
  (5, 'O-3', 'DE', 2),
  (6, 'O-5', 'AT', 2),
  (8, 'O-6', 'DE', 3),
  (10, 'O-10', 'DE', 3),
  (11, 'O-11', 'AT', 3),
  (12, 'O-123', 'DE', 1)
)
, customers (id, country, name) As
(
  Values(1, 'DE', 'John Doe'),
    (2, 'AT', 'John Snow'),
    (3, 'DE', 'Johnny B. Goode')
)
select name, count(case when c.country = o.country then 1 end) as same_country_orders, count(case when c.country != o.country then 1 end) as different_country_orders
from customers as c
inner join orders as o
on c.id = o.customer_id
group By name;

/* Question 2 */

drop table if exists orders cascade;
create table orders (id integer primary key, "number" text, country text, cstm_id int);
insert into orders
values
(1 ,'O-1','DE', 1),
(4 ,'O-2','AT', 2),
(5 ,'O-3','DE', 2),
(6 ,'O-5','AT', 2),
(8 ,'O-6','DE', 3),
(10,'O-10','DE', 3),
(11,'O-11','AT', 3),
(12,'O-123','DE', 1);

select id + 1 as start,
       next_id - 1 as stop
from (
  select id,
         lead(id) over w as next_id,
         lead(id) over w - id as diff
  from orders
  window w as (order by id)
) t
where diff > 1
;

/* Question 3 */
with clean_ids as (
  select regexp_replace("number", '[^0-9]', '', 'g')::int as order_id
  from orders
)
select order_id + 1 as start_order_id,
       next_id - 1 as end_order_id
from (
  select order_id,
         lead(order_id) over w as next_id,
         lead(order_id) over w - order_id as diff
  from clean_ids
  window w as (order by order_id)
) t
where diff > 1;
