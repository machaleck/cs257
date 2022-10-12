CREATE TABLE athletes (
	id INT,
	full_name VARCHAR,
	sex VARCHAR,
	height VARCHAR,
	weight VARCHAR
);

CREATE TABLE athlete_team (
	athlete_id INT,
	team_id INT
);

CREATE TABLE teams (
	id INT,
	team_name VARCHAR,
	noc_id INT
);

CREATE TABLE nocs (
	id INT,
	noc_name VARCHAR
);

CREATE TABLE ages (
	athlete_id INT,
	age VARCHAR
);

CREATE TABLE games (
	id INT,
	game_name VARCHAR,
	game_year VARCHAR
);

CREATE TABLE games_city (
	games_id INT,
	city_id INT
);

CREATE TABLE cities (
	id INT,
	city_name VARCHAR
);

CREATE TABLE athlete_event (
	athlete_id INT,
	event_id INT,
	game_id INT,
	medal_id INT
);

CREATE TABLE events (
	id INT,
	sport_id INT,
	event_name VARCHAR
);

CREATE TABLE sports (
	id INT,
	sport_name VARCHAR
);

CREATE TABLE medals (
	id INT,
	medal_name VARCHAR
);

