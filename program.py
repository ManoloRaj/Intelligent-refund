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
        money = str(money)
        print (len(money))
        print (money[0])
        
        #decompose the money into simple decimal number
        
        dec_mon = []
        for j in range(len(money)):
            temp_var = money[j]
            for i in range(len(money)-j-1):
                temp_var = temp_var + "0"

            dec_mon.append(temp_var)
        print (dec_mon)
        return money


if __name__ == "__main__":
    money = Money()
    print(money.getRestOfMoney(700, 67))
    
    print(money.computeIntelligentRest(money.getRestOfMoney(700, 67)))


