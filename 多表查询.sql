DROP DATABASE IF EXISTS company;
CREATE DATABASE IF NOT EXISTS company CHARACTER SET utf8;
USE company;

DROP TABLE IF EXISTS `t_dept`;
CREATE TABLE `t_dept` (
  `deptno` INT(11) NOT NULL,
  `dname` VARCHAR(20) DEFAULT NULL,
  `loc` VARCHAR(40) DEFAULT NULL,
  PRIMARY KEY (`deptno`),
  KEY `index_dept` (`deptno`)
) ENGINE=INNODB DEFAULT CHARSET=utf8;

LOCK TABLES `t_dept` WRITE;
INSERT INTO `t_dept` VALUES (10,'董事部','江东'),(20,'公关部','四川'),
			    (30,'武统部','咸阳'),(40,'财务部','洛阳');
UNLOCK TABLES;

DROP TABLE IF EXISTS `t_employees`;
CREATE TABLE `t_employees` (
  `empno` INT(11) NOT NULL,
  `ename` VARCHAR(20) DEFAULT NULL,
  `job` VARCHAR(40) DEFAULT NULL,
  `MGR` INT(11) DEFAULT NULL,
  `hiredate` DATE DEFAULT NULL,
  `sal` DOUBLE(10,2) DEFAULT NULL,
  `comm` DOUBLE(10,2) DEFAULT NULL,
  `deptno` INT(11) DEFAULT NULL,
  PRIMARY KEY (`empno`),
  KEY `fk_deptno` (`deptno`),
  CONSTRAINT `fk_deptno` FOREIGN KEY (`deptno`) REFERENCES `t_dept` (`deptno`)
) ENGINE=INNODB DEFAULT CHARSET=utf8;

LOCK TABLES `t_employees` WRITE;
INSERT INTO `t_employees` VALUES (7369,'周瑜','高级公关',7566,'1981-03-21',1800.00,NULL,20),
				 (7499,'张飞','武装教习',7698,'1982-03-21',2600.00,300.00,30),
				 (7521,'关二爷','武装副司令',7698,'1983-03-21',2250.00,500.00,30),
				 (7566,'孙权','经理',7839,'1981-03-21',3975.00,NULL,10),
				 (7654,'黄忠','武装司令',7698,'1981-03-21',2250.00,1400.00,30),
				 (7698,'刘备','经理',7839,'1984-03-21',3850.00,NULL,10),
				 (7782,'曹操','经理',7839,'1985-03-21',3450.00,NULL,10),
				 (7788,'许褚','武装上将',7782,'1981-03-21',4000.00,NULL,30),
				 (7839,'汉献帝','董事长',NULL,'1981-03-21',6000.00,NULL,10),
				 (7844,'魏延','武装上将',7698,'1989-03-21',2500.00,0.00,30),
				 (7876,'黄盖','人事专员',7566,'1998-03-21',2100.00,NULL,20),
				 (7902,'荀彧','分析员',7782,'2005-03-12',4000.00,NULL,20),
				 (7934,'甘宁','中级公关',7782,'1981-03-21',2300.00,NULL,20),
				 (7952,'马超','武装大校',7698,'2001-03-21',2750.00,0.00,30),
				 (7953,'吕布','武装教习',7698,'2001-03-21',2750.00,0.00,30);
UNLOCK TABLES;


/*
1. 查出至少有一个员工的部门。显示部门编号、部门名称、部门位置、部门人数。
列：d.deptno, d.dname, d.loc, 部门人数
表：dept d, emp e
条件：e.deptno=d.deptno
*/
SELECT t_dept.*,COUNT(empno)
FROM t_dept,t_employees
WHERE t_employees.`deptno`=t_dept.`deptno`
GROUP BY t_dept.`deptno`;

SELECT d.*, z1.cnt 
FROM t_dept d, (SELECT deptno, COUNT(*) cnt FROM t_employees GROUP BY deptno) z1
WHERE d.deptno = z1.deptno

/*
3. 列出所有员工的姓名及其直接上级的姓名。
列：员工姓名、上级姓名
表：emp e, emp m
条件：员工的mgr = 上级的empno
*/
SELECT e.`ename`,m.`ename`
FROM t_employees e,t_employees m
WHERE e.`MGR`=m.`empno`;

/*
4. 列出受雇日期早于直接上级的所有员工的编号、姓名、部门名称。
列：e.empno, e.ename, d.dname
表：emp e, emp m, dept d
条件：e.hiredate<m.hiredate
思路：
1. 先不查部门名称，只查部门编号!
列：e.empno, e.ename, e.deptno
表：emp e, emp m
条件：e.mgr=m.empno, e.hiredate<m.hireadate
*/
SELECT e.`empno`,e.`ename`,d.`dname`
FROM t_employees e,t_employees m,t_dept d
WHERE e.`deptno`=d.`deptno` AND (e.`MGR`=m.`empno` AND e.`hiredate`<m.`hiredate`);

/*
5. 列出部门名称和这些部门的员工信息，同时列出那些没有员工的部门。
列：* 
表：emp e, dept d
条件：e.deptno=d.deptno
*/
SELECT d.`dname`,e.*
FROM t_employees e RIGHT JOIN t_dept d ON e.`deptno`=d.`deptno`;

/*
7. 列出最低薪金大于15000的各种工作及从事此工作的员工人数。
列：job, count(*)
表：emp e
条件：min(sal) > 15000
分组：job
*/
SELECT job,COUNT(empno) FROM t_employees GROUP BY job HAVING MIN(sal)>1500;

/*
8. 列出在公关部工作的员工的姓名，假定不知道公关部的部门编号。
列：e.ename
表：emp
条件：e.deptno=(select deptno from dept where dname='公关部')
*/
SELECT e.`ename` FROM t_employees e WHERE e.`deptno`=(SELECT deptno FROM t_dept WHERE dname='公关部');

/*
9. 列出薪金高于公司平均薪金的所有员工信息，所在部门名称，上级领导，工资等级。
列：* 
表：emp e
条件：sal>(查询出公司的平均工资)
*/
SELECT * FROM t_employees e WHERE e.`sal`>(SELECT AVG(sal) FROM t_employees);
SELECT e.*,d.`dname`,m.`ename` 上级领导
FROM t_employees e,t_employees m,t_dept d
WHERE e.`MGR`=m.`empno` AND e.`deptno`=d.`deptno` AND e.`sal`>(SELECT AVG(sal) FROM t_employees);

/*
10.列出与张飞从事相同工作的所有员工及部门名称。
列：e.*, d.dname
表：emp e, dept d
条件：job=(查询出张飞的工作)
*/
SELECT e.*,d.`dname`
FROM t_employees e,t_dept d
WHERE job=(SELECT job FROM t_employees WHERE ename='张飞') AND e.`deptno`=d.`deptno`;

/*
11.列出薪金高于在部门30工作的所有员工的薪金的员工姓名和薪金、部门名称。
列：e.ename, e.sal, d.dname
表：emp e, dept d
条件；sal>all (30部门薪金)
*/
SELECT e.`ename`,e.`sal`,d.`dname`
FROM t_employees e,t_dept d
WHERE e.`deptno`=d.`deptno` AND e.`sal`>ALL(SELECT sal FROM t_employees WHERE deptno=30);

