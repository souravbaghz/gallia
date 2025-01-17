<!--
SPDX-FileCopyrightText: AISEC Pentesting Team

SPDX-License-Identifier: CC0-1.0
-->

# Gallia -- Rebellion Against the Romans

```{warning}
This project is intended for research and development usage only!
Inappropriate usage might cause irreversible damage to the device under test.
We do not take any responsibility for damage caused by the usage of this tool.
```

Gallia is an extendable pentesting framework with the focus on the automotive domain.
The scope of the toolchain is conducting penetration tests from a single ECU up to whole cars.
Currently, the main focus lies on the [UDS](https://www.iso.org/standard/72439.html) interface.
Taking advantage of this modular design, the [logging and archiving](https://fraunhofer-aisec.github.io/gallia/penlog.7.html) functionality was developed separately.
Acting as a generic interface, the logging functionality implements reproducible tests and enables post-processing tasks.

----

```{toctree}
:maxdepth: 1
:caption: Usage

setup
architecture
automation
transports
```

----

```{toctree}
:maxdepth: 1
:caption: UDS

uds/database
uds/scan_modes
uds/virtual_ecu
```

The current main focus of `gallia` is the UDS protocol.
Several concepts and ideas are implemented in `gallia` in order to provide comprehensive tests.

----

```{toctree}
:maxdepth: 1
:caption: API

penlog.7
api/modules
```

`gallia` is designed as a pentesting framework where each test produces a lot of data.
It is possible to design own standalone tools or plugins utilizing the `gallia` Python modules.

