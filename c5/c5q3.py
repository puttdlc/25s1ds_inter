class node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def createList(l=[]):
    if not l:
        return None
    head = node(l[0])
    current = head
    for i in range(1, len(l)):
        current.next = node(l[i])
        current = current.next
    return head

def printList(H):
    current = H
    values = []
    while current:
        values.append(current.data)
        current = current.next
    print(" ".join(values))

def mergeOrderesList(p, q):
    temp = node(None)
    tail = temp

    while p and q:
        if int(p.data) <= int(q.data):
            tail.next = node(p.data)
            p = p.next
        else:
            tail.next = node(q.data)
            q = q.next
        tail = tail.next

    while p:
        tail.next = node(p.data)
        p = p.next
        tail = tail.next

    while q:
        tail.next = node(q.data)
        q = q.next
        tail = tail.next

    return temp.next

L1, L2 = input("Enter 2 Lists : ").split(' ')
L1, L2 = L1.split(','), L2.split(',')

LL1 = createList(L1)
LL2 = createList(L2)
print('LL1 : ',end='')
printList(LL1)
print('LL2 : ',end='')
printList(LL2)
m = mergeOrderesList(LL1,LL2)
print('Merge Result : ',end='')
printList(m)