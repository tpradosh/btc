import plotly.graph_objects as go
import pandas as pd
import sqlite3
from datetime import datetime

from sklearn.linear_model import LinearRegression
import numpy as np

def create_line_graph(beg, end):        


    beg = beg.timestamp()
    end = end.timestamp()

    connection = sqlite3.connect('./data/btc_data.db')

    cmd = """SELECT Datetime, Open, High, Low, Close
    FROM btc_data
    WHERE Timestamp between ? and ?
    ORDER BY Datetime ASC
    """


    df = pd.read_sql_query(cmd, connection, params=(beg, end))

    connection.close()

    df['Datetime'] = pd.to_datetime(df['Datetime'])

    #plot current data
    fig = go.Figure(data=go.Ohlc(x=df['Datetime'],
                        open=df['Open'],
                        high=df['High'],
                        low=df['Low'],
                        close=df['Close']))


    fig.update_layout(
        plot_bgcolor = 'black',
        paper_bgcolor = 'slategray',
        xaxis_title='Date',
        yaxis_title='Price',
        xaxis_tickangle=45,  
        autosize=True,
        margin=dict(l=40, r=40, t=40, b=40)
    )


    #Linear Regression for the closing variable

    #x values , turn back into the unix seconsd then reshape
    X = np.array(df['Datetime'].astype(np.int64) // 10**9).reshape(-1, 1) 

    Y = df['Close'].values

    #create model
    model = LinearRegression()
    model.fit(X,Y)
    trendline = model.predict(X)


    #add to the fig
    fig.add_trace(
        go.Scatter(
            x=df['Datetime'],
            y=trendline,
            mode='lines',
            name='Linear Regression',
            line=dict(color='cyan', dash='dash')
        )
    )


    fig.show()

