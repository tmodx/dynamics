from manim import *
import numpy as np
import random

from circuits import resistor

def set_math_colors(*equations):
    for equation in equations:
        equation.set_color_by_tex("{F}",RED)
        equation.set_color_by_tex("{f}",GREEN)
        equation.set_color_by_tex("{r}",RED)
        equation.set_color_by_tex("{N}",BLUE)
        equation.set_color_by_tex("{W}",RED)
        equation.set_color_by_tex("{T}",PURPLE)
        equation.set_color_by_tex("{x}",RED)
        equation.set_color_by_tex("{v}",BLUE)
        equation.set_color_by_tex("{a}",GREEN)
        equation.set_color_by_tex("{m}",PURPLE)
        equation.set_color_by_tex("{g}",GREY)
        equation.set_color_by_tex("{k}",GREY)
        equation.set_color_by_tex("frac",WHITE)

class KinematicsToDynamics(MovingCameraScene):
    def construct(self):
        kinematics_circle = VGroup(Circle(color=WHITE,radius=3.5,stroke_width=8),
                                   Text("Kinematics").scale(1.5))
        dynamics_circle = VGroup(Circle(color=WHITE,radius=10,stroke_width=8),
                                 Text("Dynamics").scale(1.5).move_to(5*UR))

        self.play(FadeIn(kinematics_circle))
        self.add(dynamics_circle)
        self.wait()
        self.play(self.camera.frame.animate.set(width=45),rate_func=rate_functions.smooth,run_time=1.5)
        self.wait()
        self.play(FadeOut(kinematics_circle,dynamics_circle))
        self.wait()

class SphereInSpace(Scene):
    def construct(self):
        sphere = Circle(radius=1,color=WHITE,fill_opacity=0.1,fill_color=WHITE)

        push_vector = Vector(color=RED).put_start_and_end_on(4*LEFT,2*LEFT)
        pull_vector = Vector(color=BLUE).put_start_and_end_on(2*RIGHT,4*RIGHT)

        self.play(Write(sphere))
        self.wait()
        self.play(Write(push_vector))
        self.wait()
        self.play(Write(pull_vector))
        self.wait()

class ForceMagnitudeDirection(Scene):
    def construct(self):
        force_angle = ValueTracker(0)
        
        force = Vector(5*RIGHT,color=RED).move_to(ORIGIN).add_updater(lambda mob: mob.set_angle(force_angle.get_value()))

        force_bottom_line = Line(start=force.get_start(),end=force.get_end()).set_z_index(-5)
        force_angle_arc = always_redraw(lambda: Arc(radius=2,start_angle=0,angle=force_angle.get_value()).move_arc_center_to(force.get_start()))
        force_theta_label = Tex(r"$\theta$",color=WHITE).shift(0.5*UP)

        force_arrow_label = Tex(r"$\vec{F}$",color=RED).add_updater(lambda mob: mob.next_to(force.get_end(),UP))

        self.play(Write(force),FadeIn(force_arrow_label))
        self.add(force_angle_arc)
        self.wait()
        self.play(force_angle.animate.set_value(PI/6),FadeIn(force_bottom_line,force_theta_label))
        self.wait()
        self.play(VGroup(force,force_bottom_line,force_angle_arc,force_theta_label,force_arrow_label).animate.move_to(ORIGIN))
        self.wait()

class MultipleForces(Scene):
    def construct(self):
        force_1 = Vector(color=RED).put_start_and_end_on(3*DOWN,ORIGIN) 
        force_2 = Vector(color=YELLOW_B).put_start_and_end_on(3*LEFT,ORIGIN)
        force_3 = Vector(color=ORANGE).put_start_and_end_on(ORIGIN,ORIGIN+3*UR)

        forces = VGroup(force_1,force_2,force_3).shift(LEFT+0.5*DOWN)

        f1_label = Tex(r"$\vec{F_1}$",color=RED).next_to(force_1.get_end(),DR)
        f2_label = Tex(r"$\vec{F_2}$",color=YELLOW_B).next_to(force_2.get_end(),UL)
        f3_label = MathTex(r"\vec{F_3}","=",r"\vec{F_1}","+",r"\vec{F_2}").next_to(force_3.get_end(),UP)
        f3_label.set_color_by_tex("F_1",RED)
        f3_label.set_color_by_tex("F_2",YELLOW_B)
        f3_label.set_color_by_tex("F_3",ORANGE)

        self.play(Write(force_1),FadeIn(f1_label))
        self.play(Write(force_2),FadeIn(f2_label))
        self.wait()
        self.play(Write(force_3),FadeIn(f3_label))
        self.wait()

# Also add in the push vector in post
class DriftingSphere(Scene):
    def construct(self):
        sphere = Circle(radius=1,color=WHITE,fill_opacity=0.1,fill_color=WHITE).shift(3*LEFT)

        self.play(Write(sphere))
        self.wait()
        self.play(sphere.animate.shift(15*RIGHT),rate_func=rate_functions.linear,run_time=15)
        self.wait()

class NewtonsFirstLaw(Scene):
    def construct(self):
        header = Text("Newton's 1st Law").scale(1.5)
        # add the body text in post

        self.play(Write(header))
        self.wait()
        self.play(header.animate.to_edge(UP))
        self.wait()

