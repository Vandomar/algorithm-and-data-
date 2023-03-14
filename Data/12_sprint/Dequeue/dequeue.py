# ID Решения 83871511
class Deque:
    def __init__(self, max_size: int):
        self.queue = [None] * max_size
        self.max_size = max_size
        self.head = 0
        self.tail = 0
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def push_back(self, item: int):
        if self.size != self.max_size:
            self.queue[self.tail] = item
            self.tail = (self.tail + 1) % self.max_size
            self.size += 1
        else:
            raise OverflowError

    def push_front(self, item: int):
        if self.size != self.max_size:
            self.queue[self.head - 1] = item
            self.head = (self.head - 1) % self.max_size
            self.size += 1
        else:
            raise OverflowError

    def pop_back(self):
        if self.is_empty():
            raise IndexError
        x = self.queue[self.tail - 1]
        self.queue[self.tail - 1] = None
        self.tail = (self.tail - 1) % self.max_size
        self.size -= 1
        return x

    def pop_front(self):
        if self.is_empty():
            raise IndexError
        x = self.queue[self.head]
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.max_size
        self.size -= 1
        return x


def data_input():
    count_command = int(input())
    queue_size = int(input())

    return count_command, queue_size


def main():
    count_command, queue_size = data_input()

    queue = Deque(queue_size)
    commands = {
        'push_front': queue.push_front,
        'push_back': queue.push_back,
        'pop_front': queue.pop_front,
        'pop_back': queue.pop_back,
    }
    for i in range(count_command):
        command = input()
        operation, *value = command.split()
        if value:
            try:
                result = commands[operation](int(*value))
                if result is not None:
                    print(result)
            except OverflowError:
                print('error')
        else:
            try:
                result = commands[operation]()
                print(result)
            except IndexError:
                print('error')


if __name__ == '__main__':
    main()
