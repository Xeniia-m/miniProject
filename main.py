import pandas as pd
objects = {"woman": ["woman", "Woman", "אישה", "גברת", "בת", "ילדה"],
           "man": ["Man", "man", "בן אדם", "גבר", "בן"],
           "mask": ["Mask", "mask", "מסיכה"]}

colors = {"black": "#000000",
          "white": "#FFFFFF",
          "yellow": "#F2D41C",
          "red": "#F70B0B",
          "brown": "#420606",
          "green": "#429014",
          "purple": "#901488",
          "orange": "#E26721",
          "pink": "#F7286D"

          }

skinColors = {"light": "#EFD6BD",
              "dark": "#A58869",
              "black": "#6B3F34"
            }

originColors = {"mask": "",
                "woman": "#f4e3d7",
                "man": "#f4e3d7",
                "covid": "#ffffff",
                "distance": "",
                "soap": ""}

def changeColorSvg(obj,color):
    # read input file
    svgfile = obj+".svg"
    fin = open("woman.svg", "rt")

    # read file contents to string
    data = fin.read()

    data = data.replace('style="fill:#f4e3d7;', 'style="fill:'+color+';')

    # close the input file
    fin.close()

    # open the input file in write mode
    fin = open("data.svg", "wt")

    # overrite the input file with the resulting data
    fin.write(data)

    # close the file
    fin.close()

tbl = pd.read_csv("mask_please.csv", encoding="utf_8_sig")
tbl["SVG tags"] = ""
for line in tbl["image"]:
    objects = line.split("|")
    for objectColor in objects:
        obj = objectColor.split()[0]
        color = objectColor.split()[1]
        print(obj+" "+color)
       # if obj in objects['woman']:
        changeColorSvg(obj,skinColors['dark'])
        # TODO: create SVG of the obj with the color by putting the color into the file
        # TODO: put the name of the SVG into the column "SVG tags" - it can be more than one SVG image
        # TODO: tagged with the same photo
tbl.to_csv("masks.csv", encoding="utf_8_sig", index=False)


