graph = {
    'A' : ['B','C'],
    'B' : ['C','D', 'E'],
    'C' : ['F'],
    'D' : [],
    'E' : ['F'],
    'F' : ['H'],
    'G' : ['H'],
    'H' : ['G']
}
visited = set() # List to keep track of visited nodes.
def dfs(visited, graph, node): # Function to implement DFS
    if node not in visited: # Jika node belum dikunjungi (tidak ada dalam list visited)
        print (node) # Print node tersebut
        visited.add(node) # Tandai node tersebut sudah dikunjungi dengan menambahkannya dalam
        for neighbour in graph[node]: # Melakukan perulangan untuk setiap tetangga dari node
            dfs(visited, graph, neighbour) # Lakukan rekursi untuk setiap tetangga dari node

print("Hasil penelusuran graf menggunakan DFS: ")
dfs(visited, graph, 'A')