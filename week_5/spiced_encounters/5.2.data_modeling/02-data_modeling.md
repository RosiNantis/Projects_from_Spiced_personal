# Data modeling

11/04/2022

​	Data is stored in `tables`     
​	The information is connected

### Create a table

```{SQL}
CREATE TABLE [IF NOT EXISTS] tablename (
	column1 datatype(length) column_constraint,
	column2 datatype(length) column_constraint,
	column3 datatype(length) column_constraint,
	table_constraints
);
```

`IF NOT EXISTS` creates table only if it does not exist yet

### Constraints

​	`NOT NULL` - values in column cannot be `NULL`    
​	`UNIQUE` - values in column have to be unique across rows in the table    
​	`PRIMARY KEY` - uniquely identifies rows (table can only have one) `UNIQUE` + `NOT NULL`     
​	`CHECK (...)` - data must satisfy the boolean expression   
​	`FOREIGN KEY` - values (referencing table) must exist in another table (referenced table)    

​	Table constraints are applied on more than one column   
​	Primary keys can span over more than one column `PRIMARY KEY (column1, column3)`       
​	Foreign keys can set to different behavior if the referenced item is deleted (NO ACTION / CASCADE)
​	Constraints can have a name to make them identifiable:     

```{SQL}
CREATE TABLE ... (
price numeric CONSTRAINT positive_price CHECK (price > 0)
);
```

### Data Types

​	`INT` - integer number    
​	`NUMERIC` - floating point number    
​	`TEXT` - long text   
​	`VARCHAR(N)` - text with maximum length of N characters    
​	`DATE` - year/month/day     
​	`TIMESTAMP` - year/month/day hour:min:sec     
​	`SERIAL` - integer that counts up automatically   
​	`BOOL` - boolean    
​	`JSON` - JSON document 

## Commands

​	Delete table

```{SQL}
DROP TABLE tablename;
```

​	Add column
```{SQL}
ALTER TABLE tablename ADD COLUMN columnname datatype(length) column_constraint;
```

## Remove column

```{SQL}
ALTER TABLE tablename DROP COLUMN columnname; 
```

​	Fill table from `csv` file

```{SQL}
COPY tablename(col2, ...) FROM `file.csv` DELIMITER `,` CSV HEADER;
```

## `psql` Commands

`\dt`	-	display tables    
`\d columnname` 	-	display definitions of ont table    
`\c dbname` 			-	connect to the database `dbname`     
`\timing` 				-	switch time measurement of queries on/off    
`\?` 						 -	shows al psql commands   
`\h` 						 -	shows all SQL commands     
`\h SELECT`		   -	shows help for the command SELECT

## Example

```{SQL}
CREATE TABLE author (
id SERIAL,
name VARCHAR(30) NOT NULL,
CONSTRAINT PK_id PRIMARY KEY (id)
);
```

```{SQL}
CREATE TABLE publication (
id SERIAL PRIMARY KEY,
title TEXT NOT NULL,
published DATE NOT NULL,
author INT NOT NULL,
CONSTRAINT FK_author FOREIGN KEY (author) REFERENCES author (id)
);
```

```{SQL}
INSERT INTO author (name) VALUES ('jens');
```

```{SQL}
INSERT INTO publication (title, published, author) 
	VALUES ('yeast is great', '2022-01-01', 01);
```