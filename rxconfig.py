import reflex as rx
import os

# Detect if running in static export mode (Vercel deployment)
IS_STATIC_EXPORT = os.getenv("VERCEL") is not None or os.getenv("REFLEX_DISABLE_WEBSOCKET") == "1"

config = rx.Config(
    app_name="goldsight",
    backend_host="0.0.0.0" if not IS_STATIC_EXPORT else None,
    backend_port=int(os.getenv("PORT", 8000)) if not IS_STATIC_EXPORT else None,
    disable_plugins=["reflex.plugins.sitemap.SitemapPlugin"],
    # For static deployments, disable backend URL to prevent WebSocket connection attempts
    backend_url=None if IS_STATIC_EXPORT else None,
)