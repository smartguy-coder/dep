from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

router = APIRouter(
    prefix='/pages',
    tags=['Pages']
)

templates = Jinja2Templates(directory='templates')


@router.get('/base')
def get_base_page(request: Request):
    return templates.TemplateResponse('base.html', {'request': request})

@router.get('/books')
def get_all_books(request: Request):

    features = ['first', 'second']

    books = [
        {'name': '12 chairs', 'price': 18},
        {'name': 'Smiles', 'price': 32},
    ]
    return templates.TemplateResponse(
        'all_books.html',
        {
            'request': request,
            'features': features,
            'books': books,
        }
    )
