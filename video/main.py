from manim import *
import math
import json
import sympy as sp
import numpy as np

ssot_cols_file = open("../ssot/colors.json", 'r')
colors = json.load(ssot_cols_file)

config.frame_width = 30

class FirstLook(Scene):
    def construct(self):
        self.camera.background_color = colors["bg"]


        x_range = [-15, 15, 1]
        y_range = x_range # [x * 9 / 16 for x in x_range]

        grid = NumberPlane(
            x_range = x_range, 
            y_range = y_range,
            **{"axis_config": {"stroke_width": 5, "color": colors["blue"]}}
        )
        
        self.wait()
        a = ValueTracker(-0.6)
        b = ValueTracker(3)
        
        equation = MathTex("y^2 = x^3 + ax + b").scale(2).set_color(colors["text"])
        equation_rect = Rectangle(
            width = equation.width + 0.5,
            height = equation.height + 0.5,
            color = colors["text"]
        ).set_fill(colors["bg"], opacity = 0.4)

        equation_rect.set_z_index(equation.z_index - 1)

        equation_group = Group(equation, equation_rect)
        equation_group.move_to([-7, 6, 0])

        def get_ec():
            graph = ImplicitFunction(
                lambda x, y: y ** 2 - (x**3 + a.get_value() * x + b.get_value()),
                color = colors["red"], x_range = x_range, y_range = y_range,
                min_depth = 3, max_quads = 800, **{"stroke_width": 8}
            )
            return graph
        
        ec = get_ec()
        ec.add_updater(lambda m: m.become(get_ec()))

        self.play(Create(grid, lag_ratio = 0.07, run_time = 6))
        self.play(
            Write(equation),
            Create(equation_rect),
            run_time = 3
        )
        self.wait(2)
        self.play(Create(ec), run_time = 6)

        def get_tracker_tex(name, tracker):
            return MathTex(f"{name} = {round(tracker.get_value(), 2)}").set_color(colors["text"]).scale(2)

        a_tex = get_tracker_tex("a", a).next_to(equation_group, DOWN, buff = 1.5)
        b_tex = get_tracker_tex("b", b).next_to(a_tex, DOWN, buff = 1.5)
        a_tex.add_updater(lambda m: m.become(get_tracker_tex("a", a).next_to(equation_group, DOWN, buff = 1.5)))
        b_tex.add_updater(lambda m: m.become(get_tracker_tex("b", b).next_to(a_tex, DOWN, buff = 1.5)))
        
        self.play(Write(a_tex), Write(b_tex))

        self.play(a.animate.set_value(-6), run_time = 1)
        self.wait()
        self.play(b.animate.set_value( 9), run_time = 1)
        self.wait()
        self.play(a.animate.set_value( 3),
                  b.animate.set_value(-8), run_time = 1)
        self.wait()
        self.play(a.animate.set_value( 0),                   # this makes the curve non-elliptical
                  b.animate.set_value( 0), run_time = 1)
        self.wait()

class SymmetricalProperty(Scene):
    def construct(self):
        self.camera.frame_width = 16
        self.camera.frame_height = 9
        self.camera.background_color = colors["bg"]
        x_range = [-8, 8, 1]
        y_range = [-4.5, 4.5, 1]
        grid = NumberPlane(
            x_range = x_range,
            y_range = y_range,
            **{"axis_config": {"stroke_width": 2, "color": colors["blue"]}}
        )

        eq = ImplicitFunction(
            lambda x, y: y**2 - (x**3 - 1.5*x + 2),
            x_range = x_range, y_range = y_range,
            color = colors["red"], min_depth = 5, max_quads = 4000,
            **{"stroke_width": 3}
        )

        line_x = ValueTracker(1)

        def get_point(neg):
            x = line_x.get_value()
            return Dot([x, neg * math.sqrt(x**3 - 1.5*x + 2), 0], color = colors["text"])

        intersectionA = get_point( 1)
        intersectionB = get_point(-1)
        
        intersectionA.add_updater(lambda m: m.become(get_point( 1)))
        intersectionB.add_updater(lambda m: m.become(get_point(-1)))
        
        intersection_line = Line([1, -5, 0], [1, 5, 0], color = colors["text"])
        intersection_line.add_updater(lambda m: 
                m.put_start_and_end_on([line_x.get_value(), -5, 0], [line_x.get_value(), 5, 0]))

        self.play(Create(grid, lag_ratio = 0.07, run_time = 1.5))
        self.play(Create(eq))
        self.wait(1)
        self.play(Create(intersection_line, run_time = 4))

        self.play(Create(intersectionA))
        self.play(Create(intersectionB))
        
        #self.play(line_x.animate.set_value(-1.2), run_time = 4)
        #self.play(line_x.animate.set_value( 2.5), run_time = 4)
        self.play(line_x.animate.set_value(-1.6474), run_time = 2)
        
        arrow_text = Tex("Points coincide").set_color(colors["text"]).scale(0.8).move_to([-5, 2, 0]) 
        arrow = Arrow(
            start = arrow_text.get_center(), 
            end = intersectionA.get_center(), 
            buff = 0.5, color = colors["text"],
            stroke_width = 4,
            tip_length = 0.24
        )

        self.play(Write(arrow_text), Create(arrow))

        self.wait(3)

