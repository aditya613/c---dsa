
def stack_retrieve(list_stack):
    return list_stack[-1]

def stack_store(list_stack, element):
    list_stack.insert(-1, element)


def stack_delete_last(list_stack):
    return list_stack.pop()


students = ["Aditya", "Arpit", "Daksh", "Aryan"]

stack_store(students, "abcD")

print(stack_retrieve(students))



