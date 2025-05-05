SET SEARCH_PATH TO autotechcenter;

-- 1. Загрузка справочника видов работ
copy typeofwork FROM 'D:\csv\typeofwork.csv' DELIMITER ';' CSV HEADER;

-- 2. Загрузка данных о работах
copy work FROM 'D:\csv\work.csv' DELIMITER ';' CSV HEADER;

-- 3. Загрузка данных об автомобилях
copy automobile FROM 'D:\csv\automobile.csv' DELIMITER ';' CSV HEADER;

-- 4. Загрузка данных о клиентах
copy client FROM 'D:\csv\client.csv' DELIMITER ';' CSV HEADER;

-- 5. Загрузка данных о заказ-нарядах
copy zakaznaryad FROM 'D:\csv\zakaznaryad.csv' DELIMITER ';' CSV HEADER;

-- 6. Загрузка данных о выполненных работах
copy donework FROM 'D:\csv\donework.csv' DELIMITER ';' CSV HEADER;