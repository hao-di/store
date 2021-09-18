CREATE DATABASE market CHARACTER SET utf8;
DROP TABLE sell;
CREATE TABLE sell(
	日期 VARCHAR(50),
	服装名称 VARCHAR(50),
	单价 DOUBLE,
	本月库存数量 INT,
	日销售量 INT
);