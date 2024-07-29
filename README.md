System Information Display Tool

This script retrieves and displays system information on a Linux-based operating system.

Features:
- Basic System Information: Display the hostname, kernel version, and distribution of the Linux system.
- CPU Information: Retrieve details about the CPU, such as the model, architecture, and number of cores. Optionally, display CPU temperature if available.
- Memory Information: Show the total, used, and free memory available on the system.
- Disk Usage: Display disk usage statistics for each mounted partition, including total, used, and available space. Highlight any partitions that are close to full capacity.
- Network Information: Retrieve details about network interfaces, including IP addresses, MAC addresses, and current network activity.
- Uptime: Show the system uptime since the last boot.
- Colorized Output: Enhance the output with color-coding to make it more readable and visually appealing.
- Interactive Mode: Allow users to choose which information they want to display interactively.
- Error Handling: Implement error handling to gracefully handle cases where certain information cannot be retrieved.
- Ping Test: Perform a ping test to a specified host or IP address to check for connectivity. Requires administrative privileges.

Usage:
Run the `system_info_tool.py` script and follow the prompts to retrieve and display the desired system information. Use `sudo` to run the script if you need to perform a ping test.

Challenges:
- Handling different outputs for network interfaces on various Linux distributions.
- Ensuring the script works across multiple Linux distributions and kernel versions.

Special Considerations:
- The script uses standard system commands and libraries, so it needs appropriate permissions to execute these commands.

Version Control:
- The project is managed using Git for version control.
- Different versions are managed using branches and merges.

Developer:
[OGUNLADE OLAMIDE]
