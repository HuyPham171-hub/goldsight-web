import reflex as rx
import os

config = rx.Config(
    app_name="goldsight",
    backend_host="0.0.0.0",
    backend_port=int(os.getenv("PORT", 10000)),
    api_url=os.getenv("API_URL", "http://127.0.0.1:8000"),
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ]
)