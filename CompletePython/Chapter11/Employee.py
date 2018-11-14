class Employee:
	def __init__(self, firstname, lastname, annualsalary):
		self.firstname = firstname
		self.lastname = lastname
		self.annualsalary = annualsalary
		
	def give_raise(self,raiseamount=0):
		if raiseamount == 0:
			self.annualsalary = self.annualsalary + 5000
		else:
			self.annualsalary = self.annualsalary + raiseamount
		
