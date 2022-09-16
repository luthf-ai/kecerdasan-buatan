graph = {
    'A' : ['B','C'],
    'B' : ['D', 'E'],
    'C' : ['F'],
    'D' : [],
    'E' : ['F', 'G'],
    'F' : ['H'],
    'G' : ['H'],
    'H' : ['G']
}
visited = [] # List to keep track of visited nodes.
queue = []   # Initialize a queue

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

print("Hasil penelusuran graf menggunakan BFS: ")
bfs(visited, graph, 'A')