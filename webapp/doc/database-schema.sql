CREATE TABLE incident_types (
    id INTEGER, 
    incident TEXT
);

CREATE TABLE states (
    id INTEGER,
    name TEXT
);

CREATE TABLE declaration_titles (
    id INTEGER,
    title TEXT
);

CREATE TABLE years (
    id INTEGER, 
    year INTEGER
);

CREATE TABLE disasters (
    id INTEGER, 
    incident_type_id INTEGER,
    state_id INTEGER,
    declaration_title_id INTEGER,
    year INTEGER, 
    ih_program INTEGER, 
    ia_program INTEGER, 
    pa_program INTEGER,
    hm_program INTEGER
);


