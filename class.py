# 1. Class defination
class ThisIsMyClass:
    #1. Property

    #2. Constructor

    #3. Method
    def addMyTwoNumbers(self,fa1,fa2):
        result = fa1+fa2
        print(f"The sum of {fa1} and {fa2} is {result}")

#class instantiation / calling
#classObject = ClassName()
co = ThisIsMyClass()

#classObject.method()
co.addMyTwoNumbers(5,5) #actualargument1,actualArgument2
co.addMyTwoNumbers(50,20)
