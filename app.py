import streamlit as st
st.title("Мини тест – География и История")
st.write("Въведи отговорите си и натисни „Провери резултата“")
q1 = st.text_input("1. Коя е столицата на България?")
q2 = st.number_input("2. Колко континента има на Земята?", min_value=1, max_value=10)
q3 = st.text_input("3. Кой е първият български владетел?")
q4 = st.number_input("4. През коя година България влиза в ЕС?", min_value=1900, max_value=2100)
q5 = st.text_input("5. Как се казва най-дългата река в България?")
if st.button("Провери резултата"):
    points = 0
    if q1.strip().lower() == "софия":
        points += 1
    if q2 == 7:
        points += 1
    if q3.strip().lower() in ["хан аспарух", "аспарух"]:
        points += 1
    if q4 == 2007:
        points += 1
    if q5.strip().lower() == "искър":
        points += 1
    st.write(f"Твоят резултат: {points} / 5")

    if points >= 4:
        st.success("Браво! Отличен резултат ")
    elif points >= 2:
        st.warning("Добре, но можеш и по-добре ")
    else:
        st.error("Опитай пак! ")
