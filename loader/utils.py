def save_uploaded_picture(picture):
    filename = picture.filename
    file_type = filename.split('.')[-1]

    if file_type not in ['jpeg', 'bmp', 'jpg', 'svg', 'png']:
        return

    picture.save(f'./uploads/{filename}')

    return f'uploads/{filename}'