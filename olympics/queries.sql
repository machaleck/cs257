SELECT DISTINCT noc_team.noc
FROM noc_team
ORDER BY noc;

SELECT DISTINCT athletes.full_name
FROM noc_team, athlete_team, athletes
WHERE noc_team.id = athlete_team.team_id
AND athletes.id = athlete_team.athlete_id
AND noc_team.team = 'Jamaica';

SELECT events.event_name, games.game_year, medals.medal_name
FROM events, athlete_event, medals, games, athletes
WHERE athletes.id = athlete_event.athlete_id
AND games.id = athlete_event.game_id
AND medals.id = athlete_event.medal_id
AND events.id = athlete_event.event_id
AND athletes.full_name = 'Gregory Efthimios "Greg" Louganis'
AND medals.medal_name IN ('Gold', 'Silver', 'Bronze')
ORDER BY games.game_year;

SELECT noc_team.noc, COUNT(*)
FROM noc_team, athlete_team, athletes, athlete_event, medals
WHERE noc_team.id = athlete_team.team_id
AND athletes.id = athlete_team.athlete_id
AND athletes.id = athlete_event.athlete_id
AND medals.id = athlete_event.medal_id
AND medals.medal_name = 'Gold'
GROUP BY noc_team.noc
ORDER BY COUNT(*) DESC;
