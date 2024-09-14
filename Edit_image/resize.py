from PIL import Image
import os

def resize_images_and_masks(img_folder, mask_folder, output_img_folder, output_mask_folder, size=(224, 224)):
    # สร้างโฟลเดอร์เอาต์พุตถ้ายังไม่มี
    if not os.path.exists(output_img_folder):
        os.makedirs(output_img_folder)
    if not os.path.exists(output_mask_folder):
        os.makedirs(output_mask_folder)

    # รีไซส์ภาพ
    for filename in os.listdir(img_folder):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            img_path = os.path.join(img_folder, filename)
            img = Image.open(img_path)
            img_resized = img.resize(size, Image.BILINEAR)  # ใช้ Image.BILINEAR เพื่อการปรับขนาดที่ดีขึ้น
            img_resized.save(os.path.join(output_img_folder, filename))

    # รีไซส์ mask
    for filename in os.listdir(mask_folder):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            mask_path = os.path.join(mask_folder, filename)
            mask = Image.open(mask_path)
            mask_resized = mask.resize(size, Image.NEAREST)  # ใช้ Image.NEAREST สำหรับ mask เพื่อรักษาค่าป้าย
            mask_resized.save(os.path.join(output_mask_folder, filename))

    print('เสร็จสิ้น')


# ขนาดที่ต้องการรีไซส์ (width, height)
new_size = (224, 224)

# รีไซส์ภาพและ masks
resize_images_and_masks('./data/imgs/', './data/masks/', './data_non_aug/imgs/', './data_non_aug/masks/', new_size)