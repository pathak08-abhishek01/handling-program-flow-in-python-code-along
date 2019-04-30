import json
with open('file.json') as f:
    data = json.load(f)

# Code starts here

#  Can you find how many deliveries were faced by batsman  `SC Ganguly`.


def batsman_delivery(batsman_name, batsman_team):
    for inning_dict in data["innings"]:
        [(inning_name, inning_details)] = inning_dict.items()
        if inning_details['team'] == batsman_team:
            break

    n_deliveries = sum(map(lambda x: 1 if(list((x.values()))[0]['batsman'] == batsman_name) else 0, inning_details['deliveries']))
    return n_deliveries


batsman_delivery('SC Ganguly', 'Kolkata Knight Riders')

#  Who was man of the match and how many runs did he score ?
man_of_the_match = data['info']['player_of_match'][0]


def runs_of_man_of_match(player_of_match, man_of_match_team):
    if man_of_match_team == 'Kolkata Knight Riders':
        innings, key = 0, '1st innings'
    else:
        innings, key = 1, '2nd innings'

    run = 0

    for delivery_dict in data['innings'][innings][key]['deliveries']:
        if list(delivery_dict.values())[0]['batsman'] == player_of_match:
            run += list(delivery_dict.values())[0]['runs']['batsman']


runs_of_man_of_match(man_of_the_match, 'Kolkata Knight Riders')

#  Which batsman played in the first inning?
batsman_list = list(set(map(lambda x: list(x.values())[0]['batsman'], data['innings'][0]['1st innings']['deliveries'])))
# Which batsman had the most no. of sixes in first inning ?
innings_one = data['innings'][0]['1st innings']['deliveries']


def no_of_sixes(innings_name):
    dict_six = {}
    for deliveries in innings_name:
        if list(deliveries.values())[0]['runs']['batsman'] == 6:
            dict_six[(list(deliveries.values())[0]['batsman'])] = dict_six.get((list(deliveries.values())[0]['batsman']), 0) + 1
    return dict_six


max_six = no_of_sixes(innings_one)
batsman_most_six = max(max_six, key=max_six.get)

# Find the names of all players that got bowled out in the second innings.

innings_two = data['innings'][1]['2nd innings']['deliveries']


def bowled_batsman(innings_name):
    bowled_out_batsman = []
    for deliveries in innings_name:
        if 'wicket' in list(deliveries.values())[0]:
            if list(deliveries.values())[0]['wicket']['kind'] == 'bowled':
                bowled_out_batsman.append(list(deliveries.values())[0]['batsman'])
    return bowled_out_batsman


bowled_out_list = bowled_batsman(innings_two)

# How many more "extras" (wides, legbyes, etc) were bowled in the second innings as compared to the first inning?


def extras_count(innings_name):
    extra = 0
    for deliveries in innings_name:
        extra += list(deliveries.values())[0]['runs']['extras']
    return extra


innings_one_extras = extras_count(innings_one)
innings_two_extras = extras_count(innings_two)

no_of_more_extras = innings_two_extras - innings_one_extras

# Code Ends Here

