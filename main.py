from fastapi import FastAPI


app = FastAPI()


@app.get('/')
async def root():
    n = 'llllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllll'
    return {'message': 'hello'}
