import openpyxl

from openpyxl.drawing.image import Image
import os 
def link_images_to_excel(images_info,excel_file):
    if os.path.exists(excel_file):
        workbook = openpyxl.load_workbook(excel_file)
    else:
        workbook = openpyxl.Workbook()
    sheet = workbook.active
    for cell_info in images_info:
        cell , image_path = cell_info['cell'], cell_info['image_path']
        if os.path.exists(image_path):
            img = Image(image_path)
            img.anchor = cell
            sheet.add_image(img)

            sheet[cell].value = 'Image for {cell}'
        else:
            print(f'Image not found for {cell}: {image_path}')
    workbook.save(excel_file)

