import random
import math

#define Queue class
class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)
class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.lastID = 0
        self.users = {}
        self.friendships = {}

    def addFriendship(self, userID, friendID):
        """
        Creates a bi-directional friendship
        """
        if userID == friendID:
            print("WARNING: You cannot be friends with yourself")
        elif friendID in self.friendships[userID] or userID in self.friendships[friendID]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[userID].add(friendID)
            self.friendships[friendID].add(userID)

    def addUser(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.lastID += 1  # automatically increment the ID to assign the new user
        self.users[self.lastID] = User(name)
        self.friendships[self.lastID] = set()

    def populateGraph(self, numUsers, avgFriendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.lastID = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # Add users
        for i in range(numUsers):
            self.addUser(f'Test{i}')

        # Create friendships
        possible_friendships = []
        for userID in self.users:
            for friendID in range(userID + 1, self.lastID + 1):
                #appending tuple of current user and possible friends after them in a list
                possible_friendships.append((userID, friendID))
        
        #changes position of items in a list
        random.shuffle(possible_friendships)

        for i in range(0, math.floor(numUsers * avgFriendships / 2)):
            friendship = possible_friendships[i]
            self.addFriendship(friendship[0], friendship[1])

    def getAllSocialPaths(self, userID):
        """
        Takes a user's userID as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME

        #use BFS fo shortest friendship path
        #check if friendships exist
        if not self.friendships[userID]:
            return "User doesn't have any friends"
        #create new queue
        q = Queue()
        #enqueue with path to starting node
        q.enqueue([userID])
        while q.size() > 0:
            #dequeue first path
            path = q.dequeue()
            #check if current is our target, getting last item in path block
            current = path[-1]
            #iterate our set to check for visited
            if current not in visited:
                #starting user doesnt needto be in dict
                visited[current] = path
                for friend in self.friendships[current]:
                    if friend not in visited:
                        #make copy of path
                        copy = list(path)
                        copy.append(friend)
                        #enqueue the copy
                        q.enqueue(copy)
        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populateGraph(10, 2)
    print(sg.friendships)
    connections = sg.getAllSocialPaths(1)
    print(connections)
