"""
رسم طیف خروجی X_f(omega) برای سوال ۲، حالت K=1 و T=1.
خروجی: figs/2.png

سیستم: x_b(t)=x_a(t)cos(7*pi*t) -> نمونه‌برداری (T=1) -> ضربه -> LPF (cutoff = pi).
X_a(omega) = Lambda(omega/(7pi/2))  (مثلث، قله ۱، نیم‌پهنا 7pi/2).
رونوشت‌ها در گام omega_s=2pi؛ مراکز مثلث‌ها روی مضارب فرد pi. در باند [-pi,pi]
چهار مثلث (مراکز -3pi,-pi,pi,3pi) جمع می‌شوند => آلیاسینگ.
"""

import os
import math
import matplotlib.pyplot as plt

PI = math.pi
HALF = 3.5 * PI          # نیم‌پهنای هر مثلث = 7pi/2
PEAK = 0.5               # قله‌ی هر مثلث پس از مدولاسیون
CUTOFF = PI              # فرکانس قطع فیلتر (T=1)
CENTERS = [-3 * PI, -PI, PI, 3 * PI]   # مراکز موثر در باند پایه


def triangle(w, c):
    """یک مثلث با مرکز c، نیم‌پهنای HALF و قله‌ی PEAK."""
    return PEAK * max(0.0, 1.0 - abs(w - c) / HALF)


def Xf(w):
    """طیف خروجی فیلتر: جمع رونوشت‌ها، سپس برش با فیلتر پایین‌گذر."""
    if abs(w) > CUTOFF:
        return 0.0
    return sum(triangle(w, c) for c in CENTERS)


# نمونه‌برداری ریز برای رسم منحنی
N = 2000
ws = [(-1.6 * PI) + i * (3.2 * PI) / N for i in range(N + 1)]
ys = [Xf(w) for w in ws]

fig, ax = plt.subplots(figsize=(10, 4.5))
ax.axhline(0, color="black", linewidth=1.0)
ax.axvline(0, color="black", linewidth=1.0)

ax.plot(ws, ys, color="C0", lw=2.2, label=r"$X_f(\omega)$")
ax.fill_between(ws, ys, color="C0", alpha=0.15)

# خطوط راهنما برای مقادیر کلیدی 6/7 و 13/14
for val, txt in [(6 / 7, "6/7"), (13 / 14, "13/14")]:
    ax.axhline(val, color="0.6", linestyle="--", linewidth=0.8)
    ax.text(-1.55 * PI, val + 0.005, txt, color="0.4", fontsize=8, va="bottom")

# مرز فیلتر پایین‌گذر
for fc in (CUTOFF, -CUTOFF):
    ax.axvline(fc, color="red", linestyle=":", linewidth=1.2)
ax.text(CUTOFF, 0.02, r"$+\pi$", color="red", fontsize=9, ha="left", va="bottom")
ax.text(-CUTOFF, 0.02, r"$-\pi$", color="red", fontsize=9, ha="right", va="bottom")

ax.set_xlim(-1.6 * PI, 1.6 * PI)
ax.set_ylim(-0.08, 1.05)
ax.set_xlabel(r"$\omega$ (rad/s)")
ax.set_ylabel(r"$X_f(\omega)$")
ax.set_xticks([-PI, -PI / 2, 0, PI / 2, PI])
ax.set_xticklabels([r"$-\pi$", r"$-\pi/2$", "0", r"$\pi/2$", r"$\pi$"])
ax.grid(axis="x", linestyle="--", alpha=0.25)
ax.legend(loc="upper right")

plt.tight_layout()
out = os.path.join(os.path.dirname(__file__), "2.png")
plt.savefig(out, dpi=200)
print(f"saved: {out}")
