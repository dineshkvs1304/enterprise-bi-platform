from app.core.database import SessionLocal

# Import ALL models so SQLAlchemy knows them
from app.models.role import Role
from app.models.user import User
from app.models.dataset import Dataset
from app.models.kpi import KPI
from app.models.report import Report
from app.models.audit_log import AuditLog

db = SessionLocal()

roles = [
    "Admin",
    "Analyst",
    "Executive"
]

for role_name in roles:

    existing_role = (
        db.query(Role)
        .filter(Role.name == role_name)
        .first()
    )

    if not existing_role:
        db.add(Role(name=role_name))

db.commit()

print("Roles seeded successfully")