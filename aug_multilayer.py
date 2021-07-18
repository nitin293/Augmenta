# Load Image 

import os
import sys
import augly.image as imaugs
import augly.utils as utils
from IPython.display import display
import random
import pilgram
import glob
import numpy as np
import cv2 as cv



# Scalling image 

def scaleIMG(image):
    # Get input image, scale it down to avoid taking up the whole screen
    input_img_path = image
    
    # We can use the AugLy scale augmentation
    input_img = imaugs.scale(input_img_path, factor=1)
    
    return input_img


# Overlay

def overlay(image, emojipath, fontfiles, use_ftr):
    fontfiles = random.choice(glob.glob(fontfiles + '*.ttf'))
    emojipath += random.choice(os.listdir(emojipath))
    
    aug_img = scaleIMG(image)

    ftr_lst = []
    total_ftr = 2
    for i in range(use_ftr):
        feature = random.randint(1, total_ftr)
        if feature not in ftr_lst:
            ftr_lst.append(feature)
    
    if 1 in ftr_lst:
        # applying text on the image
        try:
            aug_img = imaugs.overlay_text(aug_img, font_file=fontfiles, font_size=random.uniform(0.3, 0.9), x_pos=random.uniform(0.3, 0.7), y_pos=random.uniform(0.3, 0.7))
        except OSError:
            aug_img = imaugs.overlay_text(aug_img, font_file="./dataset/fonts/AlexBrush-Regular.ttf", font_size=random.uniform(0.3, 0.9), x_pos=random.uniform(0.3, 0.7), y_pos=random.uniform(0.3, 0.7))
            

    if 2 in ftr_lst:
        # applying emoji on the image
        aug_img = imaugs.overlay_emoji(image=aug_img, emoji_path=emojipath, emoji_size=random.uniform(0.3,0.9), x_pos=random.uniform(0.3,0.7), y_pos=random.uniform(0.3,0.7))
        
        
    return aug_img


# ColorTransform 

def colorTransform(image, use_ftr):
    image = scaleIMG(image)
    image = image.convert("RGB")
    aug_img = image
    
    ftr_lst = []
    total_ftr = 3
    for i in range(use_ftr):
        feature = random.randint(1, total_ftr)
        if feature not in ftr_lst:
            ftr_lst.append(feature)


    if 1 in ftr_lst:
    #     apply grayscale
        aug_img = imaugs.grayscale(image)

    
    if 2 in ftr_lst:
        # apply color jitter [includes -> brightness, contrast, saturation]
        aug_img = imaugs.color_jitter(image, brightness_factor=random.uniform(0.3, 0.9), contrast_factor=random.uniform(0.1, 0.9))

    if 3 in ftr_lst:
        # apply insta filter
        findex = random.randint(0, 25)

        if findex==0:
            aug_img = pilgram._1977(aug_img)
        elif findex==1:
            aug_img = pilgram.aden(aug_img)
        elif findex==2:
            aug_img = pilgram.brannan(aug_img)
        elif findex==3:
            aug_img = pilgram.brooklyn(aug_img)
        elif findex==4:
            aug_img = pilgram.clarendon(aug_img)
        elif findex==5:
            aug_img = pilgram.earlybird(aug_img)
        elif findex==6:
            aug_img = pilgram.gingham(aug_img)
        elif findex==7:
            aug_img = pilgram.hudson(aug_img)
        elif findex==8:
            aug_img = pilgram.inkwell(aug_img)
        elif findex==9:
            aug_img = pilgram.kelvin(aug_img)
        elif findex==10:
            aug_img = pilgram.lark(aug_img)
        elif findex==11:
            aug_img = pilgram.lofi(aug_img)
        elif findex==12:
            aug_img = pilgram.maven(aug_img)
        elif findex==13:
            aug_img = pilgram.mayfair(aug_img)
        elif findex==14:
            aug_img = pilgram.moon(aug_img)
        elif findex==15:
            aug_img = pilgram.nashville(aug_img)
        elif findex==16:
            aug_img = pilgram.perpetua(aug_img)
        elif findex==17:
            aug_img = pilgram.reyes(aug_img)
        elif findex==18:
            aug_img = pilgram.rise(aug_img)
        elif findex==19:
            aug_img = pilgram.slumber(aug_img)
        elif findex==20:
            aug_img = pilgram.stinson(aug_img)
        elif findex==21:
            aug_img = pilgram.toaster(aug_img)
        elif findex==22:
            aug_img = pilgram.valencia(aug_img)
        elif findex==23:
            aug_img = pilgram.walden(aug_img)
        elif findex==24:
            aug_img = pilgram.willow(aug_img)
        elif findex==25:
            aug_img = pilgram.xpro2(aug_img)

    return aug_img


# Pixel Transform