class InertialFrame(Scene):
    def construct(self):
        header = Text("Inertial Reference Frame")

        velocity_arrow = Vector(6*RIGHT,color=BLUE).move_to(ORIGIN)
        velocity_label = Tex(r"$\vec{v}$",color=BLUE).next_to(velocity_arrow.get_end(),UP)

        other_object = Circle(radius=0.5,color=WHITE).move_to(5*RIGHT+UP)
        other_node_acc = Vector(DOWN,color=GREEN).next_to(other_object,DOWN)
        other_node_acc_label = Tex(r"$\vec{a}$",color=GREEN).next_to(other_node_acc.get_end(),LEFT)


        self.play(Write(header))
        self.play(header.animate.to_edge(UP))
        self.play(Write(velocity_arrow),FadeIn(velocity_label))
        self.wait()
        self.play(Write(other_object))
        self.wait()
        self.play(Write(other_node_acc),FadeIn(other_node_acc_label))
        self.wait()

class RotatingReferenceFrame(Scene):
    def construct(self):
        centrifuge_angle = ValueTracker(0)

        big_circle = Circle(radius=3.5,color=WHITE)

        person = SVGMobject("img/stick-man.svg").rotate(PI/2).shift(2.5*RIGHT)
        ball = Circle(radius=0.2,color=RED).move_to(person).set_z_index(5).shift(0.25*UR)

        centrifuge_lines = VGroup(Line(start=ORIGIN,end=3.5*LEFT),
                                  Line(start=ORIGIN,end=3.5*np.cos(PI/3)*RIGHT+3.5*np.sin(PI/3)*UP),
                                  Line(start=ORIGIN,end=3.5*np.cos(PI/3)*RIGHT-3.5*np.sin(PI/3)*UP)).set_opacity(0.33)

        centrifuge = VGroup(centrifuge_lines,person,ball).rotate(-PI/2,axis=OUT,about_point=ORIGIN)


        self.play(Write(big_circle),Write(person),Write(ball),FadeIn(centrifuge_lines))
        self.wait()
        self.play(Rotate(centrifuge,angle=2*PI,axis=OUT,about_point=ORIGIN),rate_func=rate_functions.smooth,run_time=2)
        self.wait()
        self.play(Rotate(centrifuge,angle=PI/4,axis=OUT,about_point=ORIGIN),rate_func=rate_functions.smooth)

        ball_continued_line = Vector(color=RED).put_start_and_end_on(start=ball.get_center(),end=ball.get_center()+1.35*UR)

        self.wait()
        self.play(Write(ball_continued_line))
        centrifuge.add(ball_continued_line)
        self.wait()
        self.play(Rotate(centrifuge,angle=-PI/4,axis=OUT,about_point=ORIGIN))

        centrifuge.remove(ball)
        self.add(ball,ball_continued_line)
        centrifuge.remove(ball_continued_line)

        self.wait()
        self.play(Rotate(centrifuge,angle=PI/6 - 0.1,axis=OUT,about_point=ORIGIN),
                  MoveAlongPath(ball,ball_continued_line),rate_func=rate_functions.smooth)

        false_acceleration_vector = Vector(color=GREEN).put_start_and_end_on(ORIGIN,1.25*(np.cos(3*PI/2 + PI/6 + 0.1)*RIGHT+np.sin(3*PI/2 + PI/6 + 0.1)*UP))

        self.wait()
        self.play(Write(false_acceleration_vector))
        self.wait()

class Stars(ThreeDScene):
    def construct(self):
        stars = []
        for i in range(20):
            new_star = SVGMobject("img/star.svg").scale(random.random()/8).move_to((random.random()*2-1)*7*RIGHT+(random.random()*2-1)*4*UP)
            stars.append(new_star)
        
        earth = SVGMobject("img/earth.svg")

        self.play(*[Write(star) for star in stars])
        self.wait()
        self.play(Write(earth))
        self.wait()
        self.play(Rotate(earth,angle=2*PI,axis=UP,about_point=ORIGIN),run_time=2)
        self.wait()

class NewtonsSecondLawAndThird(Scene):
    # add 3rd law text in post
    def construct(self):
        header = Text("Newton's 2nd Law").scale(1.5)
        header_third = Text("Newton's 3rd Law").scale(1.5).to_edge(UP)

        the_law = MathTex(r"\vec{F}_{\text{net}}","=","{m}",r"\vec{a}").scale(2)
        the_third_law = MathTex(r"\vec{F}_{A","B}","=","-",r"\vec{F}_{","B","A}").scale(2)

        set_math_colors(the_law,the_third_law)
        the_third_law.set_color_by_tex("A",RED)
        the_third_law.set_color_by_tex("B",BLUE)

        person = SVGMobject("img/stick-man.svg").shift(2*DOWN)
        person2 = person.copy().shift(2.5*RIGHT)
        box = Square(side_length=2.5,color=BLUE).move_to(person)

        internal_vec = Vector(color=RED).put_start_and_end_on(2*DOWN+0.25*RIGHT,2*DOWN+RIGHT)
        external_vec = Vector(color=RED).put_start_and_end_on(2*DOWN+2.25*RIGHT,2*DOWN+1.5*RIGHT)
        n3l_pair_vec = Vector(color=RED).put_start_and_end_on(2*DOWN+0.25*LEFT,2*DOWN+LEFT)
        
        node_a = VGroup(Square(color=RED).shift(2*DL+0.5*LEFT),
                          Tex(r"$A$",color=RED).shift(2*DL+0.5*LEFT))
        node_b = VGroup(Square(color=BLUE).shift(2*DR+0.5*RIGHT),
                          Tex(r"$B$",color=BLUE).shift(2*DR+0.5*RIGHT))

        force_ab = Vector(color=RED).put_start_and_end_on(2*DOWN,2*DOWN+RIGHT)
        force_ba = Vector(color=BLUE).put_start_and_end_on(2*DOWN,2*DOWN+LEFT)

        center_mass_dot = Dot(color=RED).move_to(person).set_z_index(5)

        self.play(Write(header))
        self.wait()
        self.play(header.animate.to_edge(UP))
        self.wait()
        self.play(Write(the_law))
        self.wait()
        self.play(the_law.animate.next_to(header,DOWN))
        self.wait()
        self.play(Write(person),Write(box))
        self.wait()
        self.play(Write(internal_vec))
        self.wait()
        self.play(Write(person2),Write(external_vec),FadeOut(internal_vec))
        self.wait()
        self.play(TransformMatchingShapes(header,header_third),FadeOut(the_law))
        self.wait()
        self.play(FadeOut(box,person,person2,external_vec))
        self.wait(2)
        self.play(Write(the_third_law.next_to(header,DOWN)),
                  FadeIn(node_a,node_b,force_ab,force_ba)) 
        self.wait()
        self.play(FadeOut(node_a,node_b,force_ab,force_ba),
                  FadeIn(person,box,internal_vec.shift(1.25*RIGHT)))
        self.wait()
        self.play(FadeIn(n3l_pair_vec))
        self.wait()
        self.play(Write(center_mass_dot))
        self.play(FadeOut(internal_vec,n3l_pair_vec),person.animate.shift(0.25*LEFT),box.animate.shift(0.35*RIGHT))
        self.wait()

