#Written by Kyle Machalec and Ryan Dunn. 
#This is a piece of art. Please pay attention. 
#Here is where we got our data: https://www.kaggle.com/datasets/headsortails/us-natural-disaster-declarations?select=us_disaster_declarations.csv
#Be prepared to be amazed...

import csv
#Functioned designed to return the index of the desired header inputed as a list. 
def getHeaderIndex(lst, headers):
    headerIndexes = []
    i = 0 
    for item in lst: 
      for header in headers:   
          if item == header:
              headerIndexes.append(i)
              break
          else:
            splitItem = item.split(".")
            if len(splitItem) >= 2:
              splitHeader = header.split(".")
              if splitHeader[0] == splitItem[0] and splitHeader[-1] == splitItem[-1]:
                  headerIndexes.append(i)
                  break
      i += 1
    if len(headerIndexes) > 1:                                        
        return headerIndexes
    else: 
        return headerIndexes[0]
#Testing whether or not getHeaderIndex reads quotes. 
def test_getHeaderIndex():
    with open('us_disaster_declarations.csv') as original_data_file,\
            open('nocs.csv', 'w') as events_file:
        reader = csv.reader(original_data_file)
        writer = csv.writer(events_file)
        heading_row = next(reader)
        team_index = getHeaderIndex(heading_row, ["Team"])
        print(heading_row[team_index])


def main():
    #Create NOC table
    states = {}
    with open('us_disaster_declarations.csv') as original_data_file,\
            open('states.csv', 'w') as states_file:
        reader = csv.reader(original_data_file)
        writer = csv.writer(states_file)
        heading_row = next(reader) # eat up and ignore the heading row of the data file
        state_index = getHeaderIndex(heading_row, ["state"])

        for row in reader:
            state_name = row[state_index]

            if state_name not in states:
                state_id = len(states) + 1
                states[state_name] = state_id
                writer.writerow([state_id, state_name])

    incident_types = {}
    with open('us_disaster_declarations.csv') as original_data_file,\
            open('incident_types.csv', 'w') as incident_types_file:
        reader = csv.reader(original_data_file)
        writer = csv.writer(incident_types_file)
        heading_row = next(reader) # eat up and ignore the heading row of the data file
        incident_index = getHeaderIndex(heading_row, ["incident_type"])

        for row in reader:
            incident_type_name = row[incident_index]

            if incident_type_name not in incident_types:
                incident_type_id = len(incident_types) + 1
                incident_types[incident_type_name] = incident_type_id
                writer.writerow([incident_type_id, incident_type_name])

    #Declaration Types
    declaration_titles = {}
    with open('us_disaster_declarations.csv') as original_data_file,\
            open('declaration_titles.csv', 'w') as declaration_titles_file:
        reader = csv.reader(original_data_file)
        writer = csv.writer(declaration_titles_file)
        heading_row = next(reader) # eat up and ignore the heading row of the data file
        declaration_title_index = getHeaderIndex(heading_row, ["declaration_title"])

        for row in reader:
            declaration_title = row[declaration_title_index]

            if declaration_title not in declaration_titles:
                declaration_title_id = len(declaration_titles) + 1
                declaration_titles[declaration_title] = declaration_title_id
                writer.writerow([declaration_title_id, declaration_title])

    years = {}
    with open('us_disaster_declarations.csv') as original_data_file,\
            open('years.csv', 'w') as year_file:
        reader = csv.reader(original_data_file)
        writer = csv.writer(year_file)
        heading_row = next(reader) # eat up and ignore the heading row of the data file
        declaration_date_index = getHeaderIndex(heading_row, ["fy_declared"])

        for row in reader:
            declaration_date = row[declaration_date_index]

            if declaration_date not in years:
                declaration_date_id = len(years) + 1
                years[declaration_date] = declaration_date_id
                writer.writerow([declaration_date_id, declaration_date])

    #(3) For each row in the original us_disaster_declarations.csv file, build a row
    #       for our new event_results.csv table
    with open('us_disaster_declarations.csv') as original_data_file,\
            open('disasters.csv', 'w') as disasters_file:
        reader = csv.reader(original_data_file)
        writer = csv.writer(disasters_file)
        heading_row = next(reader) # eat up and ignore the heading row of the data file
        incident_type_index = getHeaderIndex(heading_row, ["incident_type"])
        state_index = getHeaderIndex(heading_row, ["state"])
        declaration_title_index = getHeaderIndex(heading_row, ["declaration_title"])
        declaration_date_index = getHeaderIndex(heading_row, ["fy_declared"])
        disaster_id_index = getHeaderIndex(heading_row, ["disaster_number"])

        ih_program_index = getHeaderIndex(heading_row, ["ih_program_declared"])
        ia_program_index = getHeaderIndex(heading_row, ["ia_program_declared"])
        pa_program_index = getHeaderIndex(heading_row, ["pa_program_declared"])
        hm_program_index = getHeaderIndex(heading_row, ["hm_program_declared"])

        for row in reader:
            disaster_id = row[disaster_id_index]

            incident_type = row[incident_type_index]
            incident_type_id = incident_types[incident_type]

            state_name = row[state_index]
            state_id = states[state_name]

            declaration_title_name= row[declaration_title_index]
            declaration_title_id = declaration_titles[declaration_title_name]

            ih_program_declared = row[ih_program_index]
            ia_program_declared = row[ia_program_index]
            pa_program_declared = row[pa_program_index]
            hm_program_declared = row[hm_program_index]

            year = row[declaration_date_index]
            year_id = years[year]

            writer.writerow([disaster_id, incident_type_id, state_id, declaration_title_id, year_id, ih_program_declared, ia_program_declared, pa_program_declared, hm_program_declared])
main()