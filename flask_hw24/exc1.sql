SELECT * FROM Articles
LEFT JOIN article_categories ac ON articles.id=ac.id
LEFT JOIN category c ON ac.category_id=c.id