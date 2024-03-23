import re
import pandas as pd
from name_mapping import name_mapping
from player_details import player_details
from number_mapping import number_mapping

class CricketDataProcessor:
    def __init__(self, mydata):
        self.mydata = mydata

    def process_cricket_data(self):
        def get_bowler_batter_outcom(x):
            return re.search(r'^\w+', x).group(), re.search(r'to\s+(\w+)', x).group(1), re.search(r'<span>(.*?)<\/span>', x).group(1)

        def get_ball_details(x):
            return re.search(r'<span>(.*?)<\/span>', str(x)).group(1)

        self.mydata[['Bowler', 'Batter', 'Outcome']] = self.mydata['batter_bowler'].apply(lambda x: pd.Series(get_bowler_batter_outcom(x)))
        self.mydata['Runs'] = self.mydata['ball_details'].apply(lambda x: get_ball_details(x))
        self.mydata[['Batter', 'Bowler']] = self.mydata[['Batter', 'Bowler']].replace(name_mapping)

        self.mydata['Batting Style'] = ''
        self.mydata['Bowling Style'] = ''

        for index, row in self.mydata.iterrows():
            batter_name = row['Batter']
            bowler_name = row['Bowler']

            if batter_name in player_details:
                self.mydata.loc[index, 'Batting Style'] = player_details[batter_name]['batting_side']
            if bowler_name in player_details:
                self.mydata.loc[index, 'Bowling Style'] = player_details[bowler_name]['bowling_side']

        self.mydata['Runs'] = self.mydata['Runs'].replace(number_mapping)
        self.mydata['Runs'] = self.mydata['Runs'].str.replace('[A-Za-z]', '',regex=True)
        self.mydata['Runs'] = self.mydata['Runs'].apply(lambda x: int(x))

        self.mydata['ball'] = self.mydata['overs'].apply(lambda x: int(x.split('.')[1]))
        self.mydata['over'] = self.mydata['overs'].apply(lambda x: int(x.split('.')[0]))

        self.mydata.drop(columns=['ball_details', 'batter_bowler', 'overs'], inplace=True)

        self.mydata = self.mydata[['innings', 'over', 'ball', 'Batter', 'Bowler', 'Runs', 'Outcome', 'Batting Style', 'Bowling Style', 'comments', 'venue']]

        self.mydata.sort_values(by=['innings', 'over', 'ball'], ignore_index=True, inplace=True)

        return self.mydata
