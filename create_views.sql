-- Create a logical database for Tokyo Olympics data
CREATE DATABASE TokyoOlympics;
GO

USE TokyoOlympics;
GO

-- Create view for Athletes data from silver layer
CREATE VIEW athletes AS
SELECT * FROM OPENROWSET(
    BULK 'abfss://source@databricksen.dfs.core.windows.net/silverath/athletes/*.csv',
    FORMAT = 'CSV', HEADER_ROW = TRUE
) WITH (
    PersonName NVARCHAR(200),
    Country NVARCHAR(200),
    Discipline NVARCHAR(200)
) AS r;
GO

-- Create view for Coaches data from silver layer
CREATE VIEW coaches AS
SELECT * FROM OPENROWSET(
    BULK 'abfss://source@databricksen.dfs.core.windows.net/silverath/coaches/*.csv',
    FORMAT = 'CSV', HEADER_ROW = TRUE
) WITH (
    Name NVARCHAR(200),
    Country NVARCHAR(200),
    Discipline NVARCHAR(200),
    Event NVARCHAR(200)
) AS r;
GO

-- Create view for Entries by Gender data from silver layer
CREATE VIEW entriesgender AS
SELECT * FROM OPENROWSET(
    BULK 'abfss://source@databricksen.dfs.core.windows.net/silverath/entriesgender/*.csv',
    FORMAT = 'CSV', HEADER_ROW = TRUE
) WITH (
    Discipline NVARCHAR(200),
    Female INT,
    Male INT,
    Total INT
) AS r;
GO

-- Create view for Medals data from silver layer
CREATE VIEW medals AS
SELECT * FROM OPENROWSET(
    BULK 'abfss://source@databricksen.dfs.core.windows.net/silverath/medals/*.csv',
    FORMAT = 'CSV', HEADER_ROW = TRUE
) WITH (
    Rank INT,
    Team_Country NVARCHAR(200),
    Gold INT,
    Silver INT,
    Bronze INT,
    Total INT,
    [Rank by Total] INT
) AS r;
GO

-- Create view for Teams data from silver layer
CREATE VIEW teams AS
SELECT * FROM OPENROWSET(
    BULK 'abfss://source@databricksen.dfs.core.windows.net/silverath/teams/*.csv',
    FORMAT = 'CSV', HEADER_ROW = TRUE
) WITH (
    TeamName NVARCHAR(200),
    Discipline NVARCHAR(200),
    Country NVARCHAR(200),
    Event NVARCHAR(200)
) AS r;
GO
