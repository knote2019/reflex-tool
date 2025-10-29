"""主应用文件 - 包含导航栏和页面。"""
import reflex as rx


class State(rx.State):
    """应用状态。"""
    pass


def navbar() -> rx.Component:
    """创建导航栏组件。"""
    return rx.box(
        rx.hstack(
            # Logo 和品牌名称
            rx.hstack(
                rx.icon(
                    tag="layout-dashboard",
                    size=32,
                    color="white",
                ),
                rx.text(
                    "NVIDIA ModelOpt",
                    font_size="1.5rem",
                    font_weight="bold",
                    color="white",
                ),
                spacing="2",
            ),
            # 导航链接
            rx.hstack(
                rx.link(
                    "首页",
                    href="/",
                    color="white",
                    padding="0.5rem 1rem",
                    border_radius="0.5rem",
                    _hover={
                        "background_color": "rgba(255, 255, 255, 0.1)",
                        "text_decoration": "none",
                    },
                ),
                rx.link(
                    "关于",
                    href="/about",
                    color="white",
                    padding="0.5rem 1rem",
                    border_radius="0.5rem",
                    _hover={
                        "background_color": "rgba(255, 255, 255, 0.1)",
                        "text_decoration": "none",
                    },
                ),
                rx.link(
                    "服务",
                    href="/services",
                    color="white",
                    padding="0.5rem 1rem",
                    border_radius="0.5rem",
                    _hover={
                        "background_color": "rgba(255, 255, 255, 0.1)",
                        "text_decoration": "none",
                    },
                ),
                rx.link(
                    "联系",
                    href="/contact",
                    color="white",
                    padding="0.5rem 1rem",
                    border_radius="0.5rem",
                    _hover={
                        "background_color": "rgba(255, 255, 255, 0.1)",
                        "text_decoration": "none",
                    },
                ),
                spacing="1",
            ),
            # 右侧按钮
            rx.button(
                "登录",
                variant="outline",
                size="3",
                color="white",
                border_color="white",
                _hover={
                    "background_color": "rgba(255, 255, 255, 0.2)",
                },
            ),
            justify="between",
            align="center",
            width="100%",
        ),
        background="linear-gradient(135deg, #667eea 0%, #764ba2 100%)",
        padding="1rem 2rem",
        box_shadow="0 4px 6px rgba(0, 0, 0, 0.1)",
        position="sticky",
        top="0",
        z_index="1000",
        width="100%",
    )


def home_page() -> rx.Component:
    """首页。"""
    return rx.box(
        navbar(),
        rx.container(
            rx.vstack(
                rx.heading(
                    "欢迎来到 Reflex Demo",
                    font_size="3rem",
                    margin_top="4rem",
                    text_align="center",
                ),
                rx.text(
                    "这是一个使用 Reflex 框架构建的现代化导航栏示例",
                    font_size="1.2rem",
                    color="gray.600",
                    text_align="center",
                    margin_top="1rem",
                ),
                rx.hstack(
                    rx.box(
                        rx.icon(tag="zap", size=48, color="#667eea"),
                        rx.heading("快速", font_size="1.5rem", margin_top="1rem"),
                        rx.text(
                            "使用 Python 快速构建全栈应用",
                            color="gray.600",
                            text_align="center",
                        ),
                        padding="2rem",
                        border_radius="1rem",
                        box_shadow="0 4px 6px rgba(0, 0, 0, 0.1)",
                        width="300px",
                    ),
                    rx.box(
                        rx.icon(tag="layers", size=48, color="#667eea"),
                        rx.heading("灵活", font_size="1.5rem", margin_top="1rem"),
                        rx.text(
                            "组件化设计，易于定制和扩展",
                            color="gray.600",
                            text_align="center",
                        ),
                        padding="2rem",
                        border_radius="1rem",
                        box_shadow="0 4px 6px rgba(0, 0, 0, 0.1)",
                        width="300px",
                    ),
                    rx.box(
                        rx.icon(tag="sparkles", size=48, color="#667eea"),
                        rx.heading("现代", font_size="1.5rem", margin_top="1rem"),
                        rx.text(
                            "美观的用户界面，最佳用户体验",
                            color="gray.600",
                            text_align="center",
                        ),
                        padding="2rem",
                        border_radius="1rem",
                        box_shadow="0 4px 6px rgba(0, 0, 0, 0.1)",
                        width="300px",
                    ),
                    spacing="4",
                    margin_top="3rem",
                    wrap="wrap",
                    justify="center",
                ),
                spacing="4",
                padding="2rem",
            ),
            max_width="1200px",
        ),
    )


