# UFC Tournament API

A Flask-based API for managing a UFC tournament where fighters have various skills and weaknesses.

## Features

- CRUD operations for fighters
- Fight logic to determine winners and ties
- API endpoints to add fighters, create fights, and get fight winners

## Technologies Used

- Python
- Flask
- SQLAlchemy
- pytest

## Installation

### Clone the Repository

```bash
git clone https://github.com/davidmm07/ufc_api.git
cd ufc_api
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Application

```bash
python run.py
```

## API Endpoints

### Get All Fighters

```http
GET /fighters
```

### Get Single Fighter

```http
GET /fighters/{fighter_id}
```

### Add Fighter

```http
POST /fighters
```

**Request Body**

```json
{
    "name": "John",
    "skills": "Jiu-Jitsu,Wrestling",
    "weaknesses": "Striking"
}
```

### Add Fight

```http
POST /fights
```

**Request Body**

```json
{
    "fighter1_id": 1,
    "fighter2_id": 2
}
```

### Get Fight Winner

```http
GET /fights/{fight_id}/winner
```

## Fight Logic

The winner of a fight is determined based on the skills of one fighter and the weaknesses of the other fighter.

### Example

- Fighter1: Skills - Jiu-Jitsu, Wrestling
- Fighter2: Weaknesses - Striking

The winner would be Fighter1, as he has skills that Fighter2 is weak against.


## Testing

Run the following command to execute the tests:

```bash
pytest
```

## Coverage

To generate a coverage report:

```bash
coverage run -m pytest
coverage report
```

## Migrate

Migrate first before implement seed

```bash
flask db init
flask db migrate
flask db upgrade
```

## Seed Data

To seed the database with initial data:

```bash
flask seed_db
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)
