PROJECT BASIC LEGAL CITATION

This is a project developed in the course CS 5150 Software Engineering. The team revamped the website of Introduction to Basic Legal Citation (https://www.law.cornell.edu/citation/) into a more modern and interactive one based on AngularJS. In addition, the workflow of maintaining the website and another three e-book formats has been reduced by 75% by developing a customized format converter from HTML5 to PDF, mobi, and ePub. 


DEPLOYEMENT INSTRUCTIONS FOR BASIC LEGAL CITATION
--------------------------------------------------
- These instructions are specific to Amazon's AWS service.
- The project was deployed on EC2 instance, running Amazon Linux.
- No backend database or appserver is running. All the files are being served from Apache.
- The authentication for author view is handled through Apache file level access configurations and requires to configure .htaccess. These - instructions have been explained in this document.
- The convertion of the web site to other portable formats is done by a python script running in the "cgi-bin" folder.
- For basic AWS instructions, scroll to the end of this document.
- This document also contains instructions to install on Ubuntu AWS instance.

									-------------------
									Common instructions
									--------------------
Un-tar the project into /var/www/html

Create a user and password:
----------------------------
htpasswd -c /var/www/html/.htpasswd peter

Append to /var/www/html/secure/.htaccess:
-----------------------------------------
AuthUserFile "/var/www/html/.htpasswd"
AuthName "This is a secure login"
AuthType Basic
require valid-user

Create a temporary directory:
-----------------------------
mkdir /var/www/html/data
chmod 777 /var/www/html/data
									--------------------------
									Ubuntu on AWS instructions
									--------------------------
Install required software:
--------------------------
sudo apt-get install apache2 python-beautifulsoup calibre-bin calibre

Setup the cgi-bin config @
/etc/apache2/sites-enabled/lii_apache2_last:
---------------------------------------------
        ScriptAlias /cgi-bin/ /usr/lib/cgi-bin/
        <Directory "/usr/lib/cgi-bin">
                AllowOverride None
                Options +ExecCGI -MultiViews +SymLinksIfOwnerMatch
                AddHandler cgi-script .py
                Order allow,deny
                Allow from all
        </Directory>

		<Directory "/var/www/html/secure">
  			AllowOverride AuthConfig
 			Options FollowSymLinks
  			Order allow,deny
 			Allow from all
		</Directory>

									---------------------
									Amazon Linux Instance
									---------------------

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

Set up the cgi-bin
--------------------
Copy the contents of "cgi-bin" in the project folder to /var/www/cgi-bin of Amazon

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


