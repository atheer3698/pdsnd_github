#refactoring branch
import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
       city = input("enter the city do you want to explore(chicago, new york , washington)?").lower()
       if city=="chicago" or city=="new york" or city=="washington":
            break

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
       month = input("enter the month do you want to explore(all, january, february, ... , june)?").lower()
       if month=="january" or month=="february" or month=="march" or month=="april" or month=="may" or month=="june":
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
      day = input("enter the day of week do you want to explore(all, monday, tuesday, ... sunday)?").lower()
      if day=="monday" or day=="tuesday" or day=="wednesday" or day=="thursday" or day=="friday" or day=="saturday" or day=="sunday":
           break

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    #load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    popular_month = df['month'].mode()[0]
    print('the most common month:', popular_month)


    # TO DO: display the most common day of week
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    popular_day_of_week = df['day_of_week'].mode()[0]
    print('the most common day of week:', popular_day_of_week)


    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('Most Popular Start Hour:', popular_hour)


    
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_station=df['Start Station']
    popular_start_station = start_station.value_counts().idxmax()
    print('most commonly used start station:', popular_start_station)


    # TO DO: display most commonly used end station
    end_station=df['End Station']
    popular_end_station = end_station.value_counts().idxmax()
    print('most commonly used end station:', popular_end_station)


    # TO DO: display most frequent combination of start station and end station trip
    popular_start_and_end_station = df[['Start Station', 'End Station']].mode().loc[0]
    print('most frequent combination of start station and end station trip:', popular_start_and_end_station)



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel=df['Trip Duration'].sum()
    print('total travel time:', total_travel)

  

    # TO DO: display mean travel time
    mean_travel=df['Trip Duration'].mean()
    print('mean travel time:', mean_travel)



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('counts of user types:', user_types)


    # TO DO: Display counts of gender
    gender = df['Gender'].value_counts()
    print('counts of gender:', gender)


    # TO DO: Display earliest, most recent, and most common year of birth
    most_recent = df['Birth Year'].max()
    earliest_year = df['Birth Year'].min()
    most_common_year = df['Birth Year'].value_counts().idxmax()
    print("The earliest birth year:",earliest_year,"The most recent birth year:",most_recent,"The most common birth year:", most_common_year)

    view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n').lower()
    if view_data != "no":
         start_loc = 0
         view_display="y"
         while (view_display):
           print(df.iloc[start_loc:5])
           start_loc += 5
           view_display = input("Do you wish to continue?(y,n):").lower()

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        if city!='washington':
          user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
