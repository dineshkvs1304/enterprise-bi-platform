from fastapi import FastAPI

from app.routers.auth_router import router as auth_router
from app.routers.user_router import router as user_router
from app.routers.dataset_router import router as dataset_router
from app.routers.kpi_router import router as kpi_router
from app.routers.dashboard_router import router as dashboard_router
from app.routers.analytics_router import (
    router as analytics_router
)
from app.routers.trend_router import (
    router as trend_router
)

from app.routers.chart_router import (
    router as chart_router
)

from app.routers.profit_chart_router import (
    router as profit_chart_router
)

from app.routers.pie_chart_router import (
    router as pie_chart_router
)

app = FastAPI(
    title="Enterprise BI Platform",
    version="1.0.0"
)


@app.get("/")
def home():

    return {
        "message": "Enterprise BI Platform Running"
    }


app.include_router(auth_router)

app.include_router(user_router)

app.include_router(dataset_router)

app.include_router(kpi_router)

app.include_router(dashboard_router)

app.include_router(
    analytics_router
)

app.include_router(
    trend_router
)

app.include_router(
    chart_router
)

app.include_router(
    profit_chart_router
)

app.include_router(
    pie_chart_router
)