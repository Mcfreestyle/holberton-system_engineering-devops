-- creates a MySQL user `holberton_user` with the host name set to localhost and the passwd `projectcorrection280hbtn`
-- grants permissions to check the primary/replica status of the databases
CREATE USER IF NOT EXISTS 'holberton_user'@'localhost' IDENTIFIED BY 'projectcorrection280hbtn';
GRANT REPLICATION CLIENT ON *.* TO 'holberton_user'@'localhost';
FLUSH PRIVILEGES;
