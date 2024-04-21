from datetime import datetime


def user_art_path(instance, filename,):
    month = datetime.now().strftime("%B")
    return './static/images/user_{0}/{1}/{2}'.format(instance.post.auther.first_name, month, filename)


def user_profile_path(instance, filename):
    month = datetime.now().strftime("%B")
    return './static/profile_images/{0}/{1}/{2}'.format(instance.post.auther.first_name, month, filename)
