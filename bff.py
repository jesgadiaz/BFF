import random
import sys
import time
import networkx as nx

def createGraph(input_file):
    global G, n, m, d, start_time
    G = nx.Graph()
    for j in range(0,n):
        G.add_node(j)
   
    f = open(input_file, "r")    
    string = f.readline()
    for i in range(0, m):        
        string = f.readline()
        string = string.split()
        j = int(string[0])-1
        k = int(string[1])-1
        G.add_edge(j, k)
    f.close()           

    if nx.is_connected(G):
        sp = dict(nx.all_pairs_shortest_path_length(G))
        d = []
        for i in range(0,n):
            list = []
            for j in range(0,n):
                list.append(sp[i][j])
            d.append(list)
        for i in range(0, n):
            for j in range(0, n):
                if d[i][j] == float("inf"):
                    d[i][j] = (n+1);
        del sp
    else:
        d = []
        for i in range(0,n):
            list = []
            for j in range(0,n):
                list.append(float("inf"))
            d.append(list)
        connected_components = nx.connected_components(G)
        for component in connected_components:
            # create subgraph    
            G_sub = nx.Graph()
            for v in component:
                G_sub.add_node(v)
                for e in G.edges:
                    if e[0]==v or e[1]==v:
                        G_sub.add_edge(e[0],e[1])
            
            sp = dict(nx.all_pairs_shortest_path_length(G_sub))
            for item1 in sp.items():
                for item2 in item1[1].items():
                    d[item1[0]][item2[0]] = item2[1]
                    d[item2[0]][item1[0]] = item2[1]
            del G_sub
            del sp
            
        for i in range(0, n):
            for j in range(0, n):
                if d[i][j] == float("inf"):
                    d[i][j] = (n+1)
    
    conn_comp = nx.number_connected_components(G)
    n_nodes   = len(nx.nodes(G))
    n_edges   = len(nx.edges(G))
    av_degree = 0
    for e in nx.degree(G):
        av_degree = av_degree + e[1]
    av_degree = av_degree / n_nodes
    density   = nx.density(G)
    print("conn. comp.: " + str(conn_comp))
    print("num vertices: " + str(n_nodes))
    print("num edges: " + str(n_edges))
    print("density: " + str(density))
    print("av degree: " + str(av_degree))        
    print("---Compute all shortest paths - running time: %s seconds ---" % (time.time() - start_time))
    
def update_distance():
    global n, d, distance, sequence
    for i in range(n):
        if d[i][sequence[len(sequence)-1]] < distance[i]:
            distance[i] = d[i][sequence[len(sequence)-1]]

def farthest_vertex():
    global n, distance, sequence
    max_dist = 0
    f = 0
    for i in range(n):
        if distance[i] > max_dist:
            max_dist = distance[i]
            f = i
    return f
    
def neighborhood(E):
    global n, d
    LE = list(E)
    NE = []
    for i in range(n):
        for j in LE:
            if d[i][j] == 1:
                NE.append(i)
                break
    return set(NE)
                
def run():
    global n, d, distance, sequence, reps, plus, start_time
    start_time = time.time()
    len_best_sequence = float("inf")
    best_sequence = []
    if plus == 'True':
        reps = n
    else:
        reps = 1
    for k in range(reps):
        distance = []
        for i in range(n):
            distance.append(float("inf"))
        sequence = []
        if reps == 1:
            v1 = random.randint(0,n-1)
        else:
            v1 = k
        sequence.append(v1)
        update_distance()
        Bp = set([])
        Bc = set([sequence[0]])
        while len(Bc) != n:
            sequence.append(farthest_vertex())
            update_distance()
            E  = set(Bc) - set(Bp)
            NE = neighborhood(E)
            Bp = Bc
            Bc = Bc.union(NE)
            t  = []
            t.append(sequence[len(sequence)-1])
            Bc = Bc.union(t)
        if len(sequence) < len_best_sequence:
            best_sequence = sequence
            len_best_sequence = len (sequence)
    return best_sequence
            
if __name__ == "__main__":
    if len(sys.argv) != 5:
        print ("Wrong number of arguments")
        print ("bgp input_file_path n m plus")
        sys.exit()
    start_time = time.time()
    input_file  = sys.argv[1]
    n    = int(sys.argv[2])
    m    = int(sys.argv[3])
    plus = str(sys.argv[4])
    createGraph(input_file)
    sequence = run()
    print("burning sequence: " + str(sequence))
    print("burning sequence length: " + str(len(sequence)))
    print("---BFF running time: %s seconds ---" % (time.time() - start_time))
