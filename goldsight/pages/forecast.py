"""Forecast page - Real-time prediction."""
import reflex as rx


def forecast_page() -> rx.Component:
    """Forecast page component."""
    return rx.container(
        rx.vstack(
            rx.heading("Gold Price Forecast", size="9", margin_bottom="2rem"),
            
            rx.text(
                "Gold price forecast content will be added here.",
                size="4",
                color_scheme="gray"
            ),
            
            rx.link(
                rx.button("← Back to Home"),
                href="/"
            ),
            
            spacing="4",
            padding="2rem"
        )
    )
