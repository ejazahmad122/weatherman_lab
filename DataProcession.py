import re
from ShowResult import ShowReult

class DataProcessing:
    """This class calculate the different reports as per format"""
    def max_min_calculate(self, data):
        """Calculate the highest, lowest temprature resp. and most humidity 

        Args:
            data ([list]): [required data on which we do processing ]

        Returns:
            [Results]: [result storage class]
        """
        self.index1 = data.names.index('Max TemperatureC')
        self.index2 = data.names.index('Min TemperatureC')
        self.index3 = data.names.index('Max Humidity')

        max_temprature = max([(sublist[self.index1], sublist[0]) for sublist in data.values if sublist[self.index1] is not None])
        min_temprature = min([(sublist[self.index2], sublist[0]) for sublist in data.values if sublist[self.index2] is not None])
        max_humidity = max([(sublist[self.index3], sublist[0]) for sublist in data.values if sublist[self.index3] is not None])
        
        return ShowReult(max_temprature, min_temprature, max_humidity)

    def average_values_calculate(self, data):
        """Calculate the highest, lowest avarage temprature resp. and average mean humidity 

        Args:
            data ([list]): [required data on which we do processing ]

        Returns:
            [Results]: [result storage class]
        """

        self.index1 = data.names.index('Max TemperatureC')
        self.index2 = data.names.index('Min TemperatureC')
        self.index3 = data.names.index(' Mean Humidity')

        max_temprature = ([sublist[self.index1] for sublist in data.values if sublist[self.index1] is not None])
        avg_max_temprature = sum(max_temprature)/len(max_temprature)

        min_temprature = ([sublist[self.index2] for sublist in data.values if sublist[self.index2] is not None])
        avg_min_temprature = sum(min_temprature)/len(min_temprature)

        mean_humidity = ([sublist[self.index3] for sublist in data.values if sublist[self.index3] is not None])
        avg_mean_humidity = sum(mean_humidity)/len(mean_humidity)

        return ShowReult(avg_max_temprature, avg_min_temprature, avg_mean_humidity)
    
    def each_day_temprature_calculate(self, data):
        """Calculate the highest, lowest temprature resp. on each day in month 

        Args:
            data ([list]): [required data on which we do processing ]

        Returns:
            [Results]: [result storage class]
        """
        self.index1 = data.names.index('Max TemperatureC')
        self.index2 = data.names.index('Min TemperatureC')

        min_max_temprature = [(i+1, sublist[self.index2], sublist[self.index1]) for i, sublist in enumerate(data.values) if sublist[self.index1] is not None]

        result = ShowReult()            
        result.chart_set(min_max_temprature)

        return result
    