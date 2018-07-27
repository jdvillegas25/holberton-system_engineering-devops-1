# 0x0F. Load balancer

## Overview
This project gets us more familiar with load balancing with HAproxy. I was given two servers: 300-web-02 and 300-lb-01 to help create redundancy for the servers.

## Requirements
### Shell Scripts
* Allowed editors: `vi`, `vim`, `emacs`
* All your scripts will be tested on Ubuntu 14.04 LTS
* All your scripts should be exactly two lines long (`wc -l` file should print 2)
* All your files should end with a new line
* The first line of all your files should be exactly `#!/bin/bash`
* All your files must be executable
* Your Bash script must pass `Shellcheck` (version `0.3.3-1~ubuntu14.04.1` via `apt-get`) without any error
* The first line of all your Bash scripts should be exactly `#!/usr/bin/env bash`
* The second line of all your Bash scripts should be a comment explaining what is the script doing

## Tasks
### Mandatory
**[0-custom_http_response-header](0-custom_http_response-header)** - Configures 300-web-02 to be identical to 300-web-01 and displays a custom header so that it can be easily tracked which server is serving HTTP requests
```
$ curl -sI 34.198.248.145 | grep X-Served-By
X-Served-By: 03-web-01
$ curl -sI 54.89.38.100 | grep X-Served-By
X-Served-By: 03-web-02
```

**[1-install_load_balancer](1-install_load_balancer)** - Installs and configures HAproxy on the 300-lb-01 server. Configure it so that it sends traffic to web-01 and web-02, use a roundrobin algorithm, make sure it can be managed with an init script, and make sure the servers are configured to the right hostnames.
```
$ curl -Is 54.210.47.110
HTTP/1.1 200 OK
Server: nginx/1.4.6 (Ubuntu)
Date: Mon, 27 Feb 2017 06:12:17 GMT
Content-Type: text/html
Content-Length: 30
Last-Modified: Tue, 21 Feb 2017 07:21:32 GMT
Connection: keep-alive
ETag: "58abea7c-1e"
X-Served-By: 03-web-01
Accept-Ranges: bytes

$ curl -Is 54.210.47.110
HTTP/1.1 200 OK
Server: nginx/1.4.6 (Ubuntu)
Date: Mon, 27 Feb 2017 06:12:19 GMT
Content-Type: text/html
Content-Length: 612
Last-Modified: Tue, 04 Mar 2014 11:46:45 GMT
Connection: keep-alive
ETag: "5315bd25-264"
X-Served-By: 03-web-02
Accept-Ranges: bytes
```

2018 - All programs written by Derek Kwok ([@dlangshk](https://twitter.com/dlangshk)) at [Holberton School](https://www.holbertonschool.com/)