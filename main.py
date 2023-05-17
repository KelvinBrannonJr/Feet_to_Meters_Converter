import PySimpleGUI as sg
from converters import convert

feet_label = sg.Text("Enter Feet:")
feet_input = sg.Input(key='feet')

inches_label = sg.Text("Enter Inches:")
inches_input = sg.Input(key='inches')

convert_btn = sg.Button("Convert", key='Convert')
result_output = sg.Text("", key='output')

exit_btn = sg.Button("Exit")

sg.theme('Black')

layout = [
            [feet_label, feet_input],
            [inches_label, inches_input],
            [convert_btn, exit_btn, result_output],
        ]

window = sg.Window(title="Feet To Meters Converter", layout=layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == "Exit":
        break
    if event == "Convert":
        try:
            feet = float(values['feet'])
            inches = float(values['inches'])
            result = convert(feet, inches)
            window['output'].update(value=f"{result} meters", text_color="white")
            window['feet'].Update(value="")
            window['inches'].Update(value="")

        except ValueError:
            sg.popup("Please provide two numbers.")

window.close()


