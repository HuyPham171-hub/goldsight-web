import reflex as rx
import os

# Detect if running in production (Render) or local
is_prod = os.getenv("RENDER") is not None

config = rx.Config(
    app_name="goldsight",
    backend_host="0.0.0.0" if is_prod else "127.0.0.1",
    backend_port=int(os.getenv("PORT", 8000)),
    api_url=os.getenv("API_URL", "http://127.0.0.1:8000"),
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ]
)