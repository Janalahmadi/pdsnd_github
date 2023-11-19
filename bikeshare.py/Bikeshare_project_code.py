import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }


def get_filters():
    print('Hello! Let\'s explore some US bikeshare data!')

        # to get user input for city 

    while True:
        cities=['chicago','new york city','washington']
        city=str(input('select a city . \n')).lower()
        if city not in cities:
            print ('invalid city name')
        else:
            break

        # to get user input for month 
        
    while True:
        months=['all','january','february','march','april','may','june','july','august','septemper','october','november','december']
        month=str(input('select a month to filter by month, or type all for all months \n')).lower()
        if month not in months:
            print ('invalid month name')
        else:
            break

        # to get user input for day of week
         
    while True:
        days=['all','Saturday','sunday','monday','tuesday','wednesday','thursday','friday']
        day=str(input('select a day to filter by day,or type all for all days \n')).lower()
        if day not in days:
            print ('invalid day name')
        else:
            break
        
    print('-'*40)
    return city, month, day

        # load data function

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

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

        #Filter by month

    if month != 'all':
       months =['all','january','february','march','april','may','june','july','august','septemper','october','november','december']
       month = months.index(month)
       df=df[df['month'] == month]

        #Filter by day of week

    if day != 'all':
       df=df[df['day_of_week'] == day.title()]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day


    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month

    months=['all','january','february','march','april','may','june','july','august','septemper','october','november','december']
    all_months='all'
    if months==all_months:
    
     month_mode = df['months'].mode()
     print('The most common month is:{}'.format(month_mode-1))
  
    # display the most common day of week

     print('The most common day:{}'.format(df['day_of_week'].mode()))
 
    # display the most common start hour

     df['hour'] = df['Start Time'].dt.hour
     print('The most common start time: {}'.format(df['hour'].mode()))


     print("\nThis took %s seconds." % (time.time() - start_time))
     print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station

    most_used_start_statin= df['Start Station'].mode()
    print('The most commonly used start station is: {}'.format(most_used_start_statin))


    # display most commonly used end station

    most_used_end_statin= df['End Station'].mode()
    print('The most commonly used end station is:{}'.format(most_used_end_statin))


    # display most frequent combination of start station and end station trip

    df['combination'] = df['Start Station'] + ' ' + 'to' + ' ' + df['End Station']
    most_frequent_combination= df['combination'].mode()
    print('The most frequent combination is {}'.format(most_frequent_combination))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()


    # display total travel time

    total_m, total_s = divmod(df['Trip Duration'].sum(),60)
    total_h, total_m = divmod(total_m, 60)
    print('The total travel time is: ',total_h, 'hours',total_m, 'minutes,and' ,total_s, 'seconds')

    # display mean travel time

    mean_m, mean_s = divmod(df['Trip Duration'].sum(),60)
    mean_h, mean_m = divmod(mean_m, 60)
    print('The mean travel time is: ',mean_h, 'hours',mean_m, 'minutes ,and' ,mean_s, 'seconds')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types

    user_type = df['User Type'].value_counts()
    print('The user Types are \n', user_type)


    # Display counts of gender

    if ('Gender' not in df):
        print('Data unavailable for Washington')
    else:
        print('The gender are \n{}'.format(df['Gender'].value_counts()))


    # Display earliest, most recent, and most common year of birth

    if ('Birth Year' not in df):
        print('Data unavailable for Washington')
    else:
        print('The earliest birth year is:{}'.format(df['Birth Year'].min()))
        print('The most recent birth year is:{}'.format(df['Birth Year'].max()))
        print('The most common birth year is:{}'.format(df['Birth Year'].mode()))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

     #to view raw data

def view_date(df):
        start=0
        choice=input('\n Enter yes if you want to view data.\n')
        while choice=='yes':
             try:
                 n=int(input('Enter the rows number\n'))
                 n=start+n
                 print(df[start:n])
                 choice=input('to view more rows enter yes.\n')
                 start=n
             except:
              print("An exception occurred")


def main():
    while True:
        city, month, day = get_filters()
        print(city, month, day)
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()