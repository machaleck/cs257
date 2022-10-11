SELECT DISTINCT noc_team.noc
FROM noc_team
ORDER BY noc;

SELECT DISTINCT athletes.full_name
FROM noc_team, athlete_team, athletes
WHERE noc_team.id = athlete_team.team_id
AND athletes.id = athlete_team.athlete_id
AND noc_team.team = 'Jamaica';

SELECT events.event_name, games.game_year, medals.medal_name
FROM events, athlete_event, medals, games, game_competitor, athletes
WHERE athletes.id = game_competitor.athlete_id
AND games.id = game_competitor.game_id
AND game_competitor.id = athlete_event.competitor_id
AND medals.id = athlete_event.medal_id
AND events.id = athlete_event.event_id
AND athletes.full_name = 'Gregory Efthimios "Greg" Louganis'
ORDER BY games.game_year;
