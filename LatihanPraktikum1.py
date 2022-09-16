graph = {
    'A' : ['B','E','F'],
    'B' : ['A','F','G'],
    'E' : ['A','F'],
    'F' : ['A','B','E'],
    'G' : ['B','C','H'],
    'C' : ['D','G'],
    'H' : ['D','G'],
    'D' : ['C','H']
}
#using dfs and bfs
visitedD = set() # List to keep track of visited nodes.

def dfs(visited, graph, node): # Function to implement DFS
    if node not in visited: # Jika node belum dikunjungi (tidak ada dalam list visited)
        print (node,end = " ") # Print node tersebut
        visited.add(node) # Tandai node tersebut sudah dikunjungi dengan menambahkannya dalam
        for neighbour in graph[node]: # Melakukan perulangan untuk setiap tetangga dari node
            dfs(visited, graph, neighbour) # Lakukan rekursi untuk setiap tetangga dari node

print("Hasil penelusuran graf menggunakan DFS: ")
dfs(visitedD, graph, 'A')
queue = []   # Initialize a queue
visitedB = [] # List to keep track of visited nodes.
def bfs(visited, graph, node): # Function to implement BFS
    visited.append(node) # Mark the node as visited
    queue.append(node)  # Push the node into the queue

    while queue: # Melakukan perulangan sampai queue kosong
        s = queue.pop(0) # Pop elemen pertama dari queue
        print (s, end = " ") # Print elemen yang di pop

        for neighbour in graph[s]: # Melakukan perulangan untuk setiap tetangga dari node yang di pop
            if neighbour not in visited: # Jika tetangga belum dikunjungi
                visited.append(neighbour) # Tandai tetangga tersebut sudah dikunjungi
                queue.append(neighbour) # Masukkan tetangga tersebut ke dalam queue
print()
print("Hasil penelusuran graf menggunakan BFS: ")
bfs(visitedB, graph, 'A')

