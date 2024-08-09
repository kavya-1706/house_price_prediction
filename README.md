# House Price Prediction- Machine Learning- Regression technique
Created by- Kavya Anil
## Project Description:
This project involved evaluating five different regression models to predict house prices. The K-Nearest Neighbors (KNN) model demonstrated the highest performance among the tested models. Subsequently, the KNN model was integrated into a Flask application, enabling real-time predictions and a user-friendly interface for interacting with the predictive model.

## Repository consists of:
1. Dataset (housing_prices.csv)- taken from Kaggle: https://www.kaggle.com/datasets/yasserh/housing-prices-dataset?resource=download
2. Jupyter Notebook (HousePricePrediction.ipynb)- consists of Python code for all 5 regression models, implemented and tested, and serialised in a pickle file.
3. house_price_prediction_app folder- consists of a Flask web application, and a pickle file containing the serialised ML model.

## Setup steps:

## For running the ipynb file-
# Download the HousePricePrediction.ipynb file and the housing_prices.csv dataset.
# Install required Python packages:
    pip install pandas scikit-learn matplotlib seaborn numpy scipy pickle
# Run the .ipynb file in Jupyter Notebook, ensuring that housing_prices.csv is in the same directory.

## For running the Flask app-
# Install required Python packages:
    pip install Flask
    pip install pickle
# Download the house_price_prediction_app folder, and open it in VSCode.
# Open VSCode terminal and ensure that you are inside the house_price_prediction_app folder directory.
# For deploying on a development server:
    set FLASK_APP=app.py
    flask run
# This opens up a development server on http://127.0.0.1:5000 , which can be opened up on your browser.

