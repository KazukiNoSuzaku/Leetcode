# Premium SQL problem
# Forward-fill NULL values using the last non-null value in ordered rows.
#
# SELECT id,
#        LAST_VALUE(drink IGNORE NULLS) OVER (ORDER BY id) AS drink
# FROM CoffeeShop
#
# Alternative (MySQL which lacks IGNORE NULLS):
# SELECT id,
#        FIRST_VALUE(drink) OVER (
#            PARTITION BY grp ORDER BY id
#        ) AS drink
# FROM (
#     SELECT *,
#            COUNT(drink) OVER (ORDER BY id) AS grp
#     FROM CoffeeShop
# ) t
