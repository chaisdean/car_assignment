class car(object):
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed =  speed
        self.fuel = fuel
        self.mileage = mileage
        #self.displayall()
        if price > 10000:
            self.tax = .15
        else:
            self.tax = .12
        self.displayall()

    def displayall(self):
        print "your price is: " + str(self.price)
        print "your mph are: " + self.speed
        print "your fuel is: " + self.fuel
        print "your mileage is: " + self.mileage
        print "your taxes are: " + str(self.tax)


sample1 = car(2000, '35mph', 'FULL', '15MPG')
sample2 = car(2000, '5mph', 'NOT FULL', '105MPG')
sample3 = car(2000, '15mph', 'KINDA FULL', '95MPG')
sample4 = car(2000, '25mph', 'FULL', '25MPG')
sample5 = car(2000, '45mph', 'EMPTY', '25MPG')
sample6 = car(20000000, '35mph', 'EMPTY', '15MPG')
