SELECT 
    c.CodeClient,
    c.FIO,
    SUM(z.StoimostRabot) AS total_cost
FROM autotechcenter.Client c
JOIN autotechcenter.ZakazNaryad z ON c.CodeClient = z.CodeClient
GROUP BY c.CodeClient, c.FIO
HAVING SUM(z.StoimostRabot) > 2000
ORDER BY c.CodeClient;