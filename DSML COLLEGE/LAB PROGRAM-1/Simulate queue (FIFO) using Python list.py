
def queue_enqueue(list_queue, element):
    list_queue.append(element)


def queue_dequeue(list_queue):
    return list_queue.pop(0)


def queue_peek(list_queue):
    return list_queue[0] 


students = ["Aditya", "Arpit", "Aryan", "Daksh"]

queue_enqueue(students, "ABCD")

print(queue_peek(students));



