"""
رسم تبدیل فوریه‌ی خروجی فیلتر برای سوال ۱ (نمونه‌برداری از سیگنال متناوب).
خروجی: figs/1.png

Y(f) = 1/2 * sum_{f_i in {3,4,7,11,14,15}} [ delta(f - f_i) + delta(f + f_i) ]   (kHz)
"""

import os
import matplotlib.pyplot as plt

# فرکانس‌های باقی‌مانده پس از فیلتر ۱۶kHz (kHz) و مبدا هر کدام
survived = {3: 77, 4: 44, 7: 33, 11: 11, 14: 66, 15: 55}  # f_alias -> f_original
blocked = {18: 22}  # حذف‌شده توسط فیلتر (k=2)

height = 0.5  # ارتفاع هر ضربه (دامنه‌ی کسینوس = ۱ -> ضربه‌ی ۱/۲)

fig, ax = plt.subplots(figsize=(10, 4.5))

# محور افقی و عمودی
ax.axhline(0, color="black", linewidth=1.0)
ax.axvline(0, color="black", linewidth=1.0)

# ضربه‌های باقی‌مانده در ±f_i
for f in survived:
    for sgn in (+1, -1):
        ax.annotate(
            "", xy=(sgn * f, height), xytext=(sgn * f, 0),
            arrowprops=dict(arrowstyle="->", color="C0", lw=2),
        )
    ax.text(f, height + 0.04, f"{f}", ha="center", va="bottom", fontsize=9, color="C0")
    ax.text(-f, height + 0.04, f"-{f}", ha="center", va="bottom", fontsize=9, color="C0")

# نمایش مولفه‌ی حذف‌شده با خط‌چین کم‌رنگ (اختیاری، برای وضوح)
for f in blocked:
    for sgn in (+1, -1):
        ax.annotate(
            "", xy=(sgn * f, height), xytext=(sgn * f, 0),
            arrowprops=dict(arrowstyle="->", color="0.7", lw=1.5, linestyle=(0, (4, 3))),
        )
    ax.text(f, height + 0.04, f"{f} (blocked)", ha="center", va="bottom",
            fontsize=8, color="0.6")
    ax.text(-f, height + 0.04, f"-{f}", ha="center", va="bottom", fontsize=8, color="0.6")

# مرز فیلتر پایین‌گذر ۱۶kHz
for fc in (+16, -16):
    ax.axvline(fc, color="red", linestyle=":", linewidth=1.2)
ax.text(16, height + 0.18, "filter cutoff = 16 kHz", ha="center", color="red", fontsize=8)

ax.set_xlim(-22, 22)
ax.set_ylim(-0.12, height + 0.32)
ax.set_xlabel("f (kHz)")
ax.set_ylabel("Y(f)")
# ax.set_title(r"Output spectrum  $Y(f)=\frac{1}{2}\sum \delta(f\mp f_i)$")
ax.set_xticks(sorted([0] + [s * f for f in survived for s in (1, -1)]))
ax.set_yticks([0, height])
ax.set_yticklabels(["0", "1/2"])
ax.grid(axis="x", linestyle="--", alpha=0.25)

plt.tight_layout()
out = os.path.join(os.path.dirname(__file__), "1.png")
plt.savefig(out, dpi=200)
print(f"saved: {out}")
