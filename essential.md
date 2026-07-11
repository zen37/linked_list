# Linked Lists — One‑Page Guide

A linked list stores nodes where each node has a value and a pointer to the next node. You traverse by following pointers one at a time.

---

## Node

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
```

```
[val] → [next]
```

---

## Traversal

```python
cur = head
while cur:
    cur = cur.next
```

```
A → B → C → None
```

---

# Three Moves That Solve Most Problems

## 🔄 Rewire Pointers Carefully (reversal pattern)

```python
nxt = cur.next
cur.next = prev
prev = cur
cur = nxt
```

```
None ← A ← B ← C
```

---

## 🎯 Dummy Head (avoid head special cases)

```python
dummy = ListNode(0, head)
cur = dummy
return dummy.next
```

```
dummy → head → A → B
```

---

## 🐢🐇 Slow & Fast Pointers

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

## Middle of List

```python
def middle_node(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow
```

```
middle = 3
```

---

## Detect Cycle (Floyd)

```python
def has_cycle(head):
    slow = fast = head
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
```

---

## Find Cycle Start

```python
def cycle_start(head):
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

```
meet → reset slow → meet at entry
```

---

## Reverse Sublist (left..right)

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
→ 1 → 4 → 3 → 2 → 5
```

---

## Remove Nth From End

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
gap = n
```

---

## Merge Two Sorted Lists

```python
def merge_two_lists(l1, l2):
    dummy = ListNode()
    cur = dummy
    while l1 and l2:
        if l1.val < l2.val:
            cur.next = l1; l1 = l1.next
        else:
            cur.next = l2; l2 = l2.next
        cur = cur.next
    cur.next = l1 or l2
    return dummy.next
```

```
1→3→5 + 2→4→6 → 1→2→3→4→5→6
```

---

# LeetCode Practice (Core)

- Reverse Linked List  
- Middle of Linked List  
- Merge Two Sorted Lists  
- Linked List Cycle  
- Remove Nth Node From End  
- Reverse Linked List II  
- Linked List Cycle II  
- Merge K Sorted Lists  
- Reverse Nodes in k‑Group  
