import pandas as pd
from player_details import player_details


class PlayerData:
    player_details = player_details

    @classmethod
    def get_player_data(cls):
        # Convert player_details into a list of dictionaries
        player_data_list = [{'Name': player, 'Origin': details['Origin'], 'Batting Style': details['batting_side'],
                             'Bowling Style': details['bowling_side']} for player, details in
                            cls.player_details.items()]

        # Create DataFrame from the list of dictionaries
        df = pd.DataFrame(player_data_list)

        return df

# Now you can call PlayerData.get_player_data() anywhere in your code without providing arguments
