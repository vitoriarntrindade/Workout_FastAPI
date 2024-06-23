from datetime import datetime
from sqlalchemy import DateTime, ForeignKey, Integer, String, Float, Column
from sqlalchemy.orm import relationship, Mapped, mapped_column
from contrib.models import BaseModel


class AthleteModel(BaseModel):
    __tablename__ = 'athletes'

    pk_id: int = Column(Integer, primary_key=True)
    name: str = Column(String(50), nullable=False)
    cpf: str = Column(String(11), unique=True, nullable=False)
    age: int = Column(Integer, nullable=False)
    weight: float = Column(Float, nullable=False)
    height: float = Column(Float, nullable=False)
    sex: str = Column(String(1), nullable=False)
    created_at: datetime = Column(DateTime, nullable=False, default=datetime.utcnow)

    category: Mapped['CategoryModel'] = relationship(back_populates="athlete", lazy='selectin')
    category_id: Mapped[int] = mapped_column(ForeignKey("categories.pk_id"))

    training_center: Mapped['TrainingCenterModel'] = relationship(back_populates="athlete", lazy='selectin')
    training_center_id: Mapped[int] = mapped_column(ForeignKey("training_centers.pk_id"))