import os
from PIL import Image
from datetime import datetime, timedelta
from similarity import calculate_similarity
from image_processor import extract_features, calculate_sharpness

def simulate_photo_burst():
    """Create a burst of sample photos taken seconds apart."""
    os.makedirs("test_gallery", exist_ok=True)
    
    # 3 photos of a scene (burst shot)
    base_time = datetime(2026, 10, 25, 14, 0, 0)
    burst_shots = [
        {"name": "test_gallery/shot1.jpg", "color": (100, 150, 200), "delta": 0},
        {"name": "test_gallery/shot2.jpg", "color": (102, 148, 201), "delta": 2},
        {"name": "test_gallery/shot3.jpg", "color": (98, 151, 199), "delta": 4},
    ]
    
    # 1 completely different scene taken 10 minutes later
    burst_shots.append({
        "name": "test_gallery/shot4_nature.jpg",
        "color": (40, 180, 50),
        "delta": 600
    })

    metadata_list = []
    for item in burst_shots:
        img = Image.new("RGB", (300, 300), color=item["color"])
        img.save(item["name"])
        
        timestamp = base_time + timedelta(seconds=item["delta"])
        features = extract_features(item["name"])
        sharpness = calculate_sharpness(item["name"])
        
        metadata_list.append({
            "path": item["name"],
            "timestamp": timestamp,
            "features": features,
            "sharpness": sharpness
        })
        
    return metadata_list

def cluster_and_select_best(photos, time_window_seconds=10, similarity_threshold=95.0):
    """Cluster photos by time window and visual similarity, picking the sharpest."""
    clusters = []
    current_cluster = []

    for photo in photos:
        if not current_cluster:
            current_cluster.append(photo)
            continue

        prev_photo = current_cluster[-1]
        time_diff = abs((photo["timestamp"] - prev_photo["timestamp"]).total_seconds())
        sim_score = calculate_similarity(photo["features"], prev_photo["features"])

        if time_diff <= time_window_seconds and sim_score >= similarity_threshold:
            current_cluster.append(photo)
        else:
            clusters.append(current_cluster)
            current_cluster = [photo]

    if current_cluster:
        clusters.append(current_cluster)

    return clusters

if __name__ == "__main__":
    print("Step 1: Generating test burst photos...")
    photos = simulate_photo_burst()

    print("Step 2: Analyzing similarity and clustering...")
    clusters = cluster_and_select_best(photos)

    print(f"\nTotal clusters found: {len(clusters)}\n" + "-" * 40)
    for idx, cluster in enumerate(clusters, 1):
        print(f"Cluster {idx} ({len(cluster)} photo(s)):")
        # Select best photo based on sharpness
        best_photo = max(cluster, key=lambda p: p["sharpness"])
        for p in cluster:
            mark = "⭐️ [BEST KEEP]" if p["path"] == best_photo["path"] else "   [DUPLICATE]"
            print(f"  {mark} {p['path']} | Sharpness: {p['sharpness']}")
        print("-" * 40)
