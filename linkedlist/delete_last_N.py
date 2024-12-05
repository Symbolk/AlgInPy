class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def remove_nth_from_end(head, n):
    # 创建一个虚拟头节点
    dummy = ListNode(0)
    dummy.next = head
    first = dummy
    second = dummy

    # 移动 first 指针，使其与 second 指针之间有 n + 1 的间隔
    for _ in range(n + 1):
        first = first.next

    # 移动 first 到链表的末尾，同时移动 second
    while first:
        first = first.next
        second = second.next

    # 删除倒数第 N 个节点
    second.next = second.next.next

    return dummy.next  # 返回新的头节点

def print_list(head):
    while head:
        print(head.value, end=" -> ")
        head = head.next
    print("None")

# 创建链表 1 -> 2 -> 3 -> 4 -> 5
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

print("原链表:")
print_list(head)

# 删除倒数第 2 个节点
n = 2
head = remove_nth_from_end(head, n)

print(f"删除倒数第 {n} 个节点后的链表:")
print_list(head)
