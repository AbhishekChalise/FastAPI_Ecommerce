from fastapi import APIRouter, Depends, status
from app.schemas.products_schema import ProductCreate
from app.core.database import get_db
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.product import Product
from app.schemas.products_schema import ProductResponse

router = APIRouter()

@router.post('/', response_model=ProductResponse, status_code  = status.HTTP_201_CREATED)
async def create_product(payload: ProductCreate, db: AsyncSession = Depends(get_db)):

    product_data = payload.model_dump()
    new_product = Product(**product_data)

    db.add(new_product)

    await db.commit()

    await db.refresh(new_product)

    return new_product
