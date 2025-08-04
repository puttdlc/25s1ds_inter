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

print(" ***Cafe***")
inp = input("Log : ").split('/')
main = queue()
for i, entry in enumerate(inp):
    parts = entry.split(',')
    arrival = int(parts[0])
    prep = int(parts[1])
    main.enqueue({  # profile of each customer for organizational sake
        'id': i + 1,
        'arrival': arrival,
        'prep': prep,
        'start': None,
        'end': None,
        'wait': 0,
    })

baristas = [0, 0]

events = []
max_wait = 0
max_wait_id = None

while not main.isEmpty():
    customer = main.get_next()
    main.dequeue()

    barista_index = 0 if baristas[0] <= baristas[1] else 1 #get index of barista who will be freed the earliest
    barista_free = baristas[barista_index] #pick the barista with the earliest queue

    if barista_free <= customer['arrival']: #if barista is already free, serve customer
        start_time = customer['arrival']
        wait = 0
    else: #make customer wait until barista is free
        start_time = barista_free
        wait = start_time - customer['arrival']

    end_time = start_time + customer['prep'] #time calculated to finish order for customer
    baristas[barista_index] = end_time #time that the barista will be free for the next customer

    #timestamps
    customer['start'] = start_time
    customer['end'] = end_time
    customer['wait'] = wait

    events.append((end_time, customer['id']))

    if wait > max_wait: #getting the longest wait time
        max_wait = wait
        max_wait_id = customer['id']

events.sort() #sort by time of finishing order (shortest to longest)

for time, customer_id in events:
    print(f"Time {time} customer {customer_id} get coffee")

if max_wait > 0:
    print(f"The customer who waited the longest is : {max_wait_id}")
    print(f"The customer waited for {max_wait} minutes")
else:
    print("No waiting")