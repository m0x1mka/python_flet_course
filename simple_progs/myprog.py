import flet as ft


def main(page: ft.Page):
    just_num = ""
    page.title = "calculator"
    number = ft.TextField(value="0", text_align="right", width=500)

    def add_one(e):
        if number.value != "0":
            number.value += "1"
        else:
            number.value = "1"
        page.update()

    one = ft.ElevatedButton(text="1", on_click=add_one, width=100, height=100)

    def add_two(e):
        if number.value != "0":
            number.value += "2"
        else:
            number.value = "2"
        page.update()

    two = ft.ElevatedButton(text="2", on_click=add_two, width=100, height=100)

    def add_two(e):
        if number.value != "0":
            number.value += "3"
        else:
            number.value = "3"
        page.update()

    three = ft.ElevatedButton(text="3", on_click=add_two, width=100, height=100)

    def clean(e):
        global just_num
        just_num = ""
        number.value = "0"
        page.update()

    c_button = ft.ElevatedButton(text="C", on_click=clean, width=100, height=100)

    def add_four(e):
        if number.value != "0":
            number.value += "4"
        else:
            number.value = "4"
        page.update()

    four = ft.ElevatedButton(text="4", on_click=add_four, width=100, height=100)

    def add_five(e):
        if number.value != "0":
            number.value += "5"
        else:
            number.value = "5"
        page.update()

    five = ft.ElevatedButton(text="5", on_click=add_five, width=100, height=100)

    def add_six(e):
        if number.value != "0":
            number.value += "6"
        else:
            number.value = "6"
        page.update()

    six = ft.ElevatedButton(text="6", on_click=add_six, width=100, height=100)

    def add_seven(e):
        if number.value != "0":
            number.value += "7"
        else:
            number.value = "7"
        page.update()

    seven = ft.ElevatedButton(text="7", on_click=add_seven, width=100, height=100)

    def add_eight(e):
        if number.value != "0":
            number.value += "8"
        else:
            number.value = "8"
        page.update()

    eight = ft.ElevatedButton(text="8", on_click=add_eight, width=100, height=100)

    def add_nine(e):
        if number.value != "0":
            number.value += "9"
        else:
            number.value = "9"
        page.update()

    nine = ft.ElevatedButton(text="9", on_click=add_nine, width=100, height=100)

    def add_zero(e):
        if number.value != "0":
            number.value += "0"
        else:
            number.value = "0"
        page.update()

    zero = ft.ElevatedButton(text="0", on_click=add_zero, width=100, height=100)

    def plus_num(e):
        global just_num
        just_num = ""
        just_num = number.value + "+"
        number.value = "0"
        page.update()

    plus = ft.ElevatedButton(text="+", on_click=plus_num, width=100, height=100)

    def minus_num(e):
        global just_num
        just_num = ""
        just_num = number.value + "-"
        number.value = "0"
        page.update()

    minus = ft.ElevatedButton(text="-", on_click=minus_num, width=100, height=100)

    def mult_num(e):
        global just_num
        just_num = ""
        just_num = number.value + "*"
        number.value = "0"
        page.update()

    mult = ft.ElevatedButton(text="*", on_click=mult_num, width=100, height=100)

    def div_num(e):
        global just_num
        just_num = ""
        just_num = number.value + "/"
        number.value = "0"
        page.update()

    div = ft.ElevatedButton(text="/", on_click=div_num, width=100, height=100)

    def make_equality(e):
        global just_num
        just_num += number.value
        number.value = str(eval(just_num))
        page.update()

    equal = ft.ElevatedButton(text="=", on_click=make_equality, width=100, height=100)

    def delete_num(e):
        if len(number.value) > 1:
            if number.value[-2] != ".":
                number.value = number.value[:-1]
            else:
                number.value = number.value[:-2]
        else:
            number.value = "0"
        page.update()

    delete = ft.ElevatedButton(text="<", on_click=delete_num, width=100, height=100)

    def sqr_num(e):
        global just_num
        just_num = ""
        just_num = str(float(number.value) ** 2)
        number.value = ""
        page.update()

    square = ft.ElevatedButton(text="sqr", on_click=sqr_num, width=100, height=100)

    def root_num(e):
        global just_num
        just_num = ""
        just_num = str(float(number.value) ** 0.5)
        number.value = ""
        page.update()

    root = ft.ElevatedButton(text="root", on_click=root_num, width=100, height=100)

    def float_num(e):
        if type(number.value[-1]) == str:
            number.value += "."

    num_float = ft.ElevatedButton(text=".", on_click=float_num, width=100, height=100)

    page.add(number, ft.Row([one, two, three, c_button]))
    page.add(ft.Row([four, five, six, plus]))
    page.add(ft.Row([seven, eight, nine, equal]))
    page.add(ft.Row([minus, mult, div, zero]))
    page.add(ft.Row([delete, square, root, num_float]))


ft.app(target=main)
