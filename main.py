import datetime
from random import randrange
import shutil
import uvicorn

from schema import Book

from fastapi import FastAPI, Query, Path, UploadFile, File
from fastapi.staticfiles import StaticFiles
from pages.router import router as router_pages

app = FastAPI(
    title='Books app'
)

app.mount('/static', StaticFiles(directory='static'), name='static')

app.include_router(router_pages)


@app.on_event('startup')
def startup():
    print('kkkkkkkkkkk')


@app.on_event('shutdown')
def shutdown():
    print('finish')


@app.get('/')
async def root():
    pref = 'me'
    res = pref + 'ssage'

    return {res: 'hello'}


@app.get('/{number}')
async def simple_validator(number: int, q: int = None):
    multiply_coefficient = q or 2
    result = number * multiply_coefficient

    return {
        'message': f'the number {number} was multiplied by {multiply_coefficient}',
        'result': result,
    }


@app.get('/user/{user_id}/data/{operation}')
async def work_with_address(user_id: int, operation: str = 'balance'):
    random_balance = randrange(1, 10000)
    current_time = datetime.datetime.now()

    return {
        'message': 'ok',
        'result': random_balance,
        'user_id': user_id,
        'time': current_time,
    }


@app.post('/book', response_model=Book, response_model_exclude={'date'})
def create_book__pydantic_validator(item: Book):
    # https://docs.pydantic.dev/latest/usage/exporting_models/#advanced-include-and-exclude
    # print(item)
    return item


# @app.get('/book')  # doesn't work
# async def create_book__with_query(
#         # q: str = Query(
#         q: List[str] = Query(
#             'def',  # None or ...  elipsis for required param, 'default data'
#             # min_length=3,
#             # max_length=5,
#             description='Search book',
#             deprecated=True,
#         )
# ):
#     return {}
@app.post('/file')
def file_upload(file: UploadFile = File(...)):
    """file uploading"""
    with open('test.jpeg', 'wb') as buffer:
        shutil.copyfileobj(file.file, buffer)
    return {'filename': file.filename}


@app.post('/files')
def files_upload(files: list[UploadFile] = File(...)):
    """file uploading"""
    for file in files:
        with open(f'{file.filename}', 'wb') as buffer:
            shutil.copyfileobj(file.file, buffer)
    return {'filename': 'all'}


@app.get('/book/{pk}')
async def get_single_book(
        pk: int = Path(..., gt=0, le=50000),
        pages: int = Query(None, gt=10)

):
    return pk


if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0', port=80)
