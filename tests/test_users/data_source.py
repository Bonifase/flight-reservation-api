new_user = dict(
    username="Bill",
    email="Bill@gmail.com",
    password="bill124",
    isAdmin="True")
regular_user = dict(
    username="regular",
    email="regular@gmail.com",
    password="regulart124")
duplicate_user = dict(
    username="Bill",
    email="Bill@gmail.com",
    password="bill124")

user_missing_name = dict(
    username="",
    email="Bill@gmail.com",
    password="bill124")

user_missing_email = dict(
    username="Bill",
    email="",
    password="bill124")

user_missing_password = dict(
    username="Bill",
    email="Bill@gmail.com",
    password="")

invalid_username = dict(
    username=".",
    email="Bill@gmail.com",
    password="bill124")

invalid_email = dict(
    username="Bill",
    email="gmail.com",
    password="bill124")

invalid_password = dict(
    username="Bill",
    email="Bill@gmail.com",
    password=".")

missing_username_key = dict(
    email="Bill@gmail.com",
    password="bill124")

missing_email_key = dict(
    username="Bill",
    password="bill124")

missing_password_key = dict(
    username="Bill",
    email="Bill@gmail.com"
    )

special_username = dict(
    username="$%$^$%",
    password="bill124",
    email="wttrr@gmailkbkjbkjbkj")

email_with_spaces = dict(
    username="bill",
    password="bill124",
    email="wttrr@gmai   l.com")