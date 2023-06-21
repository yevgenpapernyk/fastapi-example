from enum import Enum

from fastapi import FastAPI

app = FastAPI()


@app.get('/')
async def root():
    return {'message': 'Hello World'}


@app.get('/hello_query_name/')
async def hello_query_name(first_name: str):
    message = f'Hello {first_name}'

    return {'message': message}


@app.get('/hello_path_name/{first_name}')
async def hello_path_name(first_name: str):
    message = f'Hello {first_name}'

    return {'message': message}


class FirstNameEnum(str, Enum):
    Bill = 'Bill'
    John = 'John'
    Steve = 'Steve'


@app.get('/alternatives/{name}')
async def alternatives(first_name: FirstNameEnum):
    message = f'Hello {first_name.name}'

    return {'message': message}


@app.get('/optional/{name}')
async def optional(first_name: FirstNameEnum | None = None):
    if first_name:
        message = f'Hello {first_name.name}'
    else:
        message = f'Hello unnamed!'

    return {'message': message}



