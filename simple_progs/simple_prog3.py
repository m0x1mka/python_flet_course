# Program with some buttons
# Enter your name and surname and it will greet you!
import flet as ft


def main(page):
    first_name = ft.TextField(label="First Name", autofocus=True)
    last_name = ft.TextField(label="Last Name")
    greetings = ft.Column()

    def btn_click(e):
        greetings.controls.append(ft.Text(f"Hello, {first_name.value} {last_name.value}!"))
        first_name.value = ""
        last_name.value = ""
        page.update()
        first_name.focus()

    page.add(
        first_name,
        last_name,
        ft.ElevatedButton("Say Hello", on_click=btn_click),
        greetings,
    )


ft.app(target=main)
