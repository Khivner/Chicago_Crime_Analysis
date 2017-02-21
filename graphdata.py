import matplotlib.pyplot as plt

class generate_graph:
    def __init__(self, data, yrange, results):
        self.data = data
        self.y = yrange
        self.x = range(0,28)
        self.results = results
        

    def make_fig(self):
        plt.figure(1)
        plt.suptitle('Average Number of Reported Crimes Per Day in 28 Day Lunar Cyles')
        #make the first subplot
        plt.subplot(211)
        bargraph1 = plt.bar(self.x, self.data)
        self.make_graph(bargraph1, self.y)
        #make the second subplot
        plt.subplot(212)
        bargraph2 = plt.bar(self.x, self.data)
        self.make_graph(bargraph2, [0, self.y[-1]])
        #exports plture to png
        plt.subplots_adjust(top=0.87, left=0.15, bottom=0.1, hspace=0.4)
        plt.savefig(self.results)
        
        
    def make_graph(self, bargraph,y):
        #change colors for bars representing days around full moon event
        bargraph[13].set_color('r')
        bargraph[14].set_color('r')
        plt.xlabel('Day of the Lunar Cycle')
        plt.ylabel('Number of Crimes\n Reported')
        plt.yticks(y, y)
        plt.ylim(ymin=y[0],ymax=y[-1])
        plt.tight_layout()
        #plt.show()
    


##TESTING##
##data = [211013, 210760, 209476, 210362, 209873, 210399, 209959, 210281, 209326, 210152, 209603, 208994, 208377, 208598, 209697, 210478, 210084, 207991, 208335, 209842, 209432, 208961, 207792, 208566, 209582, 210364, 212335, 211517]
##for x in range(28):
##    data[x] = round(float(data[x]/196))
##
##data =[1069, 1073, 1066, 1066, 1073, 1061, 1069, 1062, 1059, 1065, 1075, 1082, 1084, 1077, 1069, 1071, 1069, 1066, 1070, 1069, 1077, 1066, 1068, 1067, 1068, 1070, 1057, 1056]
##yrange = range(1050,1105,5)
##results = 'results.png'
##graph = generate_graph(data, yrange, results)
##graph.make_fig()

