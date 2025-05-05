SELECT 
    zn.NumberZakaz AS order_number,
    zn.DateOformlenie AS order_date,
    c.FIO AS client_name,
    am.NameModel AS car_model,
    w.NameWork AS work_name,
    dw.TrudoemkostVnch AS labor_hours,
    dw.StoimostVnch AS work_cost
FROM autotechcenter.ZakazNaryad zn
JOIN autotechcenter.Client c ON zn.CodeClient = c.CodeClient
JOIN autotechcenter.AutoMobile am ON zn.CodeModel = am.CodeModel
JOIN autotechcenter.DoneWork dw ON zn.IDZakazNaryad = dw.IDZakazNaryad
JOIN autotechcenter.work w ON dw.WorkCode = w.WorkCode
WHERE zn.DateOformlenie BETWEEN '2023-10-01' AND '2023-10-10'
ORDER BY zn.DateOformlenie, zn.NumberZakaz;