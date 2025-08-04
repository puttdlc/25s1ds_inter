class queue:
    def __init__(self, value=None):
        self.queue = value if value is not None else []
    def get_queue(self):
        return self.queue.copy()
    def dequeue(self):
        if self.queue:
            self.queue = self.queue[1:]
    def get_next(self):
        return self.queue[0] if self.queue else None
    def enqueue(self, value):
        self.queue.append(value)
    def isEmpty(self):
        return len(self.queue) == 0
    def getCount(self):
        return len(self.queue)

raw_input = input("Enter width, height, and room: ")
width, height, inp = raw_input.split()
width, height, map = int(width), int(height), inp.split(',')

directions = [
    (0,-1), #up (north)
    (1,0), #right (east)
    (0,1), #down (south)
    (-1,0) #left (west)
]

start_character = "F"
walkable_points = ['_',start_character]
goal = "O"

verifiedInput = True

continueSearch = True
starting_point = None

for i in range(0,len(map)):
    if len(map[i]) < width or len(map[i]) > width:
        verifiedInput = False
        break
    if start_character in map[i]:
        starting_point = (map[i].index(start_character),i)
if starting_point == None:
    verifiedInput = False
if len(map) > height or len(map) < height:
    verifiedInput = False


points = queue([starting_point])
visited = [starting_point]

def getValidNeighbors(point):
    global continueSearch
    for direction in directions:
        if point == None:
            print("Cannot reach the exit portal.")
            continueSearch = False
            break
        x = direction[0] + point[0] 
        y = direction[1] + point[1]
        if (x,y) in visited:
            continue
        if x < 0 or x >= width:
            continue
        if y < 0 or y >= height:
            continue
        if map[y][x] == goal:
            print("Found the exit portal.")
            continueSearch = False
            break
        if not map[y][x] in walkable_points:
            continue
        points.enqueue((x,y))
        visited.append((x,y))

if verifiedInput:
    while continueSearch:
        if not points.isEmpty():
            print(f"Queue: {points.queue}")
        getValidNeighbors(points.get_next())
        points.dequeue()
else:
    print("Invalid map input.")