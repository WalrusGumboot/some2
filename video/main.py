from manim import *
import json

ssot_cols_file = open("../ssot/colors.json", r)
colors = json.load(ssot_cols_file)

class FirstLook(Scene):
    def construct(self):
        self.camera.background_color = colors["bg"]


        x_range = [-20, 20, 1]
        y_range = x_range # [x * 9 / 16 for x in x_range]
        scale = 0.6

        grid = NumberPlane(
            x_range = x_range, 
            y_range = y_range,
            **{"axis_config": {"stroke_width": 5, "color": BLUE}}
        ).scale(scale)
        
        self.wait()
        a = ValueTracker(-0.2)
        b = ValueTracker(3)
        c = ValueTracker(5)
        graph = ImplicitFunction(
            lambda x, y: y ** 2 - (a.get_value() * x**3 + b.get_value() * x + c.get_value()),
            color = RED, x_range = x_range, y_range = y_range,
            min_depth = 7, max_quads = 2500, **{"stroke_width": 6}
        ).scale(scale).move_to([-1, 0, 0])
        
        graph.add_updater(lambda x: x.generate_points())

        mathtex = Text(f"a: {a.get_value()}", color = BLACK)
        mathtex.add_updater(lambda x : x.become(Text(f"a: {a.get_value()}", color = BLACK)))
        
        self.play(Create(grid, lag_ratio = 0.1, run_time = 3))
        self.play(Create(graph, run_time = 6), Write(mathtex))
        self.play(
            a.animate.set_value(2)
        )
        self.wait()
