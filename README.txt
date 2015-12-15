DEPLOYEMENT INSTRUCTIONS FOR BASIC LEGAL CITATION
--------------------------------------------------
- These instructions are specific to Amazon's AWS service.
- The project was deployed on EC2 instance, running Amazon Linux.
- No backend database or appserver is running. All the files are being served from Apache.
- The authentication for author view is handled through Apache file level access configurations and requires to configure .htaccess. These - instructions have been explained in this document.
- The convertion of the web site to other portable formats is done by a python script running in the "cgi-bin" folder.
- For basic AWS instructions, scroll to the end of this document.

To search for an unmet dependency on AWS:
-----------------------------------------
yum search package_name

Install Apache:
---------------
sudo yum update -y
sudo yum install -y httpd24 php56 mysql55-server php56-mysqlnd
sudo service httpd start
sudo chkconfig httpd on

Dependencies for Amazon Linux:
------------------------------
yum install libXcomposite.x86_64
yum install mesa-libGLU.x86_64

install calibre
---------------
sudo -v && wget -nv -O- https://raw.githubusercontent.com/kovidgoyal/calibre/master/setup/linux-installer.py | sudo python -c "import sys; main=lambda:sys.stderr.write('Download failed\n'); exec(sys.stdin.read()); main()"
yum install ImageMagick
yum install ImageMagick-devel

install beautiful soup
----------------------
pip install beautifulsoup4

Setting up Apache file access restictions for /var/www/html/secure/author.html:
--------------------------------------------------------------------------------
Add to /etc/httpd/conf/httpd.conf:
----------------------------------
# Supplemental configuration
<Directory "/var/www/html/secure">
  AllowOverride AuthConfig
 Options FollowSymLinks
  Order allow,deny
  Allow from all
</Directory>

Create a user and password:
----------------------------
htpasswd -c /var/www/html/.htpasswd peter

Append to /var/www/html/secure/.htaccess:
-----------------------------------------
AuthUserFile "/var/www/html/.htpasswd"
AuthName "This is a secure login"
AuthType Basic
require valid-user

Set up the cgi-bin
--------------------
Copy the contents of "cgi-bin" in the project folder to /var/www/cgi-bin of Amazon

Create a temporary directory:
-----------------------------
mkdir /var/www/html/data
chmod 777 /var/www/html/data

Restart the server
------------------
sudo service httpd restart

Basic AWS instructions:
------------------------
Deploy an EC2 instance from aws.amazon.com and save the .pem file as

1. download the .pem attachment and copy it to ~
Do a chmod 700 ~/*.pem

2. cd to the CS 5150 project folder, where "html" file is present

3. tar -cjf html.tar html/

4.  scp -i ~/LegalCitation-final-ppt-Private-Cloud.pem html.tar ec2-user@ec2-52-35-183-12.us-west-2.compute.amazonaws.com:~

5.
Login to the server:
ssh -i ~/LegalCitation-final-ppt-Private-Cloud.pem ec2-user@ec2-52-35-183-12.us-west-2.compute.amazonaws.com

6. sudo cp html.tar /var/www

7. sudo tar -xjf /var/www/html.tar

Refresh the browser!

Our current project is hosted @ 
-------------------------------
(This may be re-deployed on a different server and the URL is NOT always GUARANTEED to be valid)
http://ec2-52-35-183-12.us-west-2.compute.amazonaws.com/

The author view is accessible from:
http://ec2-52-35-183-12.us-west-2.compute.amazonaws.com/secure/author.html
Username: peter
Passwd:   peter


