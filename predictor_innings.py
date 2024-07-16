import pandas as pd
import csv
import re
import numpy as np

def read_input_file(file_name):
    """Reads the input file and returns relevant information."""
    df = pd.read_csv(file_name)
    with open(file_name) as f:
        csv_reader = csv.reader(f)
        venue = df.iloc[0, 0]
        innings = df.iloc[0, 1]
        batting_team = df.iloc[0, 2]
        bowling_team = df.iloc[0, 3]
    return venue, innings, batting_team, bowling_team

def calculate_wickets(samples):
    """Calculates the number of wickets based on the batsmen names."""
    my_regex = re.compile(",(?!\d)|(?<!\d),")
    return len(my_regex.split(samples)) - 2

def assign_venue_value(venue):
    """Assigns numerical values to venues."""
    venue_mapping = {
        'M Chinnaswamy Stadium': 4,
        'Wankhede Stadium': 2,
        'Eden Gardens': 3,
        'Sardar Patel Stadium, Motera': 6,
        'Narendra Modi Stadium, Motera': 6,
        'Feroz Shah Kotla': 5,
        'Arun Jaitley Stadium': 5,
        'MA Chidambaram Stadium': 1,
        'Chepauk': 1
    }
    return venue_mapping.get(venue, None)

def assign_team_value(team_name):
    """Assigns numerical values to teams."""
    team_mapping = {
        'Chennai Super Kings': 1,
        'Mumbai Indians': 2,
        'Kings XI Punjab': 3,
        'Kolkata Knight Riders': 4,
        'Sunrisers Hyderabad': 5,
        'Delhi Capitals': 6,
        'Royal Challengers Bangalore': 7,
        'Rajasthan Royals': 8
    }
    return team_mapping.get(team_name, None)

def calculate_runs(venue, innings, batting_team, bowling_team, wickets, bowlers):
    """Calculates predicted runs based on various factors."""
    # Constants for the calculation
    theta = 45.83889695
    venue_n = -0.18498
    innings_n = -0.09977
    batting_team_n = 0.19621
    bowling_team_n = -0.36783
    wickets_n = -3.84341
    bowlers_n = 3.702172166
    mu1 = 3.193033382
    mu2 = 1.528301887
    mu3 = 4.343976778
    mu4 = 4.345428157
    mu5 = 1.425253991
    mu6 = 3.493468795
    s1 = 1.460391075
    s2 = 0.554707802
    s3 = 2.277122542
    s4 = 2.27913568
    s5 = 1.11046854
    s6 = 0.768398941

    # Venue-specific adjustment
    venue_m = (venue - mu1) * venue_n / s1
    # Innings-specific adjustment
    innings_m = (innings - mu2) * innings_n / s2
    # Batting team-specific adjustment
    batting_team_m = (batting_team - mu3) * batting_team_n / s3
    # Bowling team-specific adjustment
    bowling_team_m = (bowling_team - mu4) * bowling_team_n / s4
    # Wickets-specific adjustment
    wickets_m = (wickets - mu5) * wickets_n / s5
    # Bowlers-specific adjustment
    bowlers_m = (bowlers - mu6) * bowlers_n / s6

    # Final run calculation
    runs = theta + venue_m + innings_m + batting_team_m + bowling_team_m + wickets_m + bowlers_m
    return int(runs)

def main():
    inputFile = 'inputFile.csv'
    venue, innings, batting_team, bowling_team = read_input_file(inputFile)
    venue_value = assign_venue_value(venue)
    batting_team_value = assign_team_value(batting_team)
    bowling_team_value = assign_team_value(bowling_team)
    wickets = calculate_wickets(df['batsmen'].values)
    bowlers = calculate_wickets(df['bowlers'].values)
    prediction = calculate_runs(venue_value, innings, batting_team_value, bowling_team_value, wickets, bowlers)
    print(prediction)

if __name__ == "__main__":
    main()
