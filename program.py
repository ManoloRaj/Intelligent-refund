#Author : ManoloRaj
#14 july-August 2021
class Money:
    def __init__(self):
        self.list_of_money = [10, 20, 50, 100, 500, 1000, 2000, 5000, 10000, 20000]
        
        #Initialise refun to 0
        self.refund = 0
        self.spacies = []

    def getRestOfMoney(self, money, price) :
        self.refund = price-money
         
    
    def computeIntelligentRest(self):
        money = str(self.refund)
        #decompose the money into simple decimal number
        
        dec_mon = []
        for j in range(len(money)):
            temp_var = money[j]
            for i in range(len(money)-j-1):
                temp_var = temp_var + "0"

            dec_mon.append(int(temp_var))

        self.spacies = dec_mon

    def getSpacies(self):
        return self.spacies

    #Return of number spacies
    def result(self):

        for i in range(len(self.spacies) - 1):
            for j in range(len(self.list_of_money) - 1):
                if (len(str(self.spacies[i+1]))==len(str(self.list_of_money[j+1]))):
                    print(" You need :"+str(self.list_of_money[i+1])+" number of "+str(self.spacies[i+1] / self.list_of_money[i+1])+" Ariary \n")

            else :
                pass

                
if __name__ == "__main__":
    #Create money object
    money = Money()

    #Compute rest
    money.getRestOfMoney(9000, 62)
    #Compute intelligent rest
    money.computeIntelligentRest()

    #print result
    print(money.getSpacies())
    money.result()
