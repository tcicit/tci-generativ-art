"""
Modul for TCI Generativ Art Generator 2
"""
import random
import numpy as np
import json


def read_file(file_name):
    with open(file_name, 'r') as file:
        data = json.load(file)
    file.close()
    return(data)

def get_palette(colors):
    palette = random.choice(list(colors))
    data =  colors[palette]
    text = palette

    return data, text



def header(config):
    rectwidth = config["rectwidth"]
    fields_x = config["fields_x"]
    fields_y = config["fields_y"]
    titel = config["titel"]
    describtion = config["describtion"]
    if config["show_palette"] == "yes":
        h = rectwidth*fields_y + 500
        w = rectwidth*fields_y + 500
    else:
        h = rectwidth*fields_y
        w = rectwidth*fields_y

    data = f"""<svg xmlns="http://www.w3.org/2000/svg"
            xmlns:xlink="http://www.w3.org/1999/xlink"
            version="1.1" 
            baseProfile="full"
            width="{rectwidth*fields_x}" height="{h}"
            viewBox="0 0 {rectwidth*fields_x} {w}">
            <title>{titel}</title>
            <desc>{describtion}</desc>\n"""
   
    return(data)
    
def footer():
    data = "</svg>"
    return(data)

def rect(rectx, recty, rectwidth, rectheight, color_palette):
    
    if type(color_palette) == list:
        fill = (random.choice(color_palette))
    else:
        fill = color_palette
        
    data = f'<rect x="{rectx}" y="{recty}" width="{rectwidth}" height="{rectheight}" fill="{fill}" />\n'
    return(data) 

def circle(circle_r, rectx, recty, rectwidth, rectheight, forground_palette):
    cx = rectx + rectwidth / 2 
    cy = recty + rectheight / 2
    fill=(random.choice(forground_palette))

    data = f'<circle cx="{cx}" cy="{cy}" r="{circle_r}" fill="{fill}"/>\n'
    return(data) 

def write_svgarc(forground_palette, xcenter,ycenter,r,startangle,endangle):
    
    fill=(random.choice(forground_palette))

    if startangle > endangle: 
        raise ValueError("startangle must be smaller than endangle")
    
    if endangle - startangle < 360:
        large_arc_flag = 0
        radiansconversion = np.pi/180.
        xstartpoint = xcenter + r*np.cos(startangle*radiansconversion)
        ystartpoint = ycenter - r*np.sin(startangle*radiansconversion)
        xendpoint = xcenter + r*np.cos(endangle*radiansconversion)
        yendpoint = ycenter - r*np.sin(endangle*radiansconversion)
         
        #If we want to plot angles larger than 180 degrees we need this
        if endangle - startangle > 180: 
            large_arc_flag = 1
          
        p = f'<path d="M {xstartpoint} {ystartpoint} A {r} {r} 0 {large_arc_flag} 0 {xendpoint} {yendpoint} L {xcenter} {ycenter} Z"/>'
        data = f'<g stroke="none" fill="{fill}" >' + p + '</g>\n'
            
    else:
        data= f'<circle cx="{xcenter}" cy="{ycenter}" r="{r}" fill="{fill}"/>\n'
       
    return(data) 
  
def print_titel(texty, text_title, text_palette):
    data = f'<text x="0" y="{texty}" style="font: bold 30px sans-serif;">{text_title} ({text_palette})</text>'
    return(data)   

def print_palette(recty, rectwidth, rectheight, color_palette, rectx):    

    for i in range(len(color_palette)):
        if i == 0:
            data = f'<rect x="{rectx}" y="{recty}" width="{rectwidth}" height="{rectheight}" fill="{color_palette[i]}"/>'
        else:
            data += f'<rect x="{rectx}" y="{recty}" width="{rectwidth}" height="{rectheight}" fill="{color_palette[i]}"/>'

        data += f'<text x="{rectx+ 20}" y="{recty+120}" style="font: 12px sans-serif;">{color_palette[i]}</text>\n'
    
        rectx += rectwidth

    return(data)
        
def show_palette_desciption(fields_y, recty, rectwidth, rectheight, forground_palette, background_palette, text_froground, text_background):
    text_title = "Forground Palette"
    texty = rectheight * fields_y + 120
    data = print_titel(texty, text_title, text_froground)
    data += "\n"

    recty = rectheight * fields_y + 150
    data += print_palette(recty, rectwidth, rectheight, forground_palette, rectx=0) 
    data += "\n"

    text_title = "Background Palette"
    texty = rectheight * fields_y + 320
    data += print_titel(texty, text_title, text_background)
    data += "\n"

    recty = rectheight * fields_y + 350
    data += print_palette(recty, rectwidth, rectheight, background_palette, rectx=0) 

    return(data)
        
        
"""        
Aufteilung des Rechteckes für Dreieck (polygon)
  
  0,0   | 50,0   | 100,0
  ------|--------|--------
  0,50  | 50,50  | 100,50
  ------|--------|--------
  0,100 | 50,100 | 100,100 
"""        
        
def triangle1(rectx, recty, color_palette):
    fill = (random.choice(color_palette)) 
    data = f'<polygon points="0,0 100,0 0,100" fill="{fill}" transform="translate({rectx},{recty})" />'
    return(data) 
        
def triangle2(rectx, recty, color_palette):
    fill = (random.choice(color_palette)) 
    data = f'<polygon points="100,0 100,100 0,100" fill="{fill}" transform="translate({rectx},{recty})" />'
    return(data) 

def triangle3(rectx, recty, color_palette):
    fill = (random.choice(color_palette)) 
    data = f'<polygon points="0,0 100,0 100,100" fill="{fill}" transform="translate({rectx},{recty})" />'
    return(data) 

def triangle4(rectx, recty, color_palette):
    fill = (random.choice(color_palette)) 
    data = f'<polygon points="0,0 100,100 0,100" fill="{fill}" transform="translate({rectx},{recty})" />'
    return(data) 

def triangle5(rectx, recty, color_palette):
    fill = (random.choice(color_palette)) 
    data = f'<polygon points="0,0 100,50 0,100" fill="{fill}" transform="translate({rectx},{recty})" />'
    return(data) 

def triangle6(rectx, recty, color_palette):
    fill = (random.choice(color_palette)) 
    data = f'<polygon points="0,50 100,0 100,100" fill="{fill}" transform="translate({rectx},{recty})" />'
    return(data) 

def triangle7(rectx, recty, color_palette):
    fill = (random.choice(color_palette)) 
    data = f'<polygon points="0,100 50,0 100,100" fill="{fill}" transform="translate({rectx},{recty})" />'
    return(data) 

def triangle8(rectx, recty, color_palette):
    fill = (random.choice(color_palette)) 
    data = f'<polygon points="0,0 50,100 100,0" fill="{fill}" transform="translate({rectx},{recty})" />'
    return(data) 
