# [Work in Progress] Demo Project: Configuring Apache Web Servers and an HAProxy Load Balancer on Ubuntu with BundleWrap

## Project Overview:
This project serves as a demonstration of using BundleWrap to automate the configuration of a high-availability infrastructure setup.
### The setup includes:
Multiple Apache Web Servers as the backend servers, responsible for serving web content.
One or more HAProxy Load Balancer to distribute incoming traffic between the Apache servers, ensuring load balancing and redundancy.
The purpose is to showcase best practices in automated configuration management with BundleWrap, using Jinja2 for templating.

## Goal of the project:
Automate the deployment of Apache web servers and an HAProxy load balancer on Ubuntu.
Use BundleWrap to ensure configurations are consistently applied across all nodes.
Implement dynamic templating in order to guarantee load balancing for an backend consisting of multiple Apache web servers.

## Bundle structure:
The projects consist of an HAProxy and an Apache Bundle
### HAProxy Bundle: Configures an HAProxy load balancer to distribute traffic to multiple Apache web servers in the backend via roundrobin load balancing.

#### HAProxy Config:
	global:
	Configures Logging
	Starts HAProxy as a daemon
	Sets max. connections to 2000 in order to reduce stress on the load balancer
	
	defaults:
	Sets log to the in global defined rules
	Uses http traffic
	Logs http requests
	Prevents logging of empty requests
	Sets connection retries to 3
	Redispatches connection if a server in the backend gets unhealthy
	Sets max. connections to 2000 in order to reduce stress on the load balancer
	Sets time limit for connection time out to 5000ms
	Sets time limit of client for connection time out to 5000ms
	Sets time limit of server backend for connection time out to 5000ms
	
	frontend:
	Allows any incomming http connections on port 80
	Uses http_backend as backend
	
	backend:
	Uses roundrobin for load balancing
	Uses every web server of the apache-webserver group as backend

### Apache Bundle: Returns its own Hostname/IP as index.html.

	 
## Requirements:
- BundleWrap installed and configured on the control machine.
- Ubuntu installed on all nodes (web servers and load balancer).
- SSH access to all nodes with appropriate permissions.
- Your user or group has ALL=(ALL) NOPASSWD: ALL set in the /etc/sudoers file

## How to use:
1. Install bundlewrap
2. Clone the repository with git clone
3. Add your hosts to the nodes.py
	- Webserver use the following naming pattern: webserver-number (eg. webserver-1)
	- load balancer use the following naming pattern: load balancer-number (eg. load balancer-1)
4. Run bw apply apache and bw apply ha_proxy in order to apply the bundles
5. Confirm if the infrastructure got configured correctly

Tested on Ubuntu 24.04 with 1 load balancer and 2 webservers

## Open issues:
1. Templating for HAProxy Conf:
Currenty the templating for the HAProxy configuration is not working due to issues with using the "apache-webserver" in the template.
I will fix the error when I have the time for it. (see comment in bundles/ha_proxy/items.py)
2. Adding an action in the Apache and the HAProxy bundle which will check the configuration of the servers(apache2ctl configtest and haproxy -c -f /etc/haproxy/haproxy.cfg)

