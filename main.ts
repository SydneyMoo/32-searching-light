basic.showIcon(IconNames.Heart)
basic.forever(function () {
    Tinybit.RGB_Car_Program().showColor(neopixel.colors(NeoPixelColors.Black))
    Tinybit.RGB_Car_Big(Tinybit.enColor.Red)
    Tinybit.RGB_Car_Big2(255, 0, 0)
})
