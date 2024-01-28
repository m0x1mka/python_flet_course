import flet as ft


def main(page: ft.Page):
    txt = ft.TextField(label="Enter your name please")
    page.add(txt)
    print(txt.value)
    txt_name = ft.Text(value=txt.value, color="green")
    page.controls.append(txt_name)
    page.update()


ft.app(target=main)
