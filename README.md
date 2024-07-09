# Network Basics

## Internal IP:
- **Definition**: An internal IP (also known as a private IP) is an IP address used within a private network to identify devices such as computers, printers, and other devices.
- **Purpose**: It's used for communication within the local network and is not routable on the internet.
- **Example**: `192.168.1.10`, `10.0.0.5`

## External IP:
- **Definition**: An external IP (also known as a public IP) is an IP address assigned to your network by your Internet Service Provider (ISP) for identifying your network on the internet.
- **Purpose**: It's used for communication over the internet. Other networks and devices on the internet use this IP to identify and communicate with your network.
- **Example**: `203.0.113.1`, `198.51.100.2`

## Ports:
- **Definition**: A port is a numerical identifier in the TCP/UDP protocols that specifies a particular process or service on a networked device.
- **Purpose**: Ports allow multiple services to run on a single IP address by differentiating traffic intended for different applications. For example, web servers typically use port 80 for HTTP and port 443 for HTTPS.
- **Example**:
  - Port `80` (HTTP)
  - Port `443` (HTTPS)
  - Port `22` (SSH)

## Example Scenario:
- **Internal IP**: `192.168.1.10` (your laptop's IP within your home network)
- **External IP**: `203.0.113.1` (your home network's IP assigned by your ISP)
- **Ports**: Your laptop's web server running on port `8000` can be accessed internally via `192.168.1.10:8000` and externally (if properly configured) via `203.0.113.1:8000`.
