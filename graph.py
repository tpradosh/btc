import plotly.graph_objects as go
import pandas as pd
import sqlite3



def create_line_graph():
    start = 1638530160
    end = 1638735080

    connection = sqlite3.connect('./data/btc_data.db')

    cmd = """SELECT Datetime, Open, High, Low, Close
    FROM btc_data
    WHERE Timestamp between ? and ?
    ORDER BY Datetime ASC
    """


    df = pd.read_sql_query(cmd, connection, params=(start, end))

    connection.close()

    df['Datetime'] = pd.to_datetime(df['Datetime'])

    #plot 
    fig = go.Figure(data=go.Ohlc(x=df['Datetime'],
                        open=df['Open'],
                        high=df['High'],
                        low=df['Low'],
                        close=df['Close']))

    #Optional: customize layout (rotation, size)
    fig.update_layout(
        plot_bgcolor = 'lightgray',
        xaxis_title='Date',
        yaxis_title='Price',
        xaxis_tickangle=45,  
        autosize=True,
        margin=dict(l=40, r=40, t=40, b=40)
    )

    fig.show()

create_line_graph()