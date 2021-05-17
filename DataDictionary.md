DataDictionary

The physical data model is having star schema

immigrations(iata) -> airports(iata_code)
immigrations(addr) -> demographics(state_code)
immigration(res) -> temperature(city)

immigrations (Fact Table)
1.	cicid -	FLOAT - PK - Traveller ID Number
2. 	year - FLOAT - Travel Year
3. 	month - FLOAT -	Travel Month
4. 	cit - FLOAT - Traveller City
5. 	res - VARCHAR -	Traveller resident of country
6. 	iata - VARCHAR(3) - IATA Port code
7. 	arrdate - VARCHAR - Arrival Date
8. 	mode - VARCHAR -	Mode of entry to us
9. 	addr - VARCHAR - Traveller arrival state
10.	depdate - VARCHAR - Depature Date
11. bir - FLOAT	- Age of Traveller
12. visa - VARCHAR - Purpose of travel
13. count - FLOAT - statistics Count
14.	entdepa - VARCHAR(1) - Arrival date matching
15. entdepd  - VARCHAR(1) - Depature date matching
16. matflag - VARCHAR(1) - mismatched arrival/departure records
17. biryear - FLOAT - Traveller year of birth
18. dtaddto - VARCHAR - date allowed to stay until
19.	gender - VARCHAR(15) - Gender of traveller
20. airline - VARCHAR - Airline by which arrived
21. admnum - BIGINT - USA admission Number
22. fltno - VARCHAR - Flight no on which vistor arrived
23. visatype - VARCHAR - Type of visa

airports (Dimension Table)

1.	iata_code - VARCHAR - PK - IATA Code
2.	name - VARCHAR - Name of Airport
3.	type - VARCHAR - Type of Airport
4.	local_code - VARCHAR - Local Code of Airport
5.	coordinate - VARCHAR - Airport Coordinates
6.	city - VARCHAR - City of Airport
7.	elevation_ft - FLOAT - Airport Elevation
8.	continent - VARCHAR - Continent Airport is
9.	iso_country - VARCHAR - Country Aiport is
10.	iso_region - VARCHAR - Region where Airport is
11.	municipality - VARCHAR - Mucnicipality where Airport is
12. gps_code - VARCHAR - Airport gps code

Demographics (Dimension Table)

1.	city - VARCHAR - Name of City
2.	state - VARCHAR - city in which state
3.	media_age - FLOAT - Median Age of Population
4.	male_population - FLOAT - Male population
5.	female_population - FLOAT - Female Population
6.	total_population - FLOAT - Total cityPopulation
7.	num_veterans - FLOAT - Num of Veterans
8.	foreign_ born - FLOAT - Num of Foreign  Born
9.	average_household_size - FLOAT - Average_Household Size
10.	state_code - FLOAT - State Code
11.	race - VARCHAR(2) - Race 
12.	count - BIGINT - Count 

temperature (Dimension Table)

1.	timestamp - DATE - Date of Temperature
2.	average_ temperature - FLOAT - Average Temp of the day
3.	average_temperature_uncertainty - FLOAT - Temperature Uncertainty
4.	city - VARCHAR - City where temp taken
5.	country - VARCHAR - city in which country
6.	latitude - VARCHAR - city latitude
7.	longitude - VARCHAR - city longitude

