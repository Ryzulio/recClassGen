try:
    class Atrribute_Archetype_Generator:
        
        def __init__(self, x, y):
            self.min =x
            self.max = y
        
        def attribute_generator(self):
            self.min = 0
            return str(self.__class__) + ": " + str(self.min)
        
        
            
    test = Atrribute_Archetype_Generator(5,10)

    print(test)
except Exception as e:
    print(e)