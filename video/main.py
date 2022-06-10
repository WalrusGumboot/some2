from manim import *
import json

ssot_cols_file = open("../ssot/colors.json", 'r')
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
            **{"axis_config": {"stroke_width": 5, "color": colors["blue"]}}
        ).scale(scale)
        
        self.wait()
        a = ValueTracker(-0.2)
        b = ValueTracker(3)
        c = ValueTracker(5)

        def get_ec():
            graph = ImplicitFunction(
                lambda x, y: y ** 2 - (a.get_value() * x**3 + b.get_value() * x + c.get_value()),
                color = colors["red"], x_range = x_range, y_range = y_range,
                min_depth = 3, max_quads = 500, **{"stroke_width": 8}
                ).scale(scale)
            return graph
        
        ec = get_ec()
        ec.add_updater(lambda m: m.become(get_ec()))

        mathtex = MathTex(f"a: {round(a.get_value(), 2)}", color = BLACK)
        mathtex.add_updater(lambda x : x.become(Text(f"a: {round(a.get_value(), 2)}", color = BLACK)))
        
        self.play(Create(grid, lag_ratio = 0.1, run_time = 3))
        self.play(Create(ec, run_time = 1), Write(mathtex))
        self.play(
            a.animate.set_value(0.6),
            run_time = 1
        )
        self.wait()
