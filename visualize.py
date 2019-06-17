import networkx as nx
import matplotlib.pyplot as plt

graph = nx.read_edgelist('C:/Users/Muneeb/Desktop/pakistaniAppData-Copy2.txt')
print(nx.info(graph))
pos1 = nx.spring_layout(graph, k=12, scale=2)
catList= ['Music&Audio', 'Productivity', 'Auto&Vehicles','House&Home','Photography', 'Communication','Social','Lifestyle', 'Medical', 'Sports', 'Education', 'Shopping', 'Finance', 'News&Magazines', 'Food&Drink', 'Travel&Local', 'Weather', 'Simulation', 'Personalization', 'Tools', 'Books&Reference', 'Action', 'Entertainment']
color_map = []
for node in graph:
    if node in catList:
        color_map.append('red')
    else: color_map.append('green')
nx.draw_networkx(graph,  pos1,node_size = 20,font_size = 9,node_color = color_map)

plt.show()