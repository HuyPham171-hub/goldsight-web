import reflex as rx


def navbar() -> rx.Component:
    """Navigation bar with professional gold theme and active page highlighting."""
    
    # JavaScript code for active link detection (inline to avoid external file loading issues)
    navbar_script = """
    (function() {
        function updateActiveNavLink() {
            const currentPath = window.location.pathname.replace(/\\/$/, '') || '/';
            const navLinks = document.querySelectorAll('.nav-link');
            
            navLinks.forEach(link => {
                const linkPath = link.getAttribute('data-path');
                const isActive = currentPath === linkPath || 
                                (linkPath !== '/' && currentPath.startsWith(linkPath));
                
                if (isActive) {
                    link.style.color = 'var(--amber-9)';
                    link.style.fontWeight = 'bold';
                    link.style.textDecoration = 'underline';
                } else {
                    link.style.color = 'var(--gray-11)';
                    link.style.fontWeight = 'medium';
                    link.style.textDecoration = 'none';
                }
            });
        }
        
        // Run on page load
        if (document.readyState === 'loading') {
            document.addEventListener('DOMContentLoaded', updateActiveNavLink);
        } else {
            updateActiveNavLink();
        }
        
        // Also run on navigation
        window.addEventListener('popstate', updateActiveNavLink);
    })();
    """
    
    inactive_link_style = {
        "color": "var(--gray-11)",
        "font_weight": "medium",
        "text_decoration": "none",
        "text_underline_offset": "4px",
    }
    
    hover_style = {"color": "var(--amber-9)"}
    
    return rx.box(
        rx.container(
            rx.hstack(
                # Logo
                rx.image(
                    src="/Gold_Ingot.png",
                    width="40px",
                    height="40px",
                    alt="GoldSight Logo"
                ),
                rx.heading(
                    "GoldSight",
                    size="7",
                    color_scheme="amber",
                    weight="bold"
                ),
                
                rx.spacer(),
                
                # Navigation links with data-path for JavaScript detection
                rx.hstack(
                    rx.link(
                        "Home",
                        href="/",
                        **inactive_link_style,
                        _hover=hover_style,
                        class_name="nav-link",
                        custom_attrs={"data-path": "/"}
                    ),
                    rx.link(
                        "Data Collection",
                        href="/data-collection",
                        **inactive_link_style,
                        _hover=hover_style,
                        class_name="nav-link",
                        custom_attrs={"data-path": "/data-collection"}
                    ),
                    rx.link(
                        "EDA",
                        href="/eda",
                        **inactive_link_style,
                        _hover=hover_style,
                        class_name="nav-link",
                        custom_attrs={"data-path": "/eda"}
                    ),
                    rx.link(
                        "Modeling",
                        href="/modeling",
                        **inactive_link_style,
                        _hover=hover_style,
                        class_name="nav-link",
                        custom_attrs={"data-path": "/modeling"}
                    ),
                    rx.link(
                        "Forecast",
                        href="/forecast",
                        color="var(--amber-9)",
                        font_weight="bold",
                        text_decoration="none",
                        text_underline_offset="4px",
                        _hover={"color": "var(--amber-11)"},
                        class_name="nav-link",
                        custom_attrs={"data-path": "/forecast"}
                    ),
                    spacing="9",
                    align="center"
                ),
                
                width="100%",
                align="center",
                justify="between"
            ),
            max_width="1200px"
        ),
        
        background_color=rx.color("gray", 1),
        border_bottom=f"1px solid {rx.color('gray', 4)}",
        padding_y="1em",
        width="100%",
        position="sticky",
        top="0",
        z_index="1000",
        box_shadow="0 1px 3px 0 rgba(0, 0, 0, 0.05)",
        backdrop_filter="blur(8px)",
        # Inline script to handle active state (using on_mount workaround)
        on_mount=rx.call_script(navbar_script)
    )