class BoxOnTable(Scene):
    def construct(self):
        ground = Line(start=1.5*DOWN+7*LEFT,end=1.5*DOWN+7*RIGHT,color=GREEN)  

        table = VGroup(Line(start=1.5*LEFT+1.5*DOWN,end=1.5*LEFT),
                        Line(start=1.5*RIGHT+1.5*DOWN,end=1.5*RIGHT),
                        Line(start=2*LEFT,end=2*RIGHT)).set_color(DARK_BROWN)
        
        box = Square(side_length=1).move_to(ORIGIN).shift(0.525*UP)

        box_weight_1 = MathTex("{F}","=","{m}","{a}").to_edge(UP).scale(1.5).shift(DOWN)
        box_weight_2 = MathTex("{F}","=","{m}_b","{g}").to_edge(UP).scale(1.5).shift(DOWN)
        box_weight_3 = MathTex("{W}_{EB}","=","{m}_b","{g}").to_edge(UP).scale(1.5).shift(DOWN)
        
        set_math_colors(box_weight_1,box_weight_2,box_weight_3)

        w_eb = Vector(color=RED).put_start_and_end_on(box.get_center(),box.get_center()+DOWN)
        w_eb_label = Tex(r"$\vec{W}_{EB}$",color=RED).next_to(w_eb.get_end(),DR)

        n_tb = Vector(color=BLUE).put_start_and_end_on(box.get_center(),box.get_center()+UP)
        n_tb_label = Tex(r"$\vec{N}_{TB}$",color=BLUE).next_to(n_tb.get_end(),UL)

        table_center_of_mass = Dot(color=DARK_BROWN).move_to(table.get_center()).shift(0.25*UP)
        w_et = Vector(color=RED).put_start_and_end_on(table_center_of_mass.get_center(),table_center_of_mass.get_center()+DOWN).shift(0.05*RIGHT)
        w_et_label = Tex(r"$\vec{W}_{ET}$",color=RED).next_to(w_et.get_end(),DR)

        n_gt = Vector(color=BLUE).put_start_and_end_on(table_center_of_mass.get_center()+0.05*LEFT+DOWN,table_center_of_mass.get_center()+0.05*LEFT)
        n_gt_label = Tex(r"$\vec{N}_{GT}$",color=BLUE).next_to(n_gt.get_end(),LEFT)

        n_bt = Vector(color=BLUE).put_start_and_end_on(table_center_of_mass.get_center()+0.75*UP,table_center_of_mass.get_center())
        n_bt_label = Tex(r"$\vec{N}_{BT}$",color=BLUE).next_to(n_bt.get_end(),RIGHT).shift(0.2*UP)

        
        self.play(Write(box))
        self.play(Write(table))
        self.play(Write(ground))
        self.wait()
        self.play(Write(box_weight_1))
        self.wait()
        self.play(Transform(box_weight_1,box_weight_2))
        self.wait()
        self.play(Write(w_eb),FadeIn(w_eb_label),Transform(box_weight_1,box_weight_3))
        self.wait(2)
        self.play(Write(n_tb),FadeIn(n_tb_label),box_weight_1.animate.shift(0.5*UP))
        self.wait(2)
        self.play(FadeOut(n_tb,n_tb_label,w_eb,w_eb_label),Write(table_center_of_mass))
        self.wait()
        self.play(Write(w_et),FadeIn(w_et_label))
        self.wait()
        self.play(Write(n_gt),FadeIn(n_gt_label))
        self.play(Write(n_bt),FadeIn(n_bt_label))
        self.wait()
        self.play(Write(w_eb),Write(n_tb),FadeIn(w_eb_label),FadeIn(n_tb_label),Circumscribe(VGroup(box,table)))
        self.wait()
        self.play(FadeOut(n_bt,n_bt_label,n_tb,n_tb_label),w_eb_label.animate.shift(0.5*UP))
        self.wait(2)

