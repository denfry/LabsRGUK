WITH avg_work_cost AS (
    SELECT AVG(StoimostOdinNCH) AS avg_cost
    FROM Work
),
work_type_avg AS (
    SELECT 
        t.NameTypeWork,
        AVG(w.StoimostOdinNCH) AS avg_type_cost
    FROM Work w
    INNER JOIN TypeOfWork t ON w.WorkTypeCode = t.WorkTypeCode
    GROUP BY t.NameTypeWork
)
SELECT 
    wta.NameTypeWork AS "Тип работы",
    ROUND(wta.avg_type_cost, 2) AS "Средняя стоимость"
FROM work_type_avg wta, avg_work_cost awc
WHERE wta.avg_type_cost < awc.avg_cost
ORDER BY wta.avg_type_cost DESC;