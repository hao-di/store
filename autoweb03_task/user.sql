CREATE DATABASE login CHARSET utf8;
USE login;
CREATE TABLE `user`(
	username VARCHAR(50),
	passwd VARCHAR(50),
	expect VARCHAR(50)
);
INSERT INTO `user` VALUES('jason','1234567','Student Login'),
			 ('不再爱了','1234567','Student Login'),
			 ('jason1213123123123','1234567','账户名错误或密码错误!别瞎弄!'),
			 ('不再爱了','123456789898945','账户名错误或密码错误!别瞎弄!');