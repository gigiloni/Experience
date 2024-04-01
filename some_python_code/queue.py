class Queue:

    def __init__(self, elements=None):
        if elements is None:
            elements = []
        self.elements = elements

    def read(self):
        return self.elements[0] if self.elements else None

    def enqueue(self, element):
        self.elements.append(element)

    def dequeue(self):
        if self.elements:
            return self.elements.pop(0)
        return None

    def is_empty(self):
        return not bool(self.elements)


class Background:
    def __init__(self):
        self.queue = Queue()

    def add(self, job):
        self.queue.enqueue(job)

    def execute(self):
        while not self.queue.is_empty():
            print(f'Processing {self.queue.dequeue()}')


bg = Background()
bg.add('job1')  # just example, if u wanna use this queue u should delete these "adds"
bg.add('job2')  # just example, if u wanna use this queue u should delete these "adds"
bg.add('job3')  # just example, if u wanna use this queue u should delete these "adds"
bg.execute()
