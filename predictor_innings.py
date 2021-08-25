
def predictRuns(inputFile):
    import pandas as pd
    import csv
    import re
    import numpy as np
    df = pd.read_csv('inputFile.csv')
    f = open('inputFile.csv')
    csv_f = csv.reader(f)
    venue = df.iloc[0, 0]
    innings = df.iloc[0, 1]
    batting_team = df.iloc[0, 2]
    bowling_team = df.iloc[0, 3]

    samples = df['batsmen'].values
    myRegex=re.compile(",(?!\d)|(?<!\d),")
    for sample in samples:
        wickets = len(myRegex.split(sample)) - 2

    samples = df['bowlers'].values
    myRegex=re.compile(",(?!\d)|(?<!\d),")

    for sample in samples:
        bowlers = len(myRegex.split(sample))    

    if venue == 'M Chinnaswamy Stadium' or 'M.Chinnaswamy Stadium':
        venue = 4
    elif venue == 'Wankhede Stadium':
        venue = 2
    elif venue == 'Eden Gardens':
        venue = 3
    elif venue == 'Sardar Patel Stadium, Motera' or 'Narendra Modi Stadium, Motera':
        venue = 6
    elif venue == 'Feroz Shah Kotla' or 'Arun Jaitley Stadium':
        venue = 5
    elif venue == 'MA Chidambaram Stadium' or 'Chepauk' or 'MA Chidambaram Stadium':
        venue = 1
    
    # converting batting teams to numbers

    if batting_team == 'Chennai Super Kings':
        batting_team = 1
    elif batting_team == 'Mumbai Indians':
        batting_team = 2
    elif batting_team == 'Kings XI Punjab':
        batting_team = 3
    elif batting_team == 'Kolkata Knight Riders':
        batting_team = 4
    elif batting_team == 'Sunrisers Hyderabad':
        batting_team = 5
    elif batting_team == 'Delhi Capitals':
        batting_team = 6
    elif batting_team == 'Royal Challengers Bangalore':
        batting_team = 7
    elif batting_team == 'Rajasthan Royals':
        batting_team = 8
    
        # converting bowling teams to numbers

    if bowling_team == 'Chennai Super Kings':
        bowling_team = 1
    elif bowling_team == 'Mumbai Indians':
        bowling_team = 2
    elif bowling_team == 'Kings XI Punjab':
        bowling_team = 3
    elif bowling_team == 'Kolkata Knight Riders':
        bowling_team = 4
    elif bowling_team == 'Sunrisers Hyderabad':
        bowling_team = 5
    elif bowling_team == 'Delhi Capitals':
        bowling_team = 6
    elif bowling_team == 'Royal Challengers Bangalore':
        bowling_team = 7
    elif bowling_team == 'Rajasthan Royals':
        bowling_team = 8
    if innings == 1:
        
        def overall(x):
        
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
            
            venue_m = (venue-mu1)*venue_n/s1
            innings_m = (innings-mu2)*innings_n/s2
            batting_team_m = (batting_team-mu3)*batting_team_n/s3
            bowling_team_m = (bowling_team-mu4)*bowling_team_n/s4
            wickets_m = (wickets-mu5)*wickets_n/s5
            bowlers_m = (bowlers-mu6)*bowlers_n/s6

            runs = x + theta + venue_m + innings_m + batting_team_m + bowling_team_m + wickets_m 
            return runs
        
        def venue1(y):
            
            theta_n = {0: 45.96428571, 1: 45.71212121, 2: 45.78169014, 3: 45.16083916, 4: 46.97014925, 5: 44.15384615}     
            innings_n = {0: -0.719993287, 1: 0.223124342, 2: 0.944833829, 3: -0.002577846, 4: -0.322785142, 5: -5.278870039}
            batting_team_n = {0: 1.427015168, 1: -1.291430481, 2: 0.184199631, 3: 0.384064487, 4: -0.626297864, 5: 3.555033384}
            bowling_team_n = {0: -1.999050857, 1: -0.402424354, 2: -0.204047732, 3: 1.354375968, 4: -0.039122897, 5: 0.840375813}
            wickets_n =  {0: -4.588801968, 1: -4.846819224, 2: -2.529457085, 3: -4.205238919, 4: -3.78842329, 5: -2.326857195}
            bowlers_n = {0: 4.188434245, 1: 4.555817064, 2: 3.573122723, 3: 3.65674877, 4: 2.739825943, 5: 3.404695843}
            mu1 = {0: 1.535714286, 1: 1.53030303, 2: 1.5, 3: 1.524475524, 4: 1.529850746, 5: 1.653846154}
            mu2 = {0: 3.089285714, 1: 3.378787879, 2: 4.176056338, 3: 5.412587413, 4: 5.082089552, 5: 5.884615385}
            mu3 = {0: 3.089285714, 1: 3.378787879, 2: 4.176056338, 3: 5.41958042, 4: 5.082089552, 5: 5.884615385}
            mu4 = {0: 1.357142857, 1: 1.431818182, 2: 1.387323944, 3: 1.461538462, 4: 1.492537313, 5: 1.346153846}
            mu5 = {0: 3.339285714, 1: 3.371212121, 2: 3.605633803, 3: 3.475524476, 4: 3.641791045, 5: 3.5}
            s1 = {0: 0.568363724, 1: 0.558615983, 2: 0.501769917, 3: 0.554522607, 4: 0.557792352, 5: 0.745241314}
            s2 = {0: 2.455196994, 1: 2.138453115, 2: 1.76369734, 3: 2.114099786, 4: 1.863977909, 5: 2.55071634}
            s3 = {0: 2.455196994, 1: 2.138453115, 2: 1.76369734, 3: 2.121030136, 4: 1.863977909, 5: 2.55071634}
            s4 = {0: 1.08931868, 1: 1.140464495, 2: 1.064238759, 3: 1.179455775, 4: 1.108723229, 5: 0.977437781}
            s5 = {0: 0.895972685, 1: 0.724756374, 2: 0.651868525, 3: 0.720251989, 4: 0.798522932, 5: 0.905538514}
        
            theta = theta_n[y-1]
            innings_m = (innings-mu1[y-1])*innings_n[y-1]/s1[y-1]
            batting_team_m = (batting_team-mu2[y-1])*batting_team_n[y-1]/s2[y-1]
            bowling_team_m = (bowling_team-mu3[y-1])*bowling_team_n[y-1]/s3[y-1]
            wickets_m = (wickets-mu4[y-1])*wickets_n[y-1]/s4[y-1]
            bowlers_m = (bowlers-mu5[y-1])*bowlers_n[y-1]/s5[y-1]
        
            runs = theta + innings_m + batting_team_m + bowling_team_m + wickets_m 
            runs = int(runs)
            return runs

        def team(y):
  
            theta_n = {0: 44.90816327, 1: 46.1509434, 2: 46.24074074, 3: 47.15044248, 4: 46.20754717, 5: 45.73076923, 6: 44.71296296, 7: 45.86792453}
            venue_n = {0: 0.053275912, 1: -1.630431918, 2: -1.121069485, 3: -0.915748544, 4: 0.865537243, 5: -1.104432694, 6: -0.516916327, 7: 0.094099452}
            innings_n =  {0: 1.183227125, 1: -0.418091816, 2: -0.348899489, 3: 0.963752232, 4: -0.767368136, 5: -1.777891237, 6: 0.396136943, 7: -1.439016448}
            bowling_team_n = {0: -0.855666074, 1: -1.458804875, 2: 2.509778488, 3: 0.384906056, 4: -1.263751518, 5: -0.078608707, 6: 1.151709388, 7: -2.48099486}
            wickets_n =  {0: -3.98434147, 1: -4.146397141, 2: -3.847295404, 3: -3.798191173, 4: -2.864635578, 5: -5.435462598, 6: -2.769885758, 7: -3.615334076}
            bowlers_n = {0: 3.560721998, 1: 3.850994491, 2: 6.795349731, 3: 3.93622329, 4: 2.88340271, 5: 1.952742442, 6: 4.000215233, 7: 5.363827112}
            mu1 = {0: 2.081632653, 1: 2.650943396, 2: 3.277777778, 3: 3.10619469, 4: 3.245283019, 5: 4.144230769, 6: 3.546296296, 7: 3.79245283}
            mu2 = {0: 1.530612245, 1: 1.518867925, 2: 1.592592593, 3: 1.513274336, 4: 1.490566038, 5: 1.557692308, 6: 1.5, 7: 1.547169811}
            mu3 ={0: 4.806122449, 1: 4.735849057, 2: 4.333333333, 3: 4.407079646, 4: 4.320754717, 5: 4.173076923, 6: 3.833333333, 7: 4.0}
            mu4 = {0: 1.367346939, 1: 1.29245283, 2: 1.592592593, 3: 1.433628319, 4: 1.264150943, 5: 1.711538462, 6: 1.435185185, 7: 1.188679245}
            mu5 = {0: 3.693877551, 1: 3.367924528, 2: 3.425925926, 3: 3.566371681, 4: 3.509433962, 5: 3.519230769, 6: 3.351851852, 7: 3.509433962}
            s1 = {0: 1.447881277, 1: 1.219230459, 2: 1.432989574, 3: 1.046787875, 4: 1.466362065, 5: 1.361169323, 6: 1.105502459, 7: 1.768946781}
            s2 = {0: 0.521774957, 1: 0.556025557, 2: 0.630020021, 3: 0.552834324, 4: 0.54145962, 5: 0.571608582, 6: 0.520603532, 7: 0.606567827}
            s3 = {0: 2.018768448, 1: 2.310645702, 2: 2.32297792, 3: 2.437201147, 4: 2.326879595, 5: 2.391093131, 6: 2.115806114, 7: 2.157277487}
            s4 = {0: 1.115844233, 1: 1.059802148, 2: 1.221173554, 3: 1.084600866, 4: 0.901941142, 5: 1.163131669, 6: 1.096069001, 7: 1.177621524}
            s5 = {0: 0.694724796, 1: 0.760018442, 2: 0.881718987, 3: 0.730412141, 4: 0.696768406, 5: 0.881093421, 6: 0.727494931, 7: 0.723842352}
        
            theta = theta_n[y-1]
            venue1 = (venue - mu1[y-1])*venue_n[y-1]/s1[y-1]
            innings_m = (innings-mu2[y-1])*innings_n[y-1]/s2[y-1]
            bowling_team_m = (bowling_team-mu3[y-1])*bowling_team_n[y-1]/s3[y-1]
            wickets_m = (wickets-mu4[y-1])*wickets_n[y-1]/s4[y-1]
            bowlers_m = (bowlers-mu5[y-1])*bowlers_n[y-1]/s5[y-1]
        
            runs = theta + venue1 + innings_m + bowling_team_m + wickets_m
            return(runs)
        prediction = (team(batting_team) + venue1(venue) + overall(0))/3
        return prediction
    elif innings==2:

        avg_i1={1:38.66666667,	2:52.47058824,  3:52,	4:46.5, 5:47.5, 6:46.57142857,  7:46.76470588,  8:50}       

        def overall2(x):
           theta0 = 47.28318584
           theta1=0.5301262193
           theta2=2.125441681
           theta3=-0.5467394162
           theta4=-0.8549742928
           theta5=-4.666116815
           theta6=1.905012312

           mu1= 3.185840708
           mu2=45.43362832
           mu3=4.321533923
           mu4=4.353982301
           mu5=1.492625369
           mu6=3.489675516



           s1= 1.45473318
           s2=	11.07896037
           s3=2.288350225
           s4=2.271200009
           s5=1.164986684
           s6=0.7065079226
            
           venue_m = (venue-mu1)*theta1/s1
           avg_i1_m = (avg_i1[x]-mu2)*theta2/s2
           batting_team_m = (batting_team-mu3)*theta3/s3
           bowling_team_m = (bowling_team-mu4)*theta4/s4
           wickets_m = (wickets-mu5)*theta5/s5
           bowlers_m = (bowlers-mu6)*theta6/s6

           runs =   theta0+ venue_m + avg_i1_m + batting_team_m + bowling_team_m + wickets_m 
           return runs
        
