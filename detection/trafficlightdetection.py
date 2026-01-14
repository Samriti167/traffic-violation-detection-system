import cv2

cap = cv2.VideoCapture(r'C:\Users\SAMRITI\Desktop\TrafficViolationSystem\data\trafficvideo\traffic_light (1080p).mp4')

lower_red1 = (0, 150, 120)
upper_red1 = (10, 255, 255)

lower_red2 = (170, 150, 120)
upper_red2 = (180, 255, 255)

lower_yellow = (18, 120, 120)
upper_yellow = (32, 255, 255)

lower_green = (45, 80, 80)
upper_green = (80, 255, 255)

while cap.isOpened():
    ret, img = cap.read()
    if not ret:
        break
    x=900
    y=50
    w=600
    h=1400

    roi = img[y:y+h, x:x+w]
    hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)

    red_roi = hsv[40:200, 200:400]
    yellow_roi = hsv[300:450, 200:400]
    green_roi = hsv[550:750, 200:400]

    red_mask1= cv2.inRange(red_roi, lower_red1, upper_red1)
    red_mask2 = cv2.inRange(red_roi, lower_red2, upper_red2)
    red_mask = red_mask1 + red_mask2
    yellow_mask = cv2.inRange(yellow_roi, lower_yellow, upper_yellow)
    green_mask = cv2.inRange(green_roi, lower_green, upper_green)

    red_pixel = cv2.countNonZero(red_mask)
    yellow_pixel = cv2.countNonZero(yellow_mask)
    green_pixel = cv2.countNonZero(green_mask)

    signal = "UNKNOWN"

    if red_pixel > 150:
        signal = "RED"

    elif yellow_pixel > 9:
        signal = "YELLOW"

    elif green_pixel > 150:
        signal = "GREEN"


    print(f"R:{red_pixel} Y:{yellow_pixel} G:{green_pixel}")


    cv2.putText(
    roi,
    f"SIGNAL: {signal}",
    (20, 50),
    cv2.FONT_HERSHEY_SIMPLEX,
    1.2,
    (0, 255, 0),
    3
    )

    cv2.imshow("traffic detection", roi)

    if cv2.waitKey(10)& 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
