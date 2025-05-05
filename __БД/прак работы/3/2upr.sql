SELECT 
    c1.FIO AS client_1,
    c2.FIO AS client_2
FROM autotechcenter.Client c1
JOIN autotechcenter.Client c2 ON c1.CodeClient < c2.CodeClient
WHERE c1.ClientType = 'юр' 
    AND c2.ClientType = 'юр'
ORDER BY c1.FIO, c2.FIO;