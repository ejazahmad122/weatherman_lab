import re
from ShowResult import ShowResult

class DataProcessing:
    """This class calculates different reports"""
    def __init__(self, data):
        """constructor for class DataProcessing which calculates different reports

        Args:
            data ([str]): [required data on which we do processing ]
        """
        self.max_temperature_index = data.names.index('Max TemperatureC')
        self.min_temperature_index = data.names.index('Min TemperatureC')
       
    def calculate_min_max(self, data):
        """Calculate the highest, lowest temprature respectively and most humidity 

        Args:
            data ([list]): [required data on which we do processing ]

        Returns:
            [Results]: [result storage class]
        """
        self.max_humidity_index = data.names.index('Max Humidity')

        max_temprature = max([(sublist[self.max_temperature_index], sublist[0]) for sublist in data.values if sublist[self.max_temperature_index] is not None])
        min_temprature = min([(sublist[self.min_temperature_index], sublist[0]) for sublist in data.values if sublist[self.min_temperature_index] is not None])
        max_humidity = max([(sublist[self.max_humidity_index], sublist[0]) for sublist in data.values if sublist[self.max_humidity_index] is not None])
        return ShowResult(max_temprature, min_temprature, max_humidity)

    def calculate_average_values(self, data):
        """Calculate the highest, lowest avarage temprature respectively and average mean humidity 

        Args:
            data ([list]): [required data on which we do processing ]

        Returns:
            [Results]: [result storage class]
        """
        self.mean_humidity_index = data.names.index(' Mean Humidity')

        max_temprature = ([sublist[self.max_temperature_index] for sublist in data.values if sublist[self.max_temperature_index] is not None])
        avg_max_temprature = sum(max_temprature)/len(max_temprature)

        min_temprature = ([sublist[self.min_temperature_index] for sublist in data.values if sublist[self.min_temperature_index] is not None])
        avg_min_temprature = sum(min_temprature)/len(min_temprature)

        mean_humidity = ([sublist[self.mean_humidity_index] for sublist in data.values if sublist[self.mean_humidity_index] is not None])
        avg_mean_humidity = sum(mean_humidity)/len(mean_humidity)
        return ShowResult(avg_max_temprature, avg_min_temprature, avg_mean_humidity)
    
    def each_day_temprature_calculate(self, data):
        """Calculate the highest, lowest temprature respectively on each day in month 

        Args:
            data ([list]): [required data on which we do processing ]

        Returns:
            [Results]: [result storage class]
        """
        min_max_temprature = [(i+1, sublist[self.min_temperature_index], sublist[self.max_temperature_index]) for i, sublist in enumerate(data.values) if sublist[self.max_temperature_index] is not None]
        result = ShowResult(chart = min_max_temprature)            
        return result
    