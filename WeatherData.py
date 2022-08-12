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
    
    def populate_values(self, searchable_files, folder_dir):
        """populate_values() is used for read the required files and populate them in lists

        Args:
            search_able_files ([str]): [all file names that is going to be searched]
            folder_dir (path): folder path where the weather files are place
        """       
        flag = False   # For only reading the header of file 
        for file_name in searchable_files:
            path = '{}/weatherfiles/{}'.format(folder_dir, file_name)  # Make the file_path that is populated
            f = open(path, 'r').readlines()
            for eachline in f:
                line = eachline.rstrip('\n')
                if flag == False:
                    self.names.extend(line.split(','))                # Get the header of file and save in list  
                    flag = True
                else:
                    comma_split_list = [el for el in line.split(',')]        # Make temp list for splitting each row of file on base of comma
                    appended_list = []
                    for i, val in enumerate(comma_split_list):               
                        if i == 0:
                            appended_list.append(val)                   # For saving year number in str format in start of each list 
                        else:
                            appended_list.append(self.type_caster(val)) # Call type_caster for change variable data type str to float
                    self.values.append(appended_list)                   # Append the temporary list in origional list
            # break
    