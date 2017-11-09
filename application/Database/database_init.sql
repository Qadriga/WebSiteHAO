BEGIN TRANSACTION;
CREATE TABLE "upcommingDates" (
	`_link`	TEXT,
	`_date`	Real NOT NULL DEFAULT 'julianday("1900-01-01")',
	`_name`	TEXT NOT NULL,
	PRIMARY KEY(_date)
);
CREATE TABLE "dates" (
	`d_day`	REAL NOT NULL DEFAULT 'julanday(1900-01-01)',
	`d_link_to_page`	TEXT DEFAULT NULL,
	`d_text`	TEXT,
	`d_name`	TEXT NOT NULL DEFAULT ""
);
COMMIT;
