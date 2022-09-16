graph = {
    'A' : ['B'],
    'B' : ['A','G','F'],
    'F' : ['B','E'],
    'E' : ['F'],
    'G' : ['B','C'],
    'C' : ['D','G'],
    'D' : ['C','H'],
    'H' : ['D'],
}
#using bfs and dfs to D node
visitedD = set() # List to keep track of visited nodes.
queue = []   # Initialize a queue
visitedB = [] # List to keep track of visited nodes.
def bfs(visited, graph, node, x):
    #find x
    i = 0
    visited.append(node) # Mark the node as visited
    queue.append(node)  # Push the node into the queue
    while queue: # Melakukan perulangan sampai queue kosong
        s = queue.pop(0) # Pop elemen pertama dari queue
        print (s, end = " ") # Print elemen yang di pops
        i+=1
        if s == x:
            print(" found in ", i, " steps")
            return True
        for neighbour in graph[s]: # Melakukan perulangan untuk setiap tetangga dari node yang di pop
            if neighbour not in visited: # Jika tetangga belum dikunjungi
                visited.append(neighbour) # Tandai tetangga tersebut sudah dikunjungi
                queue.append(neighbour) # Masukkan tetangga tersebut ke dalam queue
    print(" not found")
    return False
i=0
def dfs(visited, graph, node, x, i):
    #find x
    if node not in visited: # Jika node belum dikunjungi (tidak ada dalam list visited)
        print (node,end = " ") # Print node tersebut
        i+=1
        if node == x:
            print(" found in ",i, " steps")
            return True
        visited.add(node) # Tandai node tersebut sudah dikunjungi dengan menambahkannya dalam
        for neighbour in graph[node]: # Melakukan perulangan untuk setiap tetangga dari node
            if dfs(visited, graph, neighbour, x, i):
                return True
    return False
print("Hasil penelusuran graf menggunakan DFS: ")
dfs(visitedD, graph, 'A', 'D', i)
print()
print("Hasil penelusuran graf menggunakan BFS: ")
bfs(visitedB, graph, 'A', 'D')


