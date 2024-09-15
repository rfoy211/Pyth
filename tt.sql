CREATE TABLE battles (
  name VARCHAR(255),
  year INT,
  battle_number INT,
  attacker_king VARCHAR(255),
  defender_king VARCHAR(255),
  attacker_1 VARCHAR(255),
  attacker_2 VARCHAR(255),
  attacker_3 VARCHAR(255),
  attacker_4 VARCHAR(255),
  defender_1 VARCHAR(255),
  defender_2 VARCHAR(255),
  defender_3 VARCHAR(255),
  defender_4 VARCHAR(255),
  attacker_outcome VARCHAR(255),
  battle_type VARCHAR(255),
  major_death INT,
  major_capture INT,
  attacker_size INT,
  defender_size INT,
  attacker_commander VARCHAR(255),
  defender_commander VARCHAR(255),
  summer INT,
  location VARCHAR(255),
  region VARCHAR(255),
  note TEXT
);

INSERT INTO battles (name, year, battle_number, attacker_king, defender_king, attacker_1, attacker_2, attacker_3, attacker_4, defender_1, defender_2, defender_3, defender_4, attacker_outcome, battle_type, major_death, major_capture, attacker_size, defender_size, attacker_commander, defender_commander, summer, location, region, note)
VALUES
  ('Battle of the Golden Tooth', 298, 1, 'Joffrey/Tommen Baratheon', 'Robb Stark', 'Lannister', '', '', '', 'Tully', '', '', '', 'win', 'pitched battle', 1, 0, 15000, 4000, 'Jaime Lannister', 'Clement Piper, Vance', 1, 'Golden Tooth', 'The Westerlands', ''),
  ('Battle at the Mummer\'s Ford', 298, 2, 'Joffrey/Tommen Baratheon', 'Robb Stark', 'Lannister', '', '', '', 'Baratheon', '', '', '', 'win', 'ambush', 1, 0, '', 120, 'Gregor Clegane', 'Beric Dondarrion', 1, 'Mummer\'s Ford', 'The Riverlands', ''),
  ...;
  
  SELECT 
  year, 
  region, 
  COUNT(*) AS num_battles, 
  SUM(attacker_size) AS total_attacker_size, 
  SUM(defender_size) AS total_defender_size, 
  SUM(major_death) AS total_major_deaths, 
  SUM(major_capture) AS total_major_captures
FROM 
  battles
GROUP BY 
  year, 
  region
ORDER BY 
  year, 
  region;