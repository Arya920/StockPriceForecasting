import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from keras.models import load_model
import streamlit as st
from streamlit_option_menu import option_menu
import pandas
import datetime
from pandas_datareader import data as pdr
import yfinance as yfin
yfin.pdr_override()


def main():
    st.title("testing")
    user_input=st.text_input('**:blue[Enter Stock Ticker]**','CIPLA.NS')

    start = st.date_input(
    "Tell me the Start Date",
    datetime.date(2017,4,3))
    st.write('The start Date is:', start)
    end = st.date_input(
    "Tell me the End Date",
    datetime.date(2023,1,20))
    st.write('The End Date is:', end)
    data1=pdr.get_data_yahoo(user_input,start,end)

    st.dataframe(data1)






if __name__ =="__main__":
    main()