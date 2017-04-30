# ! /usr/bin/python3
import numpy as np
from threading import Thread
import cv2


class Recorder(Thread):
    """
    A class which capture vidéo
    @Djavan Sergent
    """

    def __init__(self, output):
        Thread.__init__(self)
        self.output = output
        self.end = False

    def run(self):
        cap = cv2.VideoCapture(0)

        # Define the codec and create VideoWriter object
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        out = cv2.VideoWriter(self.output, fourcc, 20.0, (640, 480))
        print("Staring record...")
        while (cap.isOpened()):
            ret, frame = cap.read()
            if ret:
                out.write(frame)

                # cv2.imshow('frame', frame)
                # if cv2.waitKey(25) & 0xFF == ord('q'):
                #     break
                if self.end:
                    break
            else:
                break
        # Release everything if job is finished
        cap.release()
        out.release()
        print("Record stoped")
        print("Record saved")
        cv2.destroyAllWindows()