class InclineFriction(Scene):
    def construct(self):
        plane = VGroup(Line(start=4*LEFT+2*DOWN,end=4*RIGHT+2*DOWN),
                       Line(start=4*LEFT+2*DOWN,end=4*RIGHT+UP),
                       Line(start=4*RIGHT+UP,end=4*RIGHT+2*DOWN))

        arc_angle = Angle(plane[0],plane[1],radius=2.5)
        theta = Tex(r"$\theta$").move_to(1.5*DOWN+1.25*LEFT)

        right_angle = VGroup(Line(start=3.5*RIGHT+1.5*DOWN,end=3.5*RIGHT+2*DOWN),
                             Line(start=3.5*RIGHT+1.5*DOWN,end=4*RIGHT+1.5*DOWN))

        box = Square(side_length=1.5,color=BLUE).shift(0.33*UP).rotate(np.arctan2(3,8))

        w_eb = Vector(color=RED).put_start_and_end_on(box.get_center(),DOWN)
        w_eb_label = Tex(r"$\vec{W}_{EB}$",color=RED).scale(0.75).next_to(w_eb.get_end(),DL).shift(0.2*UR)

        w_eb_dotted = DashedLine(start=DOWN,end=2*DOWN)

        dotted_angle = np.arctan2(-8,3)
        dotted_line = DashedLine(start=box.get_center(),end=box.get_center()+2.5*(RIGHT*np.cos(dotted_angle)+UP*np.sin(dotted_angle)))

        dotted2_angle = np.arctan2(3,8)
        dotted_line2 = DashedLine(start=w_eb_dotted.get_end(),end=w_eb_dotted.get_end()+0.75*(np.cos(dotted2_angle)*RIGHT+np.sin(dotted2_angle)*UP))

        right_angle2 = right_angle.copy().scale(0.33).shift(3.1*LEFT+0.1*UP).rotate(dotted2_angle)

        tilted_x_axis = Vector(color=GRAY).put_start_and_end_on(4*RIGHT+UP,4*RIGHT+UP - 1.5*(RIGHT*np.cos(dotted2_angle)+UP*np.sin(dotted2_angle)))
        tilted_y_axis = Vector(color=GRAY).put_start_and_end_on(4*RIGHT+UP,4*RIGHT+UP - 1.5*(RIGHT*np.cos(dotted_angle)+UP*np.sin(dotted_angle)))
        tilt_x_label = Tex("$x$",color=GRAY).next_to(tilted_x_axis.get_end(),UP)
        tilt_y_label = Tex("$y$",color=GRAY).next_to(tilted_y_axis.get_end(),UP).shift(0.2*DOWN)
        tilted_axes = VGroup(tilted_x_axis,tilted_y_axis,tilt_x_label,tilt_y_label)

        arc_angle2 = Angle(w_eb,dotted_line,radius=1.35)
        theta2 = Tex(r"$\theta$").scale(0.75).move_to(1.25*DOWN+0.25*RIGHT)

        n_pb = Vector(color=BLUE_D).put_start_and_end_on(box.get_center(),
                                                         box.get_center()-1.4*(RIGHT*np.cos(dotted_angle)+UP*np.sin(dotted_angle)))
        n_pb_label = Tex(r"$\vec{N}_{PB}$",color=BLUE_D).next_to(n_pb.get_end(),UP)

        no_friction_net_force = Vector(color=PURPLE).put_start_and_end_on(box.get_center(),
                                                                          box.get_center()-1.4*(RIGHT*np.cos(dotted_angle)+UP*np.sin(dotted_angle))+1.33*DOWN)

        f_pb = Vector(color=GREEN).put_start_and_end_on(box.get_center(),box.get_center()+0.75*(RIGHT*np.cos(dotted2_angle)+UP*np.sin(dotted2_angle)))

        f_pb_label1 = Tex(r"$\vec{f}_{PB}$",color=GREEN).next_to(f_pb.get_end(),UR).shift(0.15*DL)

        friction_propto1 = MathTex("{f}",r"\propto","{N}").scale(1.5).to_edge(UL).shift(0.5*RIGHT)
        friction_equals1 = MathTex("{f}","=",r"\mu_s","{N}").scale(1.5).to_edge(UL).shift(0.5*RIGHT)
        friction_equals2 = MathTex("{f}",r"\leq",r"\mu_s","{N}").scale(1.5).to_edge(UL).shift(0.5*RIGHT)

        sum_force_y1 = MathTex(r"\sum","{F}_y","=","{N}_{PB}","-","{W}_{EB}",r"\cos(\theta)","=","{m}_b","{a}_{b,y}").next_to(friction_equals2,DOWN).to_edge(LEFT)
        sum_force_y2 =  MathTex(r"\sum","{F}_y","=","{N}_{PB}","-","{W}_{EB}",r"\cos(\theta)","=","0").next_to(friction_equals2,DOWN).to_edge(LEFT)
        sum_force_y3 = MathTex("{N}_{PB}","=","{W}_{EB}",r"\cos(\theta)").next_to(friction_equals2,DOWN).to_edge(LEFT)

        sum_force_x1 = MathTex(r"\sum","{F}_x","=","{W}_{EB}",r"\sin(\theta)","-","{f}_{PB}","=","{m}_b","{a}_{b,y}").next_to(sum_force_y3,DOWN).to_edge(LEFT)
        sum_force_x2 = MathTex("{W}_{EB}",r"\sin(\theta)","-","{f}_{PB}","=","0").next_to(sum_force_y3,DOWN).to_edge(LEFT)
        sum_force_x3 = MathTex("{W}_{EB}",r"\sin(\theta)","=","{f}_{PB}").next_to(sum_force_y3,DOWN).to_edge(LEFT)
        sum_force_x4 = MathTex("{W}_{EB}",r"\sin(\theta)","=",r"\mu_s","{N}").next_to(sum_force_y3,DOWN).to_edge(LEFT)

        set_math_colors(friction_propto1,friction_equals1,friction_equals2,sum_force_y1,sum_force_y2,sum_force_y3,sum_force_x1,sum_force_x2,sum_force_x3,sum_force_x4)

        # self.add(plane,arc_angle,theta,box,w_eb,w_eb_label,dotted_line,arc_angle2,theta2,right_angle,dotted_line2,right_angle2,tilted_axes,
                #  n_pb,n_pb_label,no_friction_net_force,w_eb_dotted,f_pb,f_pb_label1)
        self.play(Write(plane),Write(box),Write(arc_angle),FadeIn(theta,right_angle))
        self.wait()
        self.play(Write(dotted_line),Write(dotted_line2),Write(arc_angle2),FadeIn(theta2,right_angle2),Write(w_eb),Write(w_eb_dotted),FadeIn(w_eb_label),lag_ratio=0.25,run_time=2)
        self.wait()
        self.play(Write(n_pb),FadeIn(n_pb_label))
        self.wait()
        self.play(Write(no_friction_net_force))
        self.wait()
        self.play(Write(f_pb),FadeIn(f_pb_label1),FadeOut(no_friction_net_force))
        self.wait()
        diagram_mobs = VGroup(plane,box,arc_angle,theta,right_angle,dotted_line,dotted_line2,arc_angle2,theta2,right_angle2,w_eb,w_eb_label,w_eb_dotted,w_eb_label,
                                n_pb,n_pb_label,f_pb,f_pb_label1)
        self.play(diagram_mobs.animate.to_edge(DR).shift(0.25*UL))
        self.wait()
        self.play(Write(friction_propto1))
        self.wait()
        self.play(Transform(friction_propto1,friction_equals1))
        self.wait()
        self.play(Transform(friction_propto1,friction_equals2))
        self.wait()
        self.play(Write(tilted_axes.shift(1.25*DOWN+2.35*RIGHT)))
        self.wait()
        self.play(Write(sum_force_y1))
        self.wait()
        self.play(Transform(sum_force_y1,sum_force_y2))
        self.wait()
        self.play(Transform(sum_force_y1,sum_force_y3))
        self.wait()
        self.play(Write(sum_force_x1))
        self.wait()
        self.play(Transform(sum_force_x1,sum_force_x2))
        self.wait()
        self.play(Transform(sum_force_x1,sum_force_x3))
        self.play(Transform(sum_force_x1,sum_force_x4))
        self.wait()

