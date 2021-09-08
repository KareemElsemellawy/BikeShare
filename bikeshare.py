import time
import pandas as pd
import numpy as np

CITY_DATA = { 'Chicago': 'C://Users/Hi55/Downloads/chicago.csv',
              'New York City': 'C://Users/Hi55/Downloads/new_york_city.csv',
              'Washington': 'C://Users/Hi55/Downloads/washington.csv' }
Months=['January', 'February', 'March', 'April', 'May', 'June', 'all']
days=['Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'all']
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
    city=input('Would you like to see the data for chicago, new york city or washington? ').title()

    # TO DO: get user input for month (all, january, february, ... , june)
    month=input('Which month? January, February, March, April, May, June or all: ').title()
    while month not in Months:
        print('The month you have entered not in options')
        month = input('Which month? January, February, March, April, May, June or all: ').title()


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day=input('Which Day? Saturday, Sunday, Monday, Tuesday, Wednesday, Thursday, Friday or all ').title()
    while day not in days:
        print('The day you have entered not in options')
        day = input('Which Day? Saturday, Sunday, Monday, Tuesday, Wednesday, Thursday, Friday or all ').title()
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
    citynameContinue=True
    while citynameContinue==True:
        try:
            df = pd.read_csv(CITY_DATA[city])
            citynameContinue=False
        except:
            print('You have entered invalid city name.')
            city = input('Would you like to see the data for chicago, new york city, washington? ').title()
            citynameContinue=True
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['Month'] = df['Start Time'].dt.month_name()
    df['Day'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour
    if month != 'all':
        df = df[df['Month'] == month]

        # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['Day'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month

    popular_month = df['Month'].mode()[0]
    print('The most popular month is: '+str(popular_month))

    # TO DO: display the most common day of week

    Popular_Day = df['Day'].mode()[0]
    print('The most popular day is: ' + str(Popular_Day))
    # TO DO: display the most common start hour
    Popular_hour = df['hour'].mode()[0]
    print('The most popular hour is: ' + str(Popular_hour))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    try:
        Popular_Start_Station = df['Start Station'].mode()[0]
        print('The most common start station is: ' + str(Popular_Start_Station))
    except:
        print('Warning, there is no Start Station data for city you have chosen')
    # TO DO: display most commonly used end station
    try:
        Popular_End_Station = df['End Station'].mode()[0]
        print('The most common End station is: ' + str(Popular_End_Station))
    except:
        print('Warning, there is no End Station data for city you have chosen')
    # TO DO: display most frequent combination of start station and end station trip
    try:
        df['StartAndEndStation'] = df['Start Station']+df['End Station']
        Popular_StartEnd_Station = df['StartAndEndStation'].mode()[0]
        print('The most frequent combination of start station and end station trip is:' + str(Popular_StartEnd_Station))
    except:
        print('Warning, there is no Start and End Station data for city you have chosen')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('Total drive time is:'+str(df['Trip Duration'].sum().round(3)))

    # TO DO: display mean travel time
    print('Mean drive time is:' + str(df['Trip Duration'].mean().round(3)))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def view_data(df):
    viewDataInputs=['yes','ye','y','ys']
    view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n')
    start_loc = 0
    end_loc = 5
    while (view_data.lower() in viewDataInputs):
            print(df.iloc[start_loc:end_loc])
            start_loc += 5
            end_loc += 5
            view_data = input("Do you wish to continue?: ").lower()

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    try:
        print('Counts of user types is:' + str(df['User Type'].value_counts()))
    except:
        print('Warning, there is no User Type data for city you have chosen')

    # TO DO: Display counts of gender
    try:
        print('Counts of gender is:' + str(df['Gender'].value_counts()))
    except:
        print('Warning, there is no gender data for city you have chosen')



    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        print('The earliest year of birth is:'+str(df['Birth Year'].min()))
        print('The most recent year of birth is:' + str(df['Birth Year'].max()))
        print('The most common year of birth is:' + str(df['Birth Year'].mode()[0]))
    except:
        print('Warning, the city you have entered does not contain birth year data')
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        view_data(df)
        restartinputs=['yes','ye','y','ys']
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() not in restartinputs:
            break


if __name__ == "__main__":
	main()
