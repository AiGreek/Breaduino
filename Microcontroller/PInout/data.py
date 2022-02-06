legend = [
    ("Analog", "analog"),
    ("Communication", "comms"),
    ("Ground", "gnd"),
    ("GPIO", "gpio"),
    ("Power", "pwr"),
]

# Pinlabels

left_header = [
    [("D11", "gpio")],
    [("D3", "gpio"),("SCL", "comms")],
    [("D2", "gpio"),("SDA", "comms")],
    [("D1", "gpio"),("TxD", "comms")],
    [("D0", "gpio"),("RxD", "comms")],
    [("D4", "gpio"),("A6", "analog")],
    [("D12", "gpio"),("A10", "analog")],
    [("D6", "gpio"),("A7", "analog")],
    [("D8", "gpio")],
    [("D9", "gpio"),("A8", "analog")],
    [("D10", "gpio")]
]

bottom_left_header = [
    [("GND", "gnd")],
    [("GND", "gnd")],
    [("D5", "gpio")],
    [("D13", "gpio")]
]

bottom_right_header = [
    [("5V", "pwr")],
    [("5V", "pwr")],
    [("3V3", "pwr")],
    [("3V3", "pwr")]
]

right_header = [
    [("D17", "gpio"),("MISO", "comms")],
    [("D16", "gpio"),("MOSI", "comms")],
    [("D15", "gpio"),("SCK", "comms")],
    [("D14", "gpio"),("SS", "comms")],
    [("D7", "gpio")],
    [("A5", "analog")],
    [("A4", "analog")],
    [("A3", "analog")],
    [("A2", "analog")],
    [("A1", "analog")],
    [("A0", "analog")]
]


title = "<tspan class='h1'>Breaduino Pinout</tspan>"

description = """Small Arduino based on ATMega32u4 µC. 
It consists of a temperature sensor (AHT10), 
an RTC clock (DS1307) and an IR led"""
