# Months names dictionary
MONTHS = {
    '1':'Jan',
    '2':'Feb', 
    '3':'Mar', 
    '4':'Apr', 
    '5':'May', 
    '6':'Jun', 
    '7':'Jul', 
    '8':'Aug', 
    '9':'Sep', 
    '10':'Oct', 
    '11':'Nov', 
    '12':'Dec'
}

class ShowResult:
    """Results class is used to save result and show them as per required format"""
    def __init__(self,  highest = None, lowest = None, humidity = None, chart = []):
        self.highest = highest         
        self.lowest = lowest
        self.humidity = humidity
        self.chart = chart

    # def chart_set(self,  chart):
    #     """Set the chart list

    #     Args:
    #         chart ([list]): [list that contain tuple of month number max and min temprature respectively]
    #     """
    #     self.chart = chart
    
    def show_min_max(self):
        """Show the highest, lowest temprature respectively and most humidity"""
        highest_day = self.highest[1].split('-')
        lowest_day = self.lowest[1].split('-')
        humidity_day = self.humidity[1].split('-')
        print('\nHighest temperature and day, lowest temperature and day, most humid day and humidity.\n')
        print('Highest: {}C on {} {}'.format(self.highest[0], MONTHS.get(highest_day[1]), highest_day[2]))
        print('Lowest: {}C on {} {}'.format(self.lowest[0], MONTHS.get(lowest_day[1]), lowest_day[2]))
        print('Humidity: {}C on {} {}\n'.format(self.humidity[0], MONTHS.get(humidity_day[1]), humidity_day[2]))

    def show_average_values(self):
        """Show the highest and lowest average temprature respectively and most humidity"""
        print('\nFor given month average highest temperature, average lowest temperature, average mean humidity.\n')
        print('Highest Average: {}C'.format(round(self.highest, 2)))
        print('Lowest Average: {}C'.format(round(self.lowest, 2)))
        print('Average Mean Humidity: {}%\n'.format(round(self.humidity, 2)))

    def each_day_temprature_chart(self, mon, year):
        """Show horizontal bar chart of tempratyre for each day """
        print('\nHorizontal bar charts for the highest and lowest temperature on each day for given month')
        print('{} {}\n'.format(mon, year))
        for el in self.chart:
            max_plus = '+'*int(el[2])+str(el[2])
            min_plus = '+'*int(el[1])+str(el[1])
            print('{} {}C'.format(el[0], max_plus))
            print('{} {}C'.format(el[0], min_plus))
        print('\n')

    def each_day_temprature_colored_chart(self, mon, year):
        """Shop horizontal bar chart of tempratyre for each day in colored form"""
        print('\nHorizontal bar charts for the highest and lowest temperature on each day for given month\n')
        print('{} {}\n'.format(mon, year))
        for el in self.chart:
            max_plus = '\033[91m'+'+'*int(el[2])+'\033[0m'
            min_plus = '\33[34m'+'+'*int(el[1])+'\033[0m'
            print('{} {}{} {}C - {}C'.format(el[0], min_plus, max_plus, el[1], el[2]))
        print('\n')
