Here is the updated README with all occurrences of "engineer" changed to "partner":

# Postmortem Report: Web Stack Outage on 2024-06-05

## Issue Summary

- **Duration of the outage:**
  - **Start:** 2024-06-05 08:00 UTC
  - **End:** 2024-06-05 12:00 UTC

- **Impact:**
  - Our primary web service, including the main website and API, was down.
  - Users experienced an inability to load the website and failed API requests.
  - Approximately 75% of users were affected, with a 100% outage in the most heavily trafficked regions.

- **Root Cause:**
  - The root cause was an expired SSL certificate, which caused the web servers to reject all incoming HTTPS requests.

## Timeline

- **08:00 UTC:** Issue detected by automated monitoring system, which triggered an alert due to a sudden spike in failed HTTP requests.
- **08:05 UTC:** On-call partner confirmed the issue and began investigating.
- **08:15 UTC:** Initial assumption was a network issue due to recent changes in the network configuration.
- **08:30 UTC:** Network team ruled out network configuration issues after a thorough check.
- **09:00 UTC:** Investigation shifted to the application layer, suspecting a potential DDoS attack.
- **09:30 UTC:** Security team confirmed there was no ongoing attack.
- **10:00 UTC:** A partner noticed the SSL certificate had expired, leading to the rejection of HTTPS requests.
- **10:05 UTC:** Incident escalated to the DevOps team to renew the SSL certificate.
- **10:15 UTC:** SSL certificate renewal process initiated.
- **11:00 UTC:** New SSL certificate obtained and deployed.
- **11:30 UTC:** Services began recovering as the new certificate propagated.
- **12:00 UTC:** Full service restoration confirmed.

## Root Cause and Resolution

- **Root Cause:**
  - The SSL certificate for the web servers expired, causing all HTTPS requests to be rejected. The automatic renewal process failed due to a misconfiguration in the certificate management system, which was not detected by the team.

- **Resolution:**
  - The SSL certificate was manually renewed and deployed to all affected web servers. The certificate management system configuration was corrected to ensure automatic renewals would succeed in the future.

## Corrective and Preventative Measures

- **Improvements/Fixes:**
  - Implement more robust monitoring for SSL certificate expiry.
  - Review and update the certificate management system to ensure automatic renewals are properly configured and tested regularly.
  - Enhance alerting mechanisms to include warnings for upcoming SSL certificate expirations.

- **Task List:**
  - **Patch Nginx server:** Update configuration to ensure proper SSL certificate handling.
  - **Add SSL monitoring:** Implement tools to monitor SSL certificates' expiration dates and alert in advance.
  - **Audit certificate management system:** Perform a thorough review of the certificate management system to identify and fix potential issues.
  - **Training:** Conduct training sessions for the team on SSL certificate management and renewal processes.
  - **Documentation:** Update internal documentation to include detailed steps for manual SSL renewal and common troubleshooting scenarios.

By addressing these measures, we aim to prevent future occurrences of similar incidents and improve the reliability and resilience of our web services.

