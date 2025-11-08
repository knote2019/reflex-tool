import reflex as rx

config = rx.Config(
    app_name="reflex_tool",
    favicon_path="NVIDIA-logo-white-16x9.png",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ],
    backend_host="0.0.0.0",
    backend_port=8000,
    frontend_host="0.0.0.0",
    frontend_port=3000,
)