def pixelLevel_transform(inp_img, eff_num=3):
    
    #Randomly choosing 'eff_num' number of effects to apply
    eff_to_use = set()
    while len(eff_to_use) != eff_num:
        eff_to_use.add(random.randint(0,6))

    aug_img = inp_img
    
    for eff in eff_to_use:
    
        try:
            if eff == 0:
                
                #Pixel Shuffling
                aug_img = imaugs.shuffle_pixels(aug_img, factor=0.2)
                
            elif eff == 1:
                
                #Blur
                aug_img = imaugs.blur(aug_img, radius=random.randint(1, 2))

            elif eff == 2:
                
                #JPEG Encoding Quality
                aug_img = imaugs.encoding_quality(aug_img, quality=random.randint(40, 60))

            elif eff == 3:  
                
                #Cropping
                x1 = random.choice([0, 0.2, 0.3])
                y1 = random.choice([0, 0.2, 0.3])
                aug_img = imaugs.crop(aug_img, x1=x1, y1=y1, x2=random.uniform(0.75, 1),
                                      y2=random.uniform(0.75, 1))

            elif eff == 4:
                
                #Pixelization
                aug_img = imaugs.pixelization(aug_img, ratio=random.uniform(0.2, 0.3))

            elif eff == 5:
                
                #Edge Enhancing
                aug_img = imaugs.sharpen(aug_img, factor=random.randint(20, 28))

            elif eff == 6:
                    
                    #Color palette with dithering
                    aug_img = imaugs.convert_color(
                            aug_img,
                            mode = "P",
                            dither=None,
                            palette='ADAPTIVE',
                            colors=16
                        )
        except ValueError:
            
            continue
    
    return aug_img



# Spatial Transform 

def spatialTransform(image, imgpath, use_ftr):
    aug_img = scaleIMG(image)

    imgpath += random.choice(os.listdir(imgpath))        
    
    ftr_lst = []
    total_ftr = 7
    for i in range(use_ftr):
        feature = random.randint(1, total_ftr)
        if feature not in ftr_lst:
            ftr_lst.append(feature)
    
    
    if 1 in ftr_lst:
        # rotation
        aug_img = imaugs.rotate(aug_img, degrees=random.randint(0, 360))

    if 2 in ftr_lst:
        # horizontal flip
        aug_img = imaugs.hflip(aug_img)
    
    if 3 in ftr_lst:
        # padding
        aug_img = imaugs.pad_square(aug_img)
    
    if 4 in ftr_lst:
        # aspect ratio
        aug_img = imaugs.change_aspect_ratio(aug_img, ratio=1)

    
    if 5 in ftr_lst :
        # overlay onto background image
        aug_img = imaugs.overlay_image(aug_img, overlay=scaleIMG(imgpath), opacity=random.uniform(0.5, 0.7))
        
    if 6 in ftr_lst:
        # overlay onto background image
        aug_img = imaugs.overlay_image(scaleIMG(imgpath), overlay=aug_img, opacity=random.uniform(0.85, 1), overlay_size=0.5)
    
    if 7 in ftr_lst and 5 not in ftr_lst and 6 not in ftr_lst:
        # perspective
        aug_img = imaugs.perspective_transform(aug_img)
            
    
    return aug_img


# Embade Social

def embadeSocial(img):    
    aug_img = scaleIMG(img)
    aug_img = imaugs.overlay_onto_screenshot(aug_img)
    
    return aug_img



# Main function

def main(img, filt_name):
    
    fontfiles = './dataset/fonts/'
    emojipath = './dataset/emojis/'
    imgpath = './dataset/training/'
    
    
    if filt_name == "overlay":
        aug_img = overlay(image=img, emojipath=emojipath, fontfiles=fontfiles, use_ftr=random.randint(1, 2))    # out of 2 filters

    elif filt_name == "colortransform":
        aug_img = colorTransform(img, use_ftr=random.randint(1, 3))    # out of 3
    
    elif filt_name == "spatialtransform":
        aug_img = spatialTransform(img, imgpath, use_ftr=random.randint(1, 4))     # out of 7
        
    elif filt_name == "pixelleveltransform":
        aug_img = pixelLevel_transform(img, eff_num=random.randint(1, 3))      # out of 3
        
    elif filt_name == "embadesocial":
        aug_img = embadeSocial(img)
        
    return aug_img



# Save file 

def saveIMG(aug_img, filepath):
    aug_img = np.asarray(aug_img.convert('RGB'))
    aug_img = cv.resize(aug_img,(224,224))
    aug_img = cv.cvtColor(aug_img, cv.COLOR_BGR2RGB)

    cv.imwrite(filepath, aug_img)


# Driver Code

if __name__ == '__main__':
    
#     -------------- output environment setup --------------------

    outputpath = input("Enter output path [ eg : ./dataset/ ] : ")
    
    if "output" not in os.listdir(outputpath):
        outputpath += "/output/"
        os.mkdir(outputpath)
    else:
        outputpath += "/output/"
    
    if "multilayer" not in os.listdir(outputpath):
        outputpath = outputpath + "multilayer/"
        os.mkdir(outputpath)
    
    else:
        outputpath += "multilayer/"
        
    
#     ------------------------------------------------------------


    effect_classes = ["overlay", "colortransform", "pixelleveltransform", "spatialtransform", "embadesocial"]
    
#     ------------------------- automation -----------------------
    
    imgpath = input("Enter image path [ eg : ./dataset/training/ ] : ")
    imgpath += "/*.jpg"
    img_list = glob.glob(imgpath)
    

    for img in img_list:
        outimg = img.split('/')[-1]
        outfile = outputpath + outimg
            
        try:
            if sys.argv[1] in ['-v', '--verbose']:
                print("IN_IMG : " + img + ", OUT_IMG : " + outfile)
        except IndexError:
            pass

        num_of_layers = random.randint(1, len(effect_classes)-1)
        lst = []

        aug_img = img
        aug_img = scaleIMG(aug_img)

        count = 0

        for i in range(num_of_layers):
            
            effect = effect_classes[random.randint(0, len(effect_classes)-1)]
            while effect in lst:
                effect = effect_classes[random.randint(0, len(effect_classes)-1)]

            lst.append(effect)

            aug_img = main(aug_img, effect)
            saveIMG(aug_img, outfile)
