from app.core.database import Base
from sqlalchemy.orm import Mapped, mapped_column
from app.core.mixins import TimeStampedMixin
from uuid import UUID, uuid4
from sqlalchemy import UUID as SqlAlchemyUUID, String

class Category(Base, TimeStampedMixin):
    __tablename__ = "categories"
    id: Mapped[UUID] = mapped_column(SqlAlchemyUUID(as_uuid=True), primary_key=True, default=uuid4)
    category_name: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)

