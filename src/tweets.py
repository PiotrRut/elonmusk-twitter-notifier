import os
from imageai.Detection.Custom import CustomObjectDetection
import urllib
import time
from emailsender import send_mail


# Return path to a given file based on current directory
def get_current_path(filename: str):
    if "src" in os.getcwd():
        return os.path.join(os.path.dirname(os.getcwd()), filename)
    else:
        return os.path.join(os.getcwd(), filename)


# ImageAi
detector = CustomObjectDetection()
detector.setModelTypeAsYOLOv3()
detector.setModelPath(get_current_path("doge-ai.h5"))
detector.setJsonPath(get_current_path("detection_config.json"))
detector.loadModel()

# Keywords to detect
keywords = ["stock", "share", "$", "doge", "crypto", "bitcoin"]
ai_result = None


def tweet_engine(status):
    global ai_result

    if any(tweet in status.text.lower() for tweet in keywords) and status.user.id_str == "44196397":
        send_mail(f"Elon tweeted: {status.text} - on {time.ctime()}", False)
    # If no keywords match, check if there is an image
    elif hasattr(status, "extended_entities") and status.user.id_str == "44196397":
        # Loop through each image
        for media in status.extended_entities["media"]:
            """
            Download and write the tweet image.
            This will overwrite each new tested image to
            reduce the number of files stored.
            """
            urllib.request.urlretrieve(
                media["media_url_https"], "image-to-test.jpg"
            )
            # Run the image through ImageAI to detect objects in it
            detections = detector.detectObjectsFromImage(
                input_image=os.path.join(os.getcwd(), "image-to-test.jpg"),
                output_image_path=os.path.join(os.getcwd(), "image-tested.jpg"),
            )
            # If detection data matches any of the keywords send e-mail
            for detection in detections:
                if any(name in detection["name"] for name in keywords):
                    ai_result = True
        # At this point we know image passed AI validation
        if ai_result is True:
            send_mail(f'Picture tweeted - see attachment. Tweet: {status.text}', True)
            ai_result = False
