# AUTHOR DiWu wudi@bu.edu
# AUTHOR AnindyaPaul akpaul@bu.edu
# AUTHOR ShermanSze ysze@bu.edu
# AUTHOR JianqingGao gaojq@bu.edu
# AUTHOR JiangyuWang jiangyu@bu.edu

import glob
from skimage.io import imread
import numpy as np
import operator
import hashlib


def edge_detection(img_array):
    img = img_array
    for _ in range(4):
        img = img[int(np.where(img.flatten() != 255)[0][0]/img.shape[1]/3)::]
        img = np.rot90(img)
    return img


def get_num(s):
    s = s.split(".")[0]
    for c in s:
        if c.isdigit():
            return int(s[s.find(c):])


def main():
    imageMods = dict()
    imageDict = dict()
    fileMap = dict()
    for file in glob.glob("*.png"):
        num = get_num(file)
        fileMap[num] = file
        imgArray = edge_detection(imread(file))
        key = imgArray.tostring()
        if key in imageMods:
            value = imageMods[key]
            files = imageDict[value]
            files.append(num)
            imageDict[value] = sorted(files)
        else:
            imageDict[key] = [num]
            imageMods[key] = key
            imagFlipArray = np.flipud(imgArray)
            imageMods[imagFlipArray.tostring()] = key
            count = 0
            for count in range(3):
                imgArray = np.rot90(imgArray)
                imageMods[imgArray.tostring()] = key
                imagFlipArray = np.rot90(imagFlipArray)
                imageMods[imagFlipArray.tostring()] = key
                count += 1

    f = open("answers.txt", "w")
    for k, v in sorted(imageDict.items(), key=operator.itemgetter(1)):
        newLine = True
        for item in v:
            if newLine:
                f.write("%s" % fileMap[item])
                newLine = False
            else:
                f.write(" %s" % fileMap[item])
        f.write("\n")
    f.close()

    print(hashlib.sha256(open('answers.txt', 'rb').read()).hexdigest())
if __name__ == "__main__":
    main()
