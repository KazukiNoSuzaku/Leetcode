-- Premium problem - not available without subscription
-- Author: Kaustav Ghosh
-- Typical approach: Find if each user's second sold item matches their favorite brand

SELECT u.user_id AS seller_id,
       CASE WHEN i.item_brand = u.favorite_brand THEN 'yes' ELSE 'no' END AS 2nd_item_fav_brand
FROM Users u
LEFT JOIN (
    SELECT seller_id, item_id,
           RANK() OVER (PARTITION BY seller_id ORDER BY order_date) AS rk
    FROM Orders
) o ON u.user_id = o.seller_id AND o.rk = 2
LEFT JOIN Items i ON o.item_id = i.item_id;
