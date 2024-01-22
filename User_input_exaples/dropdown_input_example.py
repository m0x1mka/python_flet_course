import flet as ft


def main(page: ft.Page):
    def button_clicked(e):
        output_text.value = f"Значение выпадающего списка:  {color_dropdown.value}"
        page.update()

    output_text = ft.Text()
    submit_btn = ft.ElevatedButton(text="Submit", on_click=button_clicked)
    color_dropdown = ft.Dropdown(
        width=100,
        options=[
            ft.dropdown.Option("Красный"),
            ft.dropdown.Option("Зеленый"),
            ft.dropdown.Option("Синий"),
        ],
    )
    page.add(color_dropdown, submit_btn, output_text)


ft.app(target=main)
