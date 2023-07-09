import csv
import os

import plotly.graph_objs as go
import plotly.offline as pyo
import requests
from dotenv import load_dotenv


def get_orderbook_data():
    load_dotenv()
    api_key = os.getenv("BINANCE__API")
    api_secret = os.getenv("BINANCE__SECRET_KEY")

    symbol = 'BTCUSDC'  # Пара, для которой нужно получить данные
    timestamp = 1647072000000  # Время, с которого нужно начать получение данных, в миллисекундах
    limit = 1000  # Максимальное количество уровней стакана, которое нужно получить

    url = 'https://api.binance.com/api/v3/depth?symbol=BTCUSDC&timestamp=1647072000000&limit=1000'

    response = requests.get(url)
    data = response.json()

    for bid in data['bids']:
        price = bid[0]  # Цена
        quantity = bid[1]  # Количество
        print(f'Bid price: {price}, quantity: {quantity}')

    for ask in data['asks']:
        price = ask[0]  # Цена
        quantity = ask[1]  # Количество
        print(f'Ask price: {price}, quantity: {quantity}')

    # Соединяемся с биржей Binance
    # symbol = 'BTCUSDT'
    # client = Client(api_key, api_secret)

    # end_time = datetime.now()
    # start_time = end_time - timedelta(days=2)

    # получение свечных данных за последние 2 недели
    # candles = client.get_historical_klines(symbol, Client.KLINE_INTERVAL_1MINUTE,
    #                                        start_time.strftime("%d %b %Y %H:%M:%S"),
    #                                        end_time.strftime("%d %b %Y %H:%M:%S"))
    #
    # # получение биржевого стакана
    # depth = client.get_order_book(symbol=symbol)
    # prices = []
    # # перебор свечей
    # for candle in candles:
    #     timestamp = datetime.fromtimestamp(candle[0] / 1000.0)  # время свечи
    #     if start_time <= timestamp <= end_time:  # фильтрация свечей за последние 2 недели
    #         for i in range(100):  # перебор уровней глубины
    #             price = float(depth['bids'][i][0])  # цена уровня глубины
    #             prices.append(price)
    #             qty = float(depth['bids'][i][1])  # количество на уровне глубины
    #             print(timestamp, price, qty)


def fire_charts():
    data, y = read_csv_file()

    # data = [
    #     [0, 0, 0.00154, 0, 0],
    #     [0, 0.00215, 0, 0, 0],
    #     [0.00094, 0, 0, 0, 0],
    #     [0, 0, 0, 0, 0.00073],
    #     [0, 0.00058, 0, 0, 0]
    # ]
    # x = [1, 2, 3, 4, 5]
    x = [00.00, 01.00, 02.00, 03.00, 04.00, 05.00, 06.00, 07.00, 08.00, 09.00, 10.00, 11.00, 12.00, 13.00, 14.00, 15.00,
         16.00, 17.00, 18.00, 19.00, 20.00, 21.00, 22.00, 23.00]
    heatmap_data = go.Heatmap(
        z=data,
        # labels=dict(x='Time', y='Price', color='Value'),
        x=x,
        y=y
    )
    layout = go.Layout(title='Heatmap')
    fig = go.Figure(data=heatmap_data, layout=layout)
    fig.update_layout(
        # template='plotly_dark',  # установить темную тему
        width=None,  # не устанавливать ширину графика
        height=600,  # установить желаемую высоту графика
        autosize=True,  # автоматически масштабировать график по размерам контейнера
    )
    pyo.plot(fig, filename='my_plot.html', auto_open=False)


def write_csv_file():
    data = [
    ]

    # Открываем файл для записи
    with open('file.csv', mode='w', newline='') as file:
        # Создаем объект writer для записи данных в CSV-файл
        writer = csv.writer(file)

        # Записываем заголовок таблицы
        writer.writerow(data[0])

        # Записываем данные
        for row in data[1:]:
            writer.writerow(row)


def read_csv_file():
    value = []
    price = []
    with open('BTCUSDT-aggTrades-2023-03-12.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in range(15000):
            row = next(reader)
            # if datetime.datetime.fromtimestamp(int(row['1678665600003']) / 1000).replace(microsecond=0) not in time:
            #     time.append(datetime.datetime.fromtimestamp(int(row['1678665600003']) / 1000).replace(microsecond=0))
            if row['20455.73000000'] not in price:
                price.append(float(row['20455.73000000']))
            value.append(float(row['0.00613000']))

    return value, price


if __name__ == "__main__":
    get_orderbook_data()
