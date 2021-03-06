# Customize a http response header
exec {'customize_http_response_header':
  provider => shell,
  command  => 'sudo apt-get -y update ;\
  	       sudo apt-get -y install nginx ;\
	       echo "Hello World" | sudo tee /var/www/html/index.nginx-debian.html ;\
	       txt_redirect="\n\tlocation /redirect_me {\n\t\trewrite ^/redirect_me(.*)$ https://www.youtube.com/watch?v=JDglMK9sgIQ permanent;\n\t}" ;\
	       sudo sed -i "/server_name _;/ a \\$txt_redirect" /etc/nginx/sites-available/default ;\
	       txt_error="\n\terror_page 404 /error_404.html; \n\tlocation = /error_404.html {\n\t\troot /var/www/html;\n\t\tinternal;\n\t}" ;\
	       sudo sed -i "/server_name _;/ a \\$txt_error" /etc/nginx/sites-available/default ;\
	       custom_header="\n\tadd_header X-Served-By \$hostname;\n" ;\
	       sudo sed -i "/server_name _;/ a \\$custom_header" /etc/nginx/sites-available/default ;\
	       sudo service nginx restart',
}
