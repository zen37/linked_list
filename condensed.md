# Linked List

## Core Moves
🔄 Rewire: nxt=cur.next; cur.next=prev; prev=cur; cur=nxt  
🎯 Dummy: dummy=ListNode(0,head); return dummy.next  
🐢🐇 Slow/Fast: slow+=1, fast+=2

---

## Middle
slow/fast → return slow

---

## Cycle
Detect: slow==fast  
Start: meet → slow=head → move both 1 step  
Length: walk until meet again

---

## Reverse
Full: use rewire pattern  
Sublist: dummy → walk to left → local rewire

---

## Remove Nth
dummy → gap n+1 → slow.next = slow.next.next

---

## Merge Two Lists
dummy → pick smaller → append → return dummy.next

---
