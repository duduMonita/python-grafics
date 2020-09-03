import math
import os
import colorsys

os.system("cls")

def rgb_to_hsv(r,g,b):
    r, g, b = r/255.0, g/255.0, b/255.0
    mx = max(r, g, b)
    mn = min(r, g, b)
    df = mx-mn
    if mx == mn:
        h = 0
    elif mx == r:
        h = (60 * ((g-b)/df) + 360) % 360
    elif mx == g:
        h = (60 * ((b-r)/df) + 120) % 360
    elif mx == b:
        h = (60 * ((r-g)/df) + 240) % 360
    if mx == 0:
        s = 0
    else:
        s = (df/mx)*100
    v = mx*100
    return h, s, v

def hsv_to_rgb(h,s,v):
    
    c = v * s
    if(c < 0):
        c = 0
    
    h = ((h / 6.0) / 2)
    x = (c * h)
    if(x < 0):
        x = 0
    
    m = (v - c)
    if(m < 0):
        m = 0
    
    if (0 <= h < 60):
        r, g, b = (0, x, 0)
    elif (60 <= h < 120):
        r, g, b = (x, c, 0)
    elif (120 <= h < 180):
        r, g, b = (0, c, x)
    elif (180 <= h < 240):
        r, g, b = (0, x, c)
    elif (240 <= h < 300):
        r, g, b = (x, 0, c)
    elif (300 <= h < 361):
        r, g, b = (c, 0, x)
      
    r, g, b = (((r + m)/100) * 255, ((g + m)/100) * 255, ((b + m)/100) * 255)
    
    while (r >= 256):
        r -= 1
    while (g >= 256):
        g -= 1
    while (b >= 256):
        b -= 1
        
    return r,g,b
        
def rgb_to_cmyk(r,g,b):
    if (r == 0) and (g == 0) and (b == 0):
        return 0, 0, 0, 100

    c = 1 - r / 255
    m = 1 - g / 255
    y = 1 - b / 255
    min_cmy = min(c, m, y)
    c = (c - min_cmy) * 100
    m = (m - min_cmy) * 100
    y = (y - min_cmy) * 100
    k = min_cmy * 100
    return c, m, y, k

def cmyk_to_rgb(c,m,y,k):
    r = 255*(1.0-(c+k)/100)
    g = 255*(1.0-(m+k)/100)
    b = 255*(1.0-(y+k)/100)
    return r,g,b

rgb_hsv = cmyk_to_rgb(100,0,100,0)
hsv_rgb = hsv_to_rgb(120,100,100)

print("**************************************")
print("Convertendo RGB para CMYK e HSV")
print(f"O  RGB  = 0,255,0")
print(f"Em CMYK = {rgb_to_cmyk(0,255,0)}")
print(f"Em HSV  = {rgb_to_hsv(0,255,0)}")
print("**************************************")
print("Convertendo CMYK para RGB e HSV")
print(f"O  CMYK = 100,0,100,0")
print(f"Em RGB  = {cmyk_to_rgb(100,0,100,0)}")
print(f"Em HSV  = {rgb_to_hsv(rgb_hsv[0],rgb_hsv[1],rgb_hsv[2])}")
print("**************************************")
print("Convertendo HSV para RGB e CMYK")
print(f"O  HSV  = 120,100,100")
print(hsv_to_rgb(120.0,100.0,100.0))
print(f"Em RGB  = {hsv_to_rgb(120.0,100.0,100.0)}")
print(f"Em CMYK = {rgb_to_cmyk(hsv_rgb[0],hsv_rgb[1],hsv_rgb[2])}")
print("**************************************")