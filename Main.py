import sys
import os
import re
from DataProcession import DataProcessing
from WeatherData import WeatherData

# Month names dictionary
month = {
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

def main():
    """Main function for run the whole code"""
    argv = sys.argv     #Read command line arguments
    filenames = next(os.walk('{}/weatherfiles'.format(argv[1])))[2]      #Reading all the file names from the given folder 
    try:
        for i in range(2, len(argv), 2):        #iterate on arguments for printing required repots
            obj = WeatherData()
            calculate = DataProcessing()
            if argv[i] == '-e':
                search_able_files = [file for file in filenames if re.search(r".{}.".format(argv[i+1]), file)]
                obj.populate_values(search_able_files, argv[1])
                result = calculate.max_min_calculate(obj)
                result.max_min_show()

            elif argv[i] == '-a':
                year_format = argv[i+1].split('/')
                search_able_files = [file for file in filenames if re.search(r".{}_{}.".format(year_format[0], month.get(str(int(year_format[1])))), file)]
                obj.populate_values(search_able_files, argv[1])
                result = calculate.average_values_calculate(obj)
                result.average_values_show()

            elif argv[i] == '-c' or argv[i] == '-b':
                year_format = argv[i+1].split('/')
                search_able_files = [file for file in filenames if re.search(r".{}_{}.".format(year_format[0], month.get(str(int(year_format[1])))), file)]
                obj.populate_values(search_able_files, argv[1])
                result = calculate.each_day_temprature_calculate(obj)
                if argv[i] == '-c':
                    result.each_day_temprature_chart(month.get(str(int(year_format[1]))), year_format[0])
                else:
                    result.each_day_temprature_colored_chart(month.get(str(int(year_format[1]))), year_format[0])

            else:
                print("Please give the correct flag in argument!!")

    except:
        print("\nPlease give correct arguments in required format for complete procession!!\n")
        sys.exit()
   
main()


        

