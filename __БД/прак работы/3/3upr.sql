SELECT 
    w1.NameWork AS work_1,
    w2.NameWork AS work_2,
    tow.worktypecode AS work_code
FROM autotechcenter.Work w1
JOIN autotechcenter.Work w2 ON w1.WorkTypeCode = w2.WorkTypeCode AND w1.WorkCode < w2.WorkCode
JOIN autotechcenter.TypeOfWork tow ON w1.WorkTypeCode = tow.WorkTypeCode
WHERE tow.worktypecode = 3
ORDER BY w1.NameWork, w2.NameWork;