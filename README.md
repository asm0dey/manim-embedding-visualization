# Vector Visualizations

A collection of mathematical animations focused on vector operations and relationships, built using Manim (Mathematical Animation Engine).

## Project Overview

This project uses Manim to create high-quality animations that help visualize:
- Vector operations and transformations
- Cosine distance relationships
- Embedding spaces and their properties

The animations aim to provide intuitive understanding of vector mathematics through clear, professional-quality visualizations.

## Prerequisites

- Python 3.13.1
- [uv](https://github.com/astral-sh/uv) - Fast Python package installer and resolver
- System dependencies for Manim (Cairo, FFmpeg, etc.)

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd vectors
```

2. Install system dependencies (if not already installed):

On Ubuntu/Debian:
```bash
sudo apt install libcairo2-dev ffmpeg texlive texlive-latex-extra texlive-fonts-extra
```

On macOS:
```bash
brew install cairo ffmpeg
```

3. Set up Python environment using uv:
```bash
uv venv
source .venv/bin/activate  # On Unix/macOS
# or
.venv\Scripts\activate  # On Windows
uv pip install -r requirements.txt
```

## Creating Animations

### Render Animations

To render an animation:

```bash
manim -pqh cosine_distance_visualization.py CosineDistanceScene
```

Command flags:
- `-p`: Preview the animation after rendering
- `-q`: Quality (l: low, m: medium, h: high, k: 4k)
- `-h`: High quality rendering

### Available Scenes

1. Cosine Distance Visualization:
```bash
manim -pqh cosine_distance_visualization.py CosineDistanceScene
```

2. Embedding Visualization:
```bash
manim -pqh embedding_visualisation.py EmbeddingScene
```

The rendered animations will be saved in the `media` directory.
