from datetime import datetime

birth_list = [{"name": "Viktor", "birthday": "23.04.1995"},
              {"name": "Oleksandr", "birthday": "15.02.1990"},
              {"name": "Olena", "birthday": "29.06.1994"},
              {"name": "Tymofii", "birthday": "06.10.1995"},
              {"name": "Anna", "birthday": "01.09.1992"},
              {"name": "Nazar", "birthday": "23.12.1993"},
              {"name": "Oleksandra", "birthday": "31.08.1997"},
              {"name": "Liliya", "birthday": "16.07.1994"},
              {"name": "Oleksii", "birthday": "09.09.1995"},
              {"name": "Borys", "birthday": "17.11.1997"},
              {"name": "Oleksandr", "birthday": "22.08.1993"},
              {"name": "Lina", "birthday": "12.05.1996"},
              {"name": "Igor", "birthday": "17.09.1995"},
              {"name": "Tatiana", "birthday": "11.09.1995"},
              {"name": "Oleksandr", "birthday": "23.12.1992"},
              {"name": "Kateryna", "birthday": "06.03.2010"},
              {"name": "Polina", "birthday": "14.03.2022"}]


def get_birthday_per_week(birth_list, d=7):
    week_dict = {
        "Monday": [],
        "Tuesday": [],
        "Wednesday": [],
        "Thursday": [],
        "Friday": []
    }
    for birthdays in birth_list:
        birthday = birthdays["birthday"]
        birthday = datetime(year=int(datetime.now().year),
                            month=int(birthday[3:5]), day=int(birthday[:2]))
        birthday = birthday.date()
        current_date = datetime.now()
        current_date = current_date.date()
        delta = birthday - current_date
        if 0 <= int(delta.days) < d:
            if birthday.strftime('%A') in ["Saturday", "Sunday"]:
                week_dict["Monday"].append(birthdays["name"])
            else:
                week_dict[birthday.strftime('%A')].append(birthdays["name"])

    for k, v in week_dict.items():
        if week_dict[k]:
            name = ""
            for i in range(len(v)):
                if i < len(v)-1:
                    name += v[i] + ", "
                else:
                    name += v[i]
            print(f"{k}: {name}")


if __name__ == "__main__":
    get_birthday_per_week(birth_list)
