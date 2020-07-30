from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# import sys
# x=2000
# sys.setrecursionlimit(2000)

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []
traversal_graph = {}
reverse_traversal = []

# traversal_graph[player.current_room.id] = {}

# for direction in player.current_room.get_exits():
# 	traversal_graph[player.current_room.id].update({direction: '?'})
    

print(traversal_graph)
reverse_direction = { 'n': 's', 's': 'n', 'e': 'w', 'w': 'e'}

first_room = player.current_room

def dft_recursive(room):
	# print(traversal_path)
	if room.id in traversal_graph.keys():
		for direction in player.current_room.get_exits():
			if direction not in traversal_graph[room.id].keys():
				traversal_graph[room.id].update({direction: '?'})
			else:
				pass
	else:
		traversal_graph[room.id] ={}
		if player.current_room.get_exits():
			for direction in player.current_room.get_exits():
				if direction not in traversal_graph[room.id].keys():
					traversal_graph[room.id].update({direction: '?'})

            
	if len(traversal_graph) == 500:
		return
	elif '?' not in traversal_graph[room.id].values(): #all rooms will have exits
		reverse_key = reverse_traversal.pop()
		traversal_path.append(reverse_key)
		player.travel(reverse_key)
		print("moved ",  reverse_key)
		print("moved to ",  player.current_room.id)
		return
	elif '?' in traversal_graph[room.id].values():
		for key, value in traversal_graph[room.id].items(): #shouldn't this already be random because dicts are unordered
			if value == '?':
				print("key",key)

				reverse_traversal.append(reverse_direction[key])	
				traversal_path.append(key)
				player.travel(key)
				print("currentroom", player.current_room.id)
				if player.current_room.id != room.id and traversal_graph[room.id][key] == '?':
					traversal_graph[room.id].update({key: player.current_room.id})
				print("coming from", room.id)
				if player.current_room.id not in traversal_graph.keys():
					traversal_graph[player.current_room.id] = {}
					traversal_graph[player.current_room.id].update({reverse_direction[key]: room.id})
				print("currentroom", traversal_graph)
				dft_recursive(player.current_room)
				print(len(traversal_path))
				if traversal_graph[room.id][key] != '?' and len(reverse_traversal) > 0: #not in traversal_graph[room.id].values(): #all rooms will have exits
					reverse_key = reverse_traversal.pop()
					traversal_path.append(reverse_key)
					player.travel(reverse_key)
					print("moved 2",  reverse_key)
					print("moved to 2",  player.current_room.id)
					continue
				elif len(reverse_traversal) == 0:
					continue
				elif '?' not in traversal_graph[player.current_room.id].values():
					if '?' in traversal_graph[room.id].values(): 
						dft_recursive(room.id)
			else:
				continue

		
# print(traversal_path)
dft_recursive(first_room)



# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")
