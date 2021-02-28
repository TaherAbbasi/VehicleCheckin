from datetime import datetime
import pandas as pd


def validate_logs(logs, from_date, to_date, absences=None, shifts=None):
    '''validate logs of a vehicle based on its absences and working shifts
    '''
    date_range_dict = {}
    date_list = pd.date_range(start=from_date, end=to_date).tolist()
    for d in date_list:
        pass
