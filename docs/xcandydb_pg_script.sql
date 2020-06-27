CREATE TABLE livestate (
	id serial PRIMARY KEY,
	name varchar(30) not NULL,
	description varchar(60) default null
);

CREATE TABLE direction (
	id serial PRIMARY KEY,
	name varchar(30) not NULL,
	description varchar(60) default null
);

CREATE TABLE livedata (
	id serial PRIMARY KEY,
	since date not null,
	glucose int NOT NULL,
	state int references livestate(id),
	direction int references direction(id),
	create_date date
);

CREATE TABLE forecastlevel (
	id serial PRIMARY KEY,
	name varchar(30) not NULL,
	description varchar(60) default null
);

CREATE TABLE forecaststate (
	id serial PRIMARY KEY,
	name varchar(30) not NULL,
	description varchar(60) default null,
	low int not null,
	high int not null,
	level int references forecastlevel(id)
);

CREATE TABLE forecast (
	id serial PRIMARY KEY,
	since date not null,
	interval int NOT NULL,
	interval_unit varchar(5),
	value int not null,
	create_date date
);

CREATE TABLE accuracylevel (
	id serial PRIMARY KEY,
	name varchar(30) not NULL,
	description varchar(60) default null
);

CREATE TABLE accuracystate (
	id serial PRIMARY KEY,
	name varchar(30) not NULL,
	description varchar(60) default null,
	low int not null,
	high int not null,
	level int references accuracylevel(id)
);

CREATE TABLE accuracy (
	id serial PRIMARY KEY,
	since date not null,
	interval int NOT NULL,
	interval_unit varchar(5),
	percent int not null,
	create_date date
);

CREATE TABLE glucose (
	id serial PRIMARY KEY,
	since date not null,
	value int not null,
	num_events int,
	create_date date
);

CREATE TABLE actysubtype (
	id serial PRIMARY KEY,
	name varchar(30) not NULL,
	description varchar(60) default null
);

CREATE TABLE actychoice (
	id serial PRIMARY KEY,
	name varchar(30) not NULL,
	description varchar(60) default null
);

CREATE TABLE actytype (
	id serial PRIMARY KEY,
	name varchar(20) not null,
	subtype int references actysubtype(id),
	choice int references actychoice(id)
);

CREATE TABLE recommended (
	id serial PRIMARY KEY,
	since date not null,
	rtype int references actytype(id),
	create_date date
);

CREATE TABLE activitylog (
	id serial PRIMARY KEY,
	since date not null,
	hour time not null,
	type int references actytype(id),
	create_date date
);



