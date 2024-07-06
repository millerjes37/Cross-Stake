from django.db import models

class Owner(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    billing_address = models.TextField(blank=True, null=True)
    card_number = models.CharField(max_length=16, blank=True, null=True)
    ccv = models.CharField(max_length=4, blank=True, null=True)
    exp_date = models.DateField(blank=True, null=True)
    card_name = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name

class Trainer(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Horse(models.Model):
    GENDER_CHOICES = [
        ('Filly', 'Filly'),
        ('Colt', 'Colt')
    ]
    
    GAIT_CHOICES = [
        ('Trotting', 'Trotting'),
        ('Pacing', 'Pacing')
    ]

    name = models.CharField(max_length=255)
    owner = models.ForeignKey(Owner, related_name='horses', on_delete=models.CASCADE)
    trainer = models.ForeignKey(Trainer, related_name='horses', on_delete=models.SET_NULL, null=True, blank=True)
    year_born = models.IntegerField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    gait = models.CharField(max_length=10, choices=GAIT_CHOICES)
    selected_stakes = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Race(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateField()
    location = models.CharField(max_length=255)
    horses = models.ManyToManyField(Horse, related_name='races')

    def __str__(self):
        return f"{self.name} at {self.location} on {self.date}"

class FeeSchedule(models.Model):
    race = models.ForeignKey(Race, related_name='fee_schedules', on_delete=models.CASCADE)
    date = models.DateField()
    entrance_fee = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    registration_fee = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    staking_fee = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return f"Fee Schedule for {self.race.name} on {self.date}"
