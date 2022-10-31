from enum import unique
from django.db import models


class Account(models.Model):
    userName = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    class Meta:
        constraints = [
            models.UniqueConstraint(name="this username is taken", fields=["userName"])
        ]

    def __str__(self) -> str:
        return self.userName


class Parent(models.Model):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    account = models.OneToOneField(
        Account, verbose_name=("Account"), on_delete=models.CASCADE
    )

    def __str__(self) -> str:
        return self.firstName + " " + self.lastName


class Token(models.Model):
    token = models.CharField(max_length=200)
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE)


class Subject(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name


class Student(models.Model):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    age = models.IntegerField()
    marks = models.IntegerField()
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE, related_name = 'students')
    subject = models.ManyToManyField(Subject)

    def __str__(self) -> str:
        return self.firstName + " " + self.lastName

    class Meta:
        constraints = [
            models.CheckConstraint(
                name="age greater than 5", check=models.Q(age__gt=5)
            ),
            models.CheckConstraint(
                name="marks greater than or equal 0", check=models.Q(marks__gt=-1)
            ),
        ]
