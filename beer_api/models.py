from django.db import models

SERVINGTYPE = (
    (0, "Bottle"),
    (1, "Draft")
)

RATING = (
    (0, "0"),
    (1, "1"),
    (2, "2"),
    (3, "3"),
    (4, "4"),
    (5, "5")
)

FLAVOUR = (
    (0, "Alcohol"),
    (1, "Hoppy"),
    (3, "Floral"),
    (4, "Spicy"),
    (5, "Malty"),
    (6, "Burnt"),
    (7, "Sweet"),
    (8, "Sour"),
    (9, "Bitter"),
    (10, "Dry"),
    (11, "Linger"),
)

class BeerDiaryItem(models.Model):
    """Beer Diary Item """
    beer_name = models.CharField(max_length=50)
    brewer = models.CharField(max_length=50)
    created_on = models.DateTimeField(auto_now_add=True)
    price = models.FloatField(null=True, blank=True, default=0.0)
    serving_type = models.IntegerField(choices=SERVINGTYPE, default=0)
    rating = models.IntegerField(choices=RATING, default=0)
    flavour = models.IntegerField(choices=FLAVOUR, default=0)
    description = models.CharField(max_length=255)

    def __str__(self):
        """Return the model as a string"""
        return self.beer_name
