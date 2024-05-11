#### In a Nutshell
This curriculum focuses on foundational concepts in Systems Engineering, including DevOps, SysAdmin, and Security. Below is an overview of the ongoing project, learning objectives, resources, and tasks associated with this curriculum.

#### Concepts
For this project, the following concepts are covered:
- DNS
- Web stack debugging

#### Background Context
Understanding the importance of securing website traffic and the consequences of neglecting it.

#### Resources
Read or watch:
- What is HTTPS?
- What are the 2 main elements that SSL is providing?
- HAProxy SSL termination on Ubuntu16.04
- SSL termination
- Bash function
Man or help:
- awk
- dig

#### Learning Objectives
Upon completion of this project, you should be able to explain:
- What HTTPS SSL is and its two main roles
- The purpose of encrypting traffic
- What SSL termination means

#### Requirements
**General:**
- Allowed editors: vi, vim, emacs
- Interpretation on Ubuntu 16.04 LTS
- Bash scripts should end with a new line
- A README.md file is mandatory at the root of the project folder
- All Bash scripts must be executable
- Bash scripts must pass Shellcheck (version 0.3.7) without errors
- The first line of all Bash scripts should be `#!/usr/bin/env bash`
- The second line of all Bash scripts should be a comment explaining the script's purpose

#### Quiz Questions
Quiz successfully completed.

#### Your Servers
- Name: 347710-web-01
  - Username: ubuntu
  - IP: 54.227.161.229
  - State: running
- Name: 347710-web-02
  - Username: ubuntu
  - IP: 100.26.175.56
  - State: running
- Name: 347710-lb-01
  - Username: ubuntu
  - IP: 54.158.79.248
  - State: running

#### Tasks
**0. World Wide Web**
- Configure domain zone for subdomains
- Write a Bash script to display information about subdomains

**1. HAProxy SSL Termination**
- Configure HAProxy to accept encrypted traffic for the subdomain www

#### Repo Information
- GitHub repository: alx-system_engineering-devops
- Directory: 0x10-https_ssl
- File: 0-world_wide_web, 1-haproxy_ssl_termination
