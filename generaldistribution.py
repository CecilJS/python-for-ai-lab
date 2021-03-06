class Distribution:
    """
    Generic distribution class for calculating and visualizing a probability distribution.

    Attributes:
        mean: float. The mean value of the distribution.
        stdev: float. The standard deviation of the distribution.
        data_list: list of floats. A list of floats extracted from the data file.
    """
    def __init__(self):
        pass


    def read_data_file(self, file_name):
        """
        Function to read in data from a txt file. 
        The txt file should have one number (float) per line. 
        The numbers are stored in the data attribute.
                
        Args:
            file_name: str. Name of a file to read from
        
        Returns:
            None
        """
        with open(file_name) as file:
            data_list = []
            line = file.readline()
            while line:
                data_list.append(int(line))
                line = file.readline()

        file.close()
        self.data = data_list
