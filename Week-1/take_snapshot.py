from robodk import robolink

# Connect to RoboDK (RoboDK must be open)
RDK = robolink.Robolink()

# Get the camera by name
cam = RDK.Item('Camera 1')

if not cam.Valid():
    raise Exception("Camera 1 not found")

# Open camera window
cam.setParam('Open', 1)

# Build correct file path (IMPORTANT)
station_path = RDK.getParam('PATH_OPENSTATION')
file = station_path + "/images/robodk_snapshot.png"

# Take snapshot
RDK.Cam2D_Snapshot(file, cam)

print("Snapshot saved at:", file)
