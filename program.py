#Author : ManoloRaj
#14 july 2021
class Money:
    def __init__(self):
        self.list_of_money = [10, 20, 50, 100, 500, 1000, 2000, 5000, 10000, 20000]
        #Initialise refun to 0
        self.refund = 0
    def getRestOfMoney(self, money, price) :
        self.refund = price-money
        return money-price 
    
    def computeIntelligentRest(self, money):
        money = []
        for count in range(1,len(self.list_of_money)):
            money = total - self.list_of_money[count]
        return money


if __name__ == "__main__":
    money = Money()
    print(money.getRestOfMoney(700, 67))


