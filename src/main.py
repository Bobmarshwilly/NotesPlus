import argparse

from src.database import engine, SessionLocal
from src.models import Base, Note


# Функция добавления заметок.
def add_note(content: str):
    db = SessionLocal()
    new_note = Note(content=content)
    db.add(new_note)
    db.commit()
    db.refresh(new_note)
    db.close()


# Функция вывода всех заметок.
def list_notes():
    db = SessionLocal()
    notes = db.query(Note).all()
    db.close()

    if not notes:
        print("Нет заметок!")
    else:
        for note in notes:
            print(note.content)


# Определение аргументов получаемых из терминала.
def parse_arguments():
    parser = argparse.ArgumentParser(description="Программа для ведения заметок")
    parser.add_argument(
        "command",
        choices=["add_note", "list_notes"],
        help="Команды для выполнения",
    )
    parser.add_argument("note", type=str, nargs="?", help="Текст заметки")
    return parser.parse_args()


def main():
    Base.metadata.create_all(bind=engine)
    args = parse_arguments()

    if args.command == "add_note":
        add_note(args.note)

    if args.command == "list_notes":
        list_notes()


if __name__ == "__main__":
    main()
