[![Build Status](https://travis-ci.org/Bonifase/flight-reservation-api.svg?branch=develop)](https://travis-ci.org/Bonifase/flight-reservation-api) [![Coverage Status](https://coveralls.io/repos/github/Bonifase/flight-reservation-api/badge.svg?branch=develop)](https://coveralls.io/github/Bonifase/flight-reservation-api?branch=develop) [![Maintainability](https://api.codeclimate.com/v1/badges/6aff2c80302fc35d4afa/maintainability)](https://codeclimate.com/github/Bonifase/flight-reservation-api/maintainability)

<!-- ABOUT THE PROJECT -->

## About The Project

Flight reservation system

### Built With

Main stack and major frameworks used in this project.

- [Python](https://www.python.org/)
- [Flask](http://flask.pocoo.org/)
- [SQlAlchemy](https://www.sqlalchemy.org/)
- [Postgresql](https://www.postgresql.org/)

<!-- GETTING STARTED -->

## Getting Started

Lets look at what we need to get started now

## API endpoints

#### See the API documentaion [here](https://web.postman.co/collections/4175392-ff45c916-b1fc-4a94-9034-4733f9dd04d3?version=latest&workspace=16c98f63-155f-41f9-8895-523531f8619c#1ab35c18-1847-4e5a-85ed-98300c490082)

| Endpoint                                                                  | Method | Description              |
| ------------------------------------------------------------------------- | ------ | ------------------------ |
| `https://book-flight.herokuapp.com/api/register`                          | POST   | Register users           |
| `https://book-flight.herokuapp.com/api/login`                             | POST   | Login users with JWT     |
| `https://book-flight.herokuapp.com/api/logout`                            | POST   | Logout users with JWT    |
| `https://book-flight.herokuapp.com/api/flight`                            | POST   | Add new flight           |
| `https://book-flight.herokuapp.com/api/flights`                           | GET    | Get all flights          |
| `https://book-flight.herokuapp.com/api/flight/<flight_id>`                | GET    | Get one flights          |
| `https://book-flight.herokuapp.com/api/flight/<flight_id>/seat`           | POST   | Add seat                 |
| `https://book-flight.herokuapp.com/api/flight/<flight_id>/seat/<seat_id>` | GET    | Get one seat in a flight |
| `https://book-flight.herokuapp.com/api/booking`                           | POST   | Book flight              |
| `https://book-flight.herokuapp.com/api/bookings`                          | GET    | Get all bookins          |
| `https://book-flight.herokuapp.com/api/bookings/<flight_id>`              | GET    | Get all users bookings   |

### Prerequisites

Use pip to install all the project dependancies.

- pip

```sh
pip install pip -g
```

### Installation

1. Clone the repo

```sh
git clone https://github.com/Bonifase/flight-reservation-rest-api.git
```

2. Install packages

```sh
pip install
```

### Running tests

1. Run test using nose

```sh
nosetests
```

## Usage

This application allows authenticated users to reserve and book flights.

## Contributing

Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request
