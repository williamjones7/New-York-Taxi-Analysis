import pandas as pd
import numpy as np

def remove_outliers(df, columns = [None]):
    """Cleans a dataframe to only include data points within three standard deviations of the mean, over given columns [1].
    
    Parameters:
        df (pd.DataFrame):      Pandas dataframe we would like to clean.
        cols (list of strings): List of dataframe headers for which we would like to remove outliers from, 
                                defaulting to every column
    
    Returns:
        df (pd.DataFrame): Cleaned dataframe with outliers removed
    """
    
    # if columns to loop over is not specified, loop over every column
    if columns[0] == None: columns = df.columns
    
    # loop over the columns we would like to remove outliers from
    for col in columns:
        
        # error checking, if the specified column isn't a column of the dataframe, then don't try and clean it
        if col not in df.columns:

            # throw an error but keep looping through anyway
            print(f"column {col} doesn't exist in dataframe")
            continue
        
        # only clean from columns which might contain outliers
        if col in ['trip_distance', 'fare_amount', 'trip_duration',
                   'total_amount', 'trip_miles', 'trip_time', 'base_passenger_fare', 'dura_distan']:
                   
            # find the mean, mu, and standard deviation, sigma, of the column 
            mu = df[col].mean()
            sigma = df[col].std()

            # remove outliers which are outside of three standard deviations of the mean
            df = df[np.abs(df[col]-mu) <= (3*sigma)]

    return df
        
        
def add_trip_duration(df):
    '''Add a trip duration column for yellow or green taxi data'''
    
    # check the column doesn't already exist, if it does just return the dataframe
    if 'trip_duration' in df.columns: return df
    
    # add a trip duration column, which we can remove outliers from, for yellow taxi data
    if ('tpep_pickup_datetime' in df and 'tpep_dropoff_datetime' in df):
        
        # find the trip duration from the difference of the drop off and pick up time, as a timedelta object
        trip_duration = (df['tpep_dropoff_datetime'] - df['tpep_pickup_datetime'])
        
        # convert the trip duration to number of seconds, rounded to the nearest second
        trip_duration = trip_duration / np.timedelta64(1, 's')
        
        # insert the column into the data fram, next to the drop off timestamp column
        df.insert(df.columns.get_loc('tpep_dropoff_datetime') + 1, 'trip_duration', trip_duration)
    
    # add a trip duration column, which we can remove outliers from, for green taxi data
    if ('lpep_pickup_datetime' in df and 'lpep_dropoff_datetime' in df):
        
        # find the trip duration from the difference of the drop off and pick up time, as a timedelta object
        trip_duration = (df['lpep_dropoff_datetime'] - df['lpep_pickup_datetime'])
        
        # convert the trip duration to number of seconds, rounded to the nearest second
        trip_duration = trip_duration / np.timedelta64(1, 's')
        
        # insert the column into the data fram, next to the drop off timestamp column
        df.insert(df.columns.get_loc('lpep_dropoff_datetime') + 1, 'trip_duration', trip_duration)
     
    return df
        
    
def clean_data(df, columns = [None]):
    """Cleans a dataframe of yellow or fhvhv data to only include data points which make valid sense, 
    according to a set of rules, over given columns. 
    
    Then remove any outliers using remove_outliers()
    
    Parameters:
        df (pd.DataFrame):      Pandas dataframe we would like to clean.
        cols (list of strings): List of dataframe headers for which we would like to remove outliers from, 
                                defaulting to every column
    
    Returns:
        df (pd.DataFrame): Cleaned dataframe with outliers removed and rules imposed
    """
    
    # if the columns to clean is not specified, then loop over every column
    if columns[0] == None: columns = df.columns
    
    # add trip duration column
    df = add_trip_duration(df)
        
    # loop over columns to clean
    for col in columns:
        
        # remove any data point which has a type NaN in it
        df = df.dropna(subset=[col])
    
        if col not in df.columns:
            print(f"column {col} doesn't exist in dataframe")
            continue
        
        # ensure we have strictly positive data for these headers
        if col in ['trip_time', 'trip_distance', 'trip_duration', 'trip_miles']: 
            df = df[1< df[col]] 
            
        # ensure we have non-negative data for these headers
        if col in ['fare_amount', 'tip_amount', 'congestion_surcharge', 'total_amount',
                  'base_passenger_fare', 'tolls', 'bcf', 'sales_tax', 'tips', 'driver_pay']:
            df = df[df[col] >= 0] 
                        
        # ensure pick-up and drop-off location IDs are in the correct range [1,263]
        if col in ['PULocationID', 'DOLocationID']: df = df[(1 <= df[col]) & (df[col] <= 263)]
          
        # ensure the number of passengers is non-zero and less than 7 as this is the law [2]
        if col == 'passenger_count': df = df[(1 <= df[col]) & (df[col] <= 6)]
    
        # ensure duration distance ratio is positive
        if col == 'dura_distan': df = df[df['dura_distan'] > 0]
    return df
        
    
def impose_date(df, years, months = [None]):
    """Cleans a dataframe to only include datetime values within the given year and months
    
    Parameters:
        df (pd.DataFrame):               Pandas dataframe we would like to clean.
        years (list of strings or int):  List of years to impose onto the dataset
        months (list of strings or int): List of months to impose onto the dataset, 
                                         defaulting to every month
    
    Returns:
        df (pd.DataFrame): Cleaned dataframe with only the year and month timestamps we want
    """
    
    # get headers of the dataframe
    columns = df.columns
    
    # loop over the columns of the dataframe
    for col in columns:
    
        # check whether the column is a datetime, to impose the date we want on to it
        if df[col].dtypes == 'datetime64[ns]':

            # loop over years we are interested in
            for year in years:
                
                # convert the datetime column to a column of years 
                colyear = pd.DatetimeIndex(df[col]).year
                
                # remove any data that doesn't have the year we want
                df = df[colyear == int(year)]
                
            # loop over months we are interested in 
            for month in months:    

                # if the default is set to None then we don't bother cleaning over the months
                if month == None: continue 
                    
                # convert the datetime column to a column of months
                colmonth = pd.DatetimeIndex(df[col]).month

                # remove any data that doesn't have the month we want
                df = df[colmonth == int(month)]
    
    return df
    
    
# [1]
# AUTHOR NAME: CT Zhu
# URL: https://stackoverflow.com/questions/23199796/detect-and-exclude-outliers-in-a-pandas-dataframe
# 5 Jul 2018
# Accessed on 18 Nov 2022

# [2]
# NYC Taxi and Limousine comission 
# URL: https://www.nyc.gov/site/tlc/passengers/passenger-frequently-asked-questions.page#:~:text=The%20maximum%20amount%20of%20passengers,of%20an%20adult%20passenger%20seated
# Accessed on 26 Nov 2022