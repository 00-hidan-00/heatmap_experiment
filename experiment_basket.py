import datetime
import json
import time

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from binance.client import Client

BINANCE__API = ''
BINANCE__SECRET_KEY = ''
client = Client(BINANCE__API, BINANCE__SECRET_KEY)


def change_unix_time_to_regular_time(transact_time):
    return datetime.datetime.fromtimestamp(transact_time / 1000)


def data_processing():
    url = "BTCUSDT-aggTrades-2023-06-01.csv"
    # import the .csv file into a pandas DataFrame
    df = pd.read_csv(url)
    price_column = df.iloc[:, 1]
    quantity_column = df.iloc[:, 2]
    transact_unix_time_column = df.iloc[:, 5]

    def heatmap_example():
        # url of the .csv file
        url = "BTCUSDT-aggTrades-2023-06-04.csv"
        # import the .csv file into a pandas DataFrame
        df = pd.read_csv(url)

        # defining the array containing the states present in the study
        price_data = np.array(df.iloc[:, 1][:10].drop_duplicates())

        # quantity_data = df.iloc[:, 2]
        # transact_time_data = df.iloc[:, 5]
        #
        # price_27_quantity = []
        # price_2705_quantity = []
        # price_271_quantity = []
        # price_2715_quantity = []
        # price_272_quantity = []
        #
        # for i, price in enumerate(price_data):
        #     if price <= 27050:
        #         price_27_quantity.append(df.iloc[:, 2][i])
        #     elif price <= 27100:
        #         price_2705_quantity.append(df.iloc[:, 2][i])
        #     elif price <= 27150:
        #         price_271_quantity.append(df.iloc[:, 2][i])
        #     elif price <= 27200:
        #         price_2715_quantity.append(df.iloc[:, 2][i])
        #     elif price <= 27300:
        #         price_272_quantity.append(df.iloc[:, 2][i])

        # print(
        #     len(price_27_quantity),
        #     len(price_2705_quantity),
        #     len(price_271_quantity),
        #     len(price_2715_quantity),
        #     len(price_272_quantity),
        # )

        # extracting the total cases for each day and each country

        overall_quantity = []
        for price in price_data:
            tot_quantity = []
            for i in range(len(df.iloc[:, 1][:10])):
                if df.iloc[:, 1][i] == price:
                    if df.iloc[:, 2][i] < 0.003:
                        tot_quantity.append(df.iloc[:, 2][i])
                else:
                    tot_quantity.append(0)
            overall_quantity.append(tot_quantity)
        data = pd.DataFrame(overall_quantity).T
        data.columns = price_data
        fig = plt.figure()
        ax = fig.subplots()
        ax = sns.heatmap(data, annot=False, linewidths=0, cmap='afmhot', xticklabels=True)
        ax.invert_yaxis()
        ax.set_xlabel('Price')
        ax.set_ylabel('Orders')
        plt.show()


def heatmap():
    # url of the .csv file
    url = "BTCUSDT-aggTrades-2023-06-01.csv"
    # import the .csv file into a pandas DataFrame
    df = pd.read_csv(url)
    limit = 300
    price_column = df.iloc[:, 1]

    quantity_column = df.iloc[:, 2]
    transact_unix_time_column = df.iloc[:, 5]

    transact_classic_time_column = [
        change_unix_time_to_regular_time(transact_time) for transact_time in transact_unix_time_column
    ]

    transact_unix_time_list = np.array(transact_unix_time_column[:limit].drop_duplicates())

    overall_times = []
    for time in transact_unix_time_list:
        tot_times = []
        for i in range(len(transact_unix_time_column[:limit])):

            if transact_unix_time_column[i] == time and quantity_column[i] < 0.003:
                tot_times.append(quantity_column[i])
            else:
                tot_times.append(0)
        overall_times.append(tot_times)

    data = pd.DataFrame(overall_times).T
    data.index = price_column[:limit]
    data.columns = transact_classic_time_column[:len((transact_unix_time_list))]

    fig = plt.figure(figsize=(30, 15))
    ax = sns.heatmap(data, annot=False, linewidths=0, cmap='afmhot', xticklabels=True)
    ax.invert_yaxis()
    ax.set_xlabel('Time')
    ax.set_ylabel('Price')
    plt.show()


def test():
    # Пример входного списка Unix-дат
    unix_dates = []

    for unix_date in unix_dates:
        # Преобразование Unix-даты в объект времени
        timestamp = time.localtime(unix_date)
        print(timestamp)

        # Получение текущего часа и минуты из объекта времени
        hour = timestamp.tm_hour
        minute = timestamp.tm_min

        # Вывод времени каждый час
        if minute == 0:
            print(f"Текущее время: {hour}:{minute:02}")

    ###

    # next_iteration = len(transact_unix_time_column) / 24
    # overall_data = []
    # start_val = 0
    # for i, transact_unix_time in enumerate(transact_unix_time_column):
    #     tot_data = {
    #         'price': 0,
    #         'quantity': 0,
    #         'time': 0,
    #         'iterations': 0
    #     }
    #     start_val += 1
    #
    #     tot_data["price"] += price_column[i]
    #     tot_data["quantity"] += quantity_column[i]
    #     tot_data["time"] += transact_unix_time_column[i]
    #     tot_data["iterations"] += 1
    #     print(
    #         tot_data["price"]
    #     )
    #
    #     if start_val == int(next_iteration):
    #         overall_data.append(tot_data)
    #         start_val = 0
    #         tot_data["price"] = 0
    #         tot_data["quantity"] = 0
    #         tot_data["time"] = 0
    #         tot_data["iterations"] = 0


def download_order_book(symbol, limit=100):
    order_book = client.get_order_book(symbol=symbol, limit=limit)
    order_book_with_timestamp = {"order_book": order_book}
    filename = f'order_book_{symbol}.json'
    with open(filename, 'w') as file:
        json.dump(order_book_with_timestamp, file)
    print(f"Order book for {symbol} with timestamp downloaded and saved to {filename}")


if __name__ == "__main__":
    # download_order_book('BTCUSDT', limit=100)
    heatmap()
