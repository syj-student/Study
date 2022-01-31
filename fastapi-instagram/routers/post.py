from fastapi import APIRouter, UploadFile, File, Depends
from sqlalchemy.orm import Session
from schemas import PostBase, PostDisplay
from DB.database import get_db
from DB import db_post

router = APIRouter(
    prefix='/post',
    tags=['post']
)


@router.post('/', response_model=PostDisplay)
def create_post(request: PostBase, db: Session = Depends(get_db)):
    return db_post.create_post(db, request)


@router.get('/all')
def get_all_post(db: Session = Depends(get_db)):
    return db_post.get_all_post(db)


@router.post('/image')
def upload_image(db: Session = Depends(get_db), request: UploadFile = File(...)):
    return db_post.upload_image(request)
