CREATE TABLE "user_types" (
	"type_id"	INTEGER,
	"name"	TEXT,
	PRIMARY KEY("type_id" AUTOINCREMENT)
);

CREATE TABLE "users" (
	"user_id"	INTEGER,
	"fio"	TEXT,
	"phone" TEXT,
	"login"	TEXT,
	"password"	TEXT,
	"type_id"	INTEGER,
	PRIMARY KEY("user_id" AUTOINCREMENT),
	FOREIGN KEY("type_id") REFERENCES user_types("type_id") ON DELETE NO ACTION
);

CREATE TABLE "car_types" (
	"type_id"	INTEGER,
	"name"	TEXT,
	PRIMARY KEY("type_id" AUTOINCREMENT)
);

CREATE TABLE "car_models" (
	"model_id"	INTEGER,
	"name"	TEXT,
	PRIMARY KEY("model_id" AUTOINCREMENT)
);

CREATE TABLE "car_brands" (
	"brand_id"	INTEGER,
	"name"	TEXT,
	PRIMARY KEY("brand_id" AUTOINCREMENT)
);

CREATE TABLE "cars" (
	"car_id"	INTEGER,
	"type_id"	INTEGER,
	"brand_id"	INTEGER,
	"model_id"	INTEGER,
	PRIMARY KEY("car_id" AUTOINCREMENT),
	FOREIGN KEY("type_id") REFERENCES car_types("type_id") ON DELETE NO ACTION,
	FOREIGN KEY("brand_id") REFERENCES car_models("model_id") ON DELETE NO ACTION,
	FOREIGN KEY("model_id") REFERENCES car_brands("brand_id") ON DELETE NO ACTION
);

CREATE TABLE "status" (
	"status_id"	INTEGER,
	"name"	TEXT,
	PRIMARY KEY("status_id" AUTOINCREMENT)
);

CREATE TABLE "requests" (
	"request_id"	INTEGER,
	"start_date"	TEXT,
	"complete_date"	TEXT,
	"car_id"	INTEGER,
	"client_id"	INTEGER,
	"description"	TEXT,
	"status_id"	INTEGER,
	"master_id"	INTEGER,
	PRIMARY KEY("request_id" AUTOINCREMENT),
	FOREIGN KEY("car_id") REFERENCES cars(car_id) ON DELETE NO ACTION,
	FOREIGN KEY("client_id") REFERENCES users("user_id") ON DELETE NO ACTION,
	FOREIGN KEY("status_id") REFERENCES status("status_id") ON DELETE NO ACTION,
	FOREIGN KEY("master_id") REFERENCES users("user_id") ON DELETE NO ACTION
);

CREATE TABLE "comments" (
	"comment_id"	INTEGER,
	"message"	TEXT,
	"master_id"	INTEGER,
	"request_id"	INTEGER,
	PRIMARY KEY("comment_id" AUTOINCREMENT),
	FOREIGN KEY("master_id") REFERENCES users("user_id") ON DELETE CASCADE,
	FOREIGN KEY("request_id") REFERENCES requests("request_id") ON DELETE CASCADE
);

CREATE TABLE "parts" (
	"part_id"	INTEGER,
	"name"	TEXT,
	PRIMARY KEY("part_id" AUTOINCREMENT)
);

CREATE TABLE "part_request" (
	"pr_id"	INTEGER,
	"request_id"	INTEGER,
	"part_id"	INTEGER,
	"received"	INTEGER,
	PRIMARY KEY("pr_id" AUTOINCREMENT),
	FOREIGN KEY("request_id") REFERENCES requests("request_id") ON DELETE CASCADE,
	FOREIGN KEY("part_id") REFERENCES parts("part_id") ON DELETE CASCADE
);




