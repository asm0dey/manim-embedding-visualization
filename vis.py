from manim import *
from scipy.spatial.distance import cosine

class WordEmbeddingAnalogy(Scene):
    def construct(self):
        # Create coordinate system
        axes = Axes(
            x_range=[-3, 6, 1], y_range=[-1, 6, 1], axis_config={"color": GREY}
        ).add_coordinates()

        axes_labels = axes.get_axis_labels(x_label="", y_label="")

        grid_group = VGroup(axes, axes_labels)
        grid_group.shift(LEFT * 0.5)
        self.play(Create(axes), Write(axes_labels))

        origin = axes.c2p(0, 0)

        # Define vectors
        king_end = axes.c2p(3, 2)
        man_end = axes.c2p(2.5, 0.8)
        woman_end = axes.c2p(-1.5, 3)

        king_vec = Arrow(origin, king_end, color=BLUE, buff=0)
        man_vec = Arrow(origin, man_end, color=GREEN, buff=0)
        woman_vec = Arrow(origin, woman_end, color=RED, buff=0)
        queen_vec = Arrow(origin, king_end - man_end + woman_end, color=PURPLE, buff=0)

        # Labels
        king_label = Text("king", color=BLUE).next_to(
            king_vec.get_end(), UP + RIGHT, buff=0.1
        )
        man_label = Text("man", color=GREEN).next_to(
            man_vec.get_end(), DOWN + RIGHT, buff=0.1
        )
        woman_label = Text("woman", color=RED).next_to(
            woman_vec.get_end(), UP + LEFT, buff=0.1
        )
        queen_label = Text("queen", color=PURPLE).next_to(
            queen_vec.get_end(), UP + RIGHT, buff=0.1
        )

        # Show initial vectors
        self.play(Create(king_vec), Write(king_label))
        self.play(Create(man_vec), Write(man_label))
        self.wait(2)

        # Demonstrate vector subtraction (king - man)
        # Create a copy of negative man vector (-man) that starts at king's end
        man_negative = Arrow(
            king_end, king_end - (man_end - origin), color=GREEN, buff=0
        )
        man_negative.set_opacity(0.5)

        # Show the movement of negative man vector
        self.play(TransformFromCopy(man_vec, man_negative), FadeOut(man_vec, man_label))

        # Create the difference vector
        king_minus_man_vector = Arrow(
            origin, king_end - (man_end - origin), color=YELLOW, buff=0
        )
        king_minus_man_label = Text("king - man", color=YELLOW).next_to(
            king_minus_man_vector.get_end(), UP, buff=0.1
        )

        self.play(
            Create(king_minus_man_vector),
            Write(king_minus_man_label),
        )
        self.wait(3)

        # Show woman vector
        self.play(
            Create(woman_vec),
            Write(woman_label),
            # FadeOut(man_negative)
        )

        # Demonstrate vector addition (king-man) + woman
        # Create a copy of woman vector that will move to king_minus_man_vector's end
        king_minus_man_plus_woman = Arrow(
            king_minus_man_vector.get_end(),
            king_minus_man_vector.get_end() + (woman_end - origin),
            color=RED,
            buff=0,
        )
        king_minus_man_plus_woman.set_opacity(0.5)

        self.wait(3)

        # Show the movement of copied woman vector
        self.play(
            TransformFromCopy(woman_vec, king_minus_man_plus_woman),
            # FadeOut(woman_vec, woman_label),
        )

        # Result vector
        result_vec = Arrow(
            origin, king_minus_man_plus_woman.get_end(), color=ORANGE, buff=0
        )
        result_label = Text("king - man + woman", color=ORANGE).next_to(
            result_vec.get_end(), RIGHT, buff=0.1
        )

        self.play(
            Create(result_vec),
            Write(result_label),
            # FadeOut(king_minus_man_vector),
            # FadeOut(king_minus_man_plus_woman)
        )
        self.wait(1)

        # Show queen vector
        self.play(Create(queen_vec), Write(queen_label))

        # Final equation
        final_equation = MathTex(
            "\\text{king} - \\text{man} + \\text{woman} = \\text{queen}"
        ).to_edge(UP)

        self.play(Write(final_equation))
        self.wait(2)

        # Optional: fade out the helper vectors
        # self.play(
        #     FadeOut(man_negative),
        #     FadeOut(king_minus_man_plus_woman)
        # )
        self.wait(2)

class CosineDistanceVisualization(Scene):
    def construct(self):

        # Create title
        title = Text("Word Relationships: Nature & Sky", font_size=36)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))

        # Add cosine distance formula on the left
        formula = MathTex(
            "S_C (A,B):= \\cos(\\theta) = {\\mathbf{A} \\cdot \\mathbf{B} \\over \\|\\mathbf{A}\\| \\|\\mathbf{B}\\|}",
            font_size=50,
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
            "sun": "#FFA500",  # Orange for sun
        }

        # Create and show vectors one by one
        for word, vec in vectors.items():
            scaled_vec = (
                vec / np.linalg.norm(vec) * (2 + 3.3)
            )  # Scale vectors to lengths of 2 to 6
            point = plane.coords_to_point(*scaled_vec)
            arrows[word] = Arrow(
                origin, point, buff=0, color=colors[word], stroke_width=5
            )
            labels[word] = Text(word, font_size=24, color=colors[word])
            label_position = UP + RIGHT if vec[1] >= 0 else DOWN
            labels[word].next_to(arrows[word].get_end(), label_position)

            self.play(Create(arrows[word]), Write(labels[word]))

        # Show angles and distances between pairs
        pairs = [("rose", "sunflower"), ("sunflower", "sun"), ("rose", "sun")]
        angles = {}
        distances = {}
        angle_texts = []
        angle_arrows = []
        for idx, (word1, word2) in enumerate(pairs):
            angle = Angle(
                arrows[word1],
                arrows[word2],
                radius=0.6 + idx * 0.3,  # Adjust radius for better visibility
                color=WHITE,
            )
            cos_dist = cosine(vectors[word1], vectors[word2])

            distance_text = Text(
                f"{word1}-{word2}: {cos_dist:.3f}", font_size=20
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
                start=angle_text.get_right(), end=angle.get_center(), color=LIGHT_GREY
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
            "Smaller cosine distance = More similar meaning", font_size=24
        ).to_edge(DOWN)
        self.play(Write(explanation), FadeOut(formula))

        # Final pause
        self.wait(3)

        # Cleanup
        self.play(
            *[
                FadeOut(obj)
                for obj in [
                    *arrows.values(),
                    *labels.values(),
                    *angles.values(),
                    distance_group,
                    plane,
                    title,
                    *angle_texts,
                    *angle_arrows,
                ]
            ]
        )
        self.play(explanation.animate.move_to(ORIGIN))
        self.play(explanation.animate.set(font_size=40))
        self.wait(2)
