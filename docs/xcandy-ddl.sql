-- xcandy.accuracy definition

-- Drop table

-- DROP TABLE xcandy.accuracy;

CREATE TABLE xcandy.accuracy (
	id serial NOT NULL,
	since timestamp NOT NULL,
	"interval" int4 NOT NULL,
	interval_unit varchar(5) NULL,
	"percent" int4 NOT NULL,
	create_date timestamp NULL DEFAULT now(),
	CONSTRAINT accuracy_pkey PRIMARY KEY (id)
);


-- xcandy.accuracylevel definition

-- Drop table

-- DROP TABLE xcandy.accuracylevel;

CREATE TABLE xcandy.accuracylevel (
	id serial NOT NULL,
	"name" varchar(30) NOT NULL,
	description varchar(60) NULL DEFAULT NULL::character varying,
	CONSTRAINT accuracylevel_pkey PRIMARY KEY (id)
);


-- xcandy.activitylog definition

-- Drop table

-- DROP TABLE xcandy.activitylog;

CREATE TABLE xcandy.activitylog (
	id serial NOT NULL,
	since timestamp NOT NULL,
	"hour" time NOT NULL,
	"type" int4 NULL,
	create_date timestamp NULL DEFAULT now(),
	CONSTRAINT activitylog_pkey PRIMARY KEY (id)
);


-- xcandy.actychoice definition

-- Drop table

-- DROP TABLE xcandy.actychoice;

CREATE TABLE xcandy.actychoice (
	id serial NOT NULL,
	"name" varchar(30) NOT NULL,
	description varchar(60) NULL DEFAULT NULL::character varying,
	CONSTRAINT actychoice_pkey PRIMARY KEY (id)
);


-- xcandy.actysubtype definition

-- Drop table

-- DROP TABLE xcandy.actysubtype;

CREATE TABLE xcandy.actysubtype (
	id serial NOT NULL,
	"name" varchar(30) NOT NULL,
	description varchar(60) NULL DEFAULT NULL::character varying,
	CONSTRAINT actysubtype_pkey PRIMARY KEY (id)
);


-- xcandy.auth_group definition

-- Drop table

-- DROP TABLE xcandy.auth_group;

CREATE TABLE xcandy.auth_group (
	id serial NOT NULL,
	"name" varchar(150) NOT NULL,
	CONSTRAINT auth_group_name_key UNIQUE (name),
	CONSTRAINT auth_group_pkey PRIMARY KEY (id)
);
CREATE INDEX auth_group_name_a6ea08ec_like ON xcandy.auth_group USING btree (name varchar_pattern_ops);


-- xcandy.auth_user definition

-- Drop table

-- DROP TABLE xcandy.auth_user;

CREATE TABLE xcandy.auth_user (
	id serial NOT NULL,
	"password" varchar(128) NOT NULL,
	last_login timestamptz NULL,
	is_superuser bool NOT NULL,
	username varchar(150) NOT NULL,
	first_name varchar(30) NOT NULL,
	last_name varchar(150) NOT NULL,
	email varchar(254) NOT NULL,
	is_staff bool NOT NULL,
	is_active bool NOT NULL,
	date_joined timestamptz NOT NULL,
	CONSTRAINT auth_user_pkey PRIMARY KEY (id),
	CONSTRAINT auth_user_username_key UNIQUE (username)
);
CREATE INDEX auth_user_username_6821ab7c_like ON xcandy.auth_user USING btree (username varchar_pattern_ops);


-- xcandy.datasource definition

-- Drop table

-- DROP TABLE xcandy.datasource;

CREATE TABLE xcandy.datasource (
	id serial NOT NULL,
	"name" varchar(10) NOT NULL,
	description varchar(100) NOT NULL,
	enabled bool NULL DEFAULT true,
	CONSTRAINT datasource_pkey PRIMARY KEY (id)
);


-- xcandy.direction definition

-- Drop table

-- DROP TABLE xcandy.direction;

CREATE TABLE xcandy.direction (
	id serial NOT NULL,
	"name" varchar(30) NOT NULL,
	description varchar(60) NULL DEFAULT NULL::character varying,
	CONSTRAINT direction_pkey PRIMARY KEY (id)
);


-- xcandy.django_content_type definition

-- Drop table

-- DROP TABLE xcandy.django_content_type;

