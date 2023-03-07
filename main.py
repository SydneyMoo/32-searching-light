basic.show_icon(IconNames.HEART)

def on_forever():
    Tinybit.RGB_Car_Program().show_color(neopixel.colors(NeoPixelColors.BLACK))
    Tinybit.RGB_Car_Big(Tinybit.enColor.RED)
    Tinybit.RGB_Car_Big2(255, 0, 0)
basic.forever(on_forever)
