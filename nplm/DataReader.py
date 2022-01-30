import pandas 
import h5py


class DataReader:
    """
    Manages data import from .h5 file to pandas.DataFrame
    
    """
    
    def __init__(self, filename: str):
        """
        Reads data from .h5 file

        Args:
            filename (str): full or relative path to the data file
        """
        
        # store the file name
        self.filename: str = filename
        
        # read hdf keys and store them
        f = h5py.File(self.filename, "r")
        self.keys: list = f.keys()
        
        # build the whole dataset 
        df = pandas.concat(
            [
                pandas.read_hdf(self.filename, key=k, mode="r") for k in self.keys
            ],
            ignore_index=True
        )
        
        # store the dataset with new column names
        self.df : pandas.DataFrame = df.rename(columns={"CH":"ch", "HIT_DRIFT_TIME":"drift_time", "THETA":"theta"})
    
    
    
    def build_sample(self, ndata: int) -> pandas.DataFrame:
        """
        Builds the dataset of ndata samples

        Args:
            ndata (int): dimensionality of the dataset

        Returns:
            df (pandas.DataFrame): dataset
        """
        
        # random data extraction from the whole dataset
        df = self.df.sample(n=ndata)
        
        return df[["drift_time", "theta"]] 

