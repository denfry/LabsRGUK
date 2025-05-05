SELECT 
    a.CodeModel,
    a.NameModel,
    SUM(z.StoimostRabot) AS total_volume
FROM autotechcenter.AutoMobile a
JOIN autotechcenter.ZakazNaryad z ON a.CodeModel = z.CodeModel
GROUP BY a.CodeModel, a.NameModel
ORDER BY a.CodeModel;