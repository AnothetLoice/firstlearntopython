class Calculator(object):
	"""docstring for Calculator"""
	def calculate(self):
		self.expression=input('please input your expression:')
		self.value=eval(self.expression)
		return self.expression
class Uishow(object):
	"""docstring for Uishow"""
	def expshow(self,expression):
		print(expression,'=',repr(self.value))
class Allofit(Calculator,Uishow):
	def getChar(self):
		self.cun=int(input('"0" to end it or other number to do next expression'))
		return self.cun
cal_1=Allofit()
while True:
	exps=cal_1.calculate();
	cal_1.expshow(exps);
	if cal_1.getChar()==0:
		break;
	