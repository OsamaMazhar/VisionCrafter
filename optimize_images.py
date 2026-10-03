import os
from PIL import Image

def optimize_images(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.lower().endswith('.png'):
                file_path = os.path.join(root, file)
                try:
                    with Image.open(file_path) as img:
                        # Check for transparency
                        has_transparency = img.mode in ('RGBA', 'LA') or (img.mode == 'P' and 'transparency' in img.info)
                        
                        # Target format
                        # We use WebP for everything as it handles transparency and compression better
                        # But user asked for jpeg.
                        # If transparency, use WebP. If not, use JPG.
                        
                        if has_transparency:
                            new_ext = '.webp'
                            save_kwargs = {'format': 'WEBP', 'quality': 80}
                        else:
                            new_ext = '.jpg'
                            img = img.convert('RGB')
                            save_kwargs = {'format': 'JPEG', 'quality': 80, 'optimize': True}

                        new_file_path = os.path.splitext(file_path)[0] + new_ext
                        
                        # Convert
                        img.save(new_file_path, **save_kwargs)
                        
                        print(f"Converted {file} to {new_ext}")
                        
                except Exception as e:
                    print(f"Failed to convert {file}: {e}")

if __name__ == "__main__":
    optimize_images('docs/syncalbum/assets')
