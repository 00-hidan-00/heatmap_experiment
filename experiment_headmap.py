import plotly.express as px
import plotly.offline as pyo

data = [[70, 36, 0, 4, 35, 21, 68, 60, 79, 85, 63, 88, 95, 79, 27, 49, 27, 92, 34, 81, 34, 36, 27, 36],
        [40, 55, 23, 4, 28, 65, 24, 89, 14, 0, 27, 40, 7, 60, 46, 96, 5, 48, 11, 6, 3, 38, 9, 64],
        [38, 50, 95, 55, 42, 89, 94, 72, 29, 30, 51, 62, 84, 38, 88, 57, 22, 82, 75, 40, 24, 45, 17, 15],
        [25, 33, 48, 10, 52, 6, 46, 98, 28, 52, 0, 6, 48, 59, 70, 88, 76, 66, 26, 41, 97, 9, 22, 86],
        [35, 38, 83, 76, 29, 92, 84, 91, 95, 50, 52, 75, 61, 55, 53, 57, 75, 61, 36, 53, 30, 22, 76, 84],
        [68, 27, 77, 3, 58, 36, 34, 30, 11, 19, 84, 31, 37, 53, 89, 1, 98, 72, 91, 71, 78, 42, 16, 54],
        [87, 51, 76, 18, 53, 12, 30, 58, 22, 65, 78, 25, 17, 2, 67, 29, 42, 42, 37, 69, 91, 7, 6, 82],
        [37, 10, 99, 54, 31, 19, 64, 21, 33, 22, 37, 92, 44, 36, 42, 2, 42, 85, 22, 87, 35, 12, 49, 17],
        [76, 53, 72, 88, 97, 23, 36, 4, 50, 57, 56, 33, 39, 60, 16, 13, 32, 87, 15, 34, 11, 49, 70, 19],
        [13, 85, 84, 0, 26, 91, 18, 63, 85, 70, 47, 77, 97, 8, 26, 30, 7, 22, 93, 44, 97, 98, 99, 71],
        [40, 37, 41, 39, 40, 73, 73, 49, 57, 7, 23, 45, 9, 18, 23, 82, 8, 82, 67, 17, 77, 41, 61, 88],
        [45, 11, 88, 16, 5, 24, 27, 2, 41, 28, 49, 12, 62, 72, 48, 33, 73, 4, 85, 44, 64, 31, 96, 27]]

fig = px.imshow(data,
                labels=dict(x="Hour", y="Month", color="Value"),
                x=['12AM', '01AM', '02AM', '03AM', '04AM', '05AM',
                   '06AM', '07AM', '08AM', '09AM', '10AM', '11AM',
                   '12PM', '01PM', '02PM', '03PM', '04PM', '05PM',
                   '06PM', '07PM', '08PM', '09PM', '10PM', '11PM'],
                y=['January', 'February', 'March', 'April', 'May', 'June',
                   'July', 'August', 'September', 'October', 'November', 'December']
                )

pyo.plot(fig, filename='my_plot.html', auto_open=False)
