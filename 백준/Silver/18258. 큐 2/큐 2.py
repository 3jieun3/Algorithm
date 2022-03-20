import sys
input = sys.stdin.readline

class MyQueue:
	def __init__(self):
		self.q = []
		self.frnt = 0
		self.rear = 0

	def push(self, x):
		self.q.append(x)
		self.rear += 1

	def pop(self):
		if self.rear != self.frnt:
			self.frnt += 1
			return self.q[self.frnt - 1]
		return -1

	def size(self):
		return self.rear - self.frnt

	def empty(self):
		if self.rear != self.frnt:
			return 0
		return 1

	def front(self):
		if self.rear != self.frnt:
			return self.q[self.frnt]
		return -1

	def back(self):
		if self.rear != self.frnt:
			return self.q[self.rear - 1]
		return -1


Q = MyQueue()
N = int(input())
for _ in range(N):
	command = input()
	if 'push' in command:
		Q.push(int(command.split()[-1]))
	elif 'pop' in command:
		print(Q.pop())
	elif 'size' in command:
		print(Q.size())
	elif 'front' in command:
		print(Q.front())
	elif 'back' in command:
		print(Q.back())
	else:
		print(Q.empty())