import reflex as rx

config = rx.Config(
    app_name="reflex_tool",
    favicon_path="NVIDIA-logo-white-16x9.png",
    frontend_port=8080,
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ],
)
