import os
import re
import pandas as pd
from bs4 import BeautifulSoup


class IPLParser:
    def __init__(self, input_filepath, output_filepath, venue,match_number):
        self._input_filepath = input_filepath
        self._output_filepath = output_filepath
        self._venue = venue
        self._match_number = match_number
        self._file1 = self._get_File(flag=1)
        self._file2 = self._get_File(flag=0)
        self._team1 = self._extract_team_name(self._file1)
        self._team2 = self._extract_team_name(self._file2)

        # Define Data
        self._pattern_span = r'<span class="ds-text-tight-s ds-font-regular ds-mb-1 lg:ds-mb-0 lg:ds-mr-3 ds-block ds-text-center ds-text-typo-mid1">(.*?)<\/span>'
        self._pattern_div = r'<div class="ds-leading-none ds-mb-0.5"><span>(.*?)<\/span><\/div>'
        self._pattern_div_new = r'<div class="[^"]*">(<span>[^<]*</span>)</div>'
        self._pattern_comment = r'<p class="ci-html-content">(.*?)<\/p>'

    def _getDatafromHtml(self, soupe):
        overs = []
        ball_details = []
        comments = []
        batter_bowler = []
        text = soupe.find_all('div', class_='lg:hover:ds-bg-ui-fill-translucent ds-hover-parent ds-relative')
        for x in text:
            try:
                overs.append(re.search(self._pattern_span, str(x), re.DOTALL).group(1).strip())
                ball_details.append(re.search(self._pattern_div_new, str(x), re.DOTALL).groups())
                comments.append(re.search(self._pattern_comment, str(x), re.DOTALL).group(1).strip())
                batter_bowler.append(re.search(self._pattern_div, str(x), re.DOTALL).group(1).strip())
            except Exception as e:
                comments.append("No commentary")

        data = {
            'overs': overs,
            'ball_details': ball_details,
            'comments': comments,
            'batter_bowler': batter_bowler
        }

        return pd.DataFrame(data)

    def _parse_html(self, filename, encoding='utf-8'):
        with open(filename, 'r', encoding=encoding) as f:
            soup = BeautifulSoup(f, 'html.parser')
        return soup

    def _includeInng(self, data, innings, venue,team,match_number):
        if innings == 1:
            return data.assign(innings=innings, venue=venue, team=team, match_number=match_number)
        else:
            return data.assign(innings=innings, venue=venue, team=team,match_number=match_number)

    def _getData(self, filename, innings, venue,team,match_number):
        data = self._getDatafromHtml(self._parse_html(filename))
        return self._includeInng(data, innings, venue,team,match_number)

    def getMatchData(self):
        df = pd.concat(
            [
                self._getData(self._file1, 1, self._venue,self._team1,self._match_number),
                self._getData(self._file2, 2, self._venue,self._team2,self._match_number)
            ],
            ignore_index=True
        )
        return df

    def _get_File(self, flag):
        os.chdir(self._input_filepath)
        if flag == 1:
            return [file for file in os.listdir() if (file.endswith(".html") and file.startswith('First_Innings'))][0]
        else:
            return [file for file in os.listdir() if (file.endswith(".html") and file.startswith('Second_Innings'))][0]

    def writeDataToFile(self, filename):
        os.chdir(self._input_filepath)
        self.getMatchData().to_csv(os.path.join(self._output_filepath, filename), index=False,)

    def _extract_team_name(self,input_string):
        words = input_string.split('_')
        team_name = words[-1].split('.')[0]
        return team_name

