import pandas as pd
import matplotlib.pyplot as plt


def print_single_plot(column_name):
    ACC_PATH = 'data/Raw Data.csv'
    df = pd.read_csv(ACC_PATH)
    df = df[column_name]
    print(df)
    df.plot()
    plt.title(f'{column_name} in time')
    plt.grid(True)
    plt.show()

def print_all_plots():
    print_single_plot('Linear Acceleration x (m/s^2)')
    print_single_plot('Linear Acceleration y (m/s^2)')
    print_single_plot('Linear Acceleration z (m/s^2)')

print_all_plots()


