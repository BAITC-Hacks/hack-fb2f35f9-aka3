# FAQ Bot

Simple terminal FAQ bot created for hackathon rehearsal.

The bot answers five predefined questions about:

- rehearsal time
- team
- track
- submission
- prizes

Questions and answers are stored in `faq.txt`.

The bot searches for keywords in the user's question and prints the corresponding answer. If no matching keyword is found, the bot replies with `Не знаю`.

## How to run

Make sure Python is installed.

Run:

```bash
python main.py
```

Then enter a question in the terminal.

Example:

```text
Вы: Во сколько начинается репетиция?
Бот: Репетиция начинается в 18:30.
```

Type `выход` to stop the program.
