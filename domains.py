import read

#read in the data
data = read.load_data()

#create a function to remove subdomains
def remove_sub(url):
    split_url = str(url).split('.')
    x = len(split_url) - 1
    if (split_url[x-1] + '.' + split_url[x]) == 'nytimes.com':
        return 'nytimes.com'
    elif (split_url[x-1] + '.' + split_url[x]) == 'co.uk':
        domain = split_url[x-2] + '.' + split_url[x-1] + '.' + split_url[x]
        return domain
    elif len(split_url) == 3:
        domain = split_url[1] + '.' + split_url[2]
        return domain
    elif len(split_url) == 4:
        domain = split_url[1] + '.' + split_url[2] + '.' + split_url[3]
        return domain
    else:
        return url

#remove subdomains from url
data['domain'] = data['url'].apply(remove_sub)

#generate the counts for each of the domain, and sort from highest occurence to the least
all_domain = data['domain'].value_counts().sort_values(ascending=False)

#obtain the top 100 and print them all
top100_domain = all_domain[0:100]
for name,row in top100_domain.items():
    print('{0}: {1}'.format(name,row))