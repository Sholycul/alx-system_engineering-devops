#FIREWALL

#### Description
In this task, we will set up the `ufw` firewall on `web-01` to block all incoming traffic except for specific TCP ports. This ensures a secure network environment while allowing essential services like SSH, HTTPS SSL, and HTTP to remain accessible.

#### Requirements
- **Target**: `web-01`
- **Firewall**: `ufw`
- **Allowed TCP Ports**:
  - 22 (SSH)
  - 443 (HTTPS SSL)
  - 80 (HTTP)

#### Steps
1. **Install `ufw` if not already installed**:
   ```bash
   sudo apt update
   sudo apt install ufw
   ```

2. **Configure `ufw` to allow specified TCP ports**:
   ```bash
   sudo ufw allow 22/tcp     # SSH
   sudo ufw allow 443/tcp    # HTTPS SSL
   sudo ufw allow 80/tcp     # HTTP
   ```

3. **Enable `ufw`**:
   ```bash
   sudo ufw enable
   ```

4. **Verify `ufw` status**:
   ```bash
   sudo ufw status
   ```

#### Solution File
- **GitHub Repository**: [alx-system_engineering-devops](https://github.com/Sholycul/alx-system_engineering-devops)
- **Directory**: `0x13-firewall`
- **File**: `0-block_all_incoming_traffic_but`

