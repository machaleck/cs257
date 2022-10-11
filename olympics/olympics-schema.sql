CREATE TABLE athletes (
	id SERIAL,
	full_name VARCHAR,
	sex VARCHAR,
	height VARCHAR,
	weight VARCHAR
);

CREATE TABLE athlete_team (
	athlete_id INT,
	team_id INT
);

CREATE TABLE noc_team (
	id SERIAL,
	noc VARCHAR,
	team VARCHAR
);

CREATE TABLE age (
	athlete_id INT,
	age VARCHAR
);

CREATE TABLE games (
	id SERIAL,
	game_name VARCHAR,
	game_year VARCHAR
);

CREATE TABLE games_city (
	games_id INT,
	city_id INT
);

CREATE TABLE cities (
	id SERIAL,
	city_name VARCHAR
);

CREATE TABLE athlete_event (
	athlete_id INT,
	event_id INT,
	game_id INT,
	medal_id INT
);

CREATE TABLE events (
	id SERIAL,
	sport_id INT,
	event_name VARCHAR
);

CREATE TABLE sports (
	id SERIAL,
	sport_name VARCHAR
);

CREATE TABLE medals (
	id SERIAL,
	medal_name VARCHAR
);

