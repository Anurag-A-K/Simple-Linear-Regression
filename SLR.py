import numpy as np
import pandas
import matplotlib.pyplot as plt
def plotting_gr(x, y, b):
    plt.scatter(x, y, color="black",marker="x", s=20)
    y_pred = b[0] + b[1] * x
    plt.plot(x, y_pred, color="black")
    plt.xlabel('x')
    plt.ylabel('y')
    xlim=np.array(plt.gca().get_xlim())
    ylim = np.array(plt.gca().get_ylim())
    plt.fill_between(xlim, y1=b[1]*xlim+b[0], y2=[ylim[0],ylim[0]], color="#e0eaf3", zorder=0)
    plt.fill_between(xlim, y1=b[1] * xlim + b[0], y2=[ylim[1], ylim[1]], color="#fae4e4", zorder=0)
    plt.margins(0)
    plt.show()

def main():
    df = pandas.read_excel('Glucose Levels.xlsx')
    x = np.array(df['Age (X)'].values)
    y = np.array(df['Glucose level(Y)'].values)
    n = np.size(x)
    meanx = np.mean(x)
    meany = np.mean(y)
    sxy = np.sum(y*x-n*meany*meanx)
    sxx = np.sum(x*x-n*meanx*meanx)
    b1 = sxy/sxx
    b0 = meany-b1*meanx
    print("b0 = ",b0)
    print("b1 = ",b1)
    k=[b0,b1]
    plotting_gr(x, y, k)

if __name__ == "__main__":
    main()
