# Dijkstra’s Algorithm using a Min Heap
Dijkstra's algorithm solves the classic problem of finding the shortest paths between nodes in a weighted graph.

## Creating the Graph
The Python script reads the edges text file and creates a list of lists where each index represents a vertex and in each index is a list of all the edges and their corresponding weight.

### Time & Space Complexity
Because the list contains all the edges and is bidirectional, it will have 2E edges and the space complexity will be O(E). Going through every edge to make the list will have a time complexity of O(E).

## Dijkstra’s Algorithm with Min Heap
All vertices connected to the initial vertex are checked to see if they are already in the discovered min heap. If the element is not in the min heap the elements value can be either -2 meaning it is not discovered or -1 meaning it has been finalised. If the vertex is in the discovered min heap but not finalised, it checks if the new path is smaller than the current one and updates it if needed. The smallest element from the discovered heap is then moved to final and the process continues till all the vertices are finalised. To recover the path, the vertex parent array is tracked back till it reaches the initial vertex.

### Time & Space Complexity
The time complexity of checking the discovered min heap is constant. This is because a vertex array full of each of the vertices indexes is kept in the min heap array, meaning the element value just needs to be checked if it is greater than 0. The space complexity of this vertex will be O(V). Dijkstra’s algorithm will go through every edge in the worst case, making the time complexity O(E). Since a min-heap is being used for the discovered array, extracting the minimum and maintaining the properties of a min heap as the height of the tree will at most be O(logV) swaps. For recovering the final path, the worst case this would be O(E) and the space complexity is O(V). 

So the overall time complexity of the algorithm is ElogV+2E but since ElogV is bigger E, the time complexity is O(ElogV) and the space complexity is 2V+E making it O(V+E)

## Lucky Customer addition
There is a list of customers given and the problem is that we want to find which customer will give the least detour from our trip. This is solved by running Dijkstra’s algorithm for both the initial and final vertices. Then it goes through each customer to see which customer gives the minimum distance. Once the lucky customer is found, we use the Dijkstra’s Algorithm function to find the path from the initial to the lucky customer and from the lucky customer to the final vertex.

### Time & Space Complexity
The time complexity of running Dijkstra’s algorithm from both the initial and final vertices would be 2ElogV meaning it’s O(ElogV). For finding the lucky customer the time complexity is O(C) and making the customer list is also O(C). This makes the time complexity O(ElogV+C) but since C can be at max V and assuming the graph is connected, this implies C<E meaning it can be disregarded making the time complexity O(ElogV). To find the final path, we use the Dijkstra’s Algorithm function twice, meaning the time complexity is 3ElogV making the time complexity O(ElogV).
