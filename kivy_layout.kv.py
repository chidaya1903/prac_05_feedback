#:kivy 2.0.0

BoxLayout:
    orientation: "vertical"
    padding: 10
    spacing: 10

    # Main content area (70%)
    BoxLayout:
        id: names_box
        orientation: "vertical"
        size_hint_y: 0.7

    # Status area (20%)
    Label:
        id: status_text
        text: "Status goes here"
        size_hint_y: 0.2

    # Bottom label (10%)
    Label:
        id: footer_label
        text: "I did this :)"
        size_hint_y: 0.1
