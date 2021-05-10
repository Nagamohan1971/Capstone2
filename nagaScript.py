create_airports = """
CREATE TABLE IF NOT EXISTS public.airports (
    IATACode        VARCHAR PRIMARY KEY,
    AirportID       VARCHAR,
    CountryCode     VARCHAR,
    StateCode       VARCHAR,
    ContinentCode   VARCHAR,
    Municipality    VARCHAR,
    AirportName     VARCHAR,
    TypeOfAirport   VARCHAR,
    ElevationInFeet DECIMAL,
    Latitude        VARCHAR,
    Longitude       VARCHAR,
    GPSCode         VARCHAR,
    LocalCode       VARCHAR
);
"""

drop_airports = "DROP TABLE IF EXISTS airports;"

airport_insert = """ 
INSERT INTO airports (IATACode, AirportID, CountryCode, StateCode, ContinentCode, Municipality, AirportName, \ TypeOfAirport, ElevationInFeet, Latitude, Longitude, GPSCode, LocalCode) \
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
;
"""

create_demographics = """
CREATE TABLE IF NOT EXISTS public.demographics (
    StateCode             VARCHAR (2),
    State                 VARCHAR,
    City                  VARCHAR,
    Race                  VARCHAR,
    MedianAge             Decimal,
    MalePopulation        Decimal,
    FemalePopulation      Decimal,
    NumOfVeterans         Decimal,
    ForeignBorn           Decimal,
    AverageHouseholdSize  Decimal,
    Count                 BIGINT
);
"""

drop_demographics = "DROP TABLE IF EXISTS demographics;"

demographic_insert = """
INSERT INTO demographics (StateCode,State,City,Race,MedianAge,MalePopulation,FemalePopulation,NumOfVeterans, \
ForeignBorn,AverageHouseholdSize,Count) \
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"""

create_immigrations = """
CREATE TABLE IF NOT EXISTS public.immigrations (
    TravellerID    INT,
    AdmissionNo    INT PRIMARY KEY,
    ArrivalDate    DATE,
    PortOfEntry    VARCHAR(3),
    StateCode      VARCHAR(2),
    ModeOfTravel    VARCHAR,
    TypeOfVisa      VARCHAR,
    Reason          VARCHAR,
    Airline         VARCHAR,
    BirthYear       INT,
    Age             INT,
    Gender          VARCHAR,
    IataCode        VARCHAR(3),
    Occupation      VARCHAR,
    DateOfDepature  DATE
);
"""

drop_immigrations = "DROP TABLE IF EXISTS immigrations;"

immigration_insert = ("""
INSERT INTO immigrations (TravellerID, AdmissionNo, ArrivalDate, PortOfEntry, StateCode, ModeOfTravel, \
TypeOfVisa, Reason, Airline, BirthYear, Age, Gender, IataCode ,Occupation, DateOfDepature) \
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""")

create_temperature = """
CREATE TABLE IF NOT EXISTS temperature (
    Date                      DATE,
    City                      VARCHAR,
    Country                   VARCHAR,
    AvgTemperature            FLOAT,
    AvgTempUncertainty        FLOAT,
    latitude                  VARCHAR,
    longitude                 VARCHAR
);
"""

temperature_insert = ("""
INSERT INTO temperature (Date, City, Country, AvgTemperature, AvgTempUncertainty, \
latitude, longitude) VALUES (%s, %s, %s, %s, %s, %s, %s)""")

drop_temperature = "DROP TABLE IF EXISTS temperature;"

drop_table_queries = [drop_airports, drop_demographics, drop_immigrations, drop_temperature]
create_table_queries = [create_airports, create_demographics, create_immigrations, create_temperature]