CREATE TABLE xcandy.django_content_type (
	id serial NOT NULL,
	app_label varchar(100) NOT NULL,
	model varchar(100) NOT NULL,
	CONSTRAINT django_content_type_app_label_model_76bd3d3b_uniq UNIQUE (app_label, model),
	CONSTRAINT django_content_type_pkey PRIMARY KEY (id)
);


-- xcandy.django_migrations definition

-- Drop table

-- DROP TABLE xcandy.django_migrations;

CREATE TABLE xcandy.django_migrations (
	id serial NOT NULL,
	app varchar(255) NOT NULL,
	"name" varchar(255) NOT NULL,
	applied timestamptz NOT NULL,
	CONSTRAINT django_migrations_pkey PRIMARY KEY (id)
);


-- xcandy.django_session definition

-- Drop table

-- DROP TABLE xcandy.django_session;

CREATE TABLE xcandy.django_session (
	session_key varchar(40) NOT NULL,
	session_data text NOT NULL,
	expire_date timestamptz NOT NULL,
	CONSTRAINT django_session_pkey PRIMARY KEY (session_key)
);
CREATE INDEX django_session_expire_date_a5c62663 ON xcandy.django_session USING btree (expire_date);
CREATE INDEX django_session_session_key_c0390e0f_like ON xcandy.django_session USING btree (session_key varchar_pattern_ops);


-- xcandy.forecast definition

-- Drop table

-- DROP TABLE xcandy.forecast;

CREATE TABLE xcandy.forecast (
	id serial NOT NULL,
	since timestamp NOT NULL,
	"interval" int4 NOT NULL,
	interval_unit varchar(5) NULL,
	value int4 NOT NULL,
	create_date timestamp NULL DEFAULT now(),
	CONSTRAINT forecast_pkey PRIMARY KEY (id)
);


-- xcandy.forecastlevel definition

-- Drop table

-- DROP TABLE xcandy.forecastlevel;

CREATE TABLE xcandy.forecastlevel (
	id serial NOT NULL,
	"name" varchar(30) NOT NULL,
	description varchar(60) NULL DEFAULT NULL::character varying,
	CONSTRAINT forecastlevel_pkey PRIMARY KEY (id)
);


-- xcandy.glucose definition

-- Drop table

-- DROP TABLE xcandy.glucose;

CREATE TABLE xcandy.glucose (
	id serial NOT NULL,
	since timestamp NOT NULL,
	value int4 NOT NULL,
	num_events int4 NULL,
	create_date timestamp NULL DEFAULT now(),
	CONSTRAINT glucose_pkey PRIMARY KEY (id)
);


-- xcandy.livestate definition

-- Drop table

-- DROP TABLE xcandy.livestate;

CREATE TABLE xcandy.livestate (
	id serial NOT NULL,
	"name" varchar(30) NOT NULL,
	description varchar(60) NULL DEFAULT NULL::character varying,
	CONSTRAINT livestate_pkey PRIMARY KEY (id)
);


-- xcandy.social_auth_association definition

-- Drop table

-- DROP TABLE xcandy.social_auth_association;

CREATE TABLE xcandy.social_auth_association (
	id serial NOT NULL,
	server_url varchar(255) NOT NULL,
	handle varchar(255) NOT NULL,
	secret varchar(255) NOT NULL,
	issued int4 NOT NULL,
	lifetime int4 NOT NULL,
	assoc_type varchar(64) NOT NULL,
	CONSTRAINT social_auth_association_pkey PRIMARY KEY (id),
	CONSTRAINT social_auth_association_server_url_handle_078befa2_uniq UNIQUE (server_url, handle)
);


-- xcandy.social_auth_code definition

-- Drop table

-- DROP TABLE xcandy.social_auth_code;

CREATE TABLE xcandy.social_auth_code (
	id serial NOT NULL,
	email varchar(254) NOT NULL,
	code varchar(32) NOT NULL,
	verified bool NOT NULL,
	"timestamp" timestamptz NOT NULL,
	CONSTRAINT social_auth_code_email_code_801b2d02_uniq UNIQUE (email, code),
	CONSTRAINT social_auth_code_pkey PRIMARY KEY (id)
);
CREATE INDEX social_auth_code_code_a2393167 ON xcandy.social_auth_code USING btree (code);
CREATE INDEX social_auth_code_code_a2393167_like ON xcandy.social_auth_code USING btree (code varchar_pattern_ops);
CREATE INDEX social_auth_code_timestamp_176b341f ON xcandy.social_auth_code USING btree ("timestamp");


-- xcandy.social_auth_nonce definition

-- Drop table

