class Stack():
    def __init__(self):
        self.stack = []
    def __repr__(self):
        return f"{self.stack}"
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)

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


def traverseMap(roomGraph, player):
    traversalPath = []

    # Create a map
    map = {
        0: { 'n': '?', 's': '?', 'e': '?', 'w': '?'}
    }

    s = Stack()
    s.push( player.currentRoom.id )
    last_room = 0
    last_move = ''
    counter = 0

    # TODO: Update previous room when traversing to prevent duplicate moves

    # while len < len(roomGraph)
    while len(map) < len(roomGraph):
        # curr_room = s.pop()

        if player.currentRoom.id not in map:
            map[player.currentRoom.id] = { 'n': '?', 's': '?', 'e': '?', 'w': '?'}

            # Checks for any exits that are dead ends and marks them as None in map
            if player.currentRoom.n_to == None:
                map[player.currentRoom.id]['n'] = None
            if player.currentRoom.s_to == None:
                map[player.currentRoom.id]['s'] = None
            if player.currentRoom.e_to == None:
                map[player.currentRoom.id]['e'] = None
            if player.currentRoom.w_to == None:
                map[player.currentRoom.id]['w'] = None

        print(f"In Room {player.currentRoom.id}: {map[player.currentRoom.id]}")

        if map[player.currentRoom.id]['n'] == '?':
            traversalPath.append('n')
            map[player.currentRoom.id]['n'] = player.currentRoom.n_to.id
            last_move = 'n'
            last_room = player.currentRoom.id
            player.travel('n')
            
        elif map[player.currentRoom.id]['s'] == '?':
            traversalPath.append('s')
            map[player.currentRoom.id]['s'] = player.currentRoom.s_to.id
            last_move = 's'
            last_room = player.currentRoom.id
            player.travel('s')

        elif map[player.currentRoom.id]['e'] == '?':
            print(f" \n Moving east from {player.currentRoom.id} to room {player.currentRoom.e_to.id}. {roomGraph[player.currentRoom.id]} --> {roomGraph[player.currentRoom.e_to.id]} \n")
            traversalPath.append('e')
            map[player.currentRoom.id]['e'] = player.currentRoom.e_to.id
            last_move = 'e'
            last_room = player.currentRoom.id
            player.travel('e')
            
        elif map[player.currentRoom.id]['w'] == '?':
            traversalPath.append('w')
            map[player.currentRoom.id]['w'] = player.currentRoom.w_to.id
            last_move = 'w'
            last_room = player.currentRoom.id
            player.travel('w')

        else:
            # BFS to nearest ?
            # append to traversalPath
            # set currentRoom.id = room with ? exit
            # loop
            print("HIT THE ELSE")
            next_path = find_nearest_unexplored(player.currentRoom.id, roomGraph, map)

            # Adds shortest path to next unexplored to traversalPath
            # Moves player through those rooms
            for direction in next_path["path"]:
                print(f"Trying to move {direction} from {player.currentRoom.id}")
                player.travel(direction)
                traversalPath.append(direction)
            
            # Updates map with newly explored rooms
            map = next_path["updated_map"]
            
    return traversalPath


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
        # print(f"Checking room {curr_room2} in graph: {map}")
        print(f"Checking room {curr_room2}")

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
        print(f"Trying to move from {curr_room} {direction}")
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