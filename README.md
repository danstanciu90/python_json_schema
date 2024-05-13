# JSON schema generator example
This project is an example of how to generate a json schema from python classes.

## Prerequisites
### Poetry
The project uses [`Poetry`]((https://python-poetry.org/docs/)) for dependency management and
creating a consistent virtual env across multiple devices, ensuring better collaboration on the
project.

> Poetry requires python 3.8+

### Python
You need to have python installed on your machine, version 3.8 or above to ensure compatibility with
`Poetry`

### Pydantic
Pydantic is used to generate the json schema from python classes. Read [the docs](https://docs.pydantic.dev/latest/concepts/json_schema/) before getting started

## Getting started
1. Clone the repo
2. Open a terminal window, navigate to the root folder of this project and run `poetry install` to
   install all dependencies
3. Execute `poetry run python ./pc_json_schema/power_curve.py` and find the generated json schema in
   the `json_schemas` folder