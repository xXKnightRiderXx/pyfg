# PyFG

PyFG is a Python 3.8+ package that allows you to interact with the configuration of a Fortigate firewall.

Quote from the original project: "API for FortiOS or how to turn FortiOS into JunOS"

## Introduction

This API allows you to interact with a device running FortiOS in a sane way. With this API you can:

* Connect to the device, retrieve the running configuration (either the entire config or just some blocks) and build a model
* Build the same model from a file
* Do changes in the candidate configuration locally
* Create a candidate configuration from a file
* Do a diff between the running configuration and the local candidate configuration
* Generate the necessary commands to go from the running configuration to the candidate configuration

## Documentation

You can find the documentation on [Read the Docs](https://pyfg.readthedocs.io/en/latest/index.html).

## Installation

To install the library clone the repository and install it with pip afterwards:

```
git clone https://github.com/xXKnightRiderXx/pyfg.git
pip install ./pyfg/
```

> [!NOTE]
> This fork is currently not available on the python package index. Hence cloning and manually installing is necessary.

## Examples

In the examples directory you will find different files with examples on how to use the API:

* example1 - How to retrieve the configuration of a VDOM
* example2 - How to get BGP information and navigate through it
* example3 - How to load BGP configuration from a file (running.conf is emulating this step), load the candidate configuration from a file and then check the differences and show to get to the candidate configuration from the running one.
* example4 - Similar as example3 but this time the changes are done programmatically instead of using a text file.
* example5 - This example will do some changes, will try to commit them, will detect that something went wrong and it will finally rollback the changes.
