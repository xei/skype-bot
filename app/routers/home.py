from fastapi import APIRouter, status
from fastapi.responses import HTMLResponse


router = APIRouter()


@router.get("/")
async def get_home_page():
    html_content = """
    <html>
        <head>
            <title>Skype Bot Service</title>
        </head>
        <body>
            <h1>Skype Bot Service</h1>
            Check the service health status <a href="/skype-bot/healthz">here</a>
            <br>
            Check out the documentation <a href="/skype-bot/docs">here</a>
            <br>
            Developed by Hamidreza Hosseinkhani
            <br>
            Be in touch with hamidreza@hosseinkhani.me in case of any problem.
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=status.HTTP_200_OK)
