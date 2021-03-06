import random

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

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}

        #Adjacency list representation of a graph
        self.friendships = {}

        self.count = 0

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship

        Therefore creates unidirectional graph

        Makes TWO friendships
        """
        self.count = self.count + 1
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)


    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def fisher_yates_shuffle(self, l):
        for i in range(0, len(l)):
            random_index = random.randint(i, len(l)-1)
            l[random_index], l[i] = l[i], l[random_index]

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # Add users
        for user in range(num_users):
            self.add_user(user)
            #starts at 1, up to and including num_users

        #hint 1: to create N random friendships
        #you could create a list with all possible friendship combinations of user ids

        friendship_combinations = []
        #O(n^2)
        for user in range(1, self.last_id + 1):
            for friend in range(user + 1, self.last_id + 1):
                friendship_combinations.append((user, friend))
        
        #shuffle the list
        self.fisher_yates_shuffle(friendship_combinations)

        #then grab the first N elements from the list
        total_friendships = num_users * avg_friendships

        friends_to_make = friendship_combinations[:total_friendships // 2]



        # Create friendships
        for friendship in friends_to_make:
            self.add_friendship(friendship[0], friendship[1])


    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME
        queue = []

        for friend in sg.friendships[user_id]:
            visited[friend] = [user_id, friend]
            queue.append(friend)
            # print("queue", queue)
        #get neighbors naive
        for new_friend in queue: #adding to queue as it goes (FIFO)
                if new_friend is None:
                    return
                elif new_friend in visited:
                    for new_connection in sg.friendships[new_friend]:
                        if new_connection == user_id:
                            continue
                        # elif new_connection in visited:
                        #     continue
                        elif new_connection not in visited: #making sure we don't already have a path (which would be the shortest)
                            queue.append(new_connection)
                            new_path = visited[new_friend].copy()
                            # print("new path", new_path)
                            new_path.append(new_connection)
                            visited[new_connection] = new_path
                            # print("new path", new_path)
                            # print("new path", visited[new_connection])
                

        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(1000, 5)
    print(sg.friendships)
    print(sg.friendships[1])
    connections = sg.get_all_social_paths(1)
    print(connections)
    print(sg.count)

#{1: {9, 4, 5, 7}, 2: {7}, 3: {8, 6}, 4: {1}, 5: {8, 1, 6}, 6: {3, 5}, 7: {8, 1, 2}, 8: {3, 5, 7}, 9: {1}, 10: set()}
#{9: [1, 9], 4: [1, 4], 5: [1, 5], 8: [1, 5, 8], 6: [1, 5, 6], 3: [1, 5, 8, 3], 7: [1, 7], 2: [1, 5, 8, 7, 2]}

#this out put shouldn't be printing the path to 2 through 5 because 7 should be being explored before 8!!!

#Ah, searching the queue needed to be done at the same scope as creation of it or it will happen before all of our first entries are made (causing issues with the sequence)


#  def get_all_social_paths(self, user_id):
#         """
#         Takes a user's user_id as an argument

#         Returns a dictionary containing every user in that user's
#         extended network with the shortest friendship path between them.

#         The key is the friend's ID and the value is the path.
#         """
#         visited = {}  # Note that this is a dictionary, not a set
#         # !!!! IMPLEMENT ME
#         queue = []

#         for friend in sg.friendships[user_id]:
#             visited[friend] = [user_id, friend]
#             queue.append(friend)
#             print("queue", queue)
#             #get neighbors naive
#             for new_friend in queue: THIS NEEDED TO MOVE TO SAME SCOPE AS LINE 170!!!
#                 if new_friend is None:
#                     return
#                 elif new_friend in visited:
#                     for new_connection in sg.friendships[new_friend]:
#                         if new_connection == user_id:
#                             continue
#                         # elif new_connection in visited:
#                         #     continue
#                         elif new_connection not in visited:
#                             queue.append(new_connection)
#                             new_path = visited[new_friend].copy()
#                             print("new path", new_path)
#                             new_path.append(new_connection)
#                             visited[new_connection] = new_path
#                             print("new path", new_path)
#                             print("new path", visited[new_connection])
                






#solved: we traverse every node and all of their nodes FIFO (bfs), the path that is already tracked should be the smallest so we wont add a node back to teh queue if we already visited it
