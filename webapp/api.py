'''
    api.py
    Jeff Ondich, 25 April 2016
    Updated 8 November 2021

'''
import sys
import flask
import json
import config
import psycopg2

api = flask.Blueprint('api', __name__)

def get_connection():
    ''' Returns a connection to the database described in the
        config module. May raise an exception as described in the
        documentation for psycopg2.connect. '''
    return psycopg2.connect(database=config.database,
                            user=config.user,
                            password=config.password)



@api.route('/disasters_year', methods= ['GET']) 
def get_incident_year_data():
    ''' Returns data for our graph # of incidents by year. 
            http://.../disasters_year/
            Data is returned in the following format of a list of three lists: [year_list, num_occurences, colors]
    '''
    query = '''SELECT states.name, years.year, incident_types.incident
                FROM incident_types, states, years, disasters
                WHERE incident_types.id = disasters.incident_type_id
                AND states.id = disasters.state_id
                AND years.id = disasters.year'''
    where_clause_args = []
    state = flask.request.args.get("state")
    start_year = flask.request.args.get("start_year")
    end_year = flask.request.args.get("end_year")
    incident_type = flask.request.args.get("incident_type")

    if state is not None and state is not "": 
        query += ' AND states.name = %s'
        where_clause_args.append(state)
    if start_year is not None and start_year is not "": 
        query += ' AND years.year >= %s'
        where_clause_args.append(start_year)
    if end_year is not None and end_year is not "": 
        query += ' AND years.year <= %s'
        where_clause_args.append(end_year)
    if incident_type is not None and incident_type is not "": 
        query += ' AND incident_types.incident = %s'
        where_clause_args.append(incident_type)

    query += ' ORDER BY years.year'
    years = {

    }
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(query, where_clause_args)
        for row in cursor:
            if row[1] in years:
                years[row[1]] += 1
            else:
                years.update({row[1]: 1})
        cursor.close()
        connection.close()
    except Exception as e:
        print(e, file=sys.stderr)
    
    year_list = list(years.keys())
    num_occurences = list(years.values())
    colors=[]

    color_options = ["red", "green", "blue", "orange", "brown"]
    a=0
    for year in year_list:
        if a >=5:
            a=0
        colors.append(color_options[a])
        a+=1
    colors = list(colors)

    if len(year_list) == len(num_occurences) & len(num_occurences) == len(colors):
        return json.dumps([year_list, num_occurences, colors])

@api.route('/pie_chart', methods= ['GET']) 
def get_pie_chart():
    ''' Returns data for our pie chart containing information about the number of incidents. 
                Data is recieved in the following format: [incident_list, num_occurences, colors]
                http://.../pie_chart/'''

    query = '''SELECT states.name, years.year, incident_types.incident
                FROM incident_types, states, years, disasters
                WHERE incident_types.id = disasters.incident_type_id
                AND states.id = disasters.state_id
                AND years.id = disasters.year'''
    where_clause_args = []
    state = flask.request.args.get("state")
    start_year = flask.request.args.get("start_year")
    end_year = flask.request.args.get("end_year")
    incident_type = flask.request.args.get("incident_type")

    
    if state is not None and state is not "": 
        query += ' AND states.name = %s'
        where_clause_args.append(state)
    if start_year is not None and start_year is not "": 
        query += ' AND years.year >= %s'
        where_clause_args.append(start_year)
    if end_year is not None and end_year is not "": 
        query += ' AND years.year <= %s'
        where_clause_args.append(end_year)
    if incident_type is not None and incident_type is not "": 
        query += ' AND incident_types.incident = %s'
        where_clause_args.append(incident_type)

    incident_types = {}
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(query, where_clause_args)

        for row in cursor:
            if row[2] in incident_types:
                incident_types[row[2]] += 1
            else:
                incident_types.update({row[2]: 1})
            
        cursor.close()
        connection.close()
    except Exception as e:
        print(e, file=sys.stderr)
    
    incident_list = list(incident_types.keys())
    num_occurences = list(incident_types.values())
    color_options=["#b91d47","#00aba9","#2b5797","#e8c3b9","#1e7145",'#e6194b', '#3cb44b', '#ffe119', '#4363d8', '#f58231', '#911eb4', '#46f0f0', '#f032e6', '#bcf60c', '#fabebe', '#008080', '#e6beff', '#9a6324', '#fffac8', '#800000', '#aaffc3', '#808000', '#ffd8b1', '#000075', '#808080', '#ffffff', '#000000'
    ]
    colors =[]
    a=0
    for item in incident_list:
        colors.append(color_options[a])
        a+=1

    if len(incident_list) == len(num_occurences) & len(num_occurences) == len(colors):
        return json.dumps([incident_list, num_occurences, colors])

