import PySimpleGUI as sg
from converters import convert

feet_label = sg.Text("Enter Feet:")
feet_input = sg.Input(key='feet')

inches_label = sg.Text("Enter Inches:")
inches_input = sg.Input(key='inches')

convert_btn = sg.Button("Convert", key='Convert')
result_output = sg.Text("", key='output')

window = sg.Window(
            title="Feet To Meters Converter",
            layout=[
                [feet_label, feet_input],
                [inches_label, inches_input],
                [convert_btn, result_output]
            ],
)

while True:
    event, values = window.read()
    print(event, values)

    if event == "Convert":
        feet = float(values['feet'])
        inches = float(values['inches'])
        result = convert(feet, inches)
        window['output'].update(value=f"{result} meters", text_color="white")

    if event == sg.WIN_CLOSED:
        break

window.close()


