from datetime import datetime

# Simulated photo timeline with metadata: ID, timestamp, and sharpness score
photo_timeline = [
    {
        "id": "IMG_001.jpg",
        "time": "2026-10-25 10:15:10",
        "features": [0.85, 0.42, 0.91, 0.12],
        "sharpness": 88  # higher score indicates a clearer image
    },
    {
        "id": "IMG_002.jpg",
        "time": "2026-10-25 10:15:25",
        "features": [0.84, 0.40, 0.90, 0.15],
        "sharpness": 95  # clearer shot
    },
    {
        "id": "IMG_003.jpg",
        "time": "2026-10-25 11:30:00",
        "features": [0.10, 0.95, 0.05, 0.88],
        "sharpness": 90
    }
]

def parse_time(time_str):
    return datetime.strptime(time_str, "%Y-%m-%d %H:%M:%S")

def find_duplicates_in_timeline(photos, max_interval_seconds=60):
    duplicate_groups = []
    
    for i in range(len(photos) - 1):
        p1 = photos[i]
        p2 = photos[i + 1]
        
        # 1. Calculate time difference between consecutive photos
        t1 = parse_time(p1["time"])
        t2 = parse_time(p2["time"])
        interval = (t2 - t1).total_seconds()
        
        # 2. Check if photos were taken within the target time window
        if interval <= max_interval_seconds:
            best_shot = p1["id"] if p1["sharpness"] > p2["sharpness"] else p2["id"]
            redundant_shot = p2["id"] if best_shot == p1["id"] else p1["id"]
            
            duplicate_groups.append({
                "pair": (p1["id"], p2["id"]),
                "recommended_keep": best_shot,
                "suggested_delete": redundant_shot
            })
            
    return duplicate_groups

# Execute timeline comparison
results = find_duplicates_in_timeline(photo_timeline)
for item in results:
    print("Found pair:", item["pair"])
    print("-> Recommended to keep:", item["recommended_keep"])
    print("-> Suggested to delete:", item["suggested_delete"])
