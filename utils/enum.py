from django.utils.translation import ugettext_lazy as _

MALE = 'MALE'
FEMALE = 'FEMALE'
SEXS = (
    (MALE, 'MALE'),
    (FEMALE, 'FEMALE')
)

RISK = 'Risk'
INCIDENT = 'Incident'
NEARMISS = 'Near miss'
ADVERSEEVENT = 'Adverse Event'
INCIDENT_CATEGORIES = (
    (RISK, 'Risk'),
    (NEARMISS, 'Near miss'),
    (INCIDENT, 'Incident'),
    (ADVERSEEVENT, 'Adverse Event'),
)
