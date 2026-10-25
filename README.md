# Similar Image Identification & Burst Cleaner

An automated, intelligent image curation pipeline designed to solve the gallery clutter problem caused by burst shots, consecutive framing, and near-duplicate captures.

## Key Features
- **Temporal Closeness Filtering:** Groups photos captured within rapid timestamps (configurable delta threshold).
- **Lightweight Feature Extraction:** Analyzes normalized average color distribution and aspect ratio via Pillow (`PIL`).
- **Cosine Similarity Engine:** Calculates mathematical visual correlation between extracted image vectors.
- **Clarity & Sharpness Scoring:** Evaluates image Laplacian variance to automatically recommend the sharpest photo (`⭐️ BEST KEEP`) and flag blurry redundant duplicates.

## Architecture & Project Structure
- `similarity.py`: Core mathematical cosine similarity vector comparison.
- `image_processor.py`: Image loading, spatial normalization, and sharpness analysis.
- `timeline_filter.py`: Temporal and visual clustering pipeline for photo batches.

## Quick Start
1. Clone the repository and navigate into the project:
   ```bash
   git clone [https://github.com/pyshana/Similar-Image-Identification.git](https://github.com/pyshana/Similar-Image-Identification.git)
   cd Similar-Image-Identification
