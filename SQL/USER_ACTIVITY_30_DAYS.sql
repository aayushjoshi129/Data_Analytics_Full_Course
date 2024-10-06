CREATE DATABASE USER_ACTIVITY_30_DAYS;

USE USER_ACTIVITY_30_DAYS;

CREATE TABLE Activity (
    user_id INT,
    session_id INT,
    activity_date DATE,
	activity_type VARCHAR(20) NOT NULL,
    CHECK (activity_type IN ('open_session', 'end_session', 'scroll_down', 'send_message'))
);

INSERT INTO Activity (user_id, session_id, activity_date, activity_type)
VALUES 
(1, 1, '2019-07-20', 'open_session'),
(1, 1, '2019-07-20', 'scroll_down'),
(1, 1, '2019-07-20', 'end_session'),
(2, 4, '2019-07-20', 'open_session'),
(2, 4, '2019-07-21', 'send_message'),
(2, 4, '2019-07-21', 'end_session'),
(3, 2, '2019-07-21', 'open_session'),
(3, 2, '2019-07-21', 'send_message'),
(3, 2, '2019-07-21', 'end_session'),
(4, 3, '2019-06-25', 'open_session'),
(4, 3, '2019-06-25', 'end_session');


SELECT * FROM Activity;

SELECT ACTIVITY_DATE, COUNT(DISTINCT USER_ID) AS ACTIVE_USERS 
FROM ACTIVITY WHERE ACTIVITY_DATE BETWEEN '2019-06-28' AND '2019-07-27'
 GROUP BY ACTIVITY_DATE;

