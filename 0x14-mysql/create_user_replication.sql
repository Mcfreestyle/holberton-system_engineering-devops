-- creates a MySQL user `replica_user` with the hostname set to `%`
-- grants privileges to replicate my primary MySQL server
CREATE USER IF NOT EXISTS replica_user IDENTIFIED BY 'replica_user';
GRANT REPLICATION SLAVE ON *.* TO 'replica_user'@'%';
FLUSH PRIVILEGES;
