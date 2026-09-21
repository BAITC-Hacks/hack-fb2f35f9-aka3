faq = []

with open("faq.txt", "r", encoding="utf-8") as file:
    for line in file:
        question, answer = line.strip().split("|")
        faq.append((question, answer))


keywords = {
    "время": ["время", "во сколько", "начинается"],
    "команда": ["команда", "человек", "участников"],
    "трек": ["трек", "направление"],
    "сдача": ["сдать", "сдача", "дедлайн", "когда"],
    "призы": ["приз", "призы", "награда"]
}


print("FAQ-бот запущен!")
print("Напиши вопрос или 'выход' для завершения.\n")


while True:
    user_question = input("Вы: ").lower()

    if user_question == "выход":
        print("Бот: Пока!")
        break

    found = False

    for i, (question, answer) in enumerate(faq):

        if i == 0:
            words = keywords["время"]
        elif i == 1:
            words = keywords["команда"]
        elif i == 2:
            words = keywords["трек"]
        elif i == 3:
            words = keywords["сдача"]
        else:
            words = keywords["призы"]

        for word in words:
            if word in user_question:
                print("Бот:", answer)
                found = True
                break

        if found:
            break

    if not found:
        print("Бот: Не знаю.")