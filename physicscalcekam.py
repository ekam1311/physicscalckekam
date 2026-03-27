#!/usr/bin/env python3
try:
    import sympy as sp
    SYMPY_AVAILABLE = True
except Exception:
    SYMPY_AVAILABLE = False

def pause():
    input("\nPress Enter to continue...")

def kinematics_menu():
    print("\nKINEMATICS CALCULATOR")
    print("1) Given u, a, t -> find v and s")
    print("2) Given u, v, a -> find s (v^2 = u^2 + 2as)")
    print("3) Given s, u, t -> find a")
    print("0) Back")
    choice = input("Choose: ").strip()
    if choice == "1":
        u = float(input("Initial velocity u (m/s): "))
        a = float(input("Acceleration a (m/s^2): "))
        t = float(input("Time t (s): "))
        v = u + a * t
        s = u * t + 0.5 * a * t**2
        print(f"\nFinal velocity v = {v:.4f} m/s")
        print(f"Displacement s = {s:.4f} m")
    elif choice == "2":
        u = float(input("Initial velocity u (m/s): "))
        v = float(input("Final velocity v (m/s): "))
        a = float(input("Acceleration a (m/s^2): "))
        s = (v**2 - u**2) / (2 * a) if a != 0 else float('inf')
        print(f"\nDisplacement s = {s:.4f} m")
    elif choice == "3":
        s = float(input("Displacement s (m): "))
        u = float(input("Initial velocity u (m/s): "))
        t = float(input("Time t (s): "))
        a = (2 * (s - u * t)) / (t**2) if t != 0 else float('inf')
        print(f"\nAcceleration a = {a:.4f} m/s^2")
    else:
        return

def projectile_menu():
    print("\nPROJECTILE MOTION CALCULATOR")
    print("1) Given speed and angle -> time of flight, range, max height")
    print("2) Given initial vertical velocity -> max height and time to reach it")
    print("0) Back")
    g = 9.80665  # m/s^2
    choice = input("Choose: ").strip()
    if choice == "1":
        v0 = float(input("Initial speed v0 (m/s): "))
        angle_deg = float(input("Launch angle (degrees): "))
        theta = math.radians(angle_deg)
        vx = v0 * math.cos(theta)
        vy = v0 * math.sin(theta)
        time_of_flight = 2 * vy / g
        range_ = vx * time_of_flight
        max_height = (vy**2) / (2 * g)
        print(f"\nTime of flight = {time_of_flight:.4f} s")
        print(f"Range = {range_:.4f} m")
        print(f"Max height = {max_height:.4f} m")
    elif choice == "2":
        vy = float(input("Initial vertical speed vy (m/s): "))
        time_to_top = vy / g
        max_height = (vy**2) / (2 * g)
        print(f"\nTime to reach max height = {time_to_top:.4f} s")
        print(f"Max height = {max_height:.4f} m")
    else:
        return

def circular_motion():
    print("\nCIRCULAR MOTION")
    v = float(input("Tangential speed v (m/s): "))
    r = float(input("Radius r (m): "))
    a_c = v**2 / r if r != 0 else float('inf')
    print(f"\nCentripetal acceleration = {a_c:.4f} m/s^2")

def vectors_menu():
    print("\nVECTOR CALCULATOR")
    print("1) Dot product of two 3D vectors")
    print("2) Magnitude of a vector")
    print("0) Back")
    choice = input("Choose: ").strip()
    if choice == "1":
        print("Enter vector A (ax ay az) separated by spaces:")
        ax, ay, az = map(float, input().split())
        print("Enter vector B (bx by bz) separated by spaces:")
        bx, by, bz = map(float, input().split())
        dot = ax*bx + ay*by + az*bz
        print(f"\nDot product A·B = {dot:.4f}")
    elif choice == "2":
        print("Enter vector (x y z) separated by spaces:")
        x, y, z = map(float, input().split())
        mag = math.sqrt(x*x + y*y + z*z)
        print(f"\nMagnitude = {mag:.4f}")
    else:
        return

def calculus_helper():
    if not SYMPY_AVAILABLE:
        print("\nCalculus helper requires sympy (optional).")
        print("To install: pip install sympy")
        print("Sympy not detected — returning to main menu.")
        return
    print("\nCALCULUS HELPER (symbolic)")
    print("1) Derivative of a position function x(t) -> velocity v(t)")
    print("2) Integral example: integrate v(t) to get displacement")
    print("0) Back")
    choice = input("Choose: ").strip()
    if choice == "1":
        t = sp.symbols('t')
        expr_str = input("Enter x(t) using 't' (e.g. 5*t**2 + 3*t):\n")
        try:
            expr = sp.sympify(expr_str)
            deriv = sp.diff(expr, t)
            print(f"\nx(t) = {expr}")
            print(f"v(t) = dx/dt = {deriv}")
        except Exception as e:
            print("Invalid expression:", e)
    elif choice == "2":
        t = sp.symbols('t')
        expr_str = input("Enter v(t) to integrate (e.g. 10*t):\n")
        try:
            expr = sp.sympify(expr_str)
            integ = sp.integrate(expr, t)
            print(f"\nv(t) = {expr}")
            print(f"Integral ∫v(t) dt = {integ} + C")
        except Exception as e:
            print("Invalid expression:", e)
    else:
        return

def main_menu():
    while True:
        print("\n=== PHYSICS FORMULA CALCULATOR ===")
        print("1) Kinematics")
        print("2) Projectile motion")
        print("3) Circular motion")
        print("4) Vector operations")
        print("5) Calculus helper (optional: sympy)")
        print("0) Exit")
        choice = input("Choose an option: ").strip()
        if choice == "1":
            kinematics_menu()
            pause()
        elif choice == "2":
            projectile_menu()
            pause()
        elif choice == "3":
            circular_motion()
            pause()
        elif choice == "4":
            vectors_menu()
            pause()
        elif choice == "5":
            calculus_helper()
            pause()
        elif choice == "0":
            print("Goodbye — keep coding and solving problems!")
            sys.exit(0)
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main_menu()
