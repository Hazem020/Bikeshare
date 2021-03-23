import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }
MONTHS = ['january', 'february', 'march', 'april', 'may', 'june']
DAYS = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday' ]

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    
    #get user input for city.
    city = input("whould you like to see data for Chicago, New York or Washington \n").lower()
    while(city not in CITY_DATA):
        print('please enter a valid city') 
        city  = input("whould you like to see data for Chicago, New York or Washington \n").lower()

    #get user input for month.
    month = input('Whcich month? (all, january, february, ... , june) \n').lower()
    while(month != 'all' and month not in MONTHS):
        print('please enter a valid month') 
        month = input('Whcich month? (all, january, february, ... , june) \n').lower()
            
    #get user input for day of week.
    day = input('Whcich day? (all, monday, tuesday, ... sunday) \n')
    while(day != 'all' and day not in DAYS):
        print('please enter a valid month') 
        day = input('Whcich day? (all, monday, tuesday, ... sunday) \n')
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
    df = pd.read_csv(CITY_DATA[city])    
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['Start Time'] = df['Start Time'].dt.hour
    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        month = MONTHS.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    #display the most common month
    print('most common month: ', MONTHS[df['month'].mode()[0] - 1])

    #display the most common day of week
    print('most common day of week: ' , df['day_of_week'].mode()[0])

    #display the most common start hour
    print('most common start hour: ', df['Start Time'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    #display most commonly used start station
    print('most commonly used start station: ', df['Start Station'].mode()[0])

    #display most commonly used end station
    print('most commonly used end station: ', df['End Station'].mode()[0])

    #display most frequent combination of start station and end station trip
    print("most commonly used start station and end station:", pd.DataFrame(df['Start Station'] + " , " + df['End Station']).mode()[0][0])
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    #display total travel time
    print("Total travel time :", df['Trip Duration'].sum())

    #display mean travel time
    print("Mean travel time :", df['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    #Display counts of user types
    print("Counts of user types:\n")
    for index, count in enumerate(df['User Type'].value_counts()):
        print(df['User Type'].value_counts().index[index], count)

    print()
    try:
        #Display counts of gender
        print("Counts of Gender types:\n")
        for index, count in enumerate(df['Gender'].value_counts()):
            print(df['Gender'].value_counts().index[index], count)
    except:
        print("\nThere is no 'Gender' column in this file.")
    try:
        #Display earliest, most recent, and most common year of birth
        print("earliest year of birth: " ,int(df['Birth Year'].min()))
        print("most recent year of birth: " ,int(df['Birth Year'].max()))
        print("most common year of birth: " ,int(df['Birth Year'].mode()[0]))
    except:
        print("\nThere is no 'birth year' column in this file.") 
       
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def display_data(df):
    """Displays 5 rows of data.
    Args:
        param1 (df): The data frame you are working with.
    """
    
    row = 0
    while True:
        viewData = input('\nWould you like to see some raw data? Enter yes or no.\n')
        if viewData.lower() == 'yes':
            print(df[row:row+5])
            print('-'*40)
            row = row+5
        else:
            break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df) 
        display_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
