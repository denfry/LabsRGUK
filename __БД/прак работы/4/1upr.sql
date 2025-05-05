WITH avg_cost AS (
    SELECT AVG(StoimostRabot) AS avg_order_cost
    FROM ZakazNaryad
)
SELECT 
    a.NameModel AS "Модель автомобиля",
    c.FIO AS "ФИО клиента",
    zn.NumberZakaz AS "Номер заказа",
    zn.StoimostRabot AS "Стоимость работ"
FROM ZakazNaryad zn
INNER JOIN AutoMobile a ON zn.CodeModel = a.CodeModel
INNER JOIN Client c ON zn.CodeClient = c.CodeClient,
avg_cost
WHERE zn.StoimostRabot < avg_cost.avg_order_cost
ORDER BY a.NameModel, c.FIO;