-- DROP TABLE xcandy.social_auth_nonce;

CREATE TABLE xcandy.social_auth_nonce (
	id serial NOT NULL,
	server_url varchar(255) NOT NULL,
	"timestamp" int4 NOT NULL,
	salt varchar(65) NOT NULL,
	CONSTRAINT social_auth_nonce_pkey PRIMARY KEY (id),
	CONSTRAINT social_auth_nonce_server_url_timestamp_salt_f6284463_uniq UNIQUE (server_url, "timestamp", salt)
);


-- xcandy.social_auth_partial definition

-- Drop table

-- DROP TABLE xcandy.social_auth_partial;

CREATE TABLE xcandy.social_auth_partial (
	id serial NOT NULL,
	"token" varchar(32) NOT NULL,
	next_step int2 NOT NULL,
	backend varchar(32) NOT NULL,
	"data" text NOT NULL,
	"timestamp" timestamptz NOT NULL,
	CONSTRAINT social_auth_partial_next_step_check CHECK ((next_step >= 0)),
	CONSTRAINT social_auth_partial_pkey PRIMARY KEY (id)
);
CREATE INDEX social_auth_partial_timestamp_50f2119f ON xcandy.social_auth_partial USING btree ("timestamp");
CREATE INDEX social_auth_partial_token_3017fea3 ON xcandy.social_auth_partial USING btree (token);
CREATE INDEX social_auth_partial_token_3017fea3_like ON xcandy.social_auth_partial USING btree (token varchar_pattern_ops);


-- xcandy.timezone definition

-- Drop table

-- DROP TABLE xcandy.timezone;

CREATE TABLE xcandy.timezone (
	id serial NOT NULL,
	"name" varchar(120) NOT NULL,
	toffset int4 NULL,
	enabled bool NULL DEFAULT true,
	gmt_offset varchar(20) NULL DEFAULT NULL::character varying,
	use_daylight bool NULL DEFAULT false,
	CONSTRAINT timezone_pkey PRIMARY KEY (id)
);


-- xcandy.accuracystate definition

-- Drop table

-- DROP TABLE xcandy.accuracystate;

CREATE TABLE xcandy.accuracystate (
	id serial NOT NULL,
	"name" varchar(30) NOT NULL,
	description varchar(60) NULL DEFAULT NULL::character varying,
	low int4 NOT NULL,
	high int4 NOT NULL,
	"level" int4 NULL,
	CONSTRAINT accuracystate_pkey PRIMARY KEY (id),
	CONSTRAINT accuracystate_level_fkey FOREIGN KEY (level) REFERENCES accuracylevel(id)
);


-- xcandy.actytype definition

-- Drop table

-- DROP TABLE xcandy.actytype;

CREATE TABLE xcandy.actytype (
	id serial NOT NULL,
	"name" varchar(20) NOT NULL,
	subtype int4 NULL,
	choice int4 NULL,
	CONSTRAINT actytype_pkey PRIMARY KEY (id),
	CONSTRAINT actytype_choice_fkey FOREIGN KEY (choice) REFERENCES actychoice(id),
	CONSTRAINT actytype_subtype_fkey FOREIGN KEY (subtype) REFERENCES actysubtype(id)
);


-- xcandy.auth_permission definition

-- Drop table

-- DROP TABLE xcandy.auth_permission;

CREATE TABLE xcandy.auth_permission (
	id serial NOT NULL,
	"name" varchar(255) NOT NULL,
	content_type_id int4 NOT NULL,
	codename varchar(100) NOT NULL,
	CONSTRAINT auth_permission_content_type_id_codename_01ab375a_uniq UNIQUE (content_type_id, codename),
	CONSTRAINT auth_permission_pkey PRIMARY KEY (id),
	CONSTRAINT auth_permission_content_type_id_2f476e4b_fk_django_co FOREIGN KEY (content_type_id) REFERENCES django_content_type(id) DEFERRABLE INITIALLY DEFERRED
);
CREATE INDEX auth_permission_content_type_id_2f476e4b ON xcandy.auth_permission USING btree (content_type_id);


-- xcandy.auth_user_groups definition

-- Drop table

-- DROP TABLE xcandy.auth_user_groups;

