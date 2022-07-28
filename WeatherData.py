# import re
class WeatherData:
    """This Data class is used to load the data from files and populate them in lists for processing"""
    def __init__(self):
        """Constructor id used for initializing two lists"""
        self.names = []
        self.values = []

    def type_caster(self, value):
        """type_caster is used for type cast any variable to float if possible

        Args:
            value ([any]): [variable send for typecasting]

        Returns:
            [float | None]: [ as per conditions ]
        """    
        try:
            return float(value)
        except:
            return None
    
    def populate_values(self, search_able_files, folder_dir):
        """populate_values is used for read the required files and populate them in lists
        Args:
            search_able_files ([str]): [all file names that is going to be searched]
        """   
        flag = False   # For only reading the header of file 
        for file_name in search_able_files:
            path = '{}/weatherfiles/{}'.format(folder_dir, file_name)  # Make the file_path that is populated
            f = open(path, 'r').readlines()
            for temp_line in f:
                line = temp_line.rstrip('\n')
                if flag == False:
                    self.names.extend(line.split(','))                # Get the header of file and save in list  
                    flag = True
                else:
                    temp_list = [el for el in line.split(',')]        # Make temp list for splitting each row of file on base of comma
                    temp_list2 = []
                    for i, val in enumerate(temp_list):               
                        if i == 0:
                            temp_list2.append(val)                   # For saving year number in str format in start of each list 
                        else:
                            temp_list2.append(self.type_caster(val)) # Call type_caster for change variable data type str to float
                    self.values.append(temp_list2)                   # Append the temporary list in origional list
            # break
    