## Orders - Multivariate Linear Regression

A quick analysis of the `orders` dataset showed that `review_score` is mostly correlated with features such as `wait_time` and `delay_vs_expected`

However, these two features were also highly correlated with each other. I use `statsmodels` to determine the effect of one feature, **holding the other one constant**

## Sellers

`wait_time` was the most significant factor explaining low review scores, but reading comments of the bad reviews also showed that some of them were linked to the seller themself...

Besides, `wait_time` is not known ahead of the order, and thus can hardly be directly addressed by your data-consulting team as a recommendation to the Olist CEO.

On the contrary, we might be able to quantify **which sellers should be removed from the marketplace due to persistent bad reviews**, in order to improve profit margin.

## Products

This challange takes a similar approach as the `sellers` one, but applies it to `products`, grouped by `product_category`

There might be some `product_category` that significantly underperforms vs others, and that could be removed from the marketplace.
