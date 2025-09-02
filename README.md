# indico-plugin-price-adjustments

This plugin provides registration price adjustment options for non-logged-in users.

## Installation

Install the plugin [package](https://pypi.org/project/indico-plugin-price-adjustments/) from PyPI
```bash
pip install indico-plugin-price-adjustments
```

Open `indico.conf` of your indico installation then add `price-adjustments` on `PLUGIN`.
```python
PLUGINS = { ... , 'price-adjustments'}
```

## Install for development for contributing to this plugin

Clone this repository on `~/dev/indico/plugins`
```bash
git clone https://github.com/RobotHanzo/indico-plugin-price-adjustments.git
```

With python virtual environment of Indico development installation enabled, enter the cloned directory then run following command to install the plugin.
```bash
pip install -e .
```

Open `indico.conf` which should be located in `~/dev/indico/src/indico` then add `price-adjustments` on `PLUGIN`.
```python
PLUGINS = { ... , 'price-adjustments'}
```

You can now test you modification on your development indico environment.