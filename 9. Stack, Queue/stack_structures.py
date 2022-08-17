class Node:
    def __init__(self, item, next):
        self.item = item #내 값
        self.next = next #가르키는 값


class Stack:
    def __init__(self):
        self.top = None #처음 값은 아직 없음

    def push(self, value):
        self.top = Node(value, self.top) #top을 노드로 지정
				#새로만든 탑 = Node(가진 값, 기존의 탑. 새로만든애가 가르킬 것)

    def pop(self):
        if self.top is None:
            return None

        node = self.top
        self.top = self.top.next

        return node.item

    def is_empty(self):
        return self.top is None