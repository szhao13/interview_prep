from stack import Stack

class MaxStack(object):

	
	def __init__(self):
		self.in_stack = Stack()
		self.max_stack = Stack()
		
	def push(self, item):
		curr_max = self.max_stack.peek()
		# print curr_max
		if not curr_max:
			self.max_stack.push(item)
		else:
			if item >= curr_max:
				self.max_stack.push(item)
		self.in_stack.push(item)

	# if item popped is curr_max, then how do we find the next
	# max in O(1)?	
	def pop(self):
		curr_item = self.in_stack.pop()
		if curr_item == self.max_stack.peek():
			self.max_stack.pop()
		return curr_item
	 
	def peek(self):
		return self.in_stack.peek()
		

	def get_max(self):
		return self.max_stack.peek()
		# curr_max = self.in_stack.peek()
		# if curr_max != None:
		  
		# 	curr_item = self.in_stack.pop()
		# 	while curr_item != None:
		# 		if curr_item > curr_max:
		# 			curr_max = curr_item
		# 		self.out_stack.push(curr_item)
		# 		curr_item = self.in_stack.pop()
		# 	curr_item = self.out_stack.pop()
		# 	while curr_item != None:
		# 		self.in_stack.push(curr_item)
		# 		curr_item = self.out_stack.pop()
		# return curr_max
					
		# Write the body of your function here


# Run your function through some test cases here
# Remember: debugging is half the battle!
in_stack = Stack()
# in_stack.push(25)
# in_stack.push(100)
# in_stack.push(125)

max_stack = MaxStack()

max_stack.push(25)
print max_stack.get_max()
max_stack.push(26)
max_stack.pop()
print max_stack.get_max()
max_stack.push(27)
print max_stack.get_max()
