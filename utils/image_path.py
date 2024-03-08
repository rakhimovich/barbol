def upload_avatar_for_user(instance, filename):
    return f"avatar/{instance.username}/{filename}"


def upload_cakes(instance, filename):
    return f"products/{instance.image}/{filename}"


def upload_flour(instance, filename):
    return f"products/{instance.image}/{filename}"