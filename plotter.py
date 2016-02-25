from matplotlib import pyplot as plt
from matplotlib import style

style.use('ggplot')


def plot(**values):
    plots = {}
    for label, val in values.iteritems():
        plots[label] = (range(len(val)), [i/1000 for i in val])

    for k,v in plots.iteritems():
        plt.plot(v[0],v[1],label=k)

    plt.ylabel('Time in seconds')
    plt.xlabel('intervals')
    plt.legend()
    plt.show()

if __name__ == '__main__':
    values1 = [123456,123546,134526,143255,1454536,143452,124344,1543443,434321]
    values2 = [123436,124546,138526,133255,1455536,143452,123344,1533443,334321]

    plot(v1=values1, v2=values2)