class Addition(Scene):
    def construct(self):
        self.camera.frame_width = 16
        self.camera.frame_height = 9
        self.camera.background_color = colors["bg"]

        x_range = [-8, 8, 1]
        y_range = [-4.5, 4.5, 1]

        grid = NumberPlane(
            x_range = x_range,
            y_range = y_range,
            **{"axis_config": {"stroke_width": 2, "color": colors["blue"]}}
        )

        ec = ImplicitFunction(
            lambda x, y: y**2 - (x**3 - 1.5*x + 2),
            x_range = x_range,
            y_range = y_range,
            color = colors["red"], min_depth = 5, max_quads = 4000,
            **{"stroke_width": 3}
        )

        def add_points(a, p, q):
            px = p[0]
            py = p[1]
            qx = q[0]
            qy = q[1]

            if p == q:
                s  = (3*(px**2) + a)/(2*py)
                rx = s**2 - 2*px
            else:
                s  = (py - qy)/(px - qx)
                rx = s**2 - px - qx

            ry = -py + s*(px - rx)

            return [rx, ry, 0]

        def find_intersects(a, b, m, q):

            ###################################################################################################
            # lijn: y  =      mx + q                                                                          #
            # e.c.: y² = x³ + ax + b                                                                          #
            #                                                                                                 #
            # gelijkheid: (mx + q)² = x³ + ax + b                                                             #
            #              m²x² + 2mqx + q² = x³ + ax + b                                                     #
            #              x³ - m²x² + ax - 2mqx - q² + b = 0                                                 #
            #              x³ - m²x² + (a - 2mq)x - (q² + b) = 0                                              #
            #              (x - x1)(x - x2)(x - x3) = x³ + x²(-x1 - x2 - x3) + x(x1x2 + x1x3 + x2x3) - x1x2x3 #
            ###################################################################################################

            x = sp.var("x")
            all_roots = sp.solve(sp.Eq(x**3 - m**2*x**2 + a*x - 2*m*q*x - q**2 + b, 0), x)
            real_roots = map(lambda x: float(sp.re(x)), filter(lambda x: abs(sp.im(x)) < 0.0001 , all_roots))

            return list(real_roots)


        def make_line(point, rico):
            x = point[0]
            y = point[1]

            ext_x1 = x
            ext_y1 = y

            while ext_x1 < x_range[1]:
                ext_x1 += 1
                ext_y1 += rico

            ext_x2 = x
            ext_y2 = y

            while ext_x2 > x_range[0]:
                ext_x2 -= 1
                ext_y2 -= rico

            return Line(start = [ext_x1, ext_y1, 0], end = [ext_x2, ext_y2, 0], color = colors["purple"])


        self.play(Create(grid, lag_ratio = 0.07, run_time = 1.5))
        self.play(Create(ec))
        self.wait(1)

        m = ValueTracker(0.75)
        q = ValueTracker(0)

        line = make_line(ORIGIN, m.get_value())
        line.add_updater(lambda l: l.become(make_line([0, q.get_value(), 0], m.get_value())))


        def intersection_points():
            return VGroup(*[Dot([x, m.get_value()*x+q.get_value(), 0], color=colors["text"]) for x in find_intersects(-1.5, 2, m.get_value(), q.get_value())])

        dots = intersection_points()
        dots.add_updater(lambda m: m.become(intersection_points()))

        self.play(Create(line))
        self.play(Create(dots))

        def number_of_intersection_points():
            return len(find_intersects(-1.5, 2, m.get_value(), q.get_value()))

        num_itsct_pts = Tex(f"Number of intersection points: {number_of_intersection_points()}", color=colors["text"]).move_to([-4, 3, 0])
        num_itsct_pts.add_updater(lambda m: m.become(Tex(f"Number of intersection points: {number_of_intersection_points()}", color=colors["text"]).move_to([-4, 3, 0])))

        text_rectangle = Rectangle(height = num_itsct_pts.height + 0.3,
                                   width  = num_itsct_pts.width  + 0.5,
                                   color = colors["text"],
                                   fill_color = colors["bg"],
                                   fill_opacity=0.4).set_z_index(-100).move_to([-4, 3, 0])

        self.play(Write(num_itsct_pts), FadeIn(text_rectangle), run_time=1)

        self.wait(2)
        self.play(m.animate.set_value(4), run_time=1)
        self.wait(3)
        self.play(m.animate.set_value(0), q.animate.set_value(-1.4), run_time=1)
        self.wait(3)


        gekleurde_punten = intersection_points()
        offset = np.array([-0.7, -0.7, 0.])
        label_a = Tex("A", color = colors["text"]).next_to(gekleurde_punten[0].get_center(), direction=offset)
        label_b = Tex("B", color = colors["text"]).next_to(gekleurde_punten[1].get_center(), direction=offset)
        label_c = Tex("C", color = colors["text"]).next_to(gekleurde_punten[2].get_center(), direction=offset)

        self.remove(dots)
        self.play(gekleurde_punten[0].animate.set_color(colors["orange"]),
                  gekleurde_punten[1].animate.set_color(colors["green"]),
                  gekleurde_punten[2].animate.set_color(colors["yellow"]),
                  FadeIn(label_a, label_b, label_c))
        self.wait(1)

        addition_formula = MathTex("A + B + C = 0", color=colors["text"]).scale(2.5)
        formula_bg_rect = Rectangle(width = addition_formula.width + 1.5, height = addition_formula.height + 1,
                                    color = colors["text"], fill_color = colors["bg"], fill_opacity = 0.4).set_z_index(addition_formula.z_index - 1)

        self.play(FadeIn(formula_bg_rect), Write(addition_formula))
        self.wait(1)
        self.play(Transform(addition_formula, MathTex("A + B = -C", color=colors["text"]).scale(2.5)))
        self.wait(3)
        self.play(FadeOut(formula_bg_rect, addition_formula))


        c_x = gekleurde_punten[2].get_center()
        vert_line_at_c = Line(start= [c_x[0], -10, 0], end = [c_x[0], 10, 0], color="#878787")
        self.play(Create(vert_line_at_c))
        self.wait(1)

        label_c.add_updater(lambda m: m.next_to(gekleurde_punten[2].get_center(), direction = offset))
        self.play(gekleurde_punten[2].animate.move_to([c_x[0], -c_x[1], 0.]))


        self.wait(1)

