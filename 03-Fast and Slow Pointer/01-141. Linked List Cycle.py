class Node:
    def __init__(self,data):
        self.data=data
        self.next=None



li = [3,2,0,-4]
pos = 1

head=Node(li[0])
current=head

for i in li[1:]:
    current.next=Node(i)
    current=current.next
    
slow=head
fast=head

while(fast and fast.next):
    slow=slow.next
    fast=fast.next.next
    if(fast==slow):
        print(True)
        break

print(False)