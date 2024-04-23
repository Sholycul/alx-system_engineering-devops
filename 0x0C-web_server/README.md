---

# 0x0C-web_server

This repository contains a Bash script for transferring files from a client to a server using SCP.

## Files

- **0-transfer_file**: Bash script for transferring a file to a server via SCP.

## Usage

To transfer a file to the server, use the following command:

```
./0-transfer_file PATH_TO_FILE IP USERNAME PATH_TO_SSH_KEY
```

If less than 3 parameters are passed, the script will display usage instructions.

Example:

```
./0-transfer_file some_page.html 8.8.8.8 sylvain /vagrant/private_key
```

## Requirements

- The script accepts 4 parameters: path to the file to be transferred, server IP, username for SCP connection, and path to the SSH private key.
- Strict host key checking is disabled when using SCP.

## Authors

This script was written by @Sholycul.

---

Feel free to adjust it according to your preferences and add any additional information you find relevant!
