from cvzone.HandTrackingModule import HandDetector

class HandTracker:
    def __init__(self, max_hands=1, detection_confidence=0.75):
        self.detector = HandDetector(maxHands=max_hands, detectionCon=detection_confidence)

    def find_hand(self, img):
        """
        Returns lmList, fingers, img
        """
        hands, img = self.detector.findHands(img)
        if hands:
            hand = hands[0]
            lmList = hand["lmList"]
            fingers = self.detector.fingersUp(hand)
            return lmList, fingers, img
        return None, None, img
    
    def find_hands(self, img):
        hands, img = self.detector.findHands(img)
        if hands:
            results = []
            for hand in hands:
                lmList = hand["lmList"]
                fingers = self.detector.fingersUp(hand)
                results.append((lmList, fingers))
            return results, img
        return None, img