from collections import deque
import queue
# At RRA, 7 clients queue. First come, first served (FIFO).
RRA_queue = deque()

print("RRA Queue Operations")
def RRA_enqueue(client):
    RRA_queue.append(client)
    return f"Enqueued: {client}"

# Enqueue 7 clients.
RRA_enqueue("Client1")
RRA_enqueue("Client2")
RRA_enqueue("Client3")
RRA_enqueue("Client4")
RRA_enqueue("Client5")
RRA_enqueue("Client6")
RRA_enqueue("Client7")
print(f"RRA Queue: {list(RRA_queue)} \n")

# After 3 served, who is front?
print("After serving 3 clients:")
def RRA_dequeue():
    if RRA_queue:
        for _ in range(3):
            served_client = RRA_queue.popleft()
            print(f"Served: {served_client}")
    else:
        print("Queue is empty, no clients to serve.")

RRA_dequeue()
print(f"Front of RRA Queue now: {RRA_queue[0] if RRA_queue else 'Queue is empty'}")

#  At BK ATM, 6 clients queue. 
BK_queue = deque()
print("\nBK ATM Queue Operations")
def BK_enqueue(client):
    BK_queue.append(client)
    return f"Enqueued: {client}"

# Enqueue 6 clients.
BK_enqueue("Client1")
BK_enqueue("Client2")
BK_enqueue("Client3")
BK_enqueue("Client4")
BK_enqueue("Client5")
BK_enqueue("Client6")
print(f"BK Queue: {list(BK_queue)} \n")

# who is second served ?
print("The second served is:")
def BK_dequeue():
    if BK_queue:
        for _ in range(1):
            served_client = BK_queue.popleft()
            print(f"Served: {served_client}")
    else:
        print("Queue is empty, no clients to serve.")

BK_dequeue()
print(f"second served of BK Queue now: {BK_queue[0] if BK_queue else 'Queue is empty'}")

# Queue vs stack for graduation ceremony seating. 
def graduation_seating(guests):
    queue = deque(guests)
    queue.append(guests)
    print(f"Guest {guests} is seated.")

print("\nGraduation Ceremony Seating:")
graduation_queue = deque()
def graduation_seating(guest):
    graduation_queue.append(guest)
    print(f"Guest {guest} is seated.")

graduation_seating("guest1")
graduation_seating("guest2")
graduation_seating("guest3")
graduation_seating("guest4")
graduation_seating("guest5")
if graduation_queue:
    print(f"In graduation, first come, {graduation_queue[0]}.\n")
else:
    print("No guests seated.\n")

# stack for graduation ceremony seating.
graduation_stack = []
def graduation_seating_stack(guest):
    graduation_stack.append(guest)
    print(f"Guest {guest} is seated.")
graduation_seating_stack("guest1")
graduation_seating_stack("guest2")  
graduation_seating_stack("guest3")
graduation_seating_stack("guest4")
graduation_seating_stack("guest5")  
if graduation_stack:
    print(f"In graduation with stack, last come, {graduation_stack[-1]}.\n")    
else:
    print("No guests seated.\n")

print("Note: In graduation, using a queue ensures first come, first served seating, while a stack would seat the last guest first, which is not ideal for such events.\n")
