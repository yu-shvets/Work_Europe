from django.db import models


class CommonInfo(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=256)

    class Meta:
        abstract = True
        ordering = ['created']


class Services(CommonInfo):
    image = models.ImageField(blank=True, null=True, upload_to='images')
    description = models.TextField(blank=True, null=True)

    class Meta(CommonInfo.Meta):
        verbose_name = "Service"
        verbose_name_plural = "Services"

    def __str__(self):
        return "{}".format(self.title)


class Countries(CommonInfo):

    class Meta(CommonInfo.Meta):
        verbose_name = "Country"
        verbose_name_plural = "Countries"

    def __str__(self):
        return "{}".format(self.title)


class Companies(CommonInfo):

    class Meta(CommonInfo.Meta):
        verbose_name = "Company"
        verbose_name_plural = "Companies"

    def __str__(self):
        return "{}".format(self.title)


class Specializations(CommonInfo):

    class Meta(CommonInfo.Meta):
        verbose_name = "Specialization"
        verbose_name_plural = "Specializations"

    def __str__(self):
        return "{}".format(self.title)


class Vacancies(CommonInfo):

    country = models.ForeignKey(Countries)
    company = models.ForeignKey(Companies)
    specialization = models.ForeignKey(Specializations)

    class Meta(CommonInfo.Meta):
        verbose_name = "Vacancy"
        verbose_name_plural = "Vacancies"

    def __str__(self):
        return "{}".format(self.title)


class Contacts(models.Model):
    phone = models.CharField(max_length=256)
    address = models.TextField()
    mail = models.EmailField()

    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"

    def __str__(self):
        return "{}".format(self.mail)


class Messages(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    mail = models.EmailField()
    message = models.TextField()

    class Meta:
        verbose_name = "Message"
        verbose_name_plural = "Messages"

    def __str__(self):
        return "{}".format(self.created)
