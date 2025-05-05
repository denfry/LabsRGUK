SELECT 
    c.CodeClient,
    c.FIO,
    COUNT(DISTINCT dw.WorkCode) AS unique_works
FROM autotechcenter.Client c
JOIN autotechcenter.ZakazNaryad z ON c.CodeClient = z.CodeClient
JOIN autotechcenter.DoneWork dw ON z.IDZakazNaryad = dw.IDZakazNaryad
GROUP BY c.CodeClient, c.FIO
ORDER BY c.CodeClient;