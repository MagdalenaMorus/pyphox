import pandas as pd
import matplotlib.pyplot as plt

ACC_PATH = 'data/Raw Data.csv'


def load_data(data_path, variables=('x', 'y', 'z')):
    df = pd.read_csv(ACC_PATH)
    columns = tuple(df[f'Linear Acceleration {var} (m/s^2)'].to_numpy()
                    for var in variables)
    return columns + (df['Time (s)'].to_numpy(),)


def print_single_plot(column):
    plt.plot(column)
    # plt.title(f'{column_name} in time')
    # plt.grid(True)
    plt.show()


def integrate(a, t):
    delta_t = 0.001
    integral = 0
    integrals_list = []
    for i in range(len(t)):
        trapeze = (a[i] + a[i+1])*(delta_t/2)
        integral = integral + trapeze
        integrals_list[i] = integral
    print(integrals_list)


if __name__ == '__main__':
    x, y, z, t = load_data(ACC_PATH)
    integrate(x, t)
