import math

def calculate_similarity(img1_features, img2_features):
    """
    Calculate Cosine Similarity between two image feature vectors.
    """
    dot_product = sum(a * b for a, b in zip(img1_features, img2_features))
    norm_a = math.sqrt(sum(a * a for a in img1_features))
    norm_b = math.sqrt(sum(b * b for b in img2_features))
    
    if norm_a == 0 or norm_b == 0:
        return 0.0
    
    similarity = dot_product / (norm_a * norm_b)
    return round(similarity * 100, 2)


# Simulated feature vectors for two very similar consecutive photos
photo_a = [0.85, 0.42, 0.91, 0.12]
photo_b = [0.84, 0.40, 0.90, 0.15]

# Simulated feature vector for a completely different photo
photo_c = [0.10, 0.95, 0.05, 0.88]

print("Similarity between Photo A and Photo B:", calculate_similarity(photo_a, photo_b), "%")
print("Similarity between Photo A and Photo C:", calculate_similarity(photo_a, photo_c), "%")