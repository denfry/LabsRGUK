SELECT 
    dw.idzakaznaryad AS "ID заказ-наряда",
    SUM(dw.stoimostvnch * dw.trudoemkostvnch) AS "Стоимость работ"
FROM 
    autotechcenter.donework dw
JOIN 
    autotechcenter.work w ON dw.workcode = w.workcode
GROUP BY 
    dw.idzakaznaryad;