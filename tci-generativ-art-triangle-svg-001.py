#!/usr/bin/env python3
"""
TCI Art Generator 2
Triangle
"""
import random
import uuid
import cairosvg
import tci_svg

run_id = uuid.uuid1()
print(f'Processing run_id: {run_id}')

config = tci_svg.read_file('config.json')
forground = tci_svg.read_file('forground_colors.json')
background = tci_svg.read_file('background_colors.json')

# init
i = 0
j = 0
rectx = 0
recty = 0
out_filename = f'./output/{run_id}'

forground_palette, text_froground = tci_svg.get_palette(forground)
background_palette, text_background = tci_svg.get_palette(background)

f = open(f'{out_filename}.svg', "w")

# generate SVG File
data = tci_svg.header(config)
f.write(data) 

for i in range(config["fields_y"]):
    for j in range(config["fields_x"]):

        # Background rectangle 
        data = tci_svg.rect(rectx, recty, config["rectwidth"], config["rectheight"], background_palette)
        f.write(data) 
        
        ori =  random.randrange(8)
        
        if ori == 0:
            data = tci_svg.triangle1(rectx, recty, forground_palette)
            f.write(data)  
        elif ori == 1:
            data = tci_svg.triangle2(rectx, recty, forground_palette) 
            f.write(data) 
        elif ori == 2:
            data = tci_svg.triangle3(rectx, recty, forground_palette)
            f.write(data) 
        elif ori == 3:
            data = tci_svg.triangle4(rectx, recty, forground_palette)
            f.write(data) 
        elif ori == 4:
            data = tci_svg.triangle5(rectx, recty, forground_palette)
            f.write(data) 
        elif ori == 5:
            data = tci_svg.triangle6(rectx, recty, forground_palette)
            f.write(data) 
        elif ori == 6:
            data = tci_svg.triangle7(rectx, recty, forground_palette)
            f.write(data) 
        elif ori == 7:
            data = tci_svg.triangle8(rectx, recty, forground_palette)
            f.write(data) 
        else:
            print ("Ups")
       
        
        rectx += config["rectwidth"]

    rectx = 0
    recty += config["rectwidth"]
       
print ("Elements: ", i+1, j+1)
   
# Paletten 
if config["show_palette"] == "yes":
    data = tci_svg.show_palette_desciption( 
                                    config["fields_y"], 
                                    recty, config["rectwidth"], 
                                    config["rectheight"], 
                                    forground_palette, 
                                    background_palette, 
                                    text_froground, 
                                    text_background)
    f.write(data) 

data = tci_svg.footer()
f.write(data) 

f.close()

if config["make_png"] == "yes":
    cairosvg.svg2png(
        url=f'{out_filename}.svg', write_to=f'{out_filename}.png')

if config["make_pdf"] == "yes":
    cairosvg.svg2pdf(
        file_obj=open(f'{out_filename}.svg', "rb"), write_to=f'{out_filename}.pdf')

    