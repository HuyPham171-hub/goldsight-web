import reflex as rx
import os

config = rx.Config(
    app_name="goldsight",
    # Backend config for production
    backend_host="0.0.0.0" if os.getenv("ENV") == "prod" else "127.0.0.1",
    backend_port=int(os.getenv("PORT", 8000)),
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ]
)