class 吃():
    def 吃飯去(self, 幾次):
        for i in range(幾次):
            print("吃飯去")
 
class 也吃(吃):
    def 吃飯去(self, 幾次):
        for i in range(幾次):
            print("第", i, "次吃飯去")
 
就要吃 = 吃()
就要吃.吃飯去(3)
 
來去吃 = 也吃()
來去吃.吃飯去(3)