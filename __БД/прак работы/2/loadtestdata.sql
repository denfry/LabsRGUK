SELECT r.namework,
       MIN(w.trudoemkostvnch * w.stoimostvnch) AS min_sales_volume
FROM autotechcenter.donework w
JOIN autotechcenter.work r ON w.workcode = r.workcode
GROUP BY r.namework
HAVING MIN(w.trudoemkostvnch * w.stoimostvnch) > 1800;