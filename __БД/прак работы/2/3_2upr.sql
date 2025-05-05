SELECT 
    a.CodeModel,
    a.NameModel
FROM autotechcenter.AutoMobile a
JOIN autotechcenter.ZakazNaryad z ON a.CodeModel = z.CodeModel
GROUP BY a.CodeModel, a.NameModel
HAVING MIN(z.StoimostRabot) > 30
ORDER BY a.CodeModel;