# Linked Lists

A linked list stores a sequence as a chain of nodes, where each node holds a value and a reference to the next node. Unlike a Python list, you cannot jump to position `i` directly; you follow the chain one node at a time. Once the core moves click, most linked list problems become short. Skim this once, then keep it open while you work.

---

## The Node

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
```

```
Node structure:
[val] → [next]
```

The last node's `next` is `None`, which is how you know you have reached the end.

---

## Traversal

```python
cur = head
while cur:
    # do something with cur.val
    cur = cur.next
```

```
Traversal:
A → B → C → None
^
cur moves one step at a time
```

---

# Three Moves That Solve Most Problems

Linked list problems often look different on the surface, but most of them boil down to **three core pointer maneuvers**. Master these and 80% of LeetCode linked‑list questions become straightforward.

---

## 🔄 1. Rewire Pointers Carefully

When you change a node’s `next`, **save the node you are about to lose first**, or you will strand the rest of the list.

### Pattern (the “three‑line dance”)

```python
nxt = cur.next     # save next
cur.next = prev    # repoint
prev = cur         # advance prev
cur = nxt          # advance cur
```

```
prev   cur   nxt
None ← A ← B ← C

Step:
nxt = B
A.next = None
prev = A
cur = B
```

---

## 🎯 2. The Dummy Head

A dummy node eliminates special cases when modifying the head of the list.

### Pattern

```python
dummy = ListNode(0, head)
cur = dummy
return dummy.next
```

```
dummy → [head] → A → B → C
```

---

## 🐢🐇 3. Two Pointers (Slow & Fast)

One pointer moves 1 step, the other moves 2 steps.

### Pattern

```python
slow = head
fast = head

while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
```

```
slow: 1 → 2 → 3 → 4 → 5
fast: 1 → 3 → 5 → None
```

---

# Essential Patterns

## 🐢🐇 Find the Middle of a Linked List

```python
def middle_node(head):
    slow = head 
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow
```

```
slow: 1 → 2 → 3 → 4 → 5
fast: 1 → 3 → 5 → None
middle = 3
```

---

## 🔁 Detect a Cycle (Floyd’s Algorithm)

```python
def has_cycle(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False
```

```
A → B → C → D
      ↑     ↓
      └─────┘
slow and fast eventually meet
```

---

## 🎯 Find the Start of the Cycle

```python
def cycle_start(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    else:
        return None

    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next

    return slow
```

```
Meet inside loop → reset slow → move both 1 step → meet at cycle start
```

---

## 🔢 Find Cycle Length

```python
def cycle_length(meet):
    cur = meet
    length = 0
    while True:
        cur = cur.next
        length += 1
        if cur == meet:
            return length
```

```
Walk until you return to meet → count steps
```

---

# More Linked List Operations

## 🔄 Reverse a Sublist (Reverse Between)

```python
def reverse_between(head, left, right):
    dummy = ListNode(0, head)
    prev = dummy

    for _ in range(left - 1):
        prev = prev.next

    cur = prev.next
    for _ in range(right - left):
        nxt = cur.next
        cur.next = nxt.next
        nxt.next = prev.next
        prev.next = nxt

    return dummy.next
```

```
1 → [2 → 3 → 4] → 5
becomes
1 → 4 → 3 → 2 → 5
```

---

## 🧹 Remove the Nth Node from the End

```python
def remove_nth_from_end(head, n):
    dummy = ListNode(0, head)
    slow = fast = dummy

    for _ in range(n + 1):
        fast = fast.next

    while fast:
        slow = slow.next
        fast = fast.next

    slow.next = slow.next.next
    return dummy.next
```

```
dummy → 1 → 2 → 3 → 4 → 5
                 ↑         ↑
                slow      fast (gap = n)
```

---

## 🔀 Merge Two Sorted Lists

```python
def merge_two_lists(l1, l2):
    dummy = ListNode()
    cur = dummy

    while l1 and l2:
        if l1.val < l2.val:
            cur.next = l1
            l1 = l1.next
        else:
            cur.next = l2
            l2 = l2.next
        cur = cur.next

    cur.next = l1 or l2
    return dummy.next
```

```
1 → 3 → 5
2 → 4 → 6
merged → 1 → 2 → 3 → 4 → 5 → 6
```

---

## 🔗 Merge K Sorted Lists (Min‑Heap)

```python
import heapq

def merge_k_lists(lists):
    heap = []
    for i, node in enumerate(lists):
        if node:
            heapq.heappush(heap, (node.val, i, node))

    dummy = ListNode()
    cur = dummy

    while heap:
        val, i, node = heapq.heappop(heap)
        cur.next = node
        cur = cur.next
        if node.next:
            heapq.heappush(heap, (node.next.val, i, node.next))

    return dummy.next
```

```
Push heads → pop smallest → push next → repeat
```

---

# LeetCode Practice Problems (Curated)

## Beginner
- Reverse Linked List  
- Middle of the Linked List  
- Merge Two Sorted Lists  
- Linked List Cycle  

## Intermediate
- Remove Nth Node From End  
- Reverse Linked List II  
- Palindrome Linked List  
- Intersection of Two Linked Lists  

## Advanced
- Linked List Cycle II  
- Rotate List  
- Copy List With Random Pointer  
- Merge K Sorted Lists  

## Expert
- Reverse Nodes in k‑Group  
- Sort List  
- Reorder List  

---

# Cheat‑Sheet Summary

## Node
```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
```

## Traversal
```python
cur = head
while cur:
    cur = cur.next
```

## Full Reverse
```python
prev = None
cur = head
while cur:
    nxt = cur.next
    cur.next = prev
    prev = cur
    cur = nxt
return prev
```

## Reverse Sublist
```python
dummy = ListNode(0, head)
prev = dummy
for _ in range(left - 1):
    prev = prev.next

cur = prev.next
for _ in range(right - left):
    nxt = cur.next
    cur.next = nxt.next
    nxt.next = prev.next
    prev.next = nxt

return dummy.next
```

## Middle Node
```python
slow = fast = head
while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
return slow
```

## Detect Cycle
```python
slow = fast = head
while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
    if slow == fast:
        return True
return False
```

## Cycle Start
```python
slow = fast = head
while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
    if slow == fast:
        break
else:
    return None

slow = head
while slow != fast:
    slow = slow.next
    fast = fast.next
return slow
```

## Remove Nth From End
```python
dummy = ListNode(0, head)
slow = fast = dummy
for _ in range(n + 1):
    fast = fast.next
while fast:
    slow = slow.next
    fast = fast.next
slow.next = slow.next.next
return dummy.next
```

## Merge Two Lists
```python
dummy = ListNode()
cur = dummy
while l1 and l2:
    if l1.val < l2.val:
        cur.next = l1
        l1 = l1.next
    else:
        cur.next = l2
        l2 = l2.next
    cur = cur.next
cur.next = l1 or l2
return dummy.next
```