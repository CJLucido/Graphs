
# from collections import deque

# class Queue():
#     def __init__(self):
#         self.queue = deque()
#     def enqueue(self, value):
#         self.queue.append(value)
#     def dequeue(self):
#         return self.queue.popleft()
#     def size(self)
#         return len(self.queue)

#would need Stack



def earliest_ancestor(ancestors, starting_node):
    cache_paths = []
    path = [starting_node]
    cache_paths.append(path)
    visited = set()

    def get_neighbors( ancestors, starting_node):
        #if the tuple contains the starting node return the value in the tuple position 0 that is not the starting node
        #else pass
        neighbors = []
        for pair in ancestors:
            if starting_node is pair[1]:
                neighbors.append(pair[0])
            else:
                pass
        return neighbors

        
    def longest_in_cache():
            last_length = 0
            longest_pedigree = []
            for pedigree in cache_paths:
                if len(pedigree) > last_length:
                    longest_pedigree = pedigree
                    last_length = len(pedigree)
                #test doesn't actually check to see if this is working!!! but I think it would
                elif len(pedigree) == len(longest_pedigree):
                    if pedigree[-1] < longest_pedigree[-1]:
                        longest_pedigree = pedigree
                    else:
                        longest_pedigree = longest_pedigree
                ##____________________________________________-
                else:
                    pass
            print(longest_pedigree[-1])
            if len(longest_pedigree) == 1:
                return -1
            else:
                return longest_pedigree[-1]
    
    def dft( ancestors, starting_node):

        current_path = cache_paths[-1]
        
        if starting_node not in visited:
                visited.add(starting_node)
                neighbors = get_neighbors(ancestors, starting_node)
                if len(neighbors)> 0:
                    for neighbor in neighbors:
                        #NEVER UPDATED CURRENT PATH
                        neighbor_path = current_path.copy()
                        neighbor_path.append(neighbor)
                        cache_paths.append(neighbor_path)
                        dft(ancestors, neighbor)
        # longest_in_cache()

    dft(ancestors, starting_node)
    return longest_in_cache()











































###This doesnt actually solve for if two pedigrees are of equal length!!! (another testing failure)