@api.route('/programs_year', methods= ['GET']) 
def get_program_year_data():
    ''' Returns program by year data.

        Returns three lists in the following order. [year_list, num_occurences, colors]

            http://.../program_year

    '''
    query = '''SELECT states.name, years.year, incident_types.incident, ih_program, ia_program, pa_program, hm_program
                FROM incident_types, states, years, disasters
                WHERE incident_types.id = disasters.incident_type_id
                AND states.id = disasters.state_id
                AND years.id = disasters.year'''
    where_clause_args = []
    state = flask.request.args.get("state")
    start_year = flask.request.args.get("start_year")
    end_year = flask.request.args.get("end_year")
    incident_type = flask.request.args.get("incident_type")

    if state is not None and state is not "": 
        query += ' AND states.name = %s'
        where_clause_args.append(state)
    if start_year is not None and start_year is not "": 
        query += ' AND years.year >= %s'
        where_clause_args.append(start_year)
    if end_year is not None and end_year is not "": 
        query += ' AND years.year <= %s'
        where_clause_args.append(end_year)
    if incident_type is not None and incident_type is not "": 
        query += ' AND incident_types.incident = %s'
        where_clause_args.append(incident_type)

    query += ' ORDER BY years.year'
    years = {

    }
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(query, where_clause_args)
        for row in cursor:
            added_program_num = 0
            if row[3] == 1: 
                added_program_num += 1
            if row[4] == 1:
                added_program_num += 1
            if row[5] == 1:
                added_program_num += 1
            if row[6] == 1:
                added_program_num += 1
            if row[1] in years:
                years[row[1]] = years[row[1]] + added_program_num
            else:
                years.update({row[1]: added_program_num})
            
        cursor.close()
        connection.close()
    except Exception as e:
        print(e, file=sys.stderr)
    
    year_list = list(years.keys())
    num_occurences = list(years.values())
    colors=[]

    color_options = ["red", "green", "blue", "orange", "brown"]
    a=0
    for year in year_list:
        if a >=5:
            a=0
        colors.append(color_options[a])
        a+=1
    colors = list(colors)

    if len(year_list) == len(num_occurences) & len(num_occurences) == len(colors):
        return json.dumps([year_list, num_occurences, colors])

@api.route('/states/') 
def get_states():
    ''' Returns a list of all the states in our database.

        By default, the list is presented in alphabetical order
        by state name.

            http://.../states/

        Returns an empty list if there's any database failure.
    '''
    query = '''SELECT states.id, states.name
               FROM states ORDER BY states.name'''

    state_list = []
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(query, tuple())
        for row in cursor:
            state = {'name':row[1]}
            state_list.append(state)
        cursor.close()
        connection.close()
    except Exception as e:
        print(e, file=sys.stderr)
    return json.dumps(state_list)

@api.route('/years/') 
def get_years():
    ''' Returns a list of all the years in our database.

        By default, the list is presented in ascending order
        by year.

            http://.../years/

        Returns an empty list if there's any database failure.
    '''
    query = '''SELECT years.year
               FROM years ORDER BY years.year'''

    year_list = []
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(query, tuple())
        for row in cursor:
            year = {'year':row[0]}
            year_list.append(year)
        cursor.close()
        connection.close()
    except Exception as e:
        print(e, file=sys.stderr)
    return json.dumps(year_list)

@api.route('/incidents/') 
def get_incidents():
    ''' Returns a list of all the incidents in our database.

        By default, the list is presented in alphabetical order
        by incident name.

            http://.../incidents/

        Returns an empty list if there's any database failure.
    '''
    query = '''SELECT incident_types.incident
               FROM incident_types ORDER BY incident_types.incident'''

    incident_types_list = []
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(query, tuple())
        for row in cursor:
            incident_type = {'incident_type' :row[0]}
            incident_types_list.append(incident_type)
        cursor.close()
        connection.close()
    except Exception as e:
        print(e, file=sys.stderr)
    return json.dumps(incident_types_list)

