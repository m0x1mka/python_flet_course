import flet as ft


def main(page):
    def checkbox_changed(e):
        output_text.value = (
            f"Вы научились кататься на лыжах :  {todo_check.value}."
        )
        page.update()

    output_text = ft.Text()
    todo_check = ft.Checkbox(label="ToDo: Learn how to use ski", value=False, on_change=checkbox_changed)
    page.add(todo_check, output_text)


ft.app(target=main)
