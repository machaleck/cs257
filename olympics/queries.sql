SELECT DISTINCT nocs.noc_name
FROM nocs
ORDER BY nocs.noc_name;

SELECT DISTINCT athletes.full_name
FROM nocs, teams, athlete_team, athletes
WHERE nocs.id = teams.noc_id
AND teams.id = athlete_team.team_id
AND athletes.id = athlete_team.athlete_id
AND nocs.noc_name = 'JAM';

SELECT events.event_name, games.game_year, medals.medal_name
FROM events, athlete_event, medals, games, athletes
WHERE athletes.id = athlete_event.athlete_id
AND games.id = athlete_event.game_id
AND medals.id = athlete_event.medal_id
AND events.id = athlete_event.event_id
AND athletes.full_name = 'Gregory Efthimios "Greg" Louganis'
AND medals.medal_name IN ('Gold', 'Silver', 'Bronze')
ORDER BY games.game_year;

SELECT nocs.noc_name, COUNT(*)
FROM nocs, teams, athlete_team, athletes, athlete_event, medals
WHERE nocs.id = teams.noc_id
AND teams.id = athlete_team.team_id
AND athletes.id = athlete_team.athlete_id
AND athletes.id = athlete_event.athlete_id
AND medals.id = athlete_event.medal_id
AND medals.medal_name = 'Gold'
GROUP BY nocs.noc_name
ORDER BY COUNT(*) DESC;
