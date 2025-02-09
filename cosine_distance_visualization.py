from manim import *
from scipy.spatial.distance import cosine


class CosineDistanceVisualization(Scene):
    def construct(self):

        # Create title
        title = Text("Word Relationships: Nature & Sky", font_size=36)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))

        # Add cosine distance formula on the left
        formula = MathTex(
            "S_C (A,B):= \\cos(\\theta) = {\\mathbf{A} \\cdot \\mathbf{B} \\over \\|\\mathbf{A}\\| \\|\\mathbf{B}\\|}",
            font_size=50
        )
        self.play(Write(formula))
        self.wait(5)
        self.play(formula.animate.set(font_size=30))
        self.play(formula.animate.to_edge(DOWN))

        # Create coordinate plane
        plane = NumberPlane(
            x_range=[-1, 5, 1],
            y_range=[-1, 5, 1],
            x_length=6,
            y_length=6,
        ).scale(0.8)
        self.play(Create(plane))

        # Example vectors for our words (these would normally come from real embeddings)
        # Using more varied 2D vectors for better visualization
        vectors = {
            "rose": np.array([2.0, 0.6]),  # flower characteristics
            "sunflower": np.array([1.8, 1.8]),  # flower + sun association
            "sun": np.array([0.5, 2.1]),  # celestial object
        }

        # Create vectors and labels
        origin = plane.coords_to_point(0, 0)
        arrows = {}
        labels = {}

        colors = {
            "rose": "#FF69B4",  # Pink for rose
            "sunflower": "#FFD700",  # Golden yellow for sunflower
            "sun": "#FFA500"  # Orange for sun
        }

        # Create and show vectors one by one
        for word, vec in vectors.items():
            scaled_vec = vec / np.linalg.norm(vec) * (2 + 3.3)  # Scale vectors to lengths of 2 to 6
            point = plane.coords_to_point(*scaled_vec)
            arrows[word] = Arrow(origin, point, buff=0, color=colors[word], stroke_width=5)
            labels[word] = Text(word, font_size=24, color=colors[word])
            label_position = UP + RIGHT if vec[1] >= 0 else DOWN
            labels[word].next_to(arrows[word].get_end(), label_position)

            self.play(
                Create(arrows[word]),
                Write(labels[word])
            )

        # Show angles and distances between pairs
        pairs = [("rose", "sunflower"), ("sunflower", "sun"), ("rose", "sun")]
        angles = {}
        distances = {}
        angle_texts = []
        angle_arrows = []
        for idx, (word1, word2) in enumerate(pairs):
            angle = Angle(
                arrows[word1], arrows[word2],
                radius=0.6 + idx * 0.3,  # Adjust radius for better visibility
                color=WHITE
            )
            cos_dist = cosine(vectors[word1], vectors[word2])

            distance_text = Text(
                f"{word1}-{word2}: {cos_dist:.3f}",
                font_size=20
            ).set_color(WHITE)

            # Position the distance texts in a column on the right
            distances[(word1, word2)] = distance_text

            self.play(Create(angle))

            # Add angle annotations
            angle_value = angle.get_value(degrees=True)
            angle_text = MathTex(f"{angle_value:.1f}^\\circ", font_size=20).next_to(
                angle.get_end(), LEFT
            )
            angle_texts.append(angle_text)

            annotation_arrow = DashedLine(
                start=angle_text.get_right(),
                end=angle.get_center(),
                color=LIGHT_GREY
            )
            angle_arrows.append(annotation_arrow)
            self.play(Write(angle_text), Create(annotation_arrow))
            angles[(word1, word2)] = angle

        # Arrange distance texts
        distance_group = VGroup(*distances.values()).arrange(DOWN, aligned_edge=LEFT)
        distance_group.to_edge(RIGHT)
        self.play(Write(distance_group))

        # Add explanation
        explanation = Text(
            "Smaller cosine distance = More similar meaning",
            font_size=24
        ).to_edge(DOWN)
        self.play(Write(explanation), FadeOut(formula))

        # Final pause
        self.wait(3)

        # Cleanup
        self.play(
            *[FadeOut(obj) for obj in [
                *arrows.values(),
                *labels.values(),
                *angles.values(),
                distance_group,
                plane,
                title,
                *angle_texts,
                *angle_arrows
            ]]
        )
        self.play(
            explanation.animate.move_to(ORIGIN)
        )
        self.play(
            explanation.animate.set(font_size=40)
        )
        self.wait(2)