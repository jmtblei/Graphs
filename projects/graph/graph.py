"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
    def add_vertex(self, vertex):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex] = set()
    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        #check if v1 and v2 exists
        if v1 in self.vertices and v2 in self.vertices:
            #add edge to v1
            self.vertices[v1].add(v2)
        else:
            raise IndexError("The vertex doesn't exist")
    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        #create an empty set to store nodes that have been visited
        visited = set()
        #create an empty queue and add (enqueue/append) the starting vertex
        q = Queue()
        q.enqueue(starting_vertex)
        #while the queue is not empty,
        while q.size() > 0:
            #remove (dequeue/pop) the first vertex from the queue
            current = q.dequeue()
            #iterate through our set to check for visited nodes
            if current not in visited:
                #print check
                print(current)
                #add them if visited
                visited.add(current)
                #add the neighboring nodes to the back of the queue (queue is fifo)
                for neighbor in self.vertices[current]:
                    q.enqueue(neighbor)
    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        #create an empty set to store nodes that have been visited
        visited = set()
        #create an empty stack and add (push/append) the starting vertex
        s = Stack()
        s.push(starting_vertex)
        #while the stack is not empty,
        while s.size() > 0:
            #remove (pop) the first vertex from the stack
            current = s.pop()
            #iterate through our set to check for visited nodes
            if current not in visited:
                #print check
                print(current)
                #add them if visited
                visited.add(current)
                #add the neighboring nodes to the top of the stack (stack is lifo)
                for neighbor in self.vertices[current]:
                    s.push(neighbor)
    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        This should be done using recursion.
        """
        #base case initialize our visited as an empty set if it doesnt exist
        if visited is None:
            visited = set()
        #iterate through out set and check for visited nodes
        if starting_vertex not in visited:
            #add the node as visited
            visited.add(starting_vertex)
            print(visited)
            #recursive call for each child
            for neighbor in self.vertices[starting_vertex]:
                self.dft_recursive(neighbor, visited)
    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        #create an empty set to store nodes that have been visited
        visited = set()
        #create an empty queue to and add a path (enqueue/append) to the starting vertex
        q = Queue()
        q.enqueue([starting_vertex])
        #while the queue is not empty,
        while q.size() > 0:
            #remove (dequeue/pop) the first vertex(path) 
            path = q.dequeue()
            #grab the last vertex from the path
            current = path[-1]
            #check if the vertex is our target destination
            if current == destination_vertex:
                return path
            #iterate our set to check for visited nodes
            if current not in visited:
                #add them if visited
                visited.add(current)
                #add the neighboring nodes to the back of the queue (queue is fifo)
                for neighbor in self.vertices[current]:
                    #first copy the path
                    copy = list(path)
                    copy.append(neighbor)
                    #add (enqueue/append) the copy
                    q.enqueue(copy)
    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        #create an empty set to store nodes that have been visited
        visited = set()
        #create an empty stack to and add a path (push/append) to the starting vertex
        s = Stack()
        s.push([starting_vertex])
        #while the stack is not empty,
        while s.size() > 0:
            #remove (pop) the first vertex(path) 
            path = s.pop()
            #grab the last vertex from the path
            current = path[-1]
            #check if the vertex is our target destination
            if current == destination_vertex:
                return path
            #iterate our set to check for visited nodes
            if current not in visited:
                #add them if visited
                visited.add(current)
                #add the neighboring nodes to the top of the stack (stack is lifo)
                for neighbor in self.vertices[current]:
                    #first copy the path
                    copy = list(path)
                    copy.append(neighbor)
                    #add (push/append) the copy
                    s.push(copy)





if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT recursive paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    # Valid DFS paths:
    #     [1, 2, 4, 6]
    #     [1, 2, 4, 7, 6]
    # '''
    print(graph.dfs(1, 6))
