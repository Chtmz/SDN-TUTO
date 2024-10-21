#!/usr/bin/python

from mininet.net import Mininet
from mininet.node import RemoteController, OVSSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel

def start_network():
    """Create and start the network with one controller and three hosts."""

    # Create a Mininet network object
    net = Mininet(controller=RemoteController, switch=OVSSwitch)

    # Add a remote controller (Ryu) at IP 127.0.0.1
    controller = net.addController('c0', controller=RemoteController, ip='127.0.0.1', port=6633)

    # Add a switch (OVS with OpenFlow 1.3 support)
    switch = net.addSwitch('s1', protocols='OpenFlow13')

    # Add three hosts
    h1 = net.addHost('h1', ip='10.0.0.1')
    h2 = net.addHost('h2', ip='10.0.0.2')
    h3 = net.addHost('h3', ip='10.0.0.3')

    # Create links between the switch and the hosts
    net.addLink(switch, h1)
    net.addLink(switch, h2)
    net.addLink(switch, h3)

    # Start the network
    net.start()

    # Run the CLI (to test with ping, etc.)
    CLI(net)

    # Stop the network when done
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')  # Set Mininet logging level to 'info'
    start_network()
