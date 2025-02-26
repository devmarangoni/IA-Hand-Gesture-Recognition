import cv2
import mediapipe as mp

mpHands = mp.solutions.hands
mpDraw = mp.solutions.drawing_utils
hands = mpHands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5)

cap = cv2.VideoCapture(0)

gestureMap = {
    (0, 1, 0, 0, 0): "Apontando",
    (1, 1, 1, 1, 1): "Mao aberta",
    (0, 0, 1, 0, 0): "Dedo do meio",
    (0, 1, 1, 0, 0): "Simbolo da paz",
    (1, 0, 0, 0, 0): "Joinha",
    (0, 0, 0, 0, 0): "Punho fechado",
    (1, 1, 0, 0, 1): "Coracao",
    (1, 1, 1, 1, 0): "Quatro dedos",
    (1, 1, 0, 0, 0): "Chifre do rock",
    (1, 1, 1, 0, 0): "Tres dedos",
    (1, 0, 0, 0, 1): "Joia lado",
    (1, 0, 0, 0, 0): "Polegar para cima",
    (1, 0, 0, 0, 0): "Polegar para baixo",
    (1, 1, 1, 0, 1): "OK",
    (1, 1, 0, 0, 0): "L",
    (1, 1, 0, 0, 1): "Coracao com os dedos",
    (1, 0, 0, 0, 0): "Sinal de pergunta"
}

recognizedGestures = set()

def detectGesture(fingerStates):
    return gestureMap.get(tuple(fingerStates), "Desconhecido")

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    
    frame = cv2.flip(frame, 1)
    rgbFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgbFrame)
    
    gesture = ""
    totalDetectedFingers = 0
    
    if results.multi_hand_landmarks:
        handLandmarks = results.multi_hand_landmarks[0]
        mpDraw.draw_landmarks(frame, handLandmarks, mpHands.HAND_CONNECTIONS)
        
        fingerTips = [4, 8, 12, 16, 20]
        fingerStates = []
        
        if handLandmarks.landmark[4].x < handLandmarks.landmark[3].x:
            fingerStates.append(1)
        else:
            fingerStates.append(0)
        
        for tip in fingerTips[1:]:
            if handLandmarks.landmark[tip].y < handLandmarks.landmark[tip - 2].y:
                fingerStates.append(1)
            else:
                fingerStates.append(0)
        
        totalDetectedFingers = sum(fingerStates)
        gesture = detectGesture(fingerStates)
        
        if gesture != "Desconhecido":
            recognizedGestures.add(gesture)
    
    cv2.putText(frame, f"Dedos: {totalDetectedFingers}", (10, 30), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 0), 2)
    cv2.putText(frame, f"Gesto: {gesture}", (10, 60), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 0), 2)
    cv2.putText(frame, f"Gestos reconhecidos: {len(recognizedGestures)}/{len(gestureMap)}", (10, 90), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 0), 2)
    
    cv2.imshow('Reconhecimento de Gestos da Mao', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()