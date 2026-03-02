from sqlalchemy import String, Text
from sqlalchemy.orm import Mapped, mapped_column
from db import Base

class Project(Base):
    __tablename__ = "projects"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(200), unique=True, index=True)
    summary: Mapped[str] = mapped_column(String(300))
    details: Mapped[str] = mapped_column(Text)


