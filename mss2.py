import mss
import mss.tools
'''
https://python-mss.readthedocs.io/examples.html#part-of-the-screen
'''

with mss.mss() as sct:
    # The screen part to capture
    monitor = {"top": 160, "left": 160, "width": 160, "height": 135}
    output = "sct-{top}x{left}_{width}x{height}.png".format(**monitor)

    # Grab the data
    sct_img = sct.grab(monitor)

    # Save to the picture file
    mss.tools.to_png(sct_img.rgb, sct_img.size, output=output)
    print(output)