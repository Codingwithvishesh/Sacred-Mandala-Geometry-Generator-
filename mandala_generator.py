import turtle
import math
import colorsys

# --- Fullscreen & High-Contrast Setup ---
screen = turtle.Screen()
screen.setup(width=1.0, height=1.0)
screen.bgcolor("#000000")  # Pure AMOLED Pitch Black
screen.title("Day 08: Ultra-Complex Sacred Mandala Engine - Coding With Vishesh")

try:
    canvas = screen.getcanvas()
    root = canvas.winfo_toplevel()
    root.state('zoomed')
except Exception:
    pass

screen.tracer(0)  # Smooth 60 FPS Render Engine

t = turtle.Turtle()
t.hideturtle()
t.speed(0)

# System Parameters
SECTORS = 24          # Ultra-high density 24-fold rotational symmetry
TOTAL_FRAMES = 900    # Exactly ~30 Seconds at 30 FPS

for frame in range(TOTAL_FRAMES):
    t.clear()
    
    # Global Kinetic Motion Modulators
    rot_cw = frame * 0.012     # Clockwise phase
    rot_ccw = -frame * 0.016   # Counter-clockwise phase
    expansion = min(1.0, (frame + 10) / 250.0)
    pulse = 1.0 + 0.12 * math.sin(frame * 0.09)
    
    # 1. Central Pulsing Singularity Core
    t.penup()
    t.goto(0, 0)
    t.dot(int(42 * pulse * expansion), "#ffd700")  # Pure Gold Core
    t.dot(int(26 * pulse * expansion), "#ff0055")  # Laser Pink Accent
    t.dot(int(12 * pulse * expansion), "#00f0ff")  # Electric Cyan Core Center
    t.dot(int(4 * pulse * expansion), "#ffffff")   # White Hot Center
    
    NUM_LAYERS = 9
    
    for layer in range(1, NUM_LAYERS + 1):
        # Counter-rotating Layer Mechanics
        layer_rot = rot_cw if layer % 2 == 1 else rot_ccw
        base_radius = layer * 42 * expansion * pulse
        
        # --- ULTRA-VIBRANT HSV COLOR PIPELINE ---
        hue = (0.72 + (layer * 0.07) + frame * 0.0035) % 1.0
        
        if layer % 4 == 0:
            rgb = colorsys.hsv_to_rgb(0.13, 1.0, 1.0)  # Pure Radiant Gold
        elif layer % 4 == 1:
            rgb = colorsys.hsv_to_rgb(0.52, 1.0, 1.0)  # Electric Cyan
        elif layer % 4 == 2:
            rgb = colorsys.hsv_to_rgb(hue, 1.0, 1.0)   # Deep Electric Violet / Purple
        else:
            rgb = colorsys.hsv_to_rgb(0.95, 1.0, 1.0)  # Neon Laser Magenta
            
        t.pencolor(rgb)
        t.pensize(max(1, int(4.0 - layer * 0.3)))
        
        # 24-Sector Symmetry Transformation Loop
        for s in range(SECTORS):
            angle = (s / SECTORS) * 2 * math.pi + layer_rot
            
            # Primary Node (Cartesian Conversion)
            x1 = math.cos(angle) * base_radius
            y1 = math.sin(angle) * base_radius
            
            # Dynamic Wave Oscillation Morphing
            morph_wave = math.sin(s * 3 + frame * 0.12) * 22 * expansion
            petal_angle = angle + (math.pi / SECTORS)
            petal_radius = base_radius * 1.42 + morph_wave
            
            x2 = math.cos(petal_angle) * petal_radius
            y2 = math.sin(petal_angle) * petal_radius
            
            # Draw Interlocking Vector Web Lines
            t.penup()
            t.goto(x1, y1)
            t.pendown()
            t.goto(x2, y2)
            
            # Glowing Intersection Dots
            if frame > 80:
                dot_size = max(2, int((8 - layer * 0.6) * expansion))
                t.dot(dot_size, rgb)
            
            # Intersecting Star-Polygon Web Linkage (Skipping 3 Sectors)
            next_angle = ((s + 3) / SECTORS) * 2 * math.pi + layer_rot
            nx = math.cos(next_angle) * base_radius
            ny = math.sin(next_angle) * base_radius
            t.goto(nx, ny)
            
            # Radiating Inner Geometry Laser Rays
            if layer >= 6 and s % 2 == 0:
                t.pencolor("#ffffff")
                t.pensize(1)
                t.goto(x1 * 0.35, y1 * 0.35)
                t.pencolor(rgb)
                t.pensize(max(1, int(4.0 - layer * 0.3)))

    screen.update()

turtle.done()