SET SEARCH_PATH TO autotechcenter;
copy typeofwork TO 'D:\csv\frompg\typeofwork.csv' DELIMITER ','
	CSV HEADER;
COPY work TO 'D:\csv\frompg\work.csv' DELIMITER ','
	CSV HEADER;
COPY donework TO 'D:\csv\frompg\donework.csv' DELIMITER ','
	CSV HEADER;
COPY automobile TO 'D:\csv\frompg\automobile.csv' DELIMITER ','
	CSV HEADER;
COPY client TO 'D:\csv\frompg\client.csv' DELIMITER ','
	CSV HEADER;
COPY zakaznaryad TO 'D:\csv\frompg\zakaznaryad.csv' DELIMITER ','
	CSV HEADER;