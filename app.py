import streamlit as st
import random

st.set_page_config(page_title="Lotto Max Picker", page_icon="🎲")
st.title("🎯 تولید ترکیب هوشمند برای Lotto Max")

# بخش ورود عددهای شخصی
st.markdown("### 🔢 عددهای شخصی خودتو وارد کن:")
user_input = st.text_input("مثلاً: 3, 12, 17, 27 (حداکثر 6 عدد)", value="3, 12, 17, 27")

# تبدیل ورودی به لیست عدد صحیح
def parse_input(text):
    try:
        numbers = [int(n.strip()) for n in text.split(",") if n.strip().isdigit()]
        return list(set([n for n in numbers if 1 <= n <= 50]))[:6]  # حداکثر 6 عدد، بین 1 تا 50
    except:
        return []

personal_numbers = parse_input(user_input)

st.markdown(f"**عددهای واردشده:** {personal_numbers}")

# گزینه نوع ترکیب
option = st.radio(
    "🎲 نوع انتخاب برای بقیه عددها:",
    ["اعداد داغ", "تصادفی از کل بازه", "ترکیب داغ و سرد"]
)

# تعریف اعداد داغ و سرد
hot_numbers = [2, 7, 19, 28, 36, 39, 46]
cold_numbers = [1, 4, 5, 8, 11, 13, 14, 30, 32, 33, 35, 42, 45, 48]

def generate_numbers(option, remaining_slots):
    available_numbers = list(set(range(1, 51)) - set(personal_numbers))
    if option == "اعداد داغ":
        pool = list(set(hot_numbers) - set(personal_numbers))
        return random.sample(pool, min(len(pool), remaining_slots))
    elif option == "ترکیب داغ و سرد":
        combined = list(set(hot_numbers + cold_numbers) - set(personal_numbers))
        return random.sample(combined, min(len(combined), remaining_slots))
    else:
        return random.sample(available_numbers, min(len(available_numbers), remaining_slots))

# دکمه برای تولید عدد
if st.button("🎰 تولید ترکیب"):
    remaining = 7 - len(personal_numbers)
    if remaining < 0:
        st.error("فقط تا 6 عدد شخصی وارد کن")
    else:
        generated = generate_numbers(option, remaining)
        final_numbers = sorted(personal_numbers + generated)
        st.success(f"🎉 ترکیب پیشنهادی شما: {final_numbers}")
