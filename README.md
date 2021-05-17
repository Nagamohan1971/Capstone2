# USA Immigration Data ETL Pipeline
### Data Engineering Capstone Project

#### Project Summary
Immigration data, Airports data, USA Demographics data and city temperature data will be used to create a database that is optimized to query and analyze immigration events. An ETL pipeline is to be build with these to data sources to create the database. Finally, the database will be used to access immigration Analysis & behaviour to city based on demographics and location temperatures.


## Database

USA Immigrants Insights database schema has a star design. Start design means that it has one Fact Table having business data, and supporting Dimension Tables. Star DB design is maybe the most common schema used in ETL pipelines since it separates Dimension data into their own tables in a clean way and collects business critical data into the Fact table allowing flexible queries.
The Fact Table can be used Analysis of Immigration data.

#### Data dictionary 

The data dictionary is placed as DataDictionary.md

#### Complete Project Write Up
1. The project is designed as I created two .py files 
	a. create_tables.py - code created for creating table and droping tables.
	b. sql_queries.py - where the queries with respect to creating the tables is coded.

2.	Used pandas and numpy libraries using IDE jupter notebook for getting the data, analysing the data and loading the data to postgreSQL DB.

3.	Used postgreSQL DB for my project as it was open source.

4.	Path of project:- ipynb file as attached.