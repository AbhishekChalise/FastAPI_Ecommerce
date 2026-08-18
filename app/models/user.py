from app.core.database import Base
from app.core.mixins import TimeStampedMixin

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import UUID as SqlAlchemyUUID, String, Boolean

from uuid import UUID, uuid4

class User(Base, TimeStampedMixin):

    __tablename__ = "users"
    id: Mapped[UUID] = mapped_column(SqlAlchemyUUID(as_uuid=True), primary_key=True, default=uuid4)
    first_name: Mapped[str] = mapped_column(String(50), nullable=False)
    middle_name: Mapped[str] = mapped_column(String(50), nullable=False)
    last_name: Mapped[str] = mapped_column(String(50), nullable=False)
    email: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(50), nullable=False)
    is_seller: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)