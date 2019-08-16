# Prints room id of connected rooms by direction
# name[5:] also removes 'Room ' from name string
# print(player.currentRoom.n_to.id)
# print(player.currentRoom.s_to.id)
# print(player.currentRoom.w_to.id)
# print(player.currentRoom.e_to.id)

print(map[player.currentRoom.id])
player.travel('n', showRooms = True)

# Adds room to map if not yet visited
if player.currentRoom.id not in map:
    map[player.currentRoom.id] = { 'n': '?', 's': '?', 'e': '?', 'w': '?'}



    
# DFT
# Create an empty set to store visited nodes
visited = list()

# Create an empty Stack and push the starting vertex
s = Stack()
s.push(starting_vertex)

# While the Stack is not empty...
while s.size() > 0:

    # Pop the first vertex from the stack
    vertex = s.pop()

    # If that vertex has not been visited...
    if vertex not in visited:

        # Mark it as visited
        visited.append(vertex)

        # Then add all of its neighbors to the top of the Stack
        for neighbor in self.vertices[vertex]:
            s.push(neighbor)
