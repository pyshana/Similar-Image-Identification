from PIL import Image, ImageStat
import math
from similarity import calculate_similarity

def extract_features(image_path):
    """Convert an image to a normalized feature vector using RGB averages and aspect ratio."""
    with Image.open(image_path) as img:
        img_small = img.resize((32, 32)).convert('RGB')
        stat = ImageStat.Stat(img_small)
        r, g, b = [val / 255.0 for val in stat.mean]
        aspect_ratio = img.width / img.height
        return [r, g, b, aspect_ratio]

def calculate_sharpness(image_path):
    """Estimate image clarity; higher variance correlates with better sharpness."""
    with Image.open(image_path) as img:
        gray = img.convert('L')
        stat = ImageStat.Stat(gray)
        return round(stat.var[0], 2)

if __name__ == "__main__":
    # Create two sample dummy images to test the pipeline automatically
    img1 = Image.new('RGB', (200, 200), color=(120, 50, 50))
    img1.save("sample1.jpg")

    # A very similar image with slightly shifted tone
    img2 = Image.new('RGB', (200, 200), color=(125, 52, 51))
    img2.save("sample2.jpg")

    feat1 = extract_features("sample1.jpg")
    feat2 = extract_features("sample2.jpg")

    sim = calculate_similarity(feat1, feat2)
    sharp1 = calculate_sharpness("sample1.jpg")
    sharp2 = calculate_sharpness("sample2.jpg")

    print(f"Calculated Real-Image Similarity: {sim}%")
    print(f"Sharpness Scores -> sample1: {sharp1} | sample2: {sharp2}")