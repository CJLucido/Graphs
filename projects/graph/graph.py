"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}


    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        self.vertices[v1].add(v2)

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # make a queue
        q = Queue()
        # enqueue our start node
        q.enqueue(starting_vertex)

        # make a set to track visited nodes
        visited = set()

        # while queue still has things in it
        while q.size() > 0:
        ## dq from front of the line, this is our current node
            current_node = q.dequeue()
        ## check if we've visited, if not:
            if current_node not in visited:
        ### mark it as visited
                visited.add(current_node)
                # print(current_nsode)
        ### get its neighbors
                neighbors = self.get_neighbors(current_node)
        ### iterate over neighbors,
                for neighbor in neighbors:
        #### add to queue
                    q.enqueue(neighbor)
      
        for i in visited:
            str(i)
            print(i)
        # return "\n".join(str(i) for i in visited)


    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # make a stack
        s = Stack()
        # push our starting node onto the stack
        s.push(starting_vertex)
        # make a set to track the nodes we've visited
        visited = set()

        # as long as our stack isn't empty
        while s.size() > 0:
        ## pop off the top, this is our current node
            current_node = s.pop()

        ## check if we have visited this before, and if not:
            if current_node not in visited:
        ### mark it as visited
                visited.add(current_node)
        ### print it (in this case)
                print(current_node)
        ### get its neighbors
                neighbors = self.get_neighbors(current_node)
        ### iterate over neighbors
                for neighbor in neighbors:
        #### and add them to our stack
                    s.push(neighbor)

    base_case = []

    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        if starting_vertex not in self.base_case:
            self.base_case.append(starting_vertex)
            print(starting_vertex)
            neighbors = self.get_neighbors(starting_vertex)
            for neighbor in neighbors:
                self.dft_recursive(neighbor)
        else:
            pass


    breadth_neighbors = []


    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # # make a queue
        # q = Queue()
        # # enqueue our start node
        # q.enqueue(starting_vertex)

        # # # make a set to track visited nodes
        # # visited = set()
        # self.breadth_neighbors.append(starting_vertex)

        # # while queue still has things in it
        # while q.size() > 0:
        # ## dq from front of the line, this is our current node
        #     current_node = q.dequeue()
        # ## check if we've visited, if not:
        #     if current_node is not destination_vertex: #not in self.breadth_neighbors and
        # ### mark it as visited
                
        #         # print(current_nsode)
        # ### get its neighbors
        #         neighbors = self.get_neighbors(current_node)
        # ### iterate over neighbors,
        #         for neighbor in neighbors:
        # #### add to queue
        #             q.enqueue(neighbor)
        #             if neighbor == destination_vertex:
        #                 self.breadth_neighbors.append(current_node)
        #                 self.breadth_neighbors.append(neighbor)
        #     else:
        #         return self.breadth_neighbors
      
        q = Queue()
        visited = set()
        path = [starting_vertex]
        q.enqueue(path)

        while q.size() > 0:
            current_path = q.dequeue()
            current_node = current_path[-1]
            if current_node == destination_vertex:
                return current_path
            elif current_node not in visited:
                visited.add(current_node)
                neighbors = self.get_neighbors(current_node)
                for neighbor in neighbors:
                    neighbor_path = current_path.copy()
                    neighbor_path.append(neighbor)
                    q.enqueue(neighbor_path)



    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        q = Stack()
        visited = set()
        path = [starting_vertex]
        q.push(path)

        while q.size() > 0:
            current_path = q.pop()
            current_node = current_path[-1]
            if current_node == destination_vertex:
                return current_path
            elif current_node not in visited:
                visited.add(current_node)
                neighbors = self.get_neighbors(current_node)
                for neighbor in neighbors:
                    neighbor_path = current_path.copy()
                    neighbor_path.append(neighbor)
                    q.push(neighbor_path)

    base_case2 = []
    recursive_end =[]

    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        if len(self.base_case2) > 0:
            # current_path = self.base_case2[-1]
            current_path = starting_vertex
        else:
            current_path = [0]
        
        current_node = current_path[-1]
        if current_node == destination_vertex:
            # print("destiny", destination_vertex)
            # print('current', current_path)
            # return current_path
            self.recursive_end.append(current_path)
            #WHY ARENT RETURN STATEMENTS EXITING THE IF CONDITIONAL HERE!!!?
            # exit
            # return self.recursive_end
            # print("hit", current_path)
            # return current_path
        elif type(starting_vertex) == list:
            if starting_vertex not in self.base_case2 and starting_vertex.count(current_node) == 1:
                self.base_case2.append(starting_vertex)
                neighbors = self.get_neighbors(current_node)
                for neighbor in neighbors:
                    neighbor_path = current_path.copy()
                    neighbor_path.append(neighbor)
                    self.dfs_recursive(neighbor_path, destination_vertex)
            else:
                pass
        else:
            self.base_case2.append([starting_vertex])
            neighbors = self.get_neighbors(starting_vertex)
            for neighbor in neighbors:
                    neighbor_path = [starting_vertex].copy()
                    neighbor_path.append(neighbor)
                    self.dfs_recursive(neighbor_path, destination_vertex)
        # print(self.recursive_end)
        if len(self.recursive_end) >= 1:
            return self.recursive_end[0]

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
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))