# Let's identify coins!
# in the image given below we want to detect each coin currency,
# and we'll do it with cv2.HoughCircles!


import cv2
from matplotlib import pyplot as plt

figsize = (10, 10)

im3 = cv2.imread("coins.png")
im3 = cv2.cvtColor(im3, cv2.COLOR_BGR2RGB)
im = cv2.cvtColor(im3, cv2.COLOR_RGB2GRAY)
res = im3.copy()

# TODO: fill in the best values possible
# to detect the right circle dimeter and place
acc_ratio = 0.5
min_dist = 60
canny_upper_th = 60
acc_th = 45
minR = 40
maxR = 74
circles = cv2.HoughCircles(
    im,
    cv2.HOUGH_GRADIENT,
    acc_ratio,
    min_dist,
    param1=canny_upper_th,
    param2=acc_th,
    minRadius=minR,
    maxRadius=maxR,
)

print("Circles detected:")
print(circles)

# === font vars
font = cv2.FONT_HERSHEY_SIMPLEX
bottomLeftCornerOfText = (10, 500)
fontScale = 0.8
fontColor = (255, 220, 0)
lineType = 2

def classify_coin(r):
    if 40 <= r <= 53:
        return "Dime"
    elif 53.5 <= r <= 54:
        return "Penny"
    elif 55 <= r <= 60:
        return "Nickel"
    elif 61 <= r <= 74:
        return "Quarter"

# ==== for each detected circle
for xyr in circles[0, :]:

    x = int(xyr[0])
    y = int(xyr[1])
    r = int(xyr[2])

    # draw the outer circle
    res = cv2.circle(res, (x, y), r, (0, 255, 0), 3)

    # TODO: write currency type on each coin.
    # write currency type
    coin_text = classify_coin(r)
    res = cv2.putText(
        res,
        coin_text,
        (x - r, y - r),
        font,
        fontScale,
        fontColor,
        lineType,
    )
    # use cv2.putText() and the font vars above.
    # If you need, different coin sizes can be found here:
    # https://avocadoughtoast.com/weights-sizes-us-coins/


plt.figure(figsize=figsize)
plt.imshow(res)
plt.title(
    f"final result - coins detection\n"
    f"dp={acc_ratio}, minDist={min_dist}, p1={canny_upper_th}, p2={acc_th}, "
    f"minR={minR}, maxR={maxR}"
)
plt.show()
