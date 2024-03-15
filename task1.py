#Структура однозв'язного списку
class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

#Функція для реверсування однозв'язного списку
def reverseList(head):
    prev = None
    current = head
    while current:
        next_temp = current.next  # Запам'ятовуємо наступний вузол
        current.next = prev  # Міняємо посилання на попередній
        prev = current  # Переміщуємо prev на поточний вузол
        current = next_temp  # Переміщуємо current на наступний вузол
    return prev

#Алгоритм сортування для однозв'язного списку
def mergeSort(head):
    if not head or not head.next:
        return head

    # Визначення середини списку
    prev_slow = None
    slow = head
    fast = head
    while fast and fast.next:
        prev_slow = slow
        slow = slow.next
        fast = fast.next.next
    
    prev_slow.next = None  # Розриваємо список на дві частини

    # Рекурсивно сортуємо дві половини
    l1 = mergeSort(head)
    l2 = mergeSort(slow)

    return merge(l1, l2)

# Функція що об'єднує два відсортовані однозв'язні списки в один відсортований список
def merge(l1, l2):
    dummy = ListNode()
    tail = dummy
    while l1 and l2:
        if l1.value < l2.value:
            tail.next, l1 = l1, l1.next
        else:
            tail.next, l2 = l2, l2.next
        tail = tail.next
    tail.next = l1 or l2
    return dummy.next


# Функція для виводу списку
def printList(node):
    while node:
        print(node.value, end=" -> ")
        node = node.next
    print("None")

# Створення списку: 4 -> 2 -> 1 -> 3
head = ListNode(4, ListNode(2, ListNode(1, ListNode(3))))

print("Original list:")
printList(head)

# Реверсування списку
reversed_list = reverseList(head)
print("\nReversed list:")
printList(reversed_list)

# Сортування реверсованого списку
sorted_list = mergeSort(reversed_list)
print("\nSorted list:")
printList(sorted_list)

# Створення другого відсортованого списку для об'єднання
second_list = ListNode(5, ListNode(6, ListNode(7)))

# Об'єднання двох відсортованих списків
merged_list = merge(sorted_list, second_list)
print("\nMerged sorted lists:")
printList(merged_list)

