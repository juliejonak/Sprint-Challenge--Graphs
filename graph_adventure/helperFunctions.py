# Prints room id of connected rooms by direction
# name[5:] also removes 'Room ' from name string
# print(player.currentRoom.n_to.id)
# print(player.currentRoom.s_to.id)
# print(player.currentRoom.w_to.id)
# print(player.currentRoom.e_to.id)

# print(map[player.currentRoom.id])
# player.travel('n', showRooms = True)

# # Adds room to map if not yet visited
# if player.currentRoom.id not in map:
#     map[player.currentRoom.id] = { 'n': '?', 's': '?', 'e': '?', 'w': '?'}

#####
#                                        #
#      017       002       014           #
#       |         |         |            #
#       |         |         |            #
#      016--015--001--012--013           #
#                 |                      #
#                 |                      #
#      008--007--000--003--004           #
#       |         |                      #
#       |         |                      #
#      009       005                     #
#       |         |                      #
#       |         |                      #
#      010--011--006                     #
#                                        #



class Queue():
    def __init__(self):
        self.queue = []
    def __repr__(self):
        return f"Queue: {self.queue}"
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

# BFS
# Create an empty list to store the visited vertices

# Create an empty Queue and enqueue & PATH TO the starting vertex

# While the queue is not empty...
    # Dequeue the first PATH
    # GRAB THE VERTEX FROM THE END OF THE PATH
    # IF VERTEX = TARGET, RETURN PATH

    # If that vertex has not been visited...
        # Mark it as visited

        # Then add & PATH TO all of its neighbors to the back of the queue
            # Copy the path so that the append is being added to the list copy, not to the actual list
            # Append neighbor to the back of the copy
            # Enqueue copy

# return dict with { "room": integer, "path": [path_to_next_room], updated_map: { map } }
def find_nearest_unexplored(curr_room, graph, map):
    visited = {}
    q = Queue()
    q.enqueue( { "room": curr_room, "path": [] } )
    print(f"Q: {q} \n")
    path_found = False
    chosen_path = None

    while not path_found:
        check = q.dequeue()
        print(f"Top of while: Check: {check}")
        curr_path = check["path"]
        curr_room2 = check["room"]
        print(f"Checking room {curr_room2} in graph: {map}")

        # check all directions of current room
        # if next room has "?", make new path
        # if not, append and keep checking
        for key, value in map[curr_room2].items():
            # key: direction, value: room number
            if value == '?':
                print(f"FOUND ? in room {curr_room2}: {key} {value}")
                curr_path.append(key)
                chosen_path = curr_path
                path_found = True
                break
            print(f"checking {key}: {value}")
            if value != None and value not in visited:
                path_copy = list(curr_path)
                path_copy.append(key)
                visited[value] = { "room": value, "path": path_copy }
                print(f"new to append: {visited[value]}")
                q.enqueue(visited[value])

    print(f"Chosen path: {chosen_path}")

    for direction in chosen_path:
        # Sets the next room to be the direction we'll traverse in
        next_room = graph[curr_room][1][direction]
        print(f"Moving {direction} from room {curr_room}. Next room is room {next_room}")

        if next_room not in map:
            print(f"Room {next_room} not in map. Graph shows {next_room}'s exits are: {graph[next_room][1]}")
            # updates map[curr_room][direction] to next_room to mark as visited
            map[curr_room][direction] = next_room
            # Adds the next room to map as well
            map[next_room] = { 'n': '?', 's': '?', 'e': '?', 'w': '?'}

            # Checks for non-valid exits to update in map so only viable un-explored exits are marked '?'
            if 'n' not in graph[next_room][1]:
                map[next_room]['n'] = None
            if 's' not in graph[next_room][1]:
                map[next_room]['s'] = None
            if 'e' not in graph[next_room][1]:
                map[next_room]['e'] = None
            if 'w' not in graph[next_room][1]:
                map[next_room]['w'] = None
            
            # Sets the curr_room to next_room
            if direction == 'n':
                map[next_room]['s'] = curr_room
            if direction == 's':
                map[next_room]['n'] = curr_room
            if direction == 'e':
                map[next_room]['w'] = curr_room
            if direction == 'w':
                map[next_room]['e'] = curr_room
            
            print(f"Because we came from {direction}, room {next_room} stored as: {map[next_room]}")
            curr_room = next_room
            print(f"\n New curr_room is room {curr_room}. Next room is {map[curr_room]}")

        else:
            curr_room = next_room
            print(f"2 New curr_room is room {curr_room}: {map[curr_room]}")


    # print({ "room": curr_room, "path": chosen_path, "map": map})
    return { "room": curr_room, "path": chosen_path, "updated_map": map}