def about_page() -> rx.Component:
    """关于页面。"""
    return rx.box(
        navbar(),
        rx.container(
            rx.vstack(
                rx.heading(
                    "关于我们",
                    font_size="2.5rem",
                    margin_top="3rem",
                ),
                rx.text(
                    "Reflex 是一个纯 Python 的全栈 Web 框架，让您无需编写 JavaScript 即可构建现代化的 Web 应用。",
                    font_size="1.1rem",
                    color="gray.700",
                    margin_top="1.5rem",
                    line_height="1.8",
                ),
                rx.text(
                    "我们的导航栏具有以下特点：",
                    font_size="1.1rem",
                    font_weight="bold",
                    margin_top="2rem",
                ),
                rx.unordered_list(
                    rx.list_item("响应式设计，适配各种屏幕尺寸"),
                    rx.list_item("现代化的渐变背景和悬停效果"),
                    rx.list_item("固定在顶部，方便导航"),
                    rx.list_item("包含 Logo、链接和操作按钮"),
                    font_size="1.1rem",
                    color="gray.700",
                    spacing="3",
                    margin_top="1rem",
                ),
                spacing="4",
                padding="2rem",
                align="start",
            ),
            max_width="800px",
        ),
    )


def services_page() -> rx.Component:
    """服务页面。"""
    return rx.box(
        navbar(),
        rx.container(
            rx.vstack(
                rx.heading(
                    "我们的服务",
                    font_size="2.5rem",
                    margin_top="3rem",
                ),
                rx.grid(
                    rx.box(
                        rx.icon(tag="code", size=40, color="#667eea"),
                        rx.heading("Web 开发", font_size="1.3rem", margin_top="1rem"),
                        rx.text(
                            "使用最新技术栈开发高性能的 Web 应用",
                            color="gray.600",
                            margin_top="0.5rem",
                        ),
                        padding="2rem",
                        border_radius="1rem",
                        border="1px solid",
                        border_color="gray.200",
                        _hover={"box_shadow": "0 8px 16px rgba(0, 0, 0, 0.1)"},
                    ),
                    rx.box(
                        rx.icon(tag="smartphone", size=40, color="#667eea"),
                        rx.heading("移动应用", font_size="1.3rem", margin_top="1rem"),
                        rx.text(
                            "跨平台移动应用开发解决方案",
                            color="gray.600",
                            margin_top="0.5rem",
                        ),
                        padding="2rem",
                        border_radius="1rem",
                        border="1px solid",
                        border_color="gray.200",
                        _hover={"box_shadow": "0 8px 16px rgba(0, 0, 0, 0.1)"},
                    ),
                    rx.box(
                        rx.icon(tag="database", size=40, color="#667eea"),
                        rx.heading("数据分析", font_size="1.3rem", margin_top="1rem"),
                        rx.text(
                            "大数据处理和商业智能分析",
                            color="gray.600",
                            margin_top="0.5rem",
                        ),
                        padding="2rem",
                        border_radius="1rem",
                        border="1px solid",
                        border_color="gray.200",
                        _hover={"box_shadow": "0 8px 16px rgba(0, 0, 0, 0.1)"},
                    ),
                    rx.box(
                        rx.icon(tag="shield", size=40, color="#667eea"),
                        rx.heading("安全咨询", font_size="1.3rem", margin_top="1rem"),
                        rx.text(
                            "网络安全评估和防护方案",
                            color="gray.600",
                            margin_top="0.5rem",
                        ),
                        padding="2rem",
                        border_radius="1rem",
                        border="1px solid",
                        border_color="gray.200",
                        _hover={"box_shadow": "0 8px 16px rgba(0, 0, 0, 0.1)"},
                    ),
                    columns="2",
                    spacing="4",
                    margin_top="2rem",
                ),
                spacing="4",
                padding="2rem",
            ),
            max_width="1000px",
        ),
    )


def contact_page() -> rx.Component:
    """联系页面。"""
    return rx.box(
        navbar(),
        rx.container(
            rx.vstack(
                rx.heading(
                    "联系我们",
                    font_size="2.5rem",
                    margin_top="3rem",
                ),
                rx.box(
                    rx.vstack(
                        rx.text(
                            "有任何问题或建议？欢迎联系我们！",
                            font_size="1.1rem",
                            color="gray.700",
                            margin_bottom="2rem",
                        ),
                        rx.hstack(
                            rx.icon(tag="mail", size=24, color="#667eea"),
                            rx.text("邮箱: contact@example.com", font_size="1rem"),
                            spacing="2",
                            align="center",
                        ),
                        rx.hstack(
                            rx.icon(tag="phone", size=24, color="#667eea"),
                            rx.text("电话: +86 123-4567-8900", font_size="1rem"),
                            spacing="2",
                            align="center",
                        ),
                        rx.hstack(
                            rx.icon(tag="map-pin", size=24, color="#667eea"),
                            rx.text("地址: 北京市朝阳区示例路123号", font_size="1rem"),
                            spacing="2",
                            align="center",
                        ),
                        spacing="4",
                        align="start",
                    ),
                    padding="3rem",
                    border_radius="1rem",
                    box_shadow="0 4px 6px rgba(0, 0, 0, 0.1)",
                    margin_top="2rem",
                ),
                spacing="4",
                padding="2rem",
                align="start",
            ),
            max_width="800px",
        ),
    )


# 创建应用并添加页面
app = rx.App()
app.add_page(home_page, route="/")
app.add_page(about_page, route="/about")
app.add_page(services_page, route="/services")
app.add_page(contact_page, route="/contact")
