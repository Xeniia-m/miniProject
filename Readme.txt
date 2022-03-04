To run the project:
 - download all the photos from the drive - https://drive.google.com/drive/folders/1iKy-94ITHD8P9nNE8NL5jvh3JEcZQ76S
 - add all the photos to a "web/Tags_photos/photos"  folder
 - run the main.py file  (make sure that there is no masks.csv file in the project folder - that will be a result table) .

If you want to add a photo with a "mask, please" sign to the library:
1. Add the photo to a "web/Tags_photos/photos"  folder
2. Add photo description to the "masks_please.csv"

  How to write an "image" description:
	Currently,  availabale SVG objects are (you can see them in the "SVG" folder):
	
                woman_with_mask
                man_with_mask
                boy_with_mask
                girl_with_mask
                mask
                distance
                soap
                arrow
                two_way_arrow
                people
                covid
                heart
                hand_washing
                ruler
                temp_check
                rabbit
                no_hand_shake
                note
                gloves
                people_sitting
                man_walking
                cough
                calendar
                paper_with_pen
                hand
                2m
                gloves

	And availible colors are:
          black
          white
          yellow
          grey
          red
          brown
          green
          purple
          orange
          pink
          blue
          blond
skin:
          light
          medium
          dark
          

	For 
		woman_with_mask
                		man_with_mask
                		boy_with_mask
                		girl_with_mask

	the rules are : [name (skin color) (hair color) (mask color)]  or [name (mask color)]
	example:[ woman_with_mask light brown black]  or [woman_with_mask black]

	All other objects should be: [object color] (Example: [mask black])

  To add a new SVG object:

	1. Download black/white SVG object
	2. Edit it and save the main color code (the place that will change according to [object color] description)
	3. Open tha main.py file and add the [(svg file name) (color code)] to the originColors dictionary
	4. Use the name of the new SVG file for Image description

 To add a new color: 

	- Add the new color name and it's code to the colors dictionary in the main.py
