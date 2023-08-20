# Stock Price Analysis & Prediction Web Application

![Stock Price Analysis & Prediction](stock2.jpg)

This web application allows you to analyze and predict stock prices using various techniques and machine learning models.

## Table of Contents
- [Overview](#overview)
- [Getting Started](#getting-started)
- [Requirements](#requirements)
- [Technologies Used](#technologies-used)
- [Project Explanation](#project-explanation)
- [Contributing](#contributing)
- [License](#license)
- [Credits](#credits)

## Overview

This Streamlit web application has been developed by [Arya Chakraborty](https://www.linkedin.com/in/arya-chakraborty-95a8411b2/) & [Rituparno Das](linkedin.com/in/rituparno-das-473a01198). The application allows users to analyze historical stock data, perform technical & statistical analysis, and even predict future stock prices using deep learning models.

## Getting Started

To run this project on your local machine, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/stock-price-analysis-app.git
   cd stock-price-analysis-app

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt

3. Run the Streamlit APP:
    ```bash
    streamlit run app.py

*Access the app in your web browser at http://localhost:8501*

## Requirements

- *`Python 3.7 or higher`*
- *`Streamlit`*
- *`Numpy`*
- *`Seaborn`*
- *`Matplotlib`*
- *`Keras`*
- *`Pandas`*
- *`datetime`*
- *`pandas_datareader`*
- *`yfinance`*
- *`PIL`*

*NS: Install these dependencies using the provided requirements.txt file*

## Technologies Used

- Streamlit: Framework for building interactive web applications using Python.

- Numpy, Seaborn, Matplotlib: Data visualization libraries for creating informative plots.

- Keras: Used for loading the LSTM model for stock price prediction.

- Pandas: Data manipulation library for handling and analyzing data.

- pandas_datareader, yfinance: Used for fetching stock data from Yahoo Finance.

- PIL: Python Imaging Library for working with images.

## Project Explanation

### The project is organized as follows:

- *Dataset:* Provides a visualization of the stock data, including the first and last five records, statistical description, and area chart for volume.

- *Analysis:* Performs statistical analysis, technical analysis, and visualizes trends and distributions in the data.

- *Prediction:* Implements a LSTM (Long Short-Term Memory) model for predicting stock prices. Users can input a number of days for future prediction and validate the model's performance.


## Contributing 

If you're interested in contributing to this project, please feel free to fork the repository, make changes, and submit a pull request. Your contributions are greatly appreciated! 

## Credits

<p align="center">
  <a href="https://arya920.github.io/My_Portfolio/">
    <img src="Arya_Chakraborty.jpg" alt="Arya Chakraborty" width="250">  
  </a>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <!-- Add some space between images -->
 <a href="https://www.linkedin.com/in/rituparno-das-473a01198/">
    <img src="Rituparno_Das.jpg" alt="Rituparno Das" width="250"> 
  </a>