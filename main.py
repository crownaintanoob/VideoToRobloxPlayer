from flask import Flask, jsonify, make_response
from util import *
import gzip
import ujson as jsonU
app = Flask(__name__)
compression_level = 5
video_path = 'ye.mp4' # This must be changed to the video file you have within the same directory
pixelsData = GetPixelFromVideo(video_path, ResizeSizeX=80, ResizeSizeY=80)
imageIndexCurrent = 0 # Which image is the latest to have been sent to the client
@app.route("/getpixelsforimagechunk")
def GetPixelsForImageChunk():
    global imageIndexCurrent, pixelsData
    if imageIndexCurrent < len(pixelsData):
        chunkOfImagesPixelsData = []
        for indexChunk in range(0, 100): # change the 100 to make it faster, but don't make it too big, otherwise if it's higher than the amount of frames in the video, it will not work
            imageIndexCurrent += 1
            if len(pixelsData) > imageIndexCurrent: # this will cause a problem that will prevent all of the frames from showing, because the step for the frames loop is "100", so if there is like 34 left or so, it will not put them
                chunkOfImagesPixelsData.insert(indexChunk, pixelsData[imageIndexCurrent])
            else:
                return "FramesAllReturned"
        # Compress JSON
        content = gzip.compress(jsonU.dumps(chunkOfImagesPixelsData).encode("utf8"), compression_level)
        response = make_response(content)
        response.headers['Content-Length'] = len(content)
        response.headers['Content-Encoding'] = 'gzip'
        return response
    else:
        return "FramesAllReturned"

if __name__ == '__main__':
    app.run(host="localhost", port=4294, debug=True, threaded=True)