@api.route('/natural_disasters', methods= ['GET'])
def get_disasters():
    
    query = '''SELECT states.name, declaration_titles.title, incident_types.incident, years.year, disasters.ih_program, disasters.ia_program, disasters.pa_program, disasters.hm_program
               FROM incident_types, states, declaration_titles, years, disasters
               WHERE incident_types.id = disasters.incident_type_id
                AND states.id = disasters.state_id
                AND declaration_titles.id = disasters.declaration_title_id
                AND years.id = disasters.year'''
    where_clause_args = []
    state = flask.request.args.get("state")
    print(state)
    start_year = flask.request.args.get("start_year")
    end_year = flask.request.args.get("end_year")
    incident_type = flask.request.args.get("incident_type")
    ih_program = flask.request.args.get("ih_program")
    ia_program = flask.request.args.get("ia_program")
    pa_program = flask.request.args.get("pa_program")
    hm_program = flask.request.args.get("hm_program")

    if state is not None: 
        query += ' AND states.name = %s'
        where_clause_args.append(state)
    if start_year is not None: 
        query += ' AND years.year >= %s'
        where_clause_args.append(start_year)
    if end_year is not None: 
        query += ' AND years.year <= %s'
        where_clause_args.append(end_year)
    if incident_type is not None: 
        query += ' AND incident_types.incident = %s'
        where_clause_args.append(incident_type)
    if ih_program is not None: 
        query += ' AND disasters.ih_program = 1'
    if ia_program is not None: 
        query += ' AND disasters.ia_program = 1'
    if pa_program is not None: 
        query += ' AND disasters.pa_program = 1'
    if hm_program is not None: 
        query += ' AND disasters.hm_program = 1'

    query+= ' ORDER BY years.year'

    disaster_list = []
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(query, where_clause_args)
        for row in cursor:
            programs = ''
            if row[4] == 1:
                programs += 'ih '
            if row[5] == 1:
                programs += 'ia '
            if row[6] == 1:
                programs += 'pa '
            if row[7] == 1:
                programs += 'hm '
                
            disaster = {'state':row[0], 'declaration_title':row[1], 'incident_type':row[2], 'programs':programs, 'year':row[3]  }
            disaster_list.append(disaster)
        cursor.close()
        connection.close()
    except Exception as e:
        print(e, file=sys.stderr)
    return json.dumps(disaster_list)

@api.route('/help')
def help():


    return '''REQUEST: /natural_disasters?state={state_requested}&start_year={year_requested}&end_year={year_requested}&incident_type={incident_requested}

RESPONSE: A JSON list of dictionaries, each of which represents one disaster, filtered by the users requests for the following parameters:
    - state
    - start year
    - end year
    - incident type 
The list will then be sorted by start year. 

All of the disasters following in the dictionary will have the following fields: 
    declaration_title -- (string) the name of the disaster.
    state -- (string) the state.
    year -- (int) the start year of the disaster.
    incident_type -- (string) the type of disaster. ex: Hurricane, Tornado
    programs -- (string) which type of programs were declared after the disaster.

EXAMPLE: /natural_disasters?state=CA&start_year=1957&end_year=1958&incident_type=Fire
[{"state": "CA", "declaration_title": "Forest Fire", "incident_type": "Fire", "programs": "ia pa hm ", "year": 1957}]


REQUEST: /states

RESPONSE: A JSON list of states sorted alphabetically. 


REQUEST: /years

RESPONSE: A JSON list of years sorted by year. 


REQUEST: /incident_types

RESPONSE: A JSON list of incident types sorted alphabetically.


REQUEST: /disasters_year?state={state_requested}&start_year={year_requested}&end_year={year_requested}&incident_type={incident_requested}

RESPONSE: A JSON list of lists containing years, number of disasters for each year, and color names

Example: /programs_year?state=MS&start_year=2009&end_year=2010
[[2009, 2010], [11, 18], ["red", "green"]]


REQUEST: /pie_chart?state={state_requested}&start_year={year_requested}&end_year={year_requested}&incident_type={incident_requested}

RESPONSE: A JSON list of lists containing incident types, number of times each incident occurred, and colors in hexadecimal

EXAMPLE: [["Severe Storm(s)"], [29], ["#b91d47"]]


REQUEST: /programs_year?state={state_requested}&start_year={year_requested}&end_year={year_requested}&incident_type={incident_requested}

RESPONSE: A JSON list of lists containing years, number of programs that were enacted each year, and color names

Example: /programs_year?state=MS&start_year=2009&end_year=2010
[[2009, 2010], [22, 46], ["red", "green"]]
'''