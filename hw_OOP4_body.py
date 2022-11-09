from hw_OOP4 import Animal,_Tiger,Monkey,Wolf
Animal1 = Animal("Лев","Мужчина","Взрослый уже")
Animal1.hello()
Animal1.Sex()
Animal1.Age()
Tiger1 = _Tiger("Тигр","Мужчина",'малой') # пример protected инкапсуляции
Tiger1.hello()
Tiger1.Sex()
Tiger1._run() # пример protected инкапсуляции
Monkey1 = Monkey("Обезьяна",'девочка',"В самом рассвете сил")
Monkey1.hello()
Monkey1.Sex()
Monkey1.Age()
Monkey1.habitat()
Wolf1 = Wolf("Волк",'пацан',"Еще может удивить")
Wolf1.hello()
Wolf1.Sex()
Wolf1.Age()
Wolf1.mult()