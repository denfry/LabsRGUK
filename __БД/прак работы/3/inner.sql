SELECT 
    w.WorkCode, 
    w.NameWork, 
    w.StoimostOdinNCH AS unit_cost, 
    dw.IDDoneWork, 
    dw.TrudoemkostVnch AS labor_hours, 
    dw.StoimostVnch AS total_cost
FROM Work w
INNER JOIN DoneWork dw ON w.WorkCode = dw.WorkCode;