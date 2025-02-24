from manim import *


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
        queen_end = axes.c2p(2.5, 4.2)

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
        queen_label = Text("queen = ", color=PURPLE).next_to(
            queen_vec.get_end(), UP + LEFT, buff=0.1
        )

        # Show initial vectors
        self.play(Create(king_vec), Write(king_label))
        self.play(Create(man_vec), Write(man_label))
        self.wait(2)

        king_plus_man_vector = Arrow(
            king_end, king_end + man_end - origin, color=YELLOW, buff=0
        )
        king_plus_man_vector_label = Text("king + man", color=YELLOW).next_to(
            king_plus_man_vector.get_end(), UP, buff=0.1
        )
        self.play(
            TransformFromCopy(man_vec, king_plus_man_vector),
            FadeOut(man_vec, man_label),
            TransformFromCopy(man_label, king_plus_man_vector_label),
        )
        self.wait(3)
        # Demonstrate vector subtraction (king - man)
        # Create a copy of negative man vector (-man) that starts at king's end
        king_minus_man = Arrow(
            king_end, king_end - man_end + origin, color=GREEN, buff=0
        )
        king_minus_man.set_opacity(0.5)
        king_minus_man_label = Text("king - man", color=GREEN).next_to(
            king_minus_man.get_end(), UP, buff=0.1
        )

        # Show the movement of negative man vector
        self.play(
            TransformFromCopy(king_plus_man_vector, king_minus_man),
            TransformFromCopy(king_plus_man_vector_label, king_minus_man_label),
            FadeOut(king_plus_man_vector, king_plus_man_vector_label),
        )

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
            # FadeOut(king_minus_man)
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
            result_vec.get_end(), UP + RIGHT, buff=0.1
        )

        self.play(
            Create(result_vec),
            Write(result_label),
            FadeOut(woman_vec),
            FadeOut(woman_label),
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
        self.wait(4)
        tmp = self.mobjects
        tmp.remove(final_equation)
        self.play(FadeOut(*tmp))
        self.play(
            Transform(
                final_equation,
                MathTex(
                    "\\text{king} - \\text{man} + \\text{woman} = \\text{queen}",
                    font_size=80,
                ),
            ),
        )
        self.wait(3)


if __name__ == "__main__":
    scene = WordEmbeddingAnalogy()
    scene.render()
