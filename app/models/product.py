from decimal import Decimal

from uuid import UUID, uuid4

from app.core.database import Base
from app.core.mixins import TimeStampedMixin

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import UUID as SqlAlchemyUUID, String, ForeignKey, Numeric


class Product(Base, TimeStampedMixin):
    __tablename__ = "products"
    id: Mapped[UUID] = mapped_column(SqlAlchemyUUID(as_uuid=True), primary_key=True, default=uuid4)
    store_id: Mapped[UUID] = mapped_column(SqlAlchemyUUID(as_uuid=True), nullable=False)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    description: Mapped[str] = mapped_column(String(1000), nullable=False)
    base_price: Mapped[Decimal] = mapped_column(Numeric(10, 2), nullable=False)
    category_id: Mapped[UUID] = mapped_column(ForeignKey("categories.id"), nullable=False)    