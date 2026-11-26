from django.contrib.auth import get_user_model


def check_article_access(user):
    if user.has_perm("accounts.change_article"):
        print("Можно редактировать статью")
    else:
        print("Доступ запрещён")


def check_student_and_teacher_access():
    user_model = get_user_model()

    for group_name in ("Student", "Teacher"):
        user = user_model.objects.filter(groups__name=group_name).first()
        if user is None:
            raise LookupError(f"В группе {group_name} нет пользователей")

        print(f"{group_name}: ", end="")
        check_article_access(user)
