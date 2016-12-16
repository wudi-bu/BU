# AUTHOR DiWu wudi@bu.edu
# AUTHOR AnindyaPaul akpaul@bu.edu
# AUTHOR ShermanSze ysze@bu.edu
# AUTHOR JianqingGao gaojq@bu.edu
# AUTHOR JiangyuWang jiangyu@bu.edu

from skimage.io import imread
import numpy as np
import json

white = 0.97749019607843146


def remove_edge(img_array):
    img = img_array
    for _ in range(4):
        ind = np.where(img.flatten() != white)[0][0]
        img = img[int(ind/img.shape[1])::]
        img = np.rot90(img)
    return img


def identify_letter(img):
    dy = int(0.07*img.shape[0])
    dx = int(0.08*img.shape[1])
    mid_row = int(0.5*img.shape[0])
    mid_col = int(0.5*img.shape[1])

    if img[dy][dx] == white:
        if img[dy][-dx] != white:
            return 'j'
        elif img[-dy][dx] != white:
            if img[dy][mid_col] == white:
                if img[-dy][mid_col] != white:
                    return 'm'
            else:
                return 'a'
        elif img[mid_row][mid_col] != white:
            return 's'
        elif img[mid_row][-dx] == white:
            return 'c'
        elif img[-dy][mid_col] == white:
            return 'q'
        elif img[int(0.44*img.shape[0])][-dx] == white:
            return 'g'
        else:
            return 'o'
    else:
        if img[dy][-dx] != white:
            if img[-dy][dx] != white:
                if img[-dy][-dx] == white:
                    return 'f'
                elif img[-dy][mid_col] != white:
                    if img[int(0.3*img.shape[0])][-dx] == white:
                        if img[mid_row][dx] == white:
                            return 'z'
                        else:
                            return 'e'
                    else:
                        return 'i'
                elif img[mid_row][dx] == white:
                    return 'x'
                elif img[mid_row][-dx] == white:
                    return 'k'
                else:
                    if img[dy][int(0.19*img.shape[1])] != white:
                        return 'h'
                    else:
                        return 'n'
            elif img[-dy][-mid_col] == white:
                return 'w'
            elif img[dy][mid_col] != white:
                return 't'
            elif img[mid_row][dx] != white:
                return 'u'
            elif img[mid_row][mid_col] != white:
                return 'y'
            else:
                return 'v'
        else:
            if img[-dy][-dx] != white:
                if img[mid_row][mid_col] != white:
                    return 'r'
                else:
                    if img[dy][dx] != white:
                        return 'l'
            elif img[mid_row][mid_col] == white:
                return 'd'
            else:
                if img[-dy][mid_col] == white:
                    return 'p'
                else:
                    return 'b'


def wordlen(img):
    lengths = []
    diff1 = np.diff(np.where(img[1998] > 0.52))
    diff2 = np.diff(np.where(img[2140] > 0.52))
    diff3 = np.diff(np.where(img[2280] > 0.52))
    ones1 = np.where(diff1 == 1)
    ones2 = np.where(diff2 == 1)
    ones3 = np.where(diff3 == 1)
    diff1 = np.delete(diff1, ones1[1])
    diff2 = np.delete(diff2, ones2[1])
    diff3 = np.delete(diff3, ones3[1])
    count = 1
    for i in range(0, len(diff1), 2):
        if i + 1 < len(diff1):
            if diff1[i] - diff1[i+1] > 0:
                count += 1
            else:
                lengths.append(count)
                count = 1
    if count != 1:
        lengths.append(count)
    count = 1
    for j in range(0, len(diff2), 2):
        if j + 1 < len(diff2):
            if diff2[j] - diff2[j+1] > 0:
                count += 1
            else:
                lengths.append(count)
                count = 1
    if count != 1:
        lengths.append(count)
    count = 1
    for k in range(0, len(diff3), 2):
        if k + 1 < len(diff3):
            if diff3[k] - diff3[k+1] > 0:
                count += 1
            else:
                lengths.append(count)
                count = 1
    if count != 1:
        lengths.append(count)

    return lengths


def main():
    while True:
        file = input()
        img = imread(file, True)
        d = {}
        grid = []
        if img[1000][800] != white:
            x1 = 479
            x2 = 673
            n = 0
            for i in range(3):
                y1 = 666
                y2 = 893
                letters = ''
                for j in range(3):
                    letters += identify_letter(remove_edge(img[y1:y2, x1:x2]))
                    y1 += 461
                    y2 += 461
                grid.append(letters)
                x1 += 463
                x2 += 463
                n += 2
            d["grid"] = grid
            d["size"] = 3
            d["lengths"] = wordlen(img)
        elif img[885][670] != white:
            x1 = 425
            x2 = 600
            n = 0
            for i in range(4):
                y1 = 618
                y2 = 810
                letters = ''
                for j in range(4):
                    letters += identify_letter(remove_edge(img[y1:y2, x1:x2]))
                    y1 += 350
                    y2 += 350
                grid.append(letters)
                x1 += 339
                x2 += 339
                n += 3
            d["grid"] = grid
            d["size"] = 4
            d["lengths"] = wordlen(img)
        else:
            x1 = 408
            x2 = 530
            n = 0
            for i in range(5):
                y1 = 612
                y2 = 752
                letters = ''
                for j in range(5):
                    letters += identify_letter(remove_edge(img[y1:y2, x1:x2]))
                    y1 += 278
                    y2 += 278
                grid.append(letters)
                x1 += 277
                x2 += 277
                n += 4
            d["grid"] = grid
            d["size"] = 5
            d["lengths"] = wordlen(img)
        print(json.dumps(d))

if __name__ == "__main__":
    main()