class FrictionZoomedIn(Scene):
    def construct(self):
        top_surface = ImageMobject("img/top-bumpy-surface.png").shift(5*UP)
        bottom_surface = ImageMobject("img/bottom-bumpy-surface.png").shift(5*DOWN)
        
        self.play(FadeIn(top_surface,bottom_surface))
        self.play(top_surface.animate.shift(5*DOWN),bottom_surface.animate.shift(5*UP))
        self.wait()
        self.play(FadeOut(top_surface,bottom_surface))
        self.wait()

class PushBoxStaticKinetic(Scene):
    def construct(self):
        stick_man = SVGMobject("img/stick-man-push.svg").shift(0.5*LEFT)
        block = Square().next_to(stick_man,RIGHT,buff=0)
        block_vector = Vector(color=BLUE).put_start_and_end_on(block.get_center(),block.get_center()+2*RIGHT)
        ground = Line(start=DOWN+7*LEFT,end=DOWN+7*RIGHT).set_opacity(0.5)

        block_group = VGroup(block,block_vector,stick_man)
        
        self.play(Write(stick_man),Write(block),Write(ground),FadeIn(block_vector))
        self.wait()
        self.play(block_group.animate.shift(5*RIGHT),rate_func=rate_functions.ease_in_out_expo,run_time=5)
        self.play(FadeOut(block_vector))
        self.wait()

class FrictionGraph(Scene):
    def construct(self):
        ax = Axes(
            x_range = [0,10,1],
            y_range = [0,5,1],
            tips=False
        )

        ax_labels = ax.get_axis_labels(x_label = Text("Force"),y_label = Text("Friction"))

        constant_line = ax.plot(lambda x: x, x_range=[0,4],color=GREEN)
        kinetic_line = ax.plot(lambda x: (1/(x-3.5))+2,x_range=[4,10],color=GREEN)

        dotted_lines = VGroup(DashedLine(start=ax.c2p(4,0,0),end=ax.c2p(4,5,0)),
                              DashedLine(start=ax.c2p(0,4,0),end=ax.c2p(4,4,0)))

        f_s_max = MathTex("f_{s,max}","=",r"\mu_s","{N}").next_to(ax.c2p(0,4,0),DR)
        label_line_fs = Line(start=ax.c2p(0,4,0),end=ax.c2p(0,4,0)+0.35*DR,buff=0.1)

        force_equal_friction = MathTex("f_s","=","F").rotate(PI/4).move_to(constant_line).shift(0.5*UP)

        f_k_arrow = DoubleArrow(start=ax.c2p(7,0,0),end=ax.c2p(7,0,0)+2.75*UP)
        f_k_equation = MathTex("f_k","=",r"\mu_k","{N}").next_to(f_k_arrow,LEFT)

        set_math_colors(f_s_max,f_k_equation)

        f_s_max.set_color_by_tex("f_",GREEN)
        f_k_equation.set_color_by_tex("f_",GREEN)

        force_equal_friction.set_color_by_tex("f_s",GREEN)
        force_equal_friction.set_color_by_tex("F",RED)

        self.play(Write(ax),Write(ax_labels))
        self.play(Write(constant_line),Write(f_s_max),FadeIn(label_line_fs),Write(force_equal_friction),Write(dotted_lines))
        self.play(Write(kinetic_line),Write(f_k_arrow),Write(f_k_equation))
        self.wait(2)

