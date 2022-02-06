from pinout.core import Group, Image, Layout
from pinout.components.layout import Diagram_2Rows
from pinout.components.pinlabel import PinLabelGroup, PinLabel
from pinout.components.text import TextBlock
from pinout.components import leaderline as lline
from pinout.components.legend import Legend
from pinout.components.annotation import AnnotationLabel

import data


# diagram = Diagram_2Rows(1920, 940, 1200, "diagram")
# diagram.add_stylesheet("styles.css", embed=True)
# graphic = diagram.panel_01.add(Group(400, 42))

diagram = Diagram_2Rows(1910, 1100, 950, "diagram")
diagram.add_stylesheet("styles.css", embed=True)
graphic = diagram.panel_01.add(Group(400, 42))

hardware = graphic.add(Image("front.png", embed=True))
hardware2 = graphic.add(Image("back.png", x=900, y=0))

hardware.add_coord("LEFT", 0, 200)
hardware.add_coord("BOTTOM_LEFT", 110, 710)
hardware.add_coord("BOTTOM_RIGHT", 260, 710)

hardware.add_coord("RIGHT", 520, 200)

hardware.add_coord("pin_pitch_v", 0, 39)
hardware.add_coord("pin_pitch_h", 39, 0)

graphic.add(
    AnnotationLabel(
        content={"x": 102, "y": 55, "content": "RTC BATTERY"},
        x=1170,
        y=210,
        scale=(-1, 1),
        body={"width": 125},
    )
)

graphic.add(
    AnnotationLabel(
        content={"x": 102, "y": 55, "content": "SQW OUT"},
        x=1265,
        y=350,
        scale=(-1, 1),
        body={"width": 125},
    )
)

graphic.add(
    AnnotationLabel(
        content={"x": 102, "y": 55, "content": "USB-C"},
        x=250,
        y=60,
        scale=(1, -1),
        body={"width": 125},
    )
)

graphic.add(
    AnnotationLabel(
        content={"x": 102, "y": 55, "content": "RTC CLOCK"},
        x=220,
        y=200,
        scale=(-1, 1),
        body={"width": 125},
    )
)

graphic.add(
    AnnotationLabel(
        content={"x": 120, "y": 55, "content": "TEMP/HUM SENSOR"},
        x=460,
        y=660,
        scale=(-1, -1),
        body={"width": 175},
    )
)

graphic.add(
    PinLabelGroup(
        x=hardware.coord("RIGHT").x,
        y=hardware.coord("RIGHT").y,
        pin_pitch=hardware.coord("pin_pitch_v", raw=True),
        label_start=(60, 0),
        label_pitch=(0, 39),
        labels=data.right_header,
    )
)

graphic.add(
    PinLabelGroup(
        x=hardware.coord("LEFT").x,
        y=hardware.coord("LEFT").y,
        pin_pitch=hardware.coord("pin_pitch_v", raw=True),
        label_start=(70, 0),
        label_pitch=(0, 39),
        scale=(-1, 1),
        labels=data.left_header,
    )
)

graphic.add(
    PinLabelGroup(
        x=hardware.coord("BOTTOM_LEFT").x,
        y=hardware.coord("BOTTOM_LEFT").y,
        scale=(-1, 1),
        pin_pitch=hardware.coord("pin_pitch_h", raw=True),
        label_start=(170, 30),
        label_pitch=(0, 39),
        labels=data.bottom_left_header,
        leaderline=lline.Curved(direction="vh"),
    )
)


graphic.add(
    PinLabelGroup(
        x=hardware.coord("BOTTOM_RIGHT").x,
        y=hardware.coord("BOTTOM_RIGHT").y,
        scale=(1, 1),
        pin_pitch=hardware.coord("pin_pitch_h", raw=True),
        label_start=(320, 30),
        label_pitch=(0, 39),
        labels=data.bottom_right_header,
        leaderline=lline.Curved(direction="vh"),
    )
)



# Create a title and description text-blocks
title_block = diagram.panel_02.add(
    TextBlock(
        data.title,
        x=20,
        y=30,
        line_height=18,
        tag="panel title_block",
    )
)
diagram.panel_02.add(
    TextBlock(
        data.description,
        x=20,
        y=60,
        width=title_block.width,
        height=diagram.panel_02.height - title_block.height,
        line_height=18,
        tag="panel text_block",
    )
)

# Create a legend
legend = diagram.panel_02.add(
    Legend(
        data.legend,
        x=340,
        y=8,
        max_height=132,
    )
)


# py -m pinout.manager --export pinout_diagram.py diagram.svg