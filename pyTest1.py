class Employee:
	""" Common base class for all employees """
	empCount = 0
	def __init__(self, name, salary, age):		
		self.name = name
		self.salary = salary
		self.age = age		
		Employee.empCount=Employee.empCount+1
		self.empId = Employee.empCount
	
	def displayCount(self):
		print "Total Employee %d" % Employee.empCount
		
	def displayEmployee(self):
		print "Name"+self.name+"Emp Id :"+str(self.empId)+"Age :"+str(self.age)+"Salary :"+str(self.salary)
		
	
	
	
