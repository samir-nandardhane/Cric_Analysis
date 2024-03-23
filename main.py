from ipl_parser import IPLParser
from  cricket_data_processor import CricketDataProcessor

Input_Filepath = 'D:\\Datasets\\IPL_2024\\RCB VS CSK'
Output_FilePath = 'D:\\Datasets\\IPL_2024\\Data Files'
stadium = 'MA Chidambaram Stadium, Chepauk, Chennai'

parser = IPLParser(Input_Filepath, Output_FilePath, stadium)

data = parser.getMatchData()

cric_process = CricketDataProcessor(data)

print(cric_process.process_cricket_data().head(10))