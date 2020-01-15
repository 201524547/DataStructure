import sys

class MyQueue:
    def __init__(self):
        self.Item = []
        self.size = 0
        self.head = 0
        self.tail = 0

    def Insert(self, data):
        self.Item.append(data)
        self.head += 1
        self.size += 1

    def Delete(self):
        self.tail += 1
        self.size -= 1

    def is_Empty(self):
        return self.head == self.tail

    def Front(self):
        result = self.Item[self.tail]
        return result

    def Back(self):
        result = self.Item[self.head-1]
        return result

    def Size(self):
        return self.size


if __name__=="__main__":
    n = int(sys.stdin.readline())
    s = MyQueue()

    for i in range (0,n):
        command = sys.stdin.readline().split()
        if command[0] == "pop":
            if s.is_Empty():
                print(-1)
            else :
                print(s.Front())
                s.Delete()
        elif command[0] == "size":
            print(s.Size())

        elif command[0] == "empty":
            if s.is_Empty():
                print(1)
            else:
                print(0)

        elif command[0] == "front":
            if not s.is_Empty():
                print(s.Front())
            else:
                print(-1)

        elif command[0] == "back":
            if not s.is_Empty():
                print(s.Back())
            else:
                print(-1)
        elif command[0] == "push":
            s.Insert(command[1])

