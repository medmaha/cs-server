import uuid
from features.models import UniqueId


def id_generator():
    def clean_id(id: str):
        id = id.replace("-", "")
        id = id.replace("_", "")
        return id + "_cs_u"

    def save(x: str, id: str):
        id = UniqueId.objects.create(used_for=x, unique_id=id)
        return id

    _uuid = uuid.uuid4()
    new_id = str(_uuid)

    while True:
        id = clean_id(new_id)
        check_existence = UniqueId.objects.filter(unique_id=id).exists()
        if check_existence == True:
            _uuid = uuid.uuid4()
            new_id = clean_id(str(_uuid))
        else:
            break

    id = clean_id(new_id)

    return (id, lambda x: save(x, id))


def get_profile_data(user):

    from api.routes.user.serializers import (
        AdminSerializer,
        CelebritySerializer,
        SupporterSerializer,
        UserMiniInfoSeriaLizer,
    )

    profiles = {
        "admin": AdminSerializer(user.profile),
        "celebrity": CelebritySerializer(user.profile),
        "supporter": SupporterSerializer(user.profile),
    }
    other = UserMiniInfoSeriaLizer(user)
    profile = profiles.get(user.user_type.lower(), other)

    return profile.data
