# Season contains
# - crops
# - days
# - sell days
# - increment day

class Season:
    def __init__(self, name, crops, field_size, no_sell_days=[4,11,18,25]):
        self.name = name
        self.crops = crops
        self.days = 28
        self.sell_days = [True for _ in range(28)]
        for day in no_sell_days:
            self.sell_days[day-1] = False
        
        self.current_day = 1


    def get_crops(self):
        return self.crops


    def sell_day(self):
        return self.sell_days[self.current_day-1]
    
    
    def next_day(self):
        self.current_day += 1
