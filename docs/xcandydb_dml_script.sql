INSERT INTO xcandymin.accuracylevel
("name", "description")
values
	('10%', NULL::character varying),
	('20%', NULL::character varying),
	('30%', NULL::character varying),
	('40%', NULL::character varying),
	('50%', NULL::character varying),
	('60%', NULL::character varying),
	('70%', NULL::character varying),
	('80%', NULL::character varying),
	('90%', NULL::character varying),
	('100%', NULL::character varying);

INSERT INTO xcandymin.forecastlevel
("name", "description")
values
	('LOW', 'Low'),
	('MEDIUM', 'Medium'),
	('HIGH', 'High');

INSERT INTO xcandymin.forecaststate
("name", "description", "low", "high", "level")
values
	('HYPOGLYCEMIA', 'Hypoglycemia', 50, 90, 3),
	('HYPOGLYCEMIA', 'Hypoglycemia', 80, 130, 2),
	('HYPOGLYCEMIA', 'Hypoglycemia', 110, 180, 1);

INSERT INTO xcandymin.accuracystate
("name", "description", "low", "high", "level")
values
	('INITIAL', 'Initial', 0, 10, 3),
	('LEARNING', 'Learning', 11, 50, 2),
	('LEARNED', 'Learned', 51, 90, 1),
	('PERFORMANT', 'Performant', 91, 100, 1);

INSERT INTO xcandymin.actychoice
("name", "description")
values
	('COOK', 'Home cooking'),
	('EAT OUT', 'Eat out');

INSERT INTO xcandymin.actysubtype
("name", "description")
values
	('Low GI', 'Low GI'),
	('Med GI', 'Med GI'),
	('High GI', 'High GI');

INSERT INTO xcandymin.actytype
("name", subtype, choice)
values
	('Eat', 1, 1),
	('Eat', 1, 2);

INSERT INTO xcandymin.accuracy
(since, "interval", interval_unit, "percent", create_date)
values
	('2020-06-25 22:59:31', 30, 'min', 59, current_timestamp),
	('2020-06-25 22:59:31', 60, 'min', 69, current_timestamp);

INSERT INTO xcandymin.forecast
(since, "interval", interval_unit, value, create_date)
values
	('2020-06-25 22:59:31', 30, 'min', 135, current_timestamp),
	('2020-06-25 22:59:31', 60, 'min', 155, current_timestamp);

INSERT INTO xcandymin.glucose
(since, value, num_events, create_date)
values
	('2020-06-17 11:59:31', 110, 2, current_timestamp),
	('2020-06-18 09:19:31', 105, 1, current_timestamp),
	('2020-06-19 11:59:31', 100, 2, current_timestamp),
	('2020-06-20 11:59:31', 92, 2, current_timestamp),
	('2020-06-21 11:59:31', 120, 6, current_timestamp),
	('2020-06-22 11:59:31', 130, 2, current_timestamp),
	('2020-06-23 11:59:31', 110, 4, current_timestamp),
	('2020-06-24 11:59:31', 96, 2, current_timestamp),
	('2020-06-25 22:59:31', 99, 3, current_timestamp);

INSERT INTO xcandymin.livestate
("name", "description")
values
	('CONNECTED', NULL::character varying),
	('OFFLINE', NULL::character varying);

INSERT INTO xcandymin.direction
("name", "description")
values
	('SingleUp', NULL::character varying),
	('DoubleUp', NULL::character varying),
	('SingleDown', NULL::character varying),
	('DoubleDown', NULL::character varying),
	('FortyFiveUp', NULL::character varying),
	('FortyFiveDown', NULL::character varying),
	('Flat', NULL::character varying);
	
INSERT INTO xcandymin.livedata
(since, glucose, state, direction, create_date)
values
	('2020-06-25 22:59:31', 223, 1, 5, current_timestamp);
