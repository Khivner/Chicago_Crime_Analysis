import matplotlib.pyplot as plt

class generate_graph:
    def __init__(self, data, yrange):
        self.data = data
        self.y = yrange
        self.x = range(0,28)
        self.bargraph = plt.bar(self.x, self.data)
        
    def make_graph(self):
        self.bargraph[13].set_color('r')
        self.bargraph[14].set_color('r')
        plt.title("Average Number of Arrests Per Day in 28 Day Lunar Cyles")
        plt.ylabel('Number of Arrests')
        plt.xlabel('Day of the Lunar Cyle')
        plt.yticks(self.y, self.y)
        plt.ylim(ymin=self.y[0],ymax=self.y[-1])
        plt.savefig('results.png')
        plt.show()
    


##TESTING##
##data = [211013, 210760, 209476, 210362, 209873, 210399, 209959, 210281, 209326, 210152, 209603, 208994, 208377, 208598, 209697, 210478, 210084, 207991, 208335, 209842, 209432, 208961, 207792, 208566, 209582, 210364, 212335, 211517]
##for x in range(28):
##    data[x] = round(float(data[x]/196))
######
##yrange = range(1050,1100,5)
##graph = generate_graph(data, yrange)
##graph.make_graph()

