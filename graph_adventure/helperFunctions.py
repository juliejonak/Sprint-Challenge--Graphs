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
    print(f"Q: {q}")
    path_found = False
    chosen_path = None

    while not path_found:
        check = q.dequeue()
        print(f"Top of while: Check: {check}")
        curr_path = check["path"]
        curr_room = check["room"]

        # check all directions of current room
        # if next room has "?", make new path
        # if not, append and keep checking
        for key, value in map[curr_room].items():
            # key: direction, value: room number
            if value == '?':
                curr_path.append(key)
                chosen_path = curr_path
                path_found = True
                break
            print(f"checking {key}: {value}")
            if value not in visited:
                path_copy = list(curr_path)
                path_copy.append(key)
                visited[value] = { "room": value, "path": path_copy }
                print(f"new to append: {visited[value]}")
                q.enqueue(visited[value])

    print(f"Chosen path: {chosen_path}")



    pass