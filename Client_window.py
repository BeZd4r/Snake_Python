import Snake
from PIL import Image

win_size_x = 600
win_size_y = 600

item_size = win_size_x + win_size_y
head_size = item_size // 30
food_size = item_size // 35
score_font_size = int(win_size_x*0.05)
tail_size = item_size // head_size // 1.1
body_offset = tail_size

def Add_im_for_sprite(names):
    for name in names:

        bef_im = rf"im_sprites\{str(name)}"
        aft_im= rf"im_sprites_player_change\{str(name)}"

        im = Image.open(bef_im)
        if names[name]["type"] == "back":
            size = (win_size_x//names[name]["divider"],win_size_y//names[name]["divider"])
        elif names[name]["type"] == "item":
            size = (item_size // names[name]["divider"],item_size // names[name]["divider"])
        im = im.resize(size)
        im.save(aft_im)

def Names_con(dev,typ):
    return {"divider":dev, "type":typ}

names =  {"forest.jpg":Names_con(1,"back"), "head.png":Names_con(head_size,"item"), "sim_food.png":Names_con(food_size,"item")}
Add_im_for_sprite(names)

Snake(win_size_y)
