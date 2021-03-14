import mss
import mss.tools


with mss.mss() as sct:
    # Use the 1st monitor
    monitor = sct.monitors[1]

    # Grab the picture
    im = sct.grab(monitor)

    # Get the entire PNG raw bytes
    raw_bytes = mss.tools.to_png(im.rgb, im.size)