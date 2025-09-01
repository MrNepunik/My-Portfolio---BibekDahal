# GPA system as list of tuples (min_mark, max_mark, grade, GP)
gpa_system = [
    (90, 100, "A+", 4.0),
    (80, 89, "A", 3.6),
    (70, 79, "B+", 3.2),
    (60, 69, "B", 2.8),
    (50, 59, "C+", 2.4),
    (40, 49, "C", 2.0),
    (0, 39, "F", 0.0)
]

# Class input
a = int(input("Enter your class (9-12): "))

if a == 9 or a == 10:
    print("Enter your marks")
    g = int(input("Nepali: "))
    h = int(input("English: "))
    i = int(input("Science: "))
    j = int(input("C.Maths: "))
    k = int(input("Social Studies: "))
    l = int(input("Optional I (O.Maths/ Economics): "))
    m = int(input("Optional II (Account/ Computer): "))

    marks = [g, h, i, j, k, l, m]

elif a >= 11:
    b = input("Enter your faculty/stream (science or management): ").lower()

    if b == "science":
        c = input("Choose subject (biology or computer): ").lower()
        if c == "biology":
            print("Enter your marks")
            n = int(input("Nepali: "))
            o = int(input("English: "))
            p = int(input("Physics: "))
            q = int(input("Chemistry: "))
            r = int(input("Biology: "))
            s = int(input("Maths: "))
            marks = [n, o, p, q, r, s]
        else:
            print("Enter your marks")
            t = int(input("Nepali: "))
            u = int(input("English: "))
            v = int(input("Physics: "))
            w = int(input("Chemistry: "))
            x = int(input("Computer: "))
            y = int(input("Maths: "))
            marks = [t, u, v, w, x, y]

    elif b == "management":
        d = input("Choose HM or CS or BS: ").lower()
        if d == "hm":
            print("Enter your marks")
            z = int(input("Nepali: "))
            A = int(input("English: "))
            B = int(input("HM: "))
            C = int(input("Social: "))
            D = int(input("Account: "))
            E = int(input("Economics: "))
            marks = [z, A, B, C, D, E]
        elif d == "cs":
            print("Enter your marks")
            F = int(input("Nepali: "))
            G = int(input("English: "))
            K = int(input("Maths/Social: "))
            H = int(input("Account: "))
            M = int(input("Economics: "))
            N = int(input("CS: "))
            marks = [F, G, K, H, M, N]
        else:
            print("Enter your marks")
            O = int(input("Nepali: "))
            P = int(input("English: "))
            Q = int(input("Social: "))
            R = int(input("Account: "))
            S = int(input("Economics: "))
            T = int(input("BS: "))
            marks = [O, P, Q, R, S, T]

# Common code to calculate GPA and percentage
total_gp = 0
print("\nSubject Marks -> GPA & Grade")
for mark in marks:
    for min_mark, max_mark, grade, gp in gpa_system:
        if min_mark <= mark <= max_mark:
            print(f"{mark} -> {gp} ({grade})")
            total_gp += gp
            break  # once matched, stop checking other ranges

# Calculate overall GPA
overall_gpa = total_gp / len(marks)
print(f"\nOverall GPA: {overall_gpa:.2f}")

# Calculate percentage
percentage = sum(marks) / len(marks)
print(f"Percentage: {percentage:.2f}%")
