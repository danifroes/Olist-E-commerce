A quick logistic regression

We have seen that many customers are unhappy, with 11% of orders receiving 1-star reviews.

Often, being able to identify clearly the worst reviews (1 star) is more important than being precise in predicting the exact review score of each order.

Run a Logit model for `dim_is_one_star` from orders and compare that with the OLS prediction of `review_score` and with a Logit model for `dim_is_five_star`.
