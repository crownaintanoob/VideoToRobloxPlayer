import cv2
import math
import time
# see code from this for inspiration: https://create.roblox.com/dashboard/creations/experiences/2975130578/overview
def GetPixelFromVideo(pathVideo, ResizeSizeX=80, ResizeSizeY=80):
    cap = cv2.VideoCapture(pathVideo)
    success, image = cap.read()
    frame_resized = cv2.resize(image, (ResizeSizeX, ResizeSizeY))
    frame_resized = cv2.cvtColor(frame_resized, cv2.COLOR_BGR2RGB) # Fix blue colors
    # flip the image vertically
    frame_resized = cv2.flip(frame_resized, 0)
    count = 0
    ListOfPixelsForFrames = []
    while success:
        ListOfPixelsForFrames.insert(count, [])
        countTemp = 0
        for x in range(1, ResizeSizeX):
            for y in range(1, ResizeSizeY):
                v = frame_resized[y, x] # y, x
                ListOfPixelsForFrames[count].insert(
                    countTemp,
                    {
                        "X": str(x),
                        "Y": str(y),
                        "R": str(v[0]),
                        "G": str(v[1]),
                        "B": str(v[2]),
                    },
                )
                countTemp += 1
        success, image = cap.read()
        if not success:
            break
        frame_resized = cv2.resize(image, (ResizeSizeX, ResizeSizeY))
        frame_resized = cv2.cvtColor(frame_resized, cv2.COLOR_BGR2RGB) # Fix blue colors
        # flip the image vertically
        frame_resized = cv2.flip(frame_resized, 0)
        count += 1
    cap.release()
    cv2.destroyAllWindows()
    return ListOfPixelsForFrames
