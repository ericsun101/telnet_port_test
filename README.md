
# telnet_port_test
A Python script for quickly testing telnet connections to public addresses.

## Description
This script allows you to batch test telnet connections to multiple IP addresses and ports. It reads connection details from a configuration file and provides quick connection test results.

## Project Structure
telnet_port_test/
├── src/
│   └── telnet_port_test.py
├── data/
│   └── telnet_ports.txt


## Configuration
The `telnet_ports.txt` file stores target IP addresses and ports in CSV format:


## Setup
1. Create virtual environment:
python -m venv venv

## Usage
1. Add your target IP addresses and ports to `data/telnet_ports.txt`
2. Run the script:
python src/telnet_port_test.py


## Output
The script will test each connection and display the results:
- Success: Connection established
- Failure: Connection failed (with error details)

## Requirements
- Python 3.x
- Virtual environment (venv)

## License
[MIT License](LICENSE)