class HookesLaw(Scene):
    def construct(self):
        header = Text("Hooke's Law").scale(1.25)

        hookes_law = MathTex("{F}_{sp}","=","-","{k}",r"\Delta {x}").scale(1.5).next_to(header.copy().to_edge(UP),DOWN).shift(0.5*DOWN)
        hookes_law2 = MathTex("{F}_{sp}","=","-","(5",r"\frac{N}{m}",")",r"\Delta {x}").scale(1.5).next_to(header.copy().to_edge(UP),DOWN).shift(0.5*DOWN)
        hookes_law3 = MathTex("{F}_{sp}","=","-","(5",r"\frac{N}{m}",")","(+2m)").scale(1.5).next_to(header.copy().to_edge(UP),DOWN).shift(0.5*DOWN)
        hookes_law4 = MathTex("{F}_{sp}","=","-","10 N").scale(1.5).next_to(header.copy().to_edge(UP),DOWN).shift(0.5*DOWN)

        set_math_colors(hookes_law,hookes_law2,hookes_law3,hookes_law4)
            
        spring_coil = resistor.Resistor(bounding_rect=Square())
        spring = VGroup(Line(start=spring_coil.get_start_pos()+LEFT,end=spring_coil.get_start_pos()),
                        Line(start=spring_coil.get_end_pos(),end=spring_coil.get_end_pos()+RIGHT),
                        Dot(spring_coil.get_start_pos()+LEFT,color=WHITE),
                        Dot(spring_coil.get_end_pos()+RIGHT,color=WHITE),
                        spring_coil.image).shift(DOWN)

        spring_coil_stretched = resistor.Resistor(bounding_rect=Rectangle(color=WHITE,height=2,width=3))
        spring_stretched = VGroup(Line(start=spring_coil_stretched.get_start_pos()+LEFT,end=spring_coil_stretched.get_start_pos()),
                                  Line(start=spring_coil_stretched.get_end_pos(),end=spring_coil_stretched.get_end_pos()+RIGHT),
                                  Dot(spring_coil_stretched.get_start_pos()+LEFT,color=WHITE),
                                  Dot(spring_coil_stretched.get_end_pos()+RIGHT,color=WHITE),
                                  spring_coil_stretched.image).shift(DOWN+0.5*RIGHT)

        dotted_lines = VGroup(DashedLine(start=2*LEFT,end=2*DL),DashedLine(start=2*RIGHT,end=2*DR),
                              DashedLine(start=3*RIGHT,end=3*RIGHT+2*DOWN))

        delta_x_brace = Brace(Square(side_length=1),DOWN).shift(1.5*DOWN+2.5*RIGHT)
        delta_x = Tex(r"$\Delta x$",color=RED).next_to(delta_x_brace,DOWN)

        spring_force_vector = Vector(color=RED).put_start_and_end_on(3*RIGHT+DOWN,2*RIGHT+DOWN)

        self.play(Write(spring))
        self.wait()
        self.play(Write(header.shift(UP)))
        self.play(header.animate.to_edge(UP))
        self.play(Write(hookes_law))
        self.wait()
        self.play(Transform(hookes_law,hookes_law2))
        self.wait()
        self.play(Write(dotted_lines[0:2]))
        self.play(Transform(spring,spring_stretched),Write(dotted_lines[2]),FadeIn(delta_x_brace,delta_x),
                  Transform(hookes_law,hookes_law3))
        self.wait()
        self.play(Transform(hookes_law,hookes_law4),Write(spring_force_vector))
        self.wait()

gravity_acceleration = 9.81

class Node():
    def __init__(self,mass=1,position=ORIGIN,is_fixed = False,drag=.7):
        self.mass = mass
        self.is_fixed = is_fixed

        self.position = np.array([position[0],position[1]])
        self.velocity = np.array([0.0,0.0])
        self.acceleration = np.array([0.0,0.0])
        self.drag = drag

        self.springs = []

        self.image = Dot(color=WHITE).move_to(np.array([self.position[0],self.position[1],0]))

    def add_spring(self, spring):
        self.springs.append(spring)

    # returns manim position
    def get_position(self):
        return np.array([self.position[0],self.position[1],0])
    
    def update(self,delta_time):
        if (self.is_fixed):
            return
        
        self.velocity += self.acceleration * (delta_time/2)
        self.position += self.velocity*delta_time

        self.acceleration = np.array([0.0,0.0])
        # gravity
        self.acceleration += np.array([0,-self.mass*gravity_acceleration])
        # drag
        velocity_magnitude = np.linalg.norm(self.velocity)
        
        # don't divide by zero
        if velocity_magnitude != 0:
            velocity_unit = self.velocity * (1 / velocity_magnitude)
            self.acceleration += -self.drag*(velocity_magnitude**2)*velocity_unit

        # spring forces
        for spring in self.springs:
            self.acceleration += (1/self.mass)*spring.get_force(self.get_position())
        
        self.velocity += self.acceleration*(delta_time/2)
    
    def draw(self):
        self.image.move_to(np.array([self.position[0],self.position[1],0]))

