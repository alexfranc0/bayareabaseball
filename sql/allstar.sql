-- all star lineups from 2015
-- need: name (f/l), year (2015), roster (AL/NL)


-- people
	-- playerID
	--nameFirst
	--nameLast

--AllStar
	--playerID
	--lgID
	--yearID

--TEams
	-- yearID
	--lgID


SELECT CONCAT(p.nameFirst, ' ', p.nameLast) AS NAME, s.lgID AS LEAGUE, s.yearID AS YEAR
FROM AllstarFull s
JOIN People p ON s.playerID = p.playerID
WHERE s.yearID = 2015
ORDER BY s.lgID ASC

