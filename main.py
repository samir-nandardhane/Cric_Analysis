from ipl_parser import IPLParser
from  cricket_data_processor import CricketDataProcessor
from player_data import PlayerData


Input_Filepath = 'D:\\Datasets\\IPL_2024\\KKR VS SRH'
Output_FilePath = 'D:\\Datasets\\IPL_2024\\Data Files'
#stadium = 'MA Chidambaram Stadium, Chepauk, Chennai'
stadium = 'Eden Gardens, Kolkata'

parser = IPLParser(Input_Filepath, Output_FilePath, stadium,3)

data = parser.getMatchData()

cric_process = CricketDataProcessor(data)

cric_process.process_cricket_data().to_csv(Output_FilePath+'\\Clean_Data\\KKR_VS_SRH.csv', index=False)
