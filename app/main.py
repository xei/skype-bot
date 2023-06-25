from fastapi import FastAPI

from routers.home import router as home_router
from routers.send_msg import router as send_msg_router
from routers.healthz import router as healthz_router



app = FastAPI(title="Skype Bot Service")


app.include_router(home_router)
app.include_router(send_msg_router)
app.include_router(healthz_router)
