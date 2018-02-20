def load_data():
    #read in data and assign column names
    import pandas as pd
    data = pd.read_csv('hn_stories.csv')
    data.columns = ['submission_time','upvotes','url','headline']
    return data

    #check if the script is ran directly and notify user that it's being ran
    if __name__ == "__main__":
        print('Running script: read.py')
        load_data()
        print('Data loaded:')
        print(data.head(5))