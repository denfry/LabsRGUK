WITH stov(tov_kod,tov_name,grup) as  
        (select '010', 'Samsung 32', 'Телевизоры' 
           union 
         select '011', 'LG DF4', 'СВЧ печь' 
           union 
         select '012', 'Bork A3', 'СВЧ печь' 
           union 
         select '013', 'LG 41', 'Телевизоры' 
           union 
         select '014', 'Panasonic 26', 'Телевизоры'), 
     book (book_id,pokup,tov_kod,kol) as 
        (select 1, 'АО Смена', '010',10 
           union 
         select 2, 'ООО Темп', '011',12 
           union 
         select 3, 'АО Смена', '011',25 
           union 
         select 4, 'АО Смена', null,16 
           union 
         select 5, null, '012',8 
           union 
         select 6, 'ПАО Крок', '013',18) 
SELECT *
FROM book b
LEFT OUTER JOIN stov s ON b.tov_kod = s.tov_kod;


