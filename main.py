import pandas as pd
import os.path

originColors = {"woman_with_mask": "#ffffff #1a1a1a #f2f2f2",
                "man_with_mask": "#ffffff #1a1a1a #e6e6e6",
                "boy_with_mask": "#ffffff #1a1a1a #ececec",
                "girl_with_mask": "#ffffff #1a1a1a #f9f9f9",
                "mask": "#1a1a1a",
                "distance": "#000000",
                "soap": "#1a1a1a",
                "arrow": "#000000",
                "two_way_arrow": "#000000",
                "people": "#000000",
                "covid": "#000000",
                "heart": "#000000",
                "hand_washing": "#000000",
                "ruler": "#ffffff",
                "temp_check": "#000000",
                "rabbit": "#ffffff",
                "no_hand_shake": "#000000",
                "note": "#000000",
                "people_sitting": "#000000",
                "man_walking": "#000000",
                "cough": "#000000",
                "calendar": "#1a1a1a",
                "paper_with_pen": "#f9f9f9",
                "hand": "#ffffff",
                "2m": "#000000",
                "gloves": "#ffffff"
                }
people_with_mask = {"man_with_mask", "woman_with_mask", "boy_with_mask", "girl_with_mask"}

colors = {"black": "#000000",
          "white": "#f2f2f2",
          "yellow": "#F2D41C",
          "grey": "#8C8C8C",
          "red": "#F70B0B",
          "brown": "#420606",
          "green": "#429014",
          "purple": "#901488",
          "orange": "#E26721",
          "pink": "#F7286D",
          "blue": "#0096FF",
          "light": "#EFD6BD",
          "medium": "#BD9B7D",
          "dark": "#675342",
          "blond": "#D5D491"

          }


def getSkinColor(obj):
    return originColors.get(obj).split()[0]


def getMaskColor(obj):
    return originColors.get(obj).split()[2]


def getHairColor(obj):
    return originColors.get(obj).split()[1]

def createPhotosPage():
    files = os.listdir("web/Tags_photos/photos")
    page = ""
    for file in files:
        #tags_page = createTags(file)
        svg = "<div class =\"gallery\" > <a   href = \"Tags_photos/photos/"+file+"\">   <img  src = \"Tags_photos/photos/" + file + \
              "\" alt = \"Image Not Found\"    width = \"100\"   height = \"100\" > </a> </div> "
        page = page + svg

    fin = open("web/templates/res.txt", "rt")
    data = fin.read()
    data = data.replace("place for svg", page)

    fin.close()
    result = open("web/photos.html", "wt")
    result.write(data)
    result.close()


def createTags(file):
    tbl = pd.read_csv("masks.csv", encoding="utf_8_sig")

    count = 0
    page = ""
    for line in tbl["SVG tags"]:
        if str(line) == "nan":
            count= count+1
            continue
        files = line.split("|")
        for svg_tag in files:
            if ''.join(svg_tag.split()) == file:
                image = tbl["identifier"][count]
                page = page + "<div class =\"gallery\" > <a  target = \"_blank\"   href = \"photos/"+image+"\">   <img  src = \"photos/"+image + \
        "\" alt = \"Image Not Found\"    width = \"100\"   height = \"100\" > </a> </div> "
        count = count+1
    fin = open("web/templates/res.txt", "rt")
    data = fin.read()
    data = data.replace("place for svg", page)

    fin.close()
    result = open("web/Tags_photos/Tags_photo_"+file.split('.')[0]+".html", "wt")
    result.write(data);
    result.close()
    return "Tags_photo_"+file.split('.')[0]+".html"

def createResultPage():

    files = os.listdir("web/Collection")
    page = ""
    for file in files:
        tags_page = createTags(file)
        svg = "<div class =\"gallery\" > <a   href = \"Tags_photos/"+tags_page+"\">   <img  src = \"Collection/"+file + \
        "\" alt = \"Image Not Found\"    width = \"100\"   height = \"100\" > </a> </div> "
        page = page + svg

    fin = open("web/templates/res.txt","rt")
    data = fin.read()
    data = data.replace("place for svg",page)

    fin.close()
    result = open("web/Result.html", "wt")
    result.write(data)
    result.close()


def changeColorSvg(objColor):
    # to prevent spaces
    objColor = ' '.join(objColor.split())
    file = '_'.join(objColor.split())
    if os.path.isfile("web/Collection/" + file + ".svg"):
        return file+".svg"
    # read input file
    words = objColor.split()
    obj = words[0]
    if obj == "":
        return
    svgfile = obj + ".svg"
    fin = open("SVG/" + svgfile, "rt")
    data = fin.read()
    fin.close()
    if len(words) > 1 and obj in people_with_mask:
        colorMask = getMaskColor(obj)
        if len(words) == 2:
            newMask = words[1]
        else:
            newMask = words[3]
        data = data.replace(colorMask, colors.get(newMask))
        if len(words) > 2 :
            colorSkin = getSkinColor(obj)
            colorHair = getHairColor(obj)
            data = data.replace(colorSkin,colors.get(words[1]))
            data = data.replace(colorHair,  colors.get(words[2]))
    else:
        if len(words)>1:
            data = data.replace(originColors.get(obj), colors.get(words[1]))
    fin = open("web/Collection/" + file + ".svg", "wt")
    fin.write(data)
    fin.close()
    return file + ".svg"


tbl = pd.read_csv("mask_please.csv", encoding="utf_8_sig")
tbl["SVG tags"] = ""
count = 0
for line in tbl["image"]:
    if str(line)=="nan":
        count=count+1
        continue

    objects = line.split("|")
    tags = []
    if objects[0] != " ":
        for objectColor in objects:
            svg_file = changeColorSvg(objectColor)
            if svg_file!="":
                tags.append(svg_file)
    if len(tags) > 0:
        tbl["SVG tags"][count] = ' | '.join(tags)
    count=count+1

tbl.to_csv("masks.csv", encoding="utf_8_sig", index=False)
createResultPage()
createPhotosPage()