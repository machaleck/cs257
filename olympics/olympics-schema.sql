CREATE TABLE athlete (
	id SERIAL,
	full_name VARCHAR,
	sex VARCHAR,
	height VARCHAR,
	weight VARCHAR
);

CREATE TABLE athlete_team (
	athlete_id INT,
	region_id INT
);

CREATE TABLE team_noc (
	id SERIAL,
	team VARCHAR,
	noc VARCHAR
);

CREATE TABLE games_athlete (
	id SERIAL,
	games_id INT,
	athlete_id INT,
	age INT
);

CREATE TABLE games (
	id SERIAL,
	year INT,
	game_name VARCHAR,
	season VARCHAR
);

CREATE TABLE games_city (
	games_id INT,
	city_id int
);

CREATE TABLE city (
	id SERIAL,
	city_name VARCHAR
);

CREATE TABLE athlete_event (
	athlete_id INT,
	event_id INT,
	medal_id INT
);

CREATE TABLE event (
	id SERIAL,
	sport_id INT,
	event_name VARCHAR
);

CREATE TABLE sport (
	id SERIAL,
	sport_name VARCHAR
);

CREATE TABLE medal (
	id SERIAL,
	medal_name VARCHAR
);

