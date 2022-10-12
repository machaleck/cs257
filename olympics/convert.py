#Written by Kyle Machalec
#Original Olympic dataset can be found at https://www.kaggle.com/datasets/heesoo37/120-years-of-olympic-history-athletes-and-results
import csv

class Convert:
    
    medals = {}
    with open('athlete_events.csv') as athlete_events_file,\
            open('medals.csv', 'w', newline='') as medals_file:
        reader = csv.reader(athlete_events_file)
        writer = csv.writer(medals_file)
        next(reader)
        for row in reader:
            medal_name = row[14]
            if medal_name not in medals:
                medal_id = len(medals) + 1
                medals[medal_name] = medal_id
                writer.writerow([medal_id, medal_name])

    sports = {}
    with open('athlete_events.csv') as athlete_events_file,\
            open('sports.csv', 'w', newline='') as sports_file:
        reader = csv.reader(athlete_events_file)
        writer = csv.writer(sports_file)
        next(reader)
        for row in reader:
            sport_name = row[12]
            if sport_name not in sports:
                sport_id = len(sports) + 1
                sports[sport_name] = sport_id
                writer.writerow([sport_id, sport_name])

    events = {}
    with open('athlete_events.csv') as athlete_events_file,\
            open('events.csv', 'w', newline='') as events_file:
        reader = csv.reader(athlete_events_file)
        writer = csv.writer(events_file)
        next(reader)
        for row in reader:
            event_name = row[13]
            if event_name not in events:
                event_id = len(events) + 1
                sport_name = row[12]
                sport_id = sports[sport_name]
                events[event_name] = event_id
                writer.writerow([event_id, sport_id, event_name])
    
    cities = {}
    with open('athlete_events.csv') as athlete_events_file,\
            open('cities.csv', 'w', newline='') as cities_file:
        reader = csv.reader(athlete_events_file)
        writer = csv.writer(cities_file)
        next(reader)
        for row in reader:
            city_name = row[11]
            if city_name not in cities:
                city_id = len(cities) + 1
                cities[city_name] = city_id
                writer.writerow([city_id, city_name])
    
    games = {}
    with open('athlete_events.csv') as athlete_events_file,\
            open('games.csv', 'w', newline='') as games_file:
        reader = csv.reader(athlete_events_file)
        writer = csv.writer(games_file)
        next(reader)
        for row in reader:
            game_name = row[8]
            game_year = row[9]
            if game_name not in games:
                game_id = len(games) + 1
                games[game_name] = game_id
                writer.writerow([game_id, game_name, game_year])
    
    games_city = set()
    with open('athlete_events.csv') as athlete_events_file,\
            open('games_city.csv', 'w', newline='') as games_city_file:
        reader = csv.reader(athlete_events_file)
        writer = csv.writer(games_city_file)
        next(reader)
        for row in reader:
            game_name = row[8]
            city_name = row[11]
            if (game_name + city_name) not in games_city:
                games_city.add(game_name + city_name)
                game_id = games[game_name]
                city_id = cities[city_name]
                writer.writerow([game_id, city_id])

    nocs = {}
    with open('athlete_events.csv') as athlete_events_file,\
            open('nocs.csv', 'w', newline='') as nocs_file:
        reader = csv.reader(athlete_events_file)
        writer = csv.writer(nocs_file)
        next(reader)
        for row in reader:
            noc_name = row[7]
            if noc_name not in nocs:
                noc_id = len(nocs) + 1
                nocs[noc_name] = noc_id
                writer.writerow([noc_id, noc_name])
    
    teams = {}
    with open('athlete_events.csv') as athlete_events_file,\
            open('teams.csv', 'w', newline='') as team_file:
        reader = csv.reader(athlete_events_file)
        writer = csv.writer(team_file)
        next(reader)
        for row in reader:
            team_name = row[6]
            if team_name not in teams:
                team_id = len(teams) + 1
                teams[team_name] = team_id
                noc_name = row[7]
                noc_id = nocs[noc_name]
                writer.writerow([team_id, team_name, noc_id])

    #height and weight do not differ between Olympic games in original database
    athletes = {}
    with open('athlete_events.csv') as athlete_events_file,\
            open('athletes.csv', 'w', newline='') as athletes_file:
        reader = csv.reader(athlete_events_file)
        writer = csv.writer(athletes_file)
        next(reader)
        for row in reader:
            athlete_id = row[0]
            athlete_name = row[1]
            athlete_sex = row[2]
            athlete_height = row[4]
            athlete_weight = row[5]
            if athlete_name not in athletes:
                athletes[athlete_name] = athlete_id
                writer.writerow([athlete_id, athlete_name, athlete_sex, athlete_height, athlete_weight])
    
    athlete_teams = set()
    with open('athlete_events.csv') as athlete_events_file,\
            open('athlete_team.csv', 'w', newline='') as athlete_team_file:
        reader = csv.reader(athlete_events_file)
        writer = csv.writer(athlete_team_file)
        next(reader)
        for row in reader:
            athlete_name = row[1]
            team_name = row[6]
            if (athlete_name + team_name) not in athlete_teams:
                athlete_teams.add(athlete_name + team_name)
                athlete_id = athletes[athlete_name]
                team_id = teams[team_name]
                writer.writerow([athlete_id, team_id])
    
    athletes = {}
    with open('athlete_events.csv') as athlete_events_file,\
            open('ages.csv', 'w', newline='') as ages_file:
        reader = csv.reader(athlete_events_file)
        writer = csv.writer(ages_file)
        next(reader)
        for row in reader:
            athlete_id = row[0]
            athlete_name = row[1]
            age = row[3]
            if (athlete_name) not in athletes:
                athletes[athlete_name] = athlete_id
                athlete_id = athletes[athlete_name]
                writer.writerow([athlete_id, age])
    
    with open('athlete_events.csv') as athlete_events_file,\
            open('athlete_event.csv', 'w', newline='') as athlete_event_file:
        reader = csv.reader(athlete_events_file)
        writer = csv.writer(athlete_event_file)
        next(reader)
        for row in reader:
            event_name = row[13]
            event_id = events[event_name]
            athlete_name = row[1]
            athlete_id = row[0]
            game_name = row[8]
            game_id = games[game_name]
            medal_name = row[14]
            medal_id = medals[medal_name]
            writer.writerow([athlete_id, event_id, game_id, medal_id])