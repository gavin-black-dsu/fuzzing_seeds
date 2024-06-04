import pandas as pd
import uuid
from collections import OrderedDict

class DataLogger:
    _data = []  # Class variable to store each row's data
    _current_row = {}  # Class variable to store the current row's data
    _columns = OrderedDict()  # Tracks encountered column names in order
    _uuid = str(uuid.uuid4()) # Unique ID for the trial for later groupings
    _pause = False # Whether to temporarily ignore new data

    @classmethod
    def pause(cls, pause=True):
        cls._pause = pause
    
    @classmethod
    def add_data(cls, column, value):
        """
        Add data to the current row for a specific column. This is a class method and can be called on the class itself.
        :param column: Column name for the data
        :param value: Value to add to the column
        """
        if cls._pause: return
        cls._current_row[column] = value
        cls._columns[column] = None  # Add column to _columns to track order, value is not used


    @classmethod
    def finish_row(cls):
        """
        Finish the current row by adding a unique ID, then add it to the main data list, and prepare for the next row. This is a class method.
        """
        if cls._pause: return
        
        # Add the trial's UUID to the row
        cls.add_data('Trial UUID', cls._uuid)
        
        # Ensure the current row has all columns, fill missing ones with NaN
        ordered_row = {col: cls._current_row.get(col, pd.NA) for col in cls._columns}
        cls._data.append(ordered_row)
        cls._current_row = {}

    @classmethod
    def create_dataframe(cls, filename=None, html=True):
        """
        Create a pandas DataFrame from the accumulated data. This is a class method and can be called on the class itself.
        Optionally, save the DataFrame to a file if a filename is provided, and rename columns if headers are provided.

        :param filename: Optional; if provided, the DataFrame is saved to this file.
        :return: Pandas DataFrame containing the experiment data
        """
        if cls._pause: return
        df = pd.DataFrame(cls._data, columns=cls._columns.keys())
        
        if filename: df.to_parquet(f"{filename}.parquet", index=False)
        if filename and html: 
            html = f"<style>body {{ color: #ccc; }}</style>\n{df.to_html()}"

            with open(f"{filename}.html", 'w') as file: 
                file.write(html)
        return df

    @classmethod
    def clear(cls, new_uuid=False):
        """
        Clear all stored data from the DataLogger, resetting it to its initial state.
        """
        if new_uuid: cls._uuid = str(uuid.uuid4())
        cls._data = []
        cls._current_row = {}
        cls._columns.clear()
        #cls._uuid = str(uuid.uuid4())