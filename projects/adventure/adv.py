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
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

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
first_prev = None

def dft_recursive(room, last_room):
	if last_room != None:
		pass
	else:
		last_room = room
	print("last_room", last_room)
	if room.id in traversal_graph.keys():
		for direction in player.current_room.get_exits():
			if direction not in traversal_graph[room.id].keys():
				traversal_graph[room.id].update({direction: '?'})
			# elif traversal_graph[room.id][direction] == '?':
			# 	dft_recursive(room)
			# elif '?' not in traversal_graph[room.id].values():
			# 	reverse_key = reverse_traversal.pop()
			# 	traversal_path.append(reverse_key)
			# 	player.travel(reverse_key)
			# 	print("moved ",  reverse_key)
			# 	print("moved to ",  player.current_room.id)
			# 	continue
			else:
				continue
	else:
		traversal_graph[room.id] ={}
		if player.current_room.get_exits():
			for direction in player.current_room.get_exits():
				if direction not in traversal_graph[room.id].keys():
					traversal_graph[room.id].update({direction: '?'})

            
	if len(traversal_graph) == 500:
		return
	elif '?' not in traversal_graph[room.id].values(): #all rooms will have exits
		# print("prepop",  player.current_room.id)
		# print("reverse",  reverse_traversal)
		# reverse_key = reverse_traversal.pop()
		# traversal_path.append(reverse_key)
		# player.travel(reverse_key)
		# print("moved ",  reverse_key)
		# print("moved to ",  player.current_room.id)
		# return
		print("prepop",  player.current_room.id)
		if len(player.current_room.get_exits()) == 1:
			only_way = player.current_room.get_exits()[0]
			traversal_path.append(only_way)
			player.travel(only_way)
			print("moved necessarily",  only_way)
			print("moved to only",  player.current_room.id)
			return
		elif len(reverse_traversal) > 0 and reverse_traversal[-1] in player.current_room.get_exits():
			reverse_key = reverse_traversal.pop()
			traversal_path.append(reverse_key)
			player.travel(reverse_key)
			print("moved reverse",  reverse_key)
			print("moved to reverse",  player.current_room.id)
			return
		else:
			rando = random.choice(player.current_room.get_exits())     #['n', 's', 'e', 'w'])
			traversal_path.append(rando)
			player.travel(rando)
			print("moved rando",  rando)
			print("moved to rando",  player.current_room.id)
			return
	elif '?' in traversal_graph[room.id].values():
		# new_keys = []
		# for item in traversal_graph[room.id].keys():
		# 	new_keys.append(item)
		# print(new_keys)
		# rando_key = random.choice(new_keys)
		# while traversal_graph[room.id][random.choice(new_keys)] == '?': #shouldn't this already be random because dicts are unordered
		for key, value in traversal_graph[room.id].items(): #shouldn't this already be random because dicts are unordered
			if value == '?':
				# key = rando_key
				print("key",key)
				if len(traversal_path) == 0:
					reverse_traversal.append(reverse_direction[key])	
					traversal_path.append(key)
					player.travel(key)
					print("first move", player.current_room.id)
				elif player.current_room.id != last_room:
					reverse_traversal.append(reverse_direction[key])	
					traversal_path.append(key)
					player.travel(key)
					print("different room", player.current_room.id)
				else:
					traversal_path.append(key)
					player.travel(key)
					print("in same rm", player.current_room.id)
				# if player.current_room.id != room.id:
				# 	reverse_traversal.append(reverse_direction[key])	
				# 	traversal_path.append(key)
				print("currentroom", player.current_room.id)
				if player.current_room.id != room.id and traversal_graph[room.id][key] == '?':
					traversal_graph[room.id].update({key: player.current_room.id})
				print("coming from", room.id)
				if player.current_room.id not in traversal_graph.keys():
					traversal_graph[player.current_room.id] = {}
					traversal_graph[player.current_room.id].update({reverse_direction[key]: room.id})
				print(traversal_graph)
				dft_recursive(player.current_room, room.id)
                #we've popped back to rm ONE but we are in rm 0's loop
				while player.current_room.id != room.id:
					# if len(reverse_traversal) > 0 and reverse_traversal[-1] in player.current_room.get_exits():
					# 	reverse_key = reverse_traversal.pop()
					# 	traversal_path.append(reverse_key)
					# 	player.travel(reverse_key)
					# 	print("moved reverse",  reverse_key)
					# 	print("moved to reverse",  player.current_room.id)
					# 	return
					# else:
						rando = random.choice(player.current_room.get_exits())     #['n', 's', 'e', 'w'])
						traversal_path.append(rando)
						player.travel(rando)
						print("moved rando 2",  rando)
						print("moved to rando 2",  player.current_room.id)
						# return	
				print(len(traversal_path))
				if traversal_graph[room.id][key] != '?' and len(reverse_traversal) > 0: #not in traversal_graph[room.id].values(): #all rooms will have exits
					reverse_key = reverse_traversal.pop()
					traversal_path.append(reverse_key)
					player.travel(reverse_key)
					print("moved next ?",  reverse_key)
					print("moved to next ?",  player.current_room.id)
					continue
				if len(reverse_traversal) == 0:
					continue
				elif '?' not in traversal_graph[player.current_room.id].values():
					if '?' in traversal_graph[room.id].values(): 
						dft_recursive(room.id, room.id)
			else:
				continue

		
# print(traversal_path)
dft_recursive(first_room, first_prev)



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
