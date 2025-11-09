import reflex as rx

config = rx.Config(
    app_name="reflex_tool",
    favicon_path="NVIDIA-logo-white-16x9.png",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ],
)
