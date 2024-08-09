# House Price Prediction- Machine Learning- Regression technique
Created by- Kavya Anil
## Project Description:
This project involved evaluating five different regression models to predict house prices. The K-Nearest Neighbors (KNN) model demonstrated the highest performance among the tested models. Subsequently, the KNN model was integrated into a Flask application, enabling real-time predictions and a user-friendly interface for interacting with the predictive model.

## Repository consists of:
1. Dataset (housing_prices.csv)- taken from Kaggle: https://www.kaggle.com/datasets/yasserh/housing-prices-dataset?resource=download
2. Jupyter Notebook (HousePricePrediction.ipynb)- consists of Python code for all 5 regression models, implemented and tested, and serialised in a pickle file.
3. house_price_prediction_app folder- consists of a Flask web application, and a pickle file containing the serialised ML model.
4. Documentation pdf- contains screenshots of the application.

## Setup steps:

## For running the ipynb file-
### 1. Download the HousePricePrediction.ipynb file and the housing_prices.csv dataset.
### 2. Install required Python packages:
    pip install pandas scikit-learn matplotlib seaborn numpy scipy pickle
### 3. Run the .ipynb file in Jupyter Notebook, ensuring that housing_prices.csv is in the same directory.

## For running the Flask app-
### 1. Install required Python packages:
    pip install Flask
###
    pip install pickle
### 2. Download the house_price_prediction_app folder, and open it in VSCode.
### 3. Open VSCode terminal and ensure that you are inside the house_price_prediction_app folder directory.
### 4. For deploying on a development server:
    set FLASK_APP=app.py
###    
    flask run
### 5. This opens up a development server on http://127.0.0.1:5000 , which can be opened up on your browser.