CREATE TABLE xcandy.auth_user_groups (
	id serial NOT NULL,
	user_id int4 NOT NULL,
	group_id int4 NOT NULL,
	CONSTRAINT auth_user_groups_pkey PRIMARY KEY (id),
	CONSTRAINT auth_user_groups_user_id_group_id_94350c0c_uniq UNIQUE (user_id, group_id),
	CONSTRAINT auth_user_groups_group_id_97559544_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES auth_group(id) DEFERRABLE INITIALLY DEFERRED,
	CONSTRAINT auth_user_groups_user_id_6a12ed8b_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED
);
CREATE INDEX auth_user_groups_group_id_97559544 ON xcandy.auth_user_groups USING btree (group_id);
CREATE INDEX auth_user_groups_user_id_6a12ed8b ON xcandy.auth_user_groups USING btree (user_id);


-- xcandy.auth_user_user_permissions definition

-- Drop table

-- DROP TABLE xcandy.auth_user_user_permissions;

CREATE TABLE xcandy.auth_user_user_permissions (
	id serial NOT NULL,
	user_id int4 NOT NULL,
	permission_id int4 NOT NULL,
	CONSTRAINT auth_user_user_permissions_pkey PRIMARY KEY (id),
	CONSTRAINT auth_user_user_permissions_user_id_permission_id_14a6b632_uniq UNIQUE (user_id, permission_id),
	CONSTRAINT auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES auth_permission(id) DEFERRABLE INITIALLY DEFERRED,
	CONSTRAINT auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED
);
CREATE INDEX auth_user_user_permissions_permission_id_1fbb5f2c ON xcandy.auth_user_user_permissions USING btree (permission_id);
CREATE INDEX auth_user_user_permissions_user_id_a95ead1b ON xcandy.auth_user_user_permissions USING btree (user_id);


-- xcandy.django_admin_log definition

-- Drop table

-- DROP TABLE xcandy.django_admin_log;

CREATE TABLE xcandy.django_admin_log (
	id serial NOT NULL,
	action_time timestamptz NOT NULL,
	object_id text NULL,
	object_repr varchar(200) NOT NULL,
	action_flag int2 NOT NULL,
	change_message text NOT NULL,
	content_type_id int4 NULL,
	user_id int4 NOT NULL,
	CONSTRAINT django_admin_log_action_flag_check CHECK ((action_flag >= 0)),
	CONSTRAINT django_admin_log_pkey PRIMARY KEY (id),
	CONSTRAINT django_admin_log_content_type_id_c4bce8eb_fk_django_co FOREIGN KEY (content_type_id) REFERENCES django_content_type(id) DEFERRABLE INITIALLY DEFERRED,
	CONSTRAINT django_admin_log_user_id_c564eba6_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED
);
CREATE INDEX django_admin_log_content_type_id_c4bce8eb ON xcandy.django_admin_log USING btree (content_type_id);
CREATE INDEX django_admin_log_user_id_c564eba6 ON xcandy.django_admin_log USING btree (user_id);


-- xcandy.forecaststate definition

-- Drop table

-- DROP TABLE xcandy.forecaststate;

CREATE TABLE xcandy.forecaststate (
	id serial NOT NULL,
	"name" varchar(30) NOT NULL,
	description varchar(60) NULL DEFAULT NULL::character varying,
	low int4 NOT NULL,
	high int4 NOT NULL,
	"level" int4 NULL,
	CONSTRAINT forecaststate_pkey PRIMARY KEY (id),
	CONSTRAINT forecaststate_level_fkey FOREIGN KEY (level) REFERENCES forecastlevel(id)
);


-- xcandy.livedata definition

-- Drop table

-- DROP TABLE xcandy.livedata;

CREATE TABLE xcandy.livedata (
	id serial NOT NULL,
	since timestamp NOT NULL,
	glucose int4 NOT NULL,
	state int4 NULL,
	direction int4 NULL,
	create_date timestamp NULL DEFAULT now(),
	CONSTRAINT livedata_pkey PRIMARY KEY (id),
	CONSTRAINT livedata_direction_fkey FOREIGN KEY (direction) REFERENCES direction(id),
	CONSTRAINT livedata_state_fkey FOREIGN KEY (state) REFERENCES livestate(id)
);


-- xcandy.nightscout definition

-- Drop table

-- DROP TABLE xcandy.nightscout;

CREATE TABLE xcandy.nightscout (
	id serial NOT NULL,
	datasource int4 NULL,
	url varchar(255) NULL DEFAULT NULL::character varying,
	secret varchar(255) NULL DEFAULT NULL::character varying,
	timezone int4 NULL,
	CONSTRAINT source_pkey PRIMARY KEY (id),
	CONSTRAINT source_datasource_fkey FOREIGN KEY (datasource) REFERENCES datasource(id),
	CONSTRAINT source_timezone_fkey FOREIGN KEY (timezone) REFERENCES timezone(id)
);


