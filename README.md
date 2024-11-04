# [Work in Progress] Demo Project: Configuring Apache Web Servers and an HAProxy Load Balancer on Ubuntu with BundleWrap

## Project Overview:
This project serves as a demonstration of using BundleWrap to automate the configuration of a high-availability infrastructure setup.
### The setup includes:
Multiple Apache Web Servers as the backend servers, responsible for serving web content.
One or more HAProxy Load Balancers to distribute incoming traffic between the Apache servers, ensuring load balancing and redundancy.
The purpose is to showcase best practices in automated configuration management with BundleWrap, using Jinja2 for templating.

## Goal of the project:
Automate the deployment of Apache web servers and an HAProxy load balancer on Ubuntu.
Use BundleWrap to ensure configurations are consistently applied across all nodes.
Implement dynamic templating in order to guarantee load balancing for a backend consisting of multiple Apache web servers.

## Bundle structure:
The project consists of an HAProxy and an Apache Bundle
### HAProxy Bundle: 
Configures an HAProxy load balancer to distribute traffic to multiple Apache web servers in the backend via round-robin load balancing.

#### HAProxy Config:
	global:
	Configures logging
	Starts HAProxy as a daemon
	Sets max connections to 2000 in order to reduce stress on the load balancer
	
	defaults:
	Sets logging to the globally defined rules
	Uses HTTP traffic
	Logs HTTP requests
	Prevents logging of empty requests
	Sets connection retries to 3
	Redispatches connection if a server in the backend gets unhealthy
	Sets max connections to 2000 in order to reduce stress on the load balancer
	Sets timeout for connection time to 5000ms
	Sets client connection timeout to 5000ms
	Sets backend server connection timeout to 5000ms
	
	frontend:
	Allows any incoming HTTP connections on port 80
	Uses http_backend as the backend
	
	backend:
	Uses round-robin for load balancing
	Uses every web server of the apache-webserver group as backend

### Apache Bundle: 
Returns its own Hostname/IP as index.html.

	 
## Requirements:
- BundleWrap installed and configured on the control machine.
- Ubuntu installed on all nodes (web servers and load balancer).
- SSH access to all nodes with sufficient permissions.
- Your user or group has ALL=(ALL) NOPASSWD: ALL set in the /etc/sudoers file

## How to use:
1. Install bundlewrap
2. Clone the repository with git clone
3. Add your hosts to the nodes.py
	- Webserver use the following naming pattern: webserver-number (eg. webserver-1)
	- load balancers use the following naming pattern: load balancer-number (eg. load balancer-1)
4. Run bw apply apache-webserver and bw apply loadbalancer in order to apply the bundles
5. Confirm that the infrastructure is configured correctly

Tested on Ubuntu 24.04 with 1 load balancer and 2 webservers

## Open issues:
1. Templating for HAProxy Configuration:
Currently the templating for the HAProxy configuration is not working due to issues with using the "apache-webserver" in the template.
I will address this error as time allows. (see comment in bundles/ha_proxy/items.py)
2. Adding an action in the Apache and the HAProxy bundle which will check the configuration of the servers (apache2ctl configtest and haproxy -c -f /etc/haproxy/haproxy.cfg)

