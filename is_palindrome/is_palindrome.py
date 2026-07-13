from create_linked_list import build, ListNode


def is_palindrome(head: ListNode) -> bool:

    values: list[int] = []

    curr: ListNode = head

    while curr:
        values.append(curr.val)
        curr = curr.next

    return values == values[::-1]


def is_palindrome2(head: ListNode) -> bool:

    values: list[int] = []

    curr: ListNode = head

    while curr:
        values.append(curr.val)
        curr = curr.next

    left: int = 0
    right: int = len(values) - 1

    while left < right:
        if values[left] != values[right]:
            return False
        else:
            left += 1
            right -= 1

    return True


if __name__ == "__main__":
    head = build([1, 2, 3, 4, 5])
    print(is_palindrome(head))

    head = build([1, 2, 2, 1])
    print(is_palindrome(head))

    head = build([1, 2, 3, 4, 5])
    print(is_palindrome2(head))

    head = build([1, 2, 2, 1])
    print(is_palindrome2(head))
