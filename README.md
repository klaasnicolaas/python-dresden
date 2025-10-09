<!-- Banner -->
![alt Banner of the ODP Dresden package](https://raw.githubusercontent.com/klaasnicolaas/python-dresden/main/assets/header_dresden-min.png)

<!-- PROJECT SHIELDS -->
[![GitHub Release][releases-shield]][releases]
[![Python Versions][python-versions-shield]][pypi]
![Project Stage][project-stage-shield]
![Project Maintenance][maintenance-shield]
[![License][license-shield]](LICENSE)

[![GitHub Activity][commits-shield]][commits-url]
[![PyPi Downloads][downloads-shield]][downloads-url]
[![GitHub Last Commit][last-commit-shield]][commits-url]
[![Open in Dev Containers][devcontainer-shield]][devcontainer]

[![Build Status][build-shield]][build-url]
[![Typing Status][typing-shield]][typing-url]
[![Code Coverage][codecov-shield]][codecov-url]

Asynchronous Python client for the open datasets of Dresden (Germany).

## About

A python package with which you can retrieve data from the Open Data Platform of Dresden via [their API][api]. This package was initially created to only retrieve parking data from the API, but the code base is made in such a way that it is easy to extend for other datasets from the same platform.

## Installation

```bash
pip install dresden
```

## Datasets

You can read the following datasets with this package:

- [Disabled parking spaces / Parken für Menschen mit Behinderungen][disabled_parkings] (477)

There are a number of parameters you can set to retrieve the data:

- **limit** (default: 10) - How many results you want to retrieve.

<details>
    <summary>Click here to get more details</summary>

### Disabled parking spaces

| Variable | Type | Description |
| :------- | :--- | :---------- |
| `entry_id` | integer | The ID of the disabled parking spot |
| `number` | integer | The number of parking spots on this location |
| `usage_time` | string | Some locations have window times where the location is only specific for disabled parking, outside these times everyone is allowed to park there |
| `photo` | string | URL that points to a photo that shows where the location is |
| `created_at` | datetime | The date when this location was added to the dataset |
| `longitude` | float | The longitude of the parking spot |
| `latitude` | float | The latitude of the parking spot |

</details>

## Example

```python
import asyncio

from dresden import ODPDresden


async def main() -> None:
    """Show example on using the Dresden API client."""
    async with ODPDresden() as client:
        disabled_parkings = await client.disabled_parkings()
        print(disabled_parkings)


if __name__ == "__main__":
    asyncio.run(main())
```

## Use cases

[NIPKaart.nl][nipkaart]

A website that provides insight into where disabled parking spaces are, based on
data from users and municipalities. Operates mainly in the Netherlands, but also
has plans to process data from abroad.

## Contributing

This is an active open-source project. We are always open to people who want to
use the code or contribute to it.

We've set up a separate document for our
[contribution guidelines](CONTRIBUTING.md).

Thank you for being involved! :heart_eyes:

## Setting up development environment

The simplest way to begin is by utilizing the [Dev Container][devcontainer]
feature of Visual Studio Code or by opening a CodeSpace directly on GitHub.
By clicking the button below you immediately start a Dev Container in Visual Studio Code.

[![Open in Dev Containers][devcontainer-shield]][devcontainer]

This Python project relies on [Poetry][poetry] as its dependency manager,
providing comprehensive management and control over project dependencies.

You need at least:

- Python 3.11+
- [Poetry][poetry-install]

### Installation

Install all packages, including all development requirements:

```bash
poetry install
```

_Poetry creates by default an virtual environment where it installs all
necessary pip packages_.

### Pre-commit

This repository uses the [pre-commit][pre-commit] framework, all changes
are linted and tested with each commit. To setup the pre-commit check, run:

```bash
poetry run pre-commit install
```

And to run all checks and tests manually, use the following command:

```bash
poetry run pre-commit run --all-files
```

### Testing

It uses [pytest](https://docs.pytest.org/en/stable/) as the test framework. To run the tests:

```bash
poetry run pytest
```

To update the [syrupy](https://github.com/tophat/syrupy) snapshot tests:

```bash
poetry run pytest --snapshot-update
```

## License

MIT License

Copyright (c) 2022-2025 Klaas Schoute

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

[api]: https://opendata.dresden.de
[nipkaart]: https://www.nipkaart.nl

[disabled_parkings]: https://opendata.dresden.de/informationsportal/?open=1&result=1788DE054C09464DB95AD54725002EA2#app/mainpage

<!-- MARKDOWN LINKS & IMAGES -->
[build-shield]: https://github.com/klaasnicolaas/python-dresden/actions/workflows/tests.yaml/badge.svg
[build-url]: https://github.com/klaasnicolaas/python-dresden/actions/workflows/tests.yaml
[commits-shield]: https://img.shields.io/github/commit-activity/y/klaasnicolaas/python-dresden.svg
[commits-url]: https://github.com/klaasnicolaas/python-dresden/commits/main
[codecov-shield]: https://codecov.io/gh/klaasnicolaas/python-dresden/branch/main/graph/badge.svg?token=70ZETUK1M6
[codecov-url]: https://codecov.io/gh/klaasnicolaas/python-dresden
[devcontainer-shield]: https://img.shields.io/static/v1?label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode
[devcontainer]: https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/klaasnicolaas/python-dresden
[downloads-shield]: https://img.shields.io/pypi/dm/dresden
[downloads-url]: https://pypistats.org/packages/dresden
[license-shield]: https://img.shields.io/github/license/klaasnicolaas/python-dresden.svg
[last-commit-shield]: https://img.shields.io/github/last-commit/klaasnicolaas/python-dresden.svg
[maintenance-shield]: https://img.shields.io/maintenance/yes/2025.svg
[project-stage-shield]: https://img.shields.io/badge/project%20stage-experimental-yellow.svg
[pypi]: https://pypi.org/project/dresden/
[python-versions-shield]: https://img.shields.io/pypi/pyversions/dresden
[typing-shield]: https://github.com/klaasnicolaas/python-dresden/actions/workflows/typing.yaml/badge.svg
[typing-url]: https://github.com/klaasnicolaas/python-dresden/actions/workflows/typing.yaml
[releases-shield]: https://img.shields.io/github/release/klaasnicolaas/python-dresden.svg
[releases]: https://github.com/klaasnicolaas/python-dresden/releases

[poetry-install]: https://python-poetry.org/docs/#installation
[poetry]: https://python-poetry.org
[pre-commit]: https://pre-commit.com
