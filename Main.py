import sys
import os
import re
from DataProcession import DataProcessing
from WeatherData import WeatherData

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

def calculate_and_display_min_max(argv, arg_index, filenames):
    """This function calculate and show the min max temprature 

    Args:
        argv (list): command arguments 
        arg_index (int): flag index
        filenames ([str]): searchable file names
    """
    obj = WeatherData()
    search_able_files = [file for file in filenames if re.search(r".{}.".format(argv[arg_index+1]), file)]
    obj.populate_values(search_able_files, argv[1])
    calculate = DataProcessing(obj)
    result = calculate.calculate_min_max(obj)
    result.show_min_max()

def calculate_and_display_average(argv, arg_index, filenames):
    """This function calculate and show the average temprature and humidity as required month

    Args:
        argv (list): command arguments 
        arg_index (int): flag index
        filenames ([str]): searchable file names
    """
    obj = WeatherData()
    year_format = argv[arg_index+1].split('/')
    search_able_files = [file for file in filenames if re.search(r".{}_{}.".format(year_format[0], MONTHS.get(str(int(year_format[1])))), file)]
    obj.populate_values(search_able_files, argv[1])
    calculate = DataProcessing(obj)
    result = calculate.calculate_average_values(obj)
    result.show_average_values()

def calculate_and_display_eachday_chart(argv, arg_index, filenames):
    """This function calculate and show the eachday temprature in chart form as required month

    Args:
        argv (list): command arguments 
        arg_index (int): flag index
        filenames ([str]): searchable file names
    """
    obj = WeatherData()
    year_format = argv[arg_index+1].split('/')
    search_able_files = [file for file in filenames if re.search(r".{}_{}.".format(year_format[0], MONTHS.get(str(int(year_format[1])))), file)]
    obj.populate_values(search_able_files, argv[1])
    calculate = DataProcessing(obj)
    result = calculate.each_day_temprature_calculate(obj)
    if argv[arg_index] == '-c':
        result.each_day_temprature_chart(MONTHS.get(str(int(year_format[1]))), year_format[0])
    else:
        result.each_day_temprature_colored_chart(MONTHS.get(str(int(year_format[1]))), year_format[0])

def main():
    """Main function for run the whole code"""
    argv = sys.argv     #Read command line arguments
    filenames = next(os.walk('{}/weatherfiles'.format(argv[1])))[2]      #Reading all the file names from the given folder 
    try:
        for i in range(2, len(argv), 2):        #iterate on arguments for printing required repots
            if argv[i] == '-e':
                calculate_and_display_min_max(argv, i, filenames)
            elif argv[i] == '-a':
                calculate_and_display_average(argv, i, filenames)
            elif argv[i] == '-c' or argv[i] == '-b':
                calculate_and_display_eachday_chart(argv, i, filenames)
            else:
                print("Please give the correct flag in argument!!")
    except:
        print("\nPlease give correct arguments in required format for complete procession!!\n")
        sys.exit()
   
main()          #calling  main function