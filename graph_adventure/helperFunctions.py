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



# BFS
#Create an empty list to store the visited vertices

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
