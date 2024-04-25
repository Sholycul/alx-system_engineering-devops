```markdown
# 0x0D. Web stack debugging #0

## Description

This project is part of the "Webstack debugging" series, which aims to train you in the art of debugging. In this specific project, you will be given a broken or bugged web stack and tasked with identifying and fixing the issues manually before writing a Bash script to automate the process.

## Background Context

The Webstack debugging series is designed to simulate real-world scenarios where computers and software do not behave as expected. Debugging skills are essential for Full-Stack Software Engineers, and mastering them requires practice.

The goal of this project is to fix a simple example of a broken web server. The server must have a copy of the /etc/passwd file in /tmp and a file named /tmp/isworking containing the string "OK". Without these elements, the web application cannot function properly.

## Tasks

Your task is to identify and fix the issues manually, then write a Bash script that, when executed, will bring the web stack to a working state.

## Example

```
vagrant@vagrant:~$ docker run -d -ti ubuntu:14.04
Unable to find image 'ubuntu:14.04' locally
...
vagrant@vagrant:~$ docker exec -ti 76f44c0da25e /bin/bash
root@76f44c0da25e:/# ls /tmp/
root@76f44c0da25e:/# cp /etc/passwd /tmp/
root@76f44c0da25e:/# echo OK > /tmp/isworking
root@76f44c0da25e:/# ls /tmp/
isworking  passwd
root@76f44c0da25e:/#
```

The answer file would contain:

```bash
#!/usr/bin/env bash
# Fix my server with these magic 2 lines
cp /etc/passwd /tmp/
echo OK > /tmp/isworking
```

## Installation

For this project, you will be given a container to solve the task. If you would like to experiment locally, you can install Docker on your machine. Instructions for installation are provided for Mac OS, Windows, and Ubuntu.

## Resources

- [curl man page](https://linux.die.net/man/1/curl)

## Requirements

- Allowed editors: vi, vim, emacs
- All files interpreted on Ubuntu 14.04 LTS
- Files must end with a new line
- README.md file at the root of the project folder is mandatory
- All Bash script files must be executable
- Bash scripts must pass Shellcheck without errors
- Bash scripts must run without errors
- The first line of all Bash scripts should be `#!/usr/bin/env bash`
- The second line of all Bash scripts should be a comment explaining the script's purpose

```

Ensure you follow the requirements and provide necessary explanations for your scripts. Good luck with your debugging adventure! 🛠️🚀
