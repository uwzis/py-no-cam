import re
import pystray
from pystray import *
import subprocess
from PIL import Image

def on_clicked(icon, item):
    # Execute lsusb command and capture output
    lsusb_output = subprocess.check_output(["lsusb"])

    # Convert the output from bytes to a string
    lsusb_output = lsusb_output.decode("utf-8")

    # Search for lines that contain "Camera" and extract the ID fields
    camera_ids = []
    for line in lsusb_output.splitlines():
        if re.search(r"Camera", line):
            match = re.search(r"ID (\S+)", line)
            if match:
                id_str = match.group(1)
                vendor_id = id_str[:4]
                product_id = id_str[5:]
                camera_ids.append((vendor_id, product_id))

    # Print the vendor and product IDs of the cameras found
    for vendor_id, product_id in camera_ids:
        print("Camera found with vendor ID", vendor_id, "and product ID", product_id)
        
        # Execute usb_modeswitch command for the camera
        cmd = ["sudo", "usb_modeswitch", "-v", vendor_id, "-p", product_id, "-d"]
        subprocess.run(cmd)

    # Print the camera IDs
    print("Camera IDs:", camera_ids)

# Create the tray icon
image = Image.open("icon.png")
menu = pystray.Menu(pystray.MenuItem("Click me", on_clicked))
icon = pystray.Icon("GLOWIE EJECT", image, "GLOWIE EJECT", menu)

# Run the tray application
icon.run()