-- xcandy.recommended definition

-- Drop table

-- DROP TABLE xcandy.recommended;

CREATE TABLE xcandy.recommended (
	id serial NOT NULL,
	since timestamp NOT NULL,
	rtype int4 NULL,
	create_date timestamp NULL DEFAULT now(),
	CONSTRAINT recommended_pkey PRIMARY KEY (id),
	CONSTRAINT recommended_rtype_fkey FOREIGN KEY (rtype) REFERENCES actytype(id)
);


-- xcandy.social_auth_usersocialauth definition

-- Drop table

-- DROP TABLE xcandy.social_auth_usersocialauth;

CREATE TABLE xcandy.social_auth_usersocialauth (
	id serial NOT NULL,
	provider varchar(32) NOT NULL,
	uid varchar(255) NOT NULL,
	extra_data text NOT NULL,
	user_id int4 NOT NULL,
	created timestamptz NOT NULL,
	modified timestamptz NOT NULL,
	CONSTRAINT social_auth_usersocialauth_pkey PRIMARY KEY (id),
	CONSTRAINT social_auth_usersocialauth_provider_uid_e6b5e668_uniq UNIQUE (provider, uid),
	CONSTRAINT social_auth_usersocialauth_user_id_17d28448_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED
);
CREATE INDEX social_auth_usersocialauth_uid_796e51dc ON xcandy.social_auth_usersocialauth USING btree (uid);
CREATE INDEX social_auth_usersocialauth_uid_796e51dc_like ON xcandy.social_auth_usersocialauth USING btree (uid varchar_pattern_ops);
CREATE INDEX social_auth_usersocialauth_user_id_17d28448 ON xcandy.social_auth_usersocialauth USING btree (user_id);


-- xcandy."source" definition

-- Drop table

-- DROP TABLE xcandy."source";

CREATE TABLE xcandy."source" (
	id serial NOT NULL,
	type_id int4 NULL,
	url varchar(255) NULL DEFAULT NULL::character varying,
	secret varchar(255) NULL DEFAULT NULL::character varying,
	"location" varchar(100) NULL DEFAULT NULL::character varying,
	timezone_id int4 NULL,
	username varchar(100) NULL DEFAULT NULL::character varying,
	"password" varchar(255) NULL DEFAULT NULL::character varying,
	CONSTRAINT source_pkey1 PRIMARY KEY (id),
	CONSTRAINT source_timezone_fkey1 FOREIGN KEY (timezone_id) REFERENCES timezone(id),
	CONSTRAINT source_type_fkey FOREIGN KEY (type_id) REFERENCES datasource(id)
);


-- xcandy.webapp_profile definition

-- Drop table

-- DROP TABLE xcandy.webapp_profile;

CREATE TABLE xcandy.webapp_profile (
	id serial NOT NULL,
	first_name varchar(100) NOT NULL,
	last_name varchar(100) NOT NULL,
	email varchar(150) NOT NULL,
	signup_confirmation bool NOT NULL,
	user_id int4 NOT NULL,
	accept bool NOT NULL,
	"source" int4 NULL,
	CONSTRAINT webapp_profile_pkey PRIMARY KEY (id),
	CONSTRAINT webapp_profile_user_id_key UNIQUE (user_id),
	CONSTRAINT webapp_profile_source_3c0e3503_fk_source_id FOREIGN KEY (source) REFERENCES source(id) DEFERRABLE INITIALLY DEFERRED,
	CONSTRAINT webapp_profile_user_id_0259005d_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED
);


-- xcandy.webapp_profile_accuracy definition

-- Drop table

-- DROP TABLE xcandy.webapp_profile_accuracy;

CREATE TABLE xcandy.webapp_profile_accuracy (
	id serial NOT NULL,
	profile_id int4 NULL,
	accuracy_id int4 NULL,
	CONSTRAINT webapp_profile_accuracy_pkey PRIMARY KEY (id),
	CONSTRAINT webapp_profile_accuracy_accuracy_id_fkey FOREIGN KEY (accuracy_id) REFERENCES accuracy(id),
	CONSTRAINT webapp_profile_accuracy_profile_id_fkey FOREIGN KEY (profile_id) REFERENCES webapp_profile(id)
);


-- xcandy.webapp_profile_activitylog definition

-- Drop table

