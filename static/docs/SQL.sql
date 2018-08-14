--1、
SELECT A.USER_ID,SUM(A.PPOINT)
  FROM POINT_BASE A
  JOIN SYS_ORG_LVL B
    ON A.USR_ORG = B.ORGID
   AND B.ORG1 = 'A0011'
  JOIN SYS_USER_INFO USR
    ON A.USER_ID = USR.USERID
   AND USR.USR_STAT IN (1, 2, 7)
   AND USR.DELFLA = 0
 WHERE A.DATA_DATE = '2018'
   AND A.PPOINT IS NOT NULL
 GROUP BY A.USER_ID;
--2、
SELECT *
  FROM POINT_BASE A
  JOIN (SELECT ORGID
          FROM SYS_ORG_INFO
         START WITH ORGID = 'A0011'
        CONNECT BY PRIOR ORGID = ORG_PID) B
    ON A.USR_ORG = B.ORGID
  JOIN SYS_USER_INFO C
    ON A.USER_ID = C.USERID
   AND C.USR_STAT IN (1, 2, 7)
   AND C.DELFLA = 0
 WHERE A.DATA_DATE = '2018'
   AND A.PPOINT IS NOT NULL;
--3、
SELECT *
  FROM POINT_BASE A
 JOIN (SELECT ORG_ID
          FROM SYS_ORG_REPORT
         START WITH ORG_ID = 'A0011'
        CONNECT BY PRIOR ORG_ID = ORG_REPORT_PID) B
    ON A.USR_ORG = B.ORG_ID
  JOIN SYS_USER_INFO C
    ON A.USER_ID = C.USERID
   AND C.USR_STAT IN (1, 2, 7)
   AND C.DELFLA = 0
 WHERE A.DATA_DATE = '2018'
 AND A.PPOINT IS NOT NULL;
--4、
SELECT * FROM ORG_LAST T WHERE T.ORGID = 'A0011' AND T.DATA_DATE = '2018'; 

--5、
select *
  from sys_user_info t,
       (SELECT ORGID
          FROM SYS_ORG_INFO
         START WITH ORGID = 'A0011'
        CONNECT BY PRIOR ORGID = ORG_PID) t1,
       point_base t2
 where t.usr_org = t1.orgid
   and t.userid = t2.user_id
   and t2.ppoint is not null
   and t2.data_date='2018';
--6、
select *
  from sys_user_info t,
       (select org_id
          from sys_org_report
         start with org_id = 'A0011'
        connect by prior org_id = org_report_pid) t1,
       point_base t2
 where t.usr_org = t1.org_id
   and t.userid = t2.user_id
   and t2.ppoint is not null
   and t2.data_date = '2018'; 
