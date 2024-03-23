import re
import pandas as pd
from name_mapping import name_mapping
from number_mapping import number_mapping
from ipl_teams import ipl_teams

class CricketDataProcessor:
    def __init__(self, mydata):
        self.mydata = mydata


    def process_cricket_data(self):
        def get_bowler_batter_outcom(x):
            return re.search(r'(\w+\s?\w*)\s+to', x).group().replace('to','').strip(), re.search(r'to\s+([\w\s]+)', x).group(1), re.search(r'<span>(.*?)<\/span>', x).group(1)

        def get_ball_details(x):
            return re.search(r'<span>(.*?)<\/span>', str(x)).group(1)

        self.mydata[['Bowler', 'Batter', 'Outcome']] = self.mydata['batter_bowler'].apply(lambda x: pd.Series(get_bowler_batter_outcom(x)))
        self.mydata['Runs'] = self.mydata['ball_details'].apply(lambda x: get_ball_details(x))
        self.mydata[['Batter', 'Bowler']] = self.mydata[['Batter', 'Bowler']].replace(name_mapping)

        self.mydata['Runs'] = self.mydata['Runs'].replace(number_mapping)
        self.mydata['Runs'] = self.mydata['Runs'].str.replace('[A-Za-z]', '',regex=True)
        self.mydata['Runs'] = self.mydata['Runs'].apply(lambda x: int(x))

        self.mydata['ball'] = self.mydata['overs'].apply(lambda x: int(x.split('.')[1]))
        self.mydata['over'] = self.mydata['overs'].apply(lambda x: int(x.split('.')[0]))

        self.mydata['team'] = self.mydata['team'].replace(ipl_teams)

        self.mydata.drop(columns=['ball_details', 'batter_bowler', 'overs'], inplace=True)

        self.mydata = self.mydata[['match_number','innings','team', 'over', 'ball', 'Batter', 'Bowler', 'Runs', 'Outcome', 'comments', 'venue']]

        self.mydata.sort_values(by=['innings', 'over', 'ball'], ignore_index=True, inplace=True)

        return self.mydata


