#!/usr/bin/python

####LII Add Public IP to Security Group Script####
#This script will:

####TODO####
#also will need to add aws cli install and config info into the README

#Import Libraries
import subprocess
import shlex
import json
import re
import smtplib
import ConfigParser
import argparse

#function to check validity of passed IP
def get_passedIP():
    return foo    

#function to get current publicIP
def get_publicIP():
    rawoutput = subprocess.Popen(shlex.split("curl -s checkip.dyndns.org"), stdout=subprocess.PIPE, shell=False)
    publicIPraw = (rawoutput.communicate()[0])
    #strip out all junk from the curl request except for the IP
    #dem REGEX
    #attempted fix
    searchString = '\d+\.\d+\.\d+\.\d+'
    publicIP = re.search(searchString.decode('utf-8'), publicIPraw.decode('utf-8'), re.I | re.U).group(0)	
    #publicIP = re.search(r"\d+\.\d+\.\d+\.\d+", publicIPraw).group(0)
    return publicIP

def add_security_rule(passed_ip):
    #add in conditional for manually entered IP    
    if (passed_ip == None):
        publicIP = get_publicIP()
    else:
        publicIP = passed_ip
        
    print "Preparing to add " + publicIP + " to student security group."
    awsCommand = "/usr/local/bin/aws --profile student ec2 authorize-security-group-ingress --group-id " + "sg-851c3ce8"
    awsCommand = awsCommand + " --protocol tcp --port 0-65535 --cidr " + publicIP + "/32"
    subprocess.Popen(shlex.split(awsCommand.encode('ascii')), shell=False)    
    
    return 0

#check to see if the config is set to something other than the default    
    
    
def main():
    
    #handle command line parameters
    parser = argparse.ArgumentParser(description='Add IP to all LII AWS Security Groups')
    parser.add_argument('--IP', dest='ipAddress', help='Valid ipv4 Address')
    args = parser.parse_args()
    
    
    #print public IP regardless
    publicIP = get_publicIP()
    print "Your public IP is currently " + publicIP
    
    if (args.ipAddress != None):
        print "You provided " + args.ipAddress + " as your desired allowed IP address."

    if (args.ipAddress == '0.0.0.0'):
        print "Nice try, but allowing access to all ports from anywhere is bad."
        return 0
    else:
        add_security_rule(args.ipAddress)
    
    return 0
    
if __name__ == "__main__":
    main()
