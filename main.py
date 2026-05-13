import flet as ft

def main(page: ft.Page):
    # Configuración de la cabina (Ventana)
    page.title = "AELIAN CHRONOS"
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = "#050505"  # Negro OLED para ahorrar batería
    page.window_width = 400
    page.window_height = 700
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # El Corazón de AELIAN: Interfaz Minimalista
    chronos_card = ft.Container(
        content=ft.Column([
            ft.Icon(ft.icons.TIMER_OUTLINED, color="#38bdf8", size=60),
            ft.Text(
                "AELIAN CHRONOS", 
                size=28, 
                weight=ft.FontWeight.BOLD, 
                color="#38bdf8",
                letter_spacing=2
            ),
            ft.Divider(color="#333333", height=20),
            ft.Text(
                "SISTEMA OPERATIVO", 
                color="gray", 
                size=12
            ),
            ft.ElevatedButton(
                "VERIFICAR CRON", 
                icon=ft.icons.PLAY_ARROW_ROUNDED,
                style=ft.ButtonStyle(
                    color="#050505",
                    bgcolor="#38bdf8",
                    shape=ft.RoundedRectangleBorder(radius=20), # Tus 20px de ley
                )
            ),
        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
        padding=40,
        width=320,
        border_radius=20, # Estética Senior confirmada
        border=ft.border.all(1, "#333333"),
        gradient=ft.LinearGradient(
            begin=ft.alignment.top_left,
            end=ft.alignment.bottom_right,
            colors=["#111111", "#050505"],
        ),
    )

    page.add(chronos_card)

if __name__ == "__main__":
    ft.app(target=main)