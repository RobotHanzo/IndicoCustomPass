# indico-custom-pass

This plugin grants admins the ability to customize Indico Google Wallet & Apple Pay passes.

## Installation

Install the plugin [package](https://pypi.org/project/indico-custom-pass/) from PyPI
```bash
pip install indico-custom-pass
```

Open `indico.conf` of your indico installation then add `custom_pass` on `PLUGIN`.
```python
PLUGINS = { ... , 'custom_pass'}
```

## Install for development for contributing to this plugin

Clone this repository on `~/dev/indico/plugins`
```bash
git clone https://github.com/RobotHanzo/IndicoCustomPass.git
```

With python virtual environment of Indico development installation enabled, enter the cloned directory then run following command to install the plugin.
```bash
pip install -e .
```

Open `indico.conf` which should be located in `~/dev/indico/src/indico` then add `custom_pass` on `PLUGIN`.
```python
PLUGINS = { ... , 'custom_pass'}
```

You can now test you modification on your development indico environment.