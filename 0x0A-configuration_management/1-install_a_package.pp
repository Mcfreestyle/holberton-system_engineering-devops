# Install flask

exec {'flask_install':
  command  => 'pip3 install Flask==2.1.0',
  provider => shell,
  #path    => ['/usr/bin', '/bin'],
}
