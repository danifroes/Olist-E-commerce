## Olist Project

The goal of this project is to analyze a dataset provided by an e-commerce marketplace called [Olist](https://www.olist.com) to answer the CEO's question:

> How to increase customer satisfaction (so as to increase profit margin) while maintaining a healthy order volume?

## About Olist 🇧🇷

Olist is a leading e-commerce service that connects merchants to main marketplaces in Brazil. They provide a wide range of offers including inventory management, dealing with reviews and customer contacts to logistic services.


## Dataset

The dataset consists of 100k orders from 2016 and 2018 that were made on the Olist store, available as a csv on [Kaggle](https://www.kaggle.com/olistbr/brazilian-ecommerce). There are 8 datasets:
- orders
- products
- sellers
- category_name
- order_payment
- order_items
- geolocation
- customers

## Project description
- 1 - olist-classes folder - In order to deal with many datasets, doing some data cleaning and create new features, I developed a folder called 'olist' with classes that will handle all the logic and make easier to load data during the analysis on jupyter notabook.
- 2 - notebooks folder - analysis and calculations to make conclusions
