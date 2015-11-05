class employee:
#common base class for all employees
	
	empcount=o
	
	def __init__(self,name,salary):
		self.name = name
		self.salary = salary
		Employee.empCount += 1

	def displayCount(self):
		print "Total Employee %d" % Employee.empCount

	def displayEmployee(self):
		print "name:", self.name, ",salary:", self.salary 
