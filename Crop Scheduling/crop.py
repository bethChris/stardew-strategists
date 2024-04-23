import math


# Crop contains
# - name
# - pricing info/methods
# - tending methods
#   - water
#   - harvest
#   - duplicate

class Crop:
    def __init__(self, name, intro_day, harvest_rate, days_to_grow, regrow_days, buy_price, sell_price):
        self.name = name
        self.intro_day = intro_day
        self.harvest_rate = harvest_rate
        self.days_to_grow = days_to_grow 
        self.regrow_days = regrow_days
        self.buy_price = buy_price
        self.sell_price = sell_price
        self.days_grown = 0

        self.total_sold_for = (harvest_rate * sell_price)
        self.initial_profit = self.total_sold_for - buy_price
        
        self.profit_per_grow_day = (self.initial_profit) / days_to_grow  
        self.profit_per_regrow_day = ((self.total_sold_for) / regrow_days) if regrow_days else 0

        self.regrow_periods_to_break_even = max(math.ceil((buy_price - (harvest_rate * sell_price))  / (harvest_rate * sell_price)), 0)
        self.total_regrow_days_to_break_even = self.regrow_days * self.regrow_periods_to_break_even

        self.seasonal_profit = self.calculate_season_profit()


    def calculate_season_profit(self, harvest_days=27):
        # season days -1 since we can get growth on day 28 but can't harvest the next day
        if self.regrow_days:
            period = harvest_days - self.days_to_grow # how many regrowable days there are
            regrow_profit = (((period // self.regrow_days) * self.harvest_rate) * self.sell_price)
            return (regrow_profit + self.total_sold_for) - self.buy_price
        else:
            # calculate how many grow times we can have.abs
            times_grown = harvest_days // (self.days_to_grow)
            return self.initial_profit * times_grown
    

    def calculate_current_season_profit(self, days_left):
        if days_left < self.days_to_grow:
            return 0
        else:
            return self.calculate_season_profit(days_left)


    def calculate_current_profit_per_day(self, days_left):
        if days_left < self.days_to_grow:
            return 0
        else:
            return self.calculate_season_profit(days_left) / days_left


    def water(self):
        self.days_grown += 1
        

    def harvest(self):
        if self.days_grown >= self.days_to_grow:
            if self.regrow_days:
                if (self.days_grown - self.days_to_grow) % self.regrow_days == 0:
                    return self.total_sold_for
            else:
                self.days_grown = 0
                return self.total_sold_for
        return 0
    

    def duplicate(self):
        return Crop(self.name, self.intro_day, self.harvest_rate, self.days_to_grow, self.regrow_days, self.buy_price, self.sell_price)


    def __str__(self):
        if self.regrow_days:
            regrow_tally = ((self.days_grown - self.days_to_grow) % self.regrow_days)
            regrow_tally = self.regrow_days if regrow_tally == 0 else regrow_tally
            regrown_days = regrow_tally if self.days_grown > self.days_to_grow else 0
            return f"{self.name}({self.days_grown}/{self.days_to_grow}) regrow: ({regrown_days}/{self.regrow_days})"
        return f"{self.name}({self.days_grown}/{self.days_to_grow})"
