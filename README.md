
# SDN TUTORIAL: Allow Only h1 to Send Traffic

This repository contains a simple SDN-based Ryu controller that allows only host `h1` to send traffic, while all other hosts are blocked. The network is simulated using Mininet.

## Table of Contents
1. [Installation](#installation)
2. [Running the Project](#running-the-project)
3. [Testing the Network](#testing-the-network)

## Installation

### 1. Install Mininet
Follow these instructions to install Mininet:

git clone https://github.com/mininet/mininet.git
cd mininet
sudo ./util/install.sh -a


### 2. Install Ryu
Install Ryu using pip:

pip3 install ryu


## Running the Project

### 1. Start the Ryu Controller
To start the Ryu controller, run the following command in the `controller` directory:

cd controller
ryu-manager allow_only_h1.py


### 2. Start Mininet with Python Script
In another terminal, navigate to the `mininet_topology` folder and run the Mininet topology:

cd mininet_topology
sudo python3 mininet_topology.py


## Testing the Network

In the Mininet CLI, use the following command to test connectivity:

mininet> pingall


You should observe the following:
- Only `h1` can communicate with the other hosts (`h2`, `h3`).
- Traffic from `h2` and `h3` will be blocked.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