class Spring():
    def __init__(self,node_a,node_b,k=1,rest_length=1,max_force=10000):
        self.k = k
        self.rest_length = rest_length
        self.node_a = node_a
        self.node_b = node_b
        self.max_force = max_force

        self.image = Line(start=self.node_a.get_position(),end=self.node_b.get_position())

    def get_force(self, position):
        if np.array_equal(position, self.node_a.get_position()):
            a_to_b = self.node_b.get_position() - self.node_a.get_position()
            a_to_b_mag = np.linalg.norm(a_to_b)
            a_to_b_unit = a_to_b / a_to_b_mag

            force = self.k * (a_to_b_mag - self.rest_length) * a_to_b_unit
            force_magnitude = np.linalg.norm(force)
            if force_magnitude > self.max_force:
                force = (self.max_force / force_magnitude) * force
            return force[:2]  # Return only the 2D component

        elif np.array_equal(position, self.node_b.get_position()):
            b_to_a = self.node_a.get_position() - self.node_b.get_position()
            b_to_a_mag = np.linalg.norm(b_to_a)
            b_to_a_unit = b_to_a / b_to_a_mag

            force = self.k * (b_to_a_mag - self.rest_length) * b_to_a_unit
            force_magnitude = np.linalg.norm(force)
            if force_magnitude > self.max_force:
                force = (self.max_force / force_magnitude) * force
            return force[:2]

        return np.array([0.0, 0.0])

    def draw(self):
        self.image.put_start_and_end_on(start=self.node_a.get_position(),end=self.node_b.get_position())


class RopeTest(MovingCameraScene):
    def construct(self):
        framerate = 30
        run_time = 3

        # nodes = [Node(mass=1,position=ORIGIN,is_fixed=True),
                #  Node(mass=5,position=RIGHT,is_fixed=False),
                #  Node(mass=5,position=2*RIGHT,is_fixed=False)]
        nodes = []
        
        rope_length = 1
        num_segments = 20
        nodes.append(Node(mass=1,position=ORIGIN,is_fixed=True))
        for i in range(num_segments-1):
            nodes.append(Node(mass=3,position=(i+1)*RIGHT*rope_length/num_segments,is_fixed=False))

        # springs = [Spring(nodes[0],nodes[1],k=2000,rest_length=1),
                #    Spring(nodes[1],nodes[2],k=2050,rest_length=1.5)]
        springs = []

        for i in range(len(nodes)-1):
            springs.append(Spring(nodes[i],nodes[i+1],k=1000,rest_length=rope_length/num_segments))
        
        for i in range(len(nodes)-1):
            nodes[i].add_spring(springs[i])
            nodes[i+1].add_spring(springs[i])


        box = Square(color=BLUE,side_length=1).move_to(nodes[-1].get_position())

        self.play(*[FadeIn(node.image) for node in nodes],*[FadeIn(spring.image) for spring in springs],Write(box))
        self.play(self.camera.frame.animate.scale(4))
        
        for i in range(round(framerate*run_time)):
            # update
            for node in nodes:
                node.update(1/framerate)

            # draw
            for spring in springs:
                spring.draw()
            for node in nodes:
                node.draw()
            
            box.move_to(nodes[-1].get_position())

            # print(nodes[-1].acceleration)
            
            self.wait(1/framerate)

class RopeIntro(Scene):
    def construct(self):
        header = Text("Ropes").scale(1.5).to_edge(UP)
        rope1 = Line(start=3*LEFT,end=3*RIGHT,color=DARK_BROWN)

        rope2 = Line(start=4*UP,end=2*UP,color=DARK_BROWN)
        block_a = Square(side_length=1.5,color=BLUE).shift(1.25*UP)
        rope3 = Line(start=0.5*UP,end=1.5*DOWN,color=DARK_BROWN)
        block_b = Square(side_length=1.5,color=RED).shift(2.25*DOWN)

        block_a_label = Tex("$A$",color=BLUE).move_to(block_a)
        block_b_label = Tex("$B$",color=RED).move_to(block_b)
        
        block_a_dot = Dot(color=BLUE).move_to(block_a)
        block_b_dot = Dot(color=RED).move_to(block_b)

        w_eb = Vector(color=RED).put_start_and_end_on(block_b.get_center(),block_b.get_center()+1.25*DOWN)
        w_eb_label = Tex("$W_{EB}$",color=RED_B).scale(0.5).next_to(w_eb,RIGHT,buff=0.05).shift(0.1*UP)

        t_ab = Vector(color=PURPLE).put_start_and_end_on(block_b.get_center(),block_b.get_center()+1.25*UP)
        t_ab_label = Tex("$T_{AB}$",color=PURPLE).scale(0.5).next_to(t_ab,RIGHT,buff=0.05).shift(0.1*DOWN)

        solve_tension_b = VGroup(MathTex(r"\sum","{F}_y","=","0","=","{T}_{AB}","-","{W}_{EB}"),
                                 MathTex("{T}_{AB}","=","{W}_{EB}","=","{m}_b","{g}")).scale(0.75).arrange(DOWN)
        set_math_colors(solve_tension_b[0],solve_tension_b[1])

        w_ea = Vector(color=BLUE).put_start_and_end_on(block_a.get_center(),block_a.get_center()+1.25*DOWN).shift(0.05*RIGHT)
        w_ea_label = Tex("$W_{EA}$",color=BLUE_B).scale(0.5).next_to(w_ea,RIGHT,buff=0.05).shift(0.1*UP+0.05*LEFT)

        t_ca = Vector(color=PURPLE).put_start_and_end_on(block_a.get_center(),block_a.get_center()+1.25*UP)
        t_ca_label = Tex("$T_{CA}$",color=PURPLE).scale(0.5).next_to(t_ca,RIGHT,buff=0.05).shift(0.1*DOWN)

        t_ba = Vector(color=PURPLE).put_start_and_end_on(block_a.get_center(),block_a.get_center()+1.25*DOWN).shift(0.05*LEFT)
        t_ba_label = Tex("$T_{BA}$",color=PURPLE).scale(0.5).next_to(t_ba,LEFT,buff=0.05).shift(0.1*UP+0.05*RIGHT)

        self.play(Write(header),Write(rope1))
        self.wait()
        self.play(FadeOut(header),Transform(rope1,rope2),Write(rope3),Write(block_a),Write(block_b),FadeIn(block_a_label,block_b_label))
        self.wait()
        self.play(block_a_label.animate.shift(1.5*RIGHT),block_b_label.animate.shift(1.5*RIGHT))
        self.wait()
        self.play(Write(block_b_dot),Write(w_eb),FadeIn(w_eb_label))
        self.wait()
        self.play(Write(t_ab),FadeIn(t_ab_label))
        self.wait()
        self.play(Write(solve_tension_b.next_to(block_b_label,RIGHT).to_edge(RIGHT)),run_time=2)
        self.wait(2)
        self.play(Write(block_a_dot),Write(w_ea),FadeIn(w_ea_label))
        self.wait()
        self.play(Write(t_ca),FadeIn(t_ca_label))
        self.wait()
        self.play(Write(t_ba),FadeIn(t_ba_label))
        self.wait(2)

