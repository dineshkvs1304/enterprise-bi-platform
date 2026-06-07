from app.core.base import Base
from app.core.database import engine

from app.models.role import Role
from app.models.user import User
from app.models.dataset import Dataset
from app.models.kpi import KPI
from app.models.report import Report
from app.models.audit_log import AuditLog

Base.metadata.create_all(bind=engine)

print("All tables created successfully")