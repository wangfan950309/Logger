import traceback
import pandas as pd
import time
class logger():
    def __init__(self):
        self.today = time.strftime("%Y-%m-%d %I:%M:%S")
    def to_df(self, file, function, date, type, msg):
        df = pd.DataFrame(data=[[file,
                                 function,
                                 date,
                                 type,
                                 msg]],
                          columns=['File', 
                                    'Function',
                                    'Date',
                                    'Type',
                                    'Message']
        )
        return df
    def info(self, msg):
        traceback = self.get_trace_back()
        func = list(traceback[1])[2]
        file = list(traceback[0])[0].split('/')[-1]
        date = self.today
        df = self.to_df(file, func, date, 'INFO', msg)
        return df
    def get_trace_back(self):
        traceback_ = list(traceback.extract_stack(None, 4))
        return traceback_
    def to_sql(self, df):
        # append the message to some table
        pass