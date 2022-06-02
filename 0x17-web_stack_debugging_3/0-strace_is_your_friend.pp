# Modify the wp-settings.php file with correct lines

exec {'modify-file':
  command => 'sed -i "s/phpp/php/" /var/www/html/wp-settings.php',
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
}
