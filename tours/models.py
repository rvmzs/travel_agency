from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
# Create your models here.

class Tourist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=1)  # Убедитесь, что у вас есть пользователь с ID 1
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    date_of_birth = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    def save(self, *args, **kwargs):
        # Обновляем значения в таблице User
        self.user.first_name = self.first_name
        self.user.last_name = self.last_name
        self.user.email = self.email
        self.user.save()  # Сохранить изменения в User
        super().save(*args, **kwargs)  # Затем вызвать метод родителя


class Tour(models.Model):
    name_tour = models.CharField(max_length = 50)
    date_of_start = models.DateField(null = True, blank = True)
    date_of_end = models.DateField(null = True, blank = True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.name_tour
    
    def average_rating(self):
        reviews = self.reviews.all()
        if reviews:
            return sum(review.rating for review in reviews) / reviews.count()
        return 0
    

class Guide(models.Model):
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length=30)
    language = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class TourGuide(models.Model):
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)
    guide = models.ForeignKey(Guide, on_delete=models.CASCADE)
    additional_info = models.TextField(blank=True, null=True)

    class Meta:
        unique_together = ('tour', 'guide')

    def __str__(self):
        return f"{self.tour.name_tour} - {self.guide.first_name} {self.guide.last_name}"


# class Order(models.Model):
#     tourist =  models.ForeignKey(Tourist, on_delete=models.CASCADE)
#     tour = models.ForeignKey(Tour, on_delete=models.CASCADE)
#     # добавить еще ключи ?
#     date_of_booking = models.DateField(auto_now_add= True)
#     status = models.CharField(max_length = 50)

#     def __str__(self):
#         return f"Order {self.id}  by {self.tourist.first_name} {self.tourist.last_name}"
    
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)  # Убедитесь, что у вас есть пользователь с ID 1
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)
    date_of_booking = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=50)

    def __str__(self):
        return f"Order {self.id} by {self.user.username}"

class Review(models.Model):
    tourist = models.ForeignKey(Tourist, on_delete=models.CASCADE)
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE, related_name='reviews')
    rating = models.IntegerField()
    comment = models.TextField()
    date_of_review = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.tourist.user.username} -- {self.tour.name_tour}"
    
    def clean(self):
        if self.rating is not None and not (1 <= self.rating <= 5):
            raise ValidationError('Rating must be between 1 and 5.')

    

