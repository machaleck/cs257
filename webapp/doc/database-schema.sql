CREATE TABLE incident_type (
    id INTEGER, 
    incident TEXT
);

CREATE TABLE declaration_title (
    id INTEGER,
    title TEXT
);

CREATE TABLE programs_declared (
    id INTEGER, 
    ih_program INTEGER, 
    ia_program INTEGER, 
    pa_program INTEGER,
    hm_program INTEGER
);

CREATE TABLE years (
    id INTEGER, 
    year INTEGER
);

CREATE TABLE disaster (
    id INTEGER, 
    incident_type_id INTEGER,
    declaration_title_id INTEGER,
    programs_declared_id INTEGER, 
    start_year_id INTEGER, 
    end_year_id INTEGER
);


