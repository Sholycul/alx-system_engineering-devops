eadme: Load Balancer Configuration

Welcome to the Load Balancer Configuration project! This project aims to set up and configure a load balancer using HAProxy to distribute traffic among multiple web servers. Below are the tasks and their requirements for the successful completion of this project.

## Tasks Overview

### Task 0: Double the number of webservers
In this task, the goal is to configure `web-02` to be identical to `web-01`. This involves automating the configuration using a Bash script and adding a custom Nginx response header (`X-Served-By`) to track which web server is handling HTTP requests. 

**Requirements:**
- Configure Nginx to include a custom HTTP header on both `web-01` and `web-02`.
- The custom HTTP header `X-Served-By` should contain the hostname of the server running Nginx.
- Write a script (`0-custom_http_response_header`) to configure a new Ubuntu machine to meet the specified requirements.

### Task 1: Install your load balancer
This task involves installing and configuring HAProxy on the `lb-01` server to distribute traffic between `web-01` and `web-02` using a round-robin algorithm. It also requires ensuring HAProxy can be managed via an init script.

**Requirements:**
- Configure HAProxy to distribute traffic to `web-01` and `web-02` using a round-robin algorithm.
- Ensure HAProxy can be managed via an init script.
- Servers should be configured with the correct hostnames (`[STUDENT_ID]-web-01` and `[STUDENT_ID]-web-02`).

## Repo Information

- **GitHub Repository:** [alx-system_engineering-devops](https://github.com/Sholycul/alx-system_engineering-devops)
- **Directory:** `0x0F-load_balancer`

## Files Included

- **Task 0 Script:** `0-custom_http_response_header`
- **Task 1 Script:** `1-install_load_balancer`

## Usage
To use the scripts provided in this project, follow these steps:

1. Clone the GitHub repository: `git clone https://github.com/Sholycul/alx-system_engineering-devops`
2. Navigate to the `0x0F-load_balancer` directory.
3. Run the respective script for each task on a new Ubuntu machine to configure and install the load balancer according to the project requirements.

## Notes
- Ensure that proper permissions are set for executing the scripts (`chmod +x script_name.sh`).
- Make sure to replace `[STUDENT_ID]` with your actual student ID when configuring hostnames.
- Additional configurations or troubleshooting may be required depending on your specific environment.
