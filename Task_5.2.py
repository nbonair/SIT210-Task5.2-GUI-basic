from tkinter import *
from gpiozero import LED
import RPi.GPIO

RPi.GPIO.setmode(RPi.GPIO.BCM)

led_y = LED(18)
led_r = LED(15)
led_g = LED(14)
led_list = [led_y,led_r,led_g]
gui = Tk()
gui.title("LED control")
gui.geometry("500x200")


def OnButtonClick(button_id):
    if button_id == "y":
        led_selected = led_y
    elif button_id == "r":
        led_selected = led_r
    elif button_id == "g":
        led_selected = led_g
    for led in led_list:
        if led == led_selected:
            led.on()
        else:
            led.off()
def close():
    RPi.GPIO.cleanup()
    gui.destroy()

led_y_button = Button(gui,text = "Yellow", command =lambda:OnButtonClick("y"),bg = "bisque2",height=5,width = 10)
led_y_button.grid(row = 0, column = 1)

led_r_button = Button(gui,text = "Red", command =lambda: OnButtonClick("r"), bg = "bisque2",height=5,width = 10)
led_r_button.grid(row = 0,column =2)

led_g_button = Button(gui, text = "Green", command =lambda: OnButtonClick("g"), bg = "bisque2",height=5,width = 10)
led_g_button.grid(row = 0,column =3)


exit_button = Button()
gui.protocol("WM_DELETE_WINDOW",close)
gui.mainloop()
