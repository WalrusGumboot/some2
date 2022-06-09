from manim import *

class FirstLook(Scene):
    def construct(self):
        x_range = [-20, 20, 1]
        y_range = x_range # [x * 9 / 16 for x in x_range]
        scale = 0.6

        grid = NumberPlane(
            x_range = x_range, 
            y_range = y_range,
            **{"axis_config": {"stroke_width": 5, "color": BLACK}}
        ).scale(scale)
        
        self.wait()

        graph = ImplicitFunction(
            lambda x, y: y ** 2 - (-0.2 * x**3 + 3*x + 5),
            color = RED, x_range = x_range, y_range = y_range,
            min_depth = 7, max_quads = 2500, 
        ).scale(scale).move_to([-1, 0, 0])

        self.play(Create(grid, lag_ratio = 0.1, run_time = 3))
        self.play(Create(graph, run_time = 6))
        self.wait()
