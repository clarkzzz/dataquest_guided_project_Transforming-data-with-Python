import read
from dateutil.parser import parse

#read in the data
data = read.load_data()

#create a function to extract hour from the submission time
def ext_hour(time):
    hour = parse(time).hour
    return hour

data['hour'] = data['submission_time'].apply(ext_hour)

#count the the number of submissions at each hour and print out in descending order
hour_counts = data['hour'].value_counts(sort=True,ascending=False)
print(hour_counts)