"""
@author: Methlesh Koshle
@institute: IITBh


import networkx as nx
import easygui
from tkinter import *
from networkx import *
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from networkx.algorithms import bipartite
from networkx.algorithms import approximation as apxa
import matplotlib.backends.tkagg as tkagg
from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.backends.backend_tkagg import NavigationToolbar2Tk

g = nx.Graph()
e1, e2, mlb = [None]*3

root = Tk()
root.title("Netwok Analyzer")
root.geometry("1500x1500")

#dummy graph
g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(3, 4)
g.add_edge(4, 1)
g.add_edge(4, 5)

fig = Figure()
sbp = fig.add_subplot(111)
pos = nx.spring_layout(g)
canvas = FigureCanvasTkAgg(fig, master=root)

def getInfo():
	abt = nx.info(g).split("\n")
	messagebox.showinfo("Information", "\n".join(abt))
def degree():
	global e1
	messagebox.showinfo("Degree Information", 
						  "Degree of node {} is {}.".format(e1.get(), g.degree(int(e1.get())))
						  )
def getDegree():
	global e1
	root1 = Tk()
	root1.title("Degree")
	l1 = Label(root1, text="Enter Node")
	
	e1 = Entry(root1)

	l1.grid(row=0, column=0)
	e1.grid(row=0, column=1)

	Button(root1, text='Get Degree', command=degree).grid(row=3, column=0, sticky=W, pady=4)
	
	root1.mainloop()
	result = root1.destroy()
	root1.after(300000, result)

def insertNode():
	global g
	g.add_node(int(e1.get()))
	messagebox.showinfo("Information", 
					  	  "Node {} added successfully".format(int(e1.get()))
					  	  )
def insertEdge():
	global g
	g.add_edge(int(e1.get()), int(e2.get()))
	messagebox.showinfo("Information", 
					  	  "Edge between {} and {} added successfully".format(int(e1.get()), 
					  	  	int(e2.get()))
					  	  )
def deleteNode():
	global g
	g.remove_node(int(e1.get()))
	messagebox.showinfo("Information", 
					  	  "Node {} is removed".format(int(e1.get()))
					  	  )
def deleteEdge():
	global g
	g.remove_edge(int(e1.get()), int(e2.get()))
	messagebox.showinfo("Information", 
					  	  "Edge between {} and {} is removed".format(int(e1.get()), 
					  	  	int(e2.get()))
					  	  )
def plot1():
	nx.draw(g, with_labels=True)
	plt.show()
def plot2():
	nx.draw(g)
	plt.show()
def ad_node():
	global e1
	root = Tk()
	root.title("Add a node")
	l1 = Label(root, text="Enter new node")
	e1 = Entry(root)
	b = Button(root, text='Add node', command=insertNode)
	l1.pack()
	e1.pack()
	b.pack()
	root.mainloop()
def ad_edge():
	global e1, e2
	root = Tk()
	root.title("Add a edge")
	l1 = Label(root, text="Enter first node")
	l2 = Label(root, text="Enter second node")
	e1 = Entry(root)
	e2 = Entry(root)
	l1.grid(row=0, column=0)
	l2.grid(row=1, column=0)
	e1.grid(row=0, column=1)
	e2.grid(row=1, column=1)
	b = Button(root, text='Add edge', command=insertEdge)
	b.grid(row=3, column=0, sticky=W, pady=4)
	root.mainloop()
def rm_node():
	global e1
	root = Tk()
	root.title("Remove a node")
	l1 = Label(root, text="Enter the node")
	e1 = Entry(root)
	b = Button(root, text='Remove node', command=deleteNode)
	l1.pack()
	e1.pack()
	b.pack()
	root.mainloop()
def rm_edge():
	global e1, e2
	root = Tk()
	root.title("Remove an edge")
	Label(root, text="Enter first node").grid(row=0, column=0)
	Label(root, text="Enter second node").grid(row=1, column=0)
	e1 = Entry(root)
	e2 = Entry(root)
	e1.grid(row=0, column=1)
	e2.grid(row=1, column=1)
	Button(root, text='Remove edge', command=deleteEdge).grid(row=3, column=0, sticky=W, pady=4)
	root.mainloop()
def displayGraph():
	root = Tk()
	root.title("Display")
	v = IntVar()
	v.set(1)
	Radiobutton(root, text="with labels", padx = 20, variable=v, command=plot1, value=0).pack(anchor=W)
	Radiobutton(root, text="without labels", padx = 20, variable=v, command=plot2, value=1).pack(anchor=W)
	root.mainloop()
def updateG(file):
	global g
	f = open(file, "r")
	g = nx.Graph()
	for edge in f.readlines():
		x, y, v = map(float, edge.split())
		g.add_edge(int(x), int(y))
def importNet():
	updateG(easygui.fileopenbox())
def save():
	global e1
	name = e1.get()
	f = open(name+".txt", "w")
	for u, v in g.edges():
		f.writelines(str(u)+" "+str(v)+" 1\n")
	f.close()
	messagebox.showinfo("Status",
				 "The network saved successfully")
def saveNet():
	global e1
	root = Tk()
	root.title("Save the Network")
	l1 = Label(root, text="Enter the name of Network(.txt)")
	e1 = Entry(root)
	b = Button(root, text='save', command=save)
	l1.pack()
	e1.pack()
	b.pack()
def abt():
	messagebox.showinfo("About", "Network Analyzer helps you to analyze, explore various networks and graphs.")
def getDegreeDistritbution():
	node, deg = [], []
	dct = dict(g.degree())
	print(dct)
	for n in dct.keys():
		node.append(n)
		deg.append(dct[n])
	plt.title("Degree Distritbution")
	plt.ylabel("degree")
	plt.xlabel("node")
	plt.grid(True)
	plt.plot(node, deg)
	plt.show()
def donothing():
	pass
def select_cmd(selected):
	pass
def btree():
    global g, e1, e2
    n = int(e1.get())
    p = int(e2.get())
    g = nx.balanced_tree(n, p)
    messagebox.showinfo("Info", 
                          "Balanced tree ({}, {}) is created".format(n, p)
                          )
def blcNet():
    global e1, e2
    root = Tk()
    root.title("Generate Balanced Tree")
    
    l1 = Label(root, text="Enter branching factor of the tree(r)")
    l2 = Label(root, text="Enter height of the tree(h)")
    e1 = Entry(root)
    e2 = Entry(root)

    l1.grid(row=0, column=0)
    l2.grid(row=1, column=0)
    e1.grid(row=0, column=1)
    e2.grid(row=1, column=1)

    b = Button(root, text='Generate', command=btree)
    b.grid(row=3, column=0, sticky=W, pady=4)
    
    root.mainloop()
def complete():
    global g, e1
    n = int(e1.get())
    g = nx.complete_graph(n)
    messagebox.showinfo("Info", 
                          "Complete Graph with {} nodes created".format(n)
                          )
def cplNet():
    global e1
    root = Tk()
    root.title("Generate Complete graph")
    
    l1 = Label(root, text="Enter number of nodes")
    e1 = Entry(root)

    l1.grid(row=0, column=0)
    e1.grid(row=0, column=1)

    b = Button(root, text='Generate', command=complete)
    b.grid(row=1, column=1, sticky=W, pady=4)
    
    root.mainloop()
def cycle():
    global g, e1
    n = int(e1.get())
    g = nx.cycle_graph(n)
    messagebox.showinfo("Info", 
                          "Cycle Graph with {} nodes created".format(n)
                          )
def cycNet():
    global e1
    root = Tk()
    root.title("Generate Cycle graph")
    
    l1 = Label(root, text="Enter number of nodes")
    e1 = Entry(root)

    l1.grid(row=0, column=0)
    e1.grid(row=0, column=1)

    b = Button(root, text='Generate', command=cycle)
    b.grid(row=1, column=1, sticky=W, pady=4)
    
    root.mainloop()
def grid():
    global g, e1, e2
    n = int(e1.get())
    p = int(e2.get())
    g = nx.grid_graph(dim=[n, p])
    messagebox.showinfo("Info", 
                          "Grid Graph with ({}, {}) is created".format(n, p)
                          )
def grdNet():
    global e1, e2
    root = Tk()
    root.title("Generate Grid graph")
    
    l1 = Label(root, text="Enter rows")
    l2 = Label(root, text="Enter cols")
    e1 = Entry(root)
    e2 = Entry(root)

    l1.grid(row=0, column=0)
    l2.grid(row=1, column=0)
    e1.grid(row=0, column=1)
    e2.grid(row=1, column=1)

    b = Button(root, text='Generate', command=grid)
    b.grid(row=3, column=0, sticky=W, pady=4)
    
    root.mainloop()
def path():
    global g, e1, e2
    n = int(e1.get())
    g = nx.path_graph(n)
    messagebox.showinfo("Info", 
                          "Path Graph with {} nodes created".format(n)
                          )
def pthNet():
    global e1, e2
    root = Tk()
    root.title("Generate Path graph")
    
    l1 = Label(root, text="Enter number of nodes")
    e1 = Entry(root)

    l1.grid(row=0, column=0)
    e1.grid(row=0, column=1)

    b = Button(root, text='Generate', command=path)
    b.grid(row=3, column=0, sticky=W, pady=4)
    
    root.mainloop()
    
def rgen():
	global g, e1, e2
	n = int(e1.get())
	p = float(e2.get())
	g = nx.fast_gnp_random_graph(n, p)
	messagebox.showinfo("Info", 
						  "Graph with {} nodes created".format(n)
						  )

def mstGen():
	global g
	g = nx.minimum_spanning_tree(g)
	messagebox.showinfo("Info", "MST of current graph generated")

def rndNet():
	global e1, e2
	root = Tk()
	root.title("Generate random graph")
	
	l1 = Label(root, text="Enter number of nodes")
	l2 = Label(root, text="Enter probability of edge creation")
	e1 = Entry(root)
	e2 = Entry(root)

	l1.grid(row=0, column=0)
	l2.grid(row=1, column=0)
	e1.grid(row=0, column=1)
	e2.grid(row=1, column=1)

	b = Button(root, text='Generate', command=rgen)
	b.grid(row=3, column=0, sticky=W, pady=4)
	
	root.mainloop()
def dsqGen():
    global g, e1, e2
    n = list(map(int, e1.get().split(',')))
    g = nx.configuration_model(n)
    messagebox.showinfo("Info", "Graph is created")
def stnGen():
    global g
    nds=g.nodes()
    g = apxa.steinertree.steiner_tree(g, list(nds))
    messagebox.showinfo("Info", "Graph is created")
def degSeqNet():
    global e1, e2
    root = Tk()
    root.title("Generate Graph with degree sequence")
    
    l1 = Label(root, text="Enter , seperated degree")
    e1 = Entry(root)

    l1.grid(row=0, column=0)
    e1.grid(row=0, column=1)

    b = Button(root, text='Generate', command=dsqGen)
    b.grid(row=1, column=0, sticky=W, pady=4)
  
    root.mainloop()
def updateTable():
	global mlb
	for i in g.nodes():
		mlb.insert('end', i, chr(96+i), g.degree(i))
def lbl():
    global g, e1, e2
    n = int(e1.get())
    p = e2.get()
    g = nx.relabel_nodes(g, {n:p})
    messagebox.showinfo("Info", "Done!")
def reLabel():
	global e1, e2
	root = Tk()
	root.title("Relable node")
	
	l1 = Label(root, text="Enter label of node")
	l2 = Label(root, text="Enter new label")
	e1 = Entry(root)
	e2 = Entry(root)

	l1.grid(row=0, column=0)
	l2.grid(row=1, column=0)
	e1.grid(row=0, column=1)
	e2.grid(row=1, column=1)

	b = Button(root, text='Relable', command=lbl)
	b.grid(row=3, column=1, sticky=W, pady=4)	
def isComplete():
    global g
    tmp = g.degree()
    deg = [y for x, y in tmp]
    msg = "Graph is Complete"
    if any(x!=deg[0] for x in deg):
        msg = "Graph is not Complete"
    messagebox.showinfo("Info", msg)
def isPlaner():
    global g
    msg = "Graph is not Planer"
    if nx.check_planarity(g):
        msg = "Graph is Planer"
    messagebox.showinfo("Info", msg)
def isEuler():
    global g
    msg = "Graph is not Eulerian"
    if is_eulerian(g):
        msg = "Graph is Eulerian"
    messagebox.showinfo("Info", msg)
def isConnected():
    global g
    msg = "Graph is not Connected"
    if is_connected(g):
        msg = "Graph is Connected"
    messagebox.showinfo("Info", msg)
def diameter():
    global g
    messagebox.showinfo("Info", "Diameter of the Graph is {}".format(nx.diameter(g)))
def center():
    global g
    messagebox.showinfo("Info", "Center of the Graph is {}".format(nx.center(g)))
def degSeq():
	global g
	e = nx.degree(g)
	e = [y for x, y in e]
	e.sort(reverse=True)
	messagebox.showinfo("Info", "Degree Sequence is {}".format(e))
def tree():
	global g
	print(g.nodes())
	res = "Graph is not a tree"
	if nx.is_tree(g):
		res = "Graph is a tree"
	messagebox.showinfo("Info", res)
def edgeCover():
	st = bipartite.min_edge_cover(g)
	messagebox.showinfo("Info", "Set of Edges are {}".format(st))
def vertexCover():
	st = dnx.min_vertex_cover(g, sampler)
	messagebox.showinfo("Info", "Vertex cover is {}".format(st))
def avgCluster():
	st = nx.average_clustering(g)
	messagebox.showinfo("Info", "Average clustering coefficient is {}".format(st))
def avgdeg():
	st = nx.algorithms.assortativity.average_neighbor_degree(g)
	tmp = st
	e = "\n"
	for i in tmp.keys():
		e += str(i)+": "
		e += str(tmp[i])
		e+="\n"
	messagebox.showinfo("Info", "Average neighbor degree is {}".format(e))
def dfs():
	st = list(nx.dfs_edges(g))
	messagebox.showinfo("Info", "DFS thgrough edges {}".format(st))
def avgclt():
	messagebox.showinfo("Info", "Average Clustering Coefficient is {}".format(apxa.clustering_coefficient.average_clustering(g)))
def maxclq():
	messagebox.showinfo("Info", "Maximum Clique is the set {}".format(apxa.clique.max_clique(g)))
def ncnt():
	messagebox.showinfo("Info", "Node Connectivity of the graph is {}".format(apxa.node_connectivity(g)))

def kcomp():
	tmp=apxa.k_components(g)
	e = ""
	for i in tmp.keys():
		e+=str(i)+": "
		e+=", ".join([str(x) for x in tmp[i]])
		e+="\n"

	messagebox.showinfo("Info", "K-component structure of a graph is {}".format(e))
def bfs():
	st = list(nx.bfs_edges(g, source=1))
	messagebox.showinfo("Info", "BSF thgrough edges {}".format(st))
def mist():
	t = nx.minimum_spanning_tree(g)
	nx.draw(t, with_labels=True)
	plt.show()
	
def getDistance():
	src = int(e1.get())
	tgt = int(e2.get())
	pos = nx.spring_layout(g)
	path = nx.shortest_path(g, src, tgt)
	path_edges = list(zip(path,path[1:]))
	print(path_edges)
	nx.draw(g, pos, with_labels=True)
	nx.draw_networkx_nodes(g, pos, nodelist=path, node_color='r')
	nx.draw_networkx_edges(g, pos, edgelist=path_edges, edge_color='r', width=5)
	plt.axis('equal')
	plt.show()

def shortest_path():
	global e1, e2
	root = Tk()
	root.title("Shortest Path")
	
	l1 = Label(root, text="Source")
	l2 = Label(root, text="Destination")
	
	e1 = Entry(root)
	e2 = Entry(root)

	l1.grid(row=0, column=0)
	l2.grid(row=1, column=0)
	e1.grid(row=0, column=1)
	e2.grid(row=1, column=1)

	Button(root, text='Show', command=getDistance).grid(row=3, column=0, sticky=W, pady=4)
	
	root.mainloop()

def nGraph():
	global g
	g = nx.Graph()
	messagebox.showinfo("Info", "Graph is now empty.")
def update():
	global g, canvas
	sbp.clear()
	pos=nx.spring_layout(g)
	nx.draw(g, pos, sbp, with_labels=True)
	canvas.draw()
	canvas.get_tk_widget().pack(side=RIGHT, fill=BOTH, expand=1)

def main():
	global mlb
	top_bar = Frame(root, height=25, relief="raised", background="light sea green")
	top_bar.pack(fill="x", side="top", pady=2)
	tool_bar = Frame(root, relief="raised", width=50, background="khaki")
	tool_bar.pack(fill="y", side="left", pady=3)
	top_bar = Frame(root, relief="raised", width=50)
	top_bar.pack(fill="y", side="right", pady=4)
	top_bar = Frame(root, height=25, relief="raised", background="green4")#, width=50)
	top_bar.pack(fill="x", side="bottom", pady=5)
	
	nx.draw(g, pos, sbp, with_labels=True)
	canvas.draw()
	canvas.get_tk_widget().pack(side=RIGHT, fill=BOTH, expand=1)
	
	menubar = Menu(root)

	file = Menu(menubar, tearoff=0)
	menubar.add_cascade(label="File", menu=file)
	file.add_command(label="New Graph            Ctrl+N", command=nGraph)
	file.add_command(label="Open            Ctrl+O", command=importNet)
	file.add_command(label="Save            Ctrl+S", command=saveNet)
	file.add_separator()
	file.add_command(label="Exit            Ctrl+Q", command=root.quit)

	analyze = Menu(menubar, tearoff=0)
	menubar.add_cascade(label="Analyze", menu=analyze)
	analyze.add_command(label="Get Degree of a Node", command=getDegree)
	analyze.add_command(label="Get Degree Sequence", command=degSeq)
	analyze.add_command(label="Diameter of Graph", command=diameter)
	analyze.add_command(label="Center of Graph", command=center)
	# analyze.add_command(label="Relable Node", command=reLabel)
	analyze.add_command(label="Is Connected", command=isConnected)
	analyze.add_command(label="Is Complete", command=isComplete)
	analyze.add_command(label="Is Tree", command=tree)
	analyze.add_command(label="Is Eulerian", command=isEuler)
	analyze.add_command(label="Plot Degree Distritbution", command=getDegreeDistritbution)
	
	algorithm = Menu(menubar, tearoff=0)
	menubar.add_cascade(label="Algorithms", menu=algorithm)
	algorithm.add_command(label="Shortest Path", command=shortest_path)
	algorithm.add_command(label="Average clustering coefficient", command=avgCluster)
	algorithm.add_command(label="Vertex Cover", command=vertexCover)
	algorithm.add_command(label="Edge Cover", command=edgeCover)
	algorithm.add_command(label="DFS", command=dfs)
	algorithm.add_command(label="BFS", command=bfs)
	algorithm.add_command(label="Node Connectivity", command=ncnt)
	algorithm.add_command(label="K-components", command=kcomp)
	algorithm.add_command(label="Average Clustering Coefficient", command=avgclt)
	algorithm.add_command(label="Average Degree", command=avgdeg)
	algorithm.add_command(label="Maximum Clique of graph", command=maxclq)
	algorithm.add_command(label="Minimum Spanning Tree", command=mist)

	tools = Menu(menubar, tearoff=0)
	menubar.add_cascade(label="Generate", menu=tools)
	tools.add_command(label="Balanced Tree", command=blcNet)
	tools.add_command(label="Complete Graph", command=cplNet)
	tools.add_command(label="Cycle Graph", command=cycNet)
	tools.add_command(label="Grid Graph", command=grdNet)
	tools.add_command(label="Path Graph", command=pthNet)
	tools.add_command(label="Random Graph", command=rndNet)
	tools.add_command(label="MST of current graph", command=mstGen)
	tools.add_command(label="Steiner Tree of current graph", command=stnGen)
	tools.add_command(label="Graph with Degree Sequence", command=degSeqNet)

	view = Menu(menubar, tearoff=0)
	mode = Menu(root)
	menubar.add_cascade(label="View", menu=view)
	view.add_cascade(label="Select mode", menu=mode)
	mode.add_command(label="With Label", command=plot1)
	mode.add_command(label="Without Label", command=plot2)

	helpmenu = Menu(menubar, tearoff=0)
	menubar.add_cascade(label="Help", menu=helpmenu)
	helpmenu.add_command(label="Graph Info.", command=getInfo)
	helpmenu.add_command(label="About...", command=abt)

	b1 = Button(root, text="Add Node", command=ad_node, height=50, width=140)
	b2 = Button(root, text="Add Edge", command=ad_edge, height=50, width=140)
	b3 = Button(root, text="Remove Node", command=rm_node, height=50, width=140)
	b4 = Button(root, text="Remove Edge", command=rm_edge, height=50, width=140)
	ubutton = Button(root, text="Update", command=update, height=2, width=5)
	adn = PhotoImage(file="e1.png")
	ade = PhotoImage(file="n2.png")
	rmn = PhotoImage(file="rmn1.png")
	rme = PhotoImage(file="rme1.png")
	b1.config(image=adn, compound=RIGHT)
	b2.config(image=ade, compound=RIGHT)
	b3.config(image=rmn, compound=RIGHT)
	b4.config(image=rme, compound=RIGHT)
	b1.pack()
	b2.pack()
	b3.pack()
	b4.pack()
	ubutton.pack()

	root.config(menu=menubar)

	root.mainloop()

if __name__=="__main__":
	main()
