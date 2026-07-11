from create_linked_list import build, ListNode


def remove_duplicates(head: ListNode) -> ListNode:

    # Time:  O(n) - one pass. Space: O(1) - pointer rewiring only.

    cur = head
    while cur and cur.next:
        if cur.val == cur.next.val:
            cur.next = cur.next.next  # skip the duplicate node
        else:
            cur = cur.next  # values differ, move on
    return head


if __name__ == "__main__":
    head = build([1, 2, 3, 4, 5])
    print(remove_duplicates(head))  # 1 -> 2 -> 3 -> 4 -> 5
    head = build([1, 1, 3, 4, 4, 5])
    print(remove_duplicates(head))  # 1 -> 3 -> 4 -> 5
