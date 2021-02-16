

import random
# 1. Create a function named get_year_born which accepts nothing (has no parameters) and
# prompts the user for the year they were born. This function needs to return an integer
# representation of the user’s response.

# 2. Create a function named get_number_to_show which accepts nothing and prompts the
# user for the number of date and time pairs to show. This function needs to return an
# integer representation of the user’s response.

# 3. Create a function named get_random_time which accepts nothing and returns a string
# representation of a random time in 24-hour format. The time must be between 00:00 and
# 23:59 (inclusive).

# birth_year = input("What year were you born?")
# number_of_dates = input("How many date/times should I show?")

def get_year_born():
    """prompts for and returns users birth year as int """
    birth_year = int(input("What year were you born?"))
    return birth_year
#print("blah blah blah: ", get_year_born())
year_to_use = get_year_born()


needed_times = int(input("How many date/times should I show?"))
def get_number_to_show():
    """returns users prompted number of date/time pairs as ints"""
    numbers_to_show = needed_times
    return numbers_to_show
#print("blah blah blah: ",  second_value)


def get_random_time():
    """returns a random time in 24hour format"""
    random_hours = str(random.randrange(24)).zfill(2)   
    random_minutes = str(random.randrange(60)).zfill(2) 
    concat_random = random_hours + ":" + random_minutes
    return concat_random   


a_random_time = get_random_time()


def get_random_date(year_for_date):
    """Gives a random date MM/DD/YYYY using prompted user birthdate"""
    random_month = str(random.randrange(1, 13)) .zfill(2)
    random_day = str(random.randrange(1, 29)) .zfill(2)
    a_random_date = random_month + "/" + random_day + "/" + str(random.randrange(year_for_date + 1, 2021))
    return a_random_date


print("Here are some possible times in your life:\n"
      "Date\t\t\t\tTime")
for date in range(1, get_number_to_show()+1):
     value_one = str((get_random_date(year_to_use)))
     value_two = str(get_random_time())
     print(value_one + "\t\t\t" + value_two)
# had to call upon "year_to_use" because the value will always be
# what is returned from get_year_born. previously, the line "value = get_random_date(get_year_born())"
# was used. However, because we were invoking the function EVERYtime the loop invoked it in the range
# (instead of invoking its result) "What year were you born?" was asked for every range in loop