class RopePulley(Scene):
    def construct(self):
        pulley_circ = Circle(radius=0.75,color=WHITE).shift(3.5*RIGHT+2*UP).set_z_index(5)
        pulley_dot = Dot(color=WHITE).move_to(pulley_circ).set_z_index(5)
        pulley_hang1 = Line(start=pulley_dot.get_center(),end=pulley_dot.get_center()+3*UR,color=GREY)
        pulley_hang2 = Line(start=pulley_dot.get_center(),end=pulley_dot.get_center()+3*UL,color=GREY)

        pulley = VGroup(pulley_circ,pulley_dot,pulley_hang1,pulley_hang2)

        wall = Rectangle(width=4,height=10,color=GREY).set_fill(color=color_gradient([GRAY,BLACK],2),opacity=0.75)
        wall.shift(5.5*LEFT)

        rope1 = Line(start=3.5*LEFT+2.75*UP,end=3.5*RIGHT+2.75*UP,color=DARK_BROWN)
        rope2 = Line(start=4.25*RIGHT+2*UP,end=4.25*RIGHT+DOWN,color=DARK_BROWN)

        block = Square(side_length=1.5,color=BLUE).shift(1.75*DOWN+4.25*RIGHT)
        block_dot = Dot(color=WHITE).move_to(block).set_z_index(5)

        vectors = VGroup(Vector(color=RED).put_start_and_end_on(block.get_center(),block.get_center()+1.25*DOWN),
                         Vector(color=PURPLE).put_start_and_end_on(rope1.get_end()+LEFT,rope1.get_end()+2*LEFT),
                         Vector(color=PURPLE).put_start_and_end_on(rope2.get_start()+0.5*DOWN,rope2.get_start()+1.5*DOWN),
                         Vector(color=PURPLE).put_start_and_end_on(block.get_center(),block.get_center()+1.25*UP),
                         Vector(color=PURPLE).put_start_and_end_on(3.5*LEFT+2.75*UP,2.5*LEFT+2.75*UP))

        self.play(Write(wall),Write(pulley),Write(rope1),Write(rope2),Write(block))
        self.wait()
        self.play(Write(block_dot),FadeIn(vectors))
        self.wait()

class Centripetal(Scene):
    def construct(self):
        circle_angle = ValueTracker(0.01)
        circle_origin = Dot()
        circle_radius = 3

        rope = Line(start=circle_origin.get_center(),end=circle_origin.get_center()+circle_radius*RIGHT,color=DARK_BROWN).add_updater(lambda mob: mob.put_start_and_end_on(circle_origin.get_center(), circle_origin.get_center()+circle_radius*np.cos(circle_angle.get_value())*RIGHT+circle_radius*np.sin(circle_angle.get_value())*UP))
        circle_arc = always_redraw(lambda: Arc(radius=circle_radius,start_angle=0,angle=circle_angle.get_value()).move_arc_center_to(circle_origin.get_center()))
        block = always_redraw(lambda: Square(side_length=1.5,color=BLUE).move_to(rope.get_end()).rotate(circle_angle.get_value()))
        block_dot = Dot().set_z_index(5).add_updater(lambda mob: mob.move_to(block.get_center()))

        centripetal_acceleration = MathTex("{a}","=","{{v}^2",r"\over","{r}}").to_edge(UL).shift(RIGHT)
        centripetal_force = MathTex("{F}","=","{m}","{{v}^2",r"\over","{r}}").next_to(centripetal_acceleration,DOWN)
        centripetal_force2 = MathTex("{F}","=","(5 kg)",r"{(10 \frac{m}{s})^2",r"\over","2 m}").move_to(centripetal_force)
        centripetal_force3 = MathTex("{F}","=","250 N").move_to(centripetal_force)

        set_math_colors(centripetal_acceleration,centripetal_force)
        centripetal_force2.set_color_by_tex("{F}",RED)
        centripetal_force3.set_color_by_tex("{F}",RED)

        self.play(Write(rope),Write(block),Write(block_dot))
        self.add(circle_arc)
        self.play(circle_angle.animate.set_value(2*PI),rate_func=rate_functions.smooth,run_time=1.5)
        self.wait()
        self.play(Write(centripetal_acceleration))
        self.wait()
        self.play(Write(centripetal_force))
        self.wait()
        self.play(Transform(centripetal_force,centripetal_force2))
        self.wait()
        self.play(Transform(centripetal_force,centripetal_force3))
        self.wait()
