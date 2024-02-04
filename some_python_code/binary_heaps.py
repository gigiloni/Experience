class Heap:
    def __init__(self, data=None, root=None):
        self.root_value = root
        if data is None:
            self.data = []
        if root:
            self.data.append(root)

    def get_root(self):
        return self.data[0]

    def last(self):
        return self.data[-1]

    def insert(self, value):
        self.data.append(value)
        self.lift_up()

    def delete(self):
        if len(self.data) == 1:
            return self.data.pop()

        root_value = self.data[0]
        self.data[0] = self.data.pop()
        self.lift_down()
        return root_value

    def lift_up(self, current_index=None):
        if current_index is None:
            current_index = len(self.data) - 1

        if current_index <= 0:
            return

        p_index = self.parent_index(index=current_index)

        if not current_index > 0 and self.data[current_index] > self.data[p_index]:
            return

        self.swap(index1=p_index, index2=current_index)

        self.lift_up(current_index=p_index)

    def lift_down(self, current_index=None):
        if current_index is None:
            current_index = 0
        indexes = {
            'c_index': current_index,
            'lc_index': self.left_child_index(index=current_index),
            'rc_index': self.right_child_index(index=current_index)
        }

        if not self.greater_child(indexes=indexes):
            return

        child_index = self.larger_child_index(indexes=indexes)
        self.swap(index1=current_index, index2=child_index)

        self.lift_down(current_index=child_index)

    def greater_child(self, indexes):

        if self.in_bounds(index=indexes['lc_index']) and self.data[indexes['lc_index']] > self.data[indexes['c_index']]:
            return True

        if self.in_bounds(index=indexes['rc_index']) and self.data[indexes['rc_index']] > self.data[indexes['c_index']]:
            return True

        return False

    def swap(self, index1, index2):
        self.data[index1], self.data[index2] = self.data[index2], self.data[index1]

    def parent_index(self, index):
        return (index - 1) // 2 if index > 0 else 0

    def left_child_index(self, index):
        return (index * 2) + 1

    def right_child_index(self, index):
        return (index * 2) + 2

    def in_bounds(self, index):
        return 0 <= index < len(self.data)

    def larger_child_index(self, indexes):

        if (not self.in_bounds(index=indexes['rc_index']) or
                self.data[indexes['rc_index']] < self.data[indexes['lc_index']]):
            return indexes['lc_index']
        else:
            return indexes['rc_index']


heap = Heap(root=42)
heap.insert(21)
heap.insert(22)
heap.insert(100)
heap.insert(4)
heap.insert(41)
heap.insert(105)
heap_data = heap.data
print(heap_data)

deleted_value_1 = heap.delete()
print(f"Deleted value: {deleted_value_1}")
heap_data_after_deletion_1 = heap.data
print(heap_data_after_deletion_1)

deleted_value_2 = heap.delete()
print(f"Deleted value: {deleted_value_2}")
heap_data_after_deletion_2 = heap.data
print(heap_data_after_deletion_2)
