import matplotlib.pyplot as plt

def pieChart(val=0,labs=''):
    values = [200,399,125]
    labels = ['A','B','C']

    fig, ax = plt.subplots()
    ax.pie(val,labels=labs)
    plt.savefig('pie.png')
    plt.close()