def is_prime(n):
  for i in range(2,n):
    if (n%i) == 0:
      return False
  return True

class PublicKeyCryptography(Scene):
    def construct(self):
        text_673 = Tex("673").scale(2).move_to(LEFT)
        text_977 = Tex("977").scale(2).move_to(RIGHT)

        self.play(Write(text_673), Write(text_977))
        self.wait(2)

        text_res = Tex(str(673*977)).scale(2)
        self.play(FadeOut(text_673), FadeOut(text_977), FadeIn(text_res))
        self.wait(2)
        self.play(FadeOut(text_res))


        text_question = Text("Two prime numbers divide 783451. Which ones?").scale(2).move_to(UP)
        self.play(Write(text_question))

        text_num = Tex("657521 / \;").scale(2).move_to(DOWN + LEFT * 2)
        self.add(text_num)

        for i in filter(is_prime, range(2, 976)):
            #if is_prime(i):
            time = 7/(i+60)
            test_num_text = Tex(f"{i}").scale(2).next_to(text_num, RIGHT, buff = 1)
            self.add(test_num_text)
            division_text = Tex(f" = {round(657521 / i, 7)}...").scale(2).next_to(test_num_text, RIGHT, buff = 1)
            if (time > 0.1):
                self.play(FadeIn(division_text, shift = RIGHT),run_time = time)
            else:
                self.add(division_text)
            self.wait(time)
            self.remove(division_text, test_num_text)
