from django.db.models import Manager


class ProfileMainManager(Manager):
    def get_grade_profile(self, user=None, club_id=None):
        if not (user and club_id):
            return 0, None

        queryset = super().get_queryset()
        try:
            if profile := queryset.get(club_id=club_id, user=user):
                return profile.permission_grade, profile
        except:
            return 0, None
