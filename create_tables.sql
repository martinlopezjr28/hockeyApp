CREATE TABLE IF NOT EXISTS Teams (
    team_id INTEGER PRIMARY KEY,
    team_name TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS Players (
    player_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    goals INTEGER,
    assists INTEGER,
    plus_minus INTEGER,
    team_id INTEGER, -- Foreign key
    FOREIGN KEY (team_id) REFERENCES Teams(team_id)
);

-- Index on player name for faster searches
CREATE INDEX IF NOT EXISTS idx_player_name ON Players (name);