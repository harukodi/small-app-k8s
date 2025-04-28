import socket
from fastapi import FastAPI, Response
from pydantic import BaseModel
from fastapi.responses import HTMLResponse

class HealthCheck(BaseModel):
    status: str = "OK"

app = FastAPI()
health_checked = False

@app.get("/")
async def get_hostname():
    """Returns the hostname of the server with some ugly css animations for fun"""
    html_content = f"""
        <html>
        <head>
            <style>
                @keyframes rainbow-text {{
                    0% {{ color: red; transform: scale(0); }}
                    6.67% {{ color: orangered; transform: scale(1.5); }}
                    13.34% {{ color: orange; transform: scale(1); }}
                    20.01% {{ color: gold; transform: scale(1.5); }}
                    26.68% {{ color: yellow; transform: scale(1); }}
                    33.35% {{ color: lime; transform: scale(1.5); }}
                    40.02% {{ color: green; transform: scale(1); }}
                    46.69% {{ color: teal; transform: scale(1.5); }}
                    53.36% {{ color: cyan; transform: scale(1); }}
                    60.03% {{ color: dodgerblue; transform: scale(1.5); }}
                    66.70% {{ color: blue; transform: scale(1); }}
                    73.37% {{ color: indigo; transform: scale(1.5); }}
                    80.04% {{ color: violet; transform: scale(1); }}
                    86.71% {{ color: pink; transform: scale(1.5); }}
                    93.38% {{ color: deeppink; transform: scale(1); }}
                    100% {{ color: red; transform: scale(1.5); }}
                }}
        
                @keyframes rainbow-bg {{
                    0% {{ background-color: blue; }}
                    6.67% {{ background-color: indigo; }}
                    13.34% {{ background-color: violet; }}
                    20.01% {{ background-color: pink; }}
                    26.68% {{ background-color: deeppink; }}
                    33.35% {{ background-color: red; }}
                    40.02% {{ background-color: orangered; }}
                    46.69% {{ background-color: orange; }}
                    53.36% {{ background-color: gold; }}
                    60.03% {{ background-color: yellow; }}
                    66.70% {{ background-color: lime; }}
                    73.37% {{ background-color: green; }}
                    80.04% {{ background-color: teal; }}
                    86.71% {{ background-color: cyan; }}
                    93.38% {{ background-color: dodgerblue; }}
                    100% {{ background-color: blue; }}
                }}
        
                body {{
                    display: flex;
                    flex-direction: column;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    margin: 0;
                    font-family: 'Comic Sans MS', cursive, sans-serif;
                    animation: rainbow-bg 20s infinite ease-in-out reverse;
                }}
        
                h1 {{
                    text-align: center;
                    font-size: 120px;
                    font-weight: bold;
                    animation: rainbow-text 5s infinite ease-in-out;
                    margin: 0;
                }}
            </style>
        </head>
        <body>
            <h1>{socket.gethostname()}</h1>
            <p></p>
            <p></p>
            <p></p>
            <h1>v3</h1>
        </body>
        </html>
    """
    return HTMLResponse(content=html_content, status_code=418)

@app.get("/health")
async def get_health(response: Response):
    global health_checked
    if health_checked == False:
        health_checked = True
        response.headers["Health-status"] = "OK"
        return HealthCheck(status="OK"), 200
    else:
        health_checked = False
        response.headers["Health-status"] = "DOWN"
        return HealthCheck(status="DOWN"), 503