CREATE TABLE process_activity (
    machine_id INT,
    process_id INT,
    activity_type VARCHAR(10),
    timestamp DECIMAL(6,3)
);

INSERT INTO process_activity (machine_id, process_id, activity_type, timestamp) VALUES
(0, 0, 'start', 0.712),
(0, 0, 'end', 1.520),
(0, 1, 'start', 3.140),
(0, 1, 'end', 4.120),
(1, 0, 'start', 0.550),
(1, 0, 'end', 1.550),
(1, 1, 'start', 0.430),
(1, 1, 'end', 1.420),
(2, 0, 'start', 4.100),
(2, 0, 'end', 4.512),
(2, 1, 'start', 2.500),
(2, 1, 'end', 5.000);


SELECT * FROM process_activity;

SELECT machine_id, ROUND(AVG(REC), 3) AS processing_time FROM (
SELECT machine_id, process_id, (MAX(timestamp) - MIN(timestamp)) AS REC 
FROM process_activity GROUP BY machine_id, process_id
) AS SUBQUERY GROUP BY MACHINE_ID;