from imutils import paths
import imutils
import os
import cv2

imagepath= list(paths.list_files('/Users/samuelsonawane/Desktop/SB_Code/chapter21-breaking_captchas/downloads/'))

counts={}

for (i, path) in enumerate(imagepath):
    print(path)
    try:
        image = cv2.imread(path)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        gray = cv2.copyMakeBorder(gray, 8,8,8,8, cv2.BORDER_REPLICATE)
        thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
        cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cnts = cnts[0] if imutils.is_cv2() else cnts[1]
        cnts = sorted(cnts, key=cv2.contourArea, reverse= True) [:4]

        for c in cnts:
            (x, y, w, h) = cv2.boundingRect(c)
            roi= gray[y - 5:y + h +5, x-5:x + w + 5]
            cv2.imshow("ROI", imutils.resize(roi, width=28))
            key = cv2.waitKey(0)

            if key== ord("'"):
                print("Ignoring character")
                continue
            key = chr(key).upper()
            
            dirpath = os.path.sep.join(["dataset", key])
            

            if not os.path.exists(dirpath):
                os.mkdir(dirpath)

            count = counts.get(key, 1)
            p = os.path.sep.join([dirpath, "{}.png".format(str(count).zfill(6))])
            cv2.imwrite(p, roi)

            counts[key]= count + 1

    except KeyboardInterrupt:
        print("Manually Leaving script")
    except IOError as e:
        print(e)
    except:
        print("Skipping Image")
        