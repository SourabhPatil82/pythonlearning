
import re
# Define a regex pattern to match IP addresses
ip_pattern = re.compile(r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b')
# Open the log file for reading
with open('SampleIp.txt', 'r') as f:
 log = f.read()
 # Find all IP addresses in the log file
ips = re.findall(ip_pattern, log)
# Write the list of IP addresses to a new file
with open('ip_addresses.txt', 'w') as f:
 for ip in ips:
  f.write(ip + '\n')