-- DROP TABLE xcandy.webapp_profile_activitylog;

CREATE TABLE xcandy.webapp_profile_activitylog (
	id serial NOT NULL,
	profile_id int4 NULL,
	activitylog_id int4 NULL,
	CONSTRAINT webapp_profile_activitylog_pkey PRIMARY KEY (id),
	CONSTRAINT webapp_profile_activitylog_activitylog_id_fkey FOREIGN KEY (activitylog_id) REFERENCES activitylog(id),
	CONSTRAINT webapp_profile_activitylog_profile_id_fkey FOREIGN KEY (profile_id) REFERENCES webapp_profile(id)
);


-- xcandy.webapp_profile_forecast definition

-- Drop table

-- DROP TABLE xcandy.webapp_profile_forecast;

CREATE TABLE xcandy.webapp_profile_forecast (
	id serial NOT NULL,
	profile_id int4 NULL,
	forecast_id int4 NULL,
	CONSTRAINT webapp_profile_forecast_pkey PRIMARY KEY (id),
	CONSTRAINT webapp_profile_forecast_forecast_id_fkey FOREIGN KEY (forecast_id) REFERENCES forecast(id),
	CONSTRAINT webapp_profile_forecast_profile_id_fkey FOREIGN KEY (profile_id) REFERENCES webapp_profile(id)
);


-- xcandy.webapp_profile_glucose definition

-- Drop table

-- DROP TABLE xcandy.webapp_profile_glucose;

CREATE TABLE xcandy.webapp_profile_glucose (
	id serial NOT NULL,
	profile_id int4 NULL,
	glucose_id int4 NULL,
	CONSTRAINT webapp_profile_glucose_pkey PRIMARY KEY (id),
	CONSTRAINT webapp_profile_glucose_glucose_id_fkey FOREIGN KEY (glucose_id) REFERENCES glucose(id),
	CONSTRAINT webapp_profile_glucose_profile_id_fkey FOREIGN KEY (profile_id) REFERENCES webapp_profile(id)
);


-- xcandy.webapp_profile_livedata definition

-- Drop table

-- DROP TABLE xcandy.webapp_profile_livedata;

CREATE TABLE xcandy.webapp_profile_livedata (
	id serial NOT NULL,
	profile_id int4 NULL,
	livedata_id int4 NULL,
	CONSTRAINT webapp_profile_livedata_pkey PRIMARY KEY (id),
	CONSTRAINT webapp_profile_livedata_livedata_id_fkey FOREIGN KEY (livedata_id) REFERENCES livedata(id),
	CONSTRAINT webapp_profile_livedata_profile_id_fkey FOREIGN KEY (profile_id) REFERENCES webapp_profile(id)
);


-- xcandy.webapp_profile_recommended definition

-- Drop table

-- DROP TABLE xcandy.webapp_profile_recommended;

CREATE TABLE xcandy.webapp_profile_recommended (
	id serial NOT NULL,
	profile_id int4 NULL,
	recommended_id int4 NULL,
	CONSTRAINT webapp_profile_recommended_pkey PRIMARY KEY (id),
	CONSTRAINT webapp_profile_recommended_profile_id_fkey FOREIGN KEY (profile_id) REFERENCES webapp_profile(id),
	CONSTRAINT webapp_profile_recommended_recommended_id_fkey FOREIGN KEY (recommended_id) REFERENCES recommended(id)
);


-- xcandy.auth_group_permissions definition

-- Drop table

-- DROP TABLE xcandy.auth_group_permissions;

CREATE TABLE xcandy.auth_group_permissions (
	id serial NOT NULL,
	group_id int4 NOT NULL,
	permission_id int4 NOT NULL,
	CONSTRAINT auth_group_permissions_group_id_permission_id_0cd325b0_uniq UNIQUE (group_id, permission_id),
	CONSTRAINT auth_group_permissions_pkey PRIMARY KEY (id),
	CONSTRAINT auth_group_permissio_permission_id_84c5c92e_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES auth_permission(id) DEFERRABLE INITIALLY DEFERRED,
	CONSTRAINT auth_group_permissions_group_id_b120cbf9_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES auth_group(id) DEFERRABLE INITIALLY DEFERRED
);
CREATE INDEX auth_group_permissions_group_id_b120cbf9 ON xcandy.auth_group_permissions USING btree (group_id);
CREATE INDEX auth_group_permissions_permission_id_84c5c92e ON xcandy.auth_group_permissions USING btree (permission_id);