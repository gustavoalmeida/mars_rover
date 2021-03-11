# Mars Rover Kata
> Exercise Version: 1.4, Last updated: 2021-02-02

### Project dependencies

* Python 3.9
* Poetry 1.1.5

## How to run


### Docker compose

Assuming you have docker compose configured. You can easily run the Mars Rover Kata with the following steps:

1. Clone this project:
```bash
git clone git@github.com:gustavoalmeida/mars_rover.git
```
2. Enter into the project folder:
```bash
cd mars_rover
```
3. Run the make command:
```bash
make compose
```

### Development

In order to run this project you need to have configured:

#### Project Dependencies

* Python 3.9
* Poetry 1.1.5


#### Running the project


```bash
make rover
```

or 

```bash
poetry install  
poetry run python rover.py ignite
```

#### Testing

Run this comand in order to run the project's test

```bash
make tests
```

or

```
poetry install
poetry run pytest
```

#### Formating

Run this command to format the code

```bash
make format
```

or

```
poetry install
poetry run black .
```