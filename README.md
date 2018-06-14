![Logo](https://raw.githubusercontent.com/idealista/prometheus_alertmanager-role/master/logo.gif)

# Prometheus Alert Manager Ansible role

This ansible role installs an Alert Manager server in a debian environment. The server is installed using the sources.

- [Getting Started](#getting-started)
	- [Prerequisities](#prerequisities)
	- [Installing](#installing)
- [Usage](#usage)
- [Testing](#testing)
- [Built With](#built-with)
- [Versioning](#versioning)
- [Authors](#authors)
- [License](#license)
- [Contributing](#contributing)

## Getting Started

These instructions will get you a copy of the role for your ansible playbook. Once launched, it will install an [Alert Manager](https://prometheus.io/docs/alerting/alertmanager/) server in a Debian system. The role is only compatible with Alert Manager versions greater than 0.13.0.

### Prerequisities

Ansible 2.2.0.0 version installed.
Inventory destination should be a Debian environment.

For testing purposes, [Molecule](https://molecule.readthedocs.io/) with [Vagrant](https://www.vagrantup.com/) as driver (with [landrush](https://github.com/vagrant-landrush/landrush) plugin) and [VirtualBox](https://www.virtualbox.org/) as provider.

### Installing

Create or add to your roles dependency file (e.g requirements.yml):

```
- src: idealista.prometheus_alertmanager-role
  version: 1.0.0
  name: alertmanager
```

Install the role with ansible-galaxy command:

```
ansible-galaxy install -p roles -r requirements.yml -f
```

Use in a playbook:

```
---
- hosts: someserver
  roles:
    - role: alertmanager
```

## Usage

Look to the [defaults](defaults/main.yml) properties file to see the possible configuration properties.

Alert Manager configuration is separated in 4 blocks (see https://prometheus.io/docs/alerting/configuration/).
First one, global configuration, is provided setting the properties for the role. The other ones: routes,
inhibit roles and receivers must be provided in 3 separated files. By default this files must be stored in
the path defined by this parameter `alertmanager_config_parts_path` and the filename headed with the position
of the block in the final config file. See [this folder](tests/files/) for example.

## Testing

```
molecule test
```

## Built With

![Ansible](https://img.shields.io/badge/ansible-2.2.0.0-green.svg)

## Versioning

For the versions available, see the [tags on this repository](https://github.com/idealista/prometheus_alertmanager-role/tags).

Additionaly you can see what change in each version in the [CHANGELOG.md](CHANGELOG.md) file.

## Authors

* **Idealista** - *Work with* - [idealista](https://github.com/idealista)

See also the list of [contributors](https://github.com/idealista/prometheus_alertmanager-role/contributors) who participated in this project.

## License

![Apache 2.0 Licence](https://img.shields.io/hexpm/l/plug.svg)

This project is licensed under the [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) license - see the [LICENSE](LICENSE) file for details.

## Contributing

Please read [CONTRIBUTING.md](.github/CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.
