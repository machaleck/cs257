#Written by Kyle Machalec

import sys
import psycopg2
import config
from argparse import ArgumentParser

def get_connection():
    '''Returns a database connection object, which can be used to create cursors and
       issue SQL queries'''
    try:
        return psycopg2.connect(database=config.database,
                                user=config.user,
                                password=config.password)
    except Exception as e:
        print(e, file=sys.stderr)
        exit()

def get_athletes_from_noc(noc_name):
    #Returns a list containing the names of all the athletes from a specified NOC
    athletes = []
    try:
        query = '''SELECT DISTINCT athletes.full_name
                   FROM nocs, teams, athlete_team, athletes
                   WHERE nocs.id = teams.noc_id
                   AND teams.id = athlete_team.team_id
                   AND athletes.id = athlete_team.athlete_id
                   AND nocs.noc_name = %s'''
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(query, (noc_name,))
        for row in cursor:
            athlete_name = row[0]
            athletes.append(f'{athlete_name}')
    
    except Exception as e:
        print(e, file=sys.stderr)
    
    connection.close()
    return athletes

def get_gold_from_nocs():
    '''Returns a list containing all the NOCs and the number of gold medals they have won, 
       in decreasing order of the number of gold medals'''
    noc_golds = []
    try:
        query = '''SELECT nocs.noc_name, COUNT(*)
                   FROM nocs, teams, athlete_team, athletes, athlete_event, medals
                   WHERE nocs.id = teams.noc_id
                   AND teams.id = athlete_team.team_id
                   AND athletes.id = athlete_team.athlete_id
                   AND athletes.id = athlete_event.athlete_id
                   AND medals.id = athlete_event.medal_id
                   AND medals.medal_name = 'Gold'
                   GROUP BY nocs.noc_name
                   ORDER BY COUNT(*) DESC'''
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(query)

        for row in cursor:
            noc_name = row[0]
            gold_count = row[1]
            noc_golds.append(f'{noc_name} | {gold_count}')
    
    except Exception as e:
        print(e, file=sys.stderr)
    
    connection.close()
    return noc_golds

def get_medals_from_athlete(athlete_name):
    '''Returns a list containing all of the medals won by an athlete whose name 
       contains (case-insensitively) the specified athlete_name as well as the 
       game each medal was won at, sorted by year.'''
    athlete_medals = []
    try:
        query = '''SELECT athletes.full_name, events.event_name, games.game_year, medals.medal_name
                   FROM events, athlete_event, medals, games, athletes
                   WHERE athletes.id = athlete_event.athlete_id
                   AND games.id = athlete_event.game_id
                   AND medals.id = athlete_event.medal_id
                   AND events.id = athlete_event.event_id
                   AND athletes.full_name ILIKE CONCAT('%%', %s, '%%')
                   AND medals.medal_name IN ('Gold', 'Silver', 'Bronze')
                   ORDER BY games.game_year'''
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(query, (athlete_name,))

        for row in cursor:
            athlete = row[0]
            event_name = row[1]
            game_year = row[2]
            medal_name = row[3]
            athlete_medals.append(f'{athlete} | {event_name} | {game_year} | {medal_name}')
    
    except Exception as e:
        print(e, file=sys.stderr)

    connection.close()
    return athlete_medals

def main():
    parser = ArgumentParser()

    parser.add_argument("-n", "--noc", 
                        help="Lists the names of all the athletes from a specified NOC.",
                        type=str)
    parser.add_argument("-g", "--gold", 
                        help='''Lists all the NOCs and the number of gold medals they have 
                        won, in decreasing order of the number of gold medals.''',
                        action = "store_true")
    parser.add_argument("-a", "--athlete", 
                        help='''Lists all of the medals won by an athlete whose name 
                        contains (case-insensitively) the specified search string as well as the game 
                        each medal was won at, sorted by year.''',
                        type=str)
    args = parser.parse_args()

    if(args.noc):
        #Get a list of athletes
        athletes = get_athletes_from_noc(args.noc)
        for athlete in athletes:
            print(athletes)
    elif(args.gold):
        #Get a list of nocs and their number of gold medals
        noc_medal_counts = get_gold_from_nocs()
        for noc_medal_count in noc_medal_counts:
            print(noc_medal_count)
    elif(args.athlete):
        #Get a list of athletes as well as the event names and years associated with their medals
        medals_from_athletes = get_medals_from_athlete(args.athlete)
        for medals_from_athlete in medals_from_athletes:
            print(medals_from_athlete)



if __name__ == "__main__":
    main()