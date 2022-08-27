
!!!!!!!!!!!!!!!! smart selects !!!!!!!!!!!!!!!!!!!
Бул библиотека качан биз админде иштеп жатканда жардам берет
мисалы: Эгер бизде бир материк болсо анын ошол материкте жайгашкан олколор бар
эгер биз бир материкти тандасак ошол материктин гана олколору керек болот
бул библиотека ошону кылгынга жардам берет биз биринчи материти тандасак ошого тишелуу болгон
маалыматтарды же олколорду чыгарып берет
!!!!!!!!!!!!!!! smart selects end !!!!!!!!!!!!!!!!!!!

############ категория же башка бир нерсе тандаганда ошого
 байланышкан нерсе чыгыш учун керек болгон биб #############
1 install smart selects
 $ pip install django-smart-selects
2 Add smart_selects to your INSTALLED_APPS
3 Add the smart_selects urls into your project’s urls.py
    '''
    url(r'^chaining/', include('smart_selects.urls')),
    '''
4 import
    from django.urls import path, include
    from django.conf.urls import url


5  Set USE_DJANGO_JQUERY = True to enable this behaviour. "in setting"
6 Chained Selects
    Given the following model:

                class Continent(models.Model):
                    name = models.CharField(max_length=255)

                class Country(models.Model):
                    continent = models.ForeignKey(Continent)
                    name = models.CharField(max_length=255)

                class Location(models.Model):
                    continent = models.ForeignKey(Continent)
                    country = models.ForeignKey(Country)
                    area = models.ForeignKey(Area)
                    city = models.CharField(max_length=50)
                    street = models.CharField(max_length=100)
   #####from smart_selects.db_fields import ChainedForeignKey########
   ############################ you should change it to same that example 👇 #######################################
                class Location(models.Model):
                    continent = models.ForeignKey(Continent)
                    country = ChainedForeignKey(
                        Country,
                        chained_field="continent",
                        chained_model_field="continent",
                        show_all=False,
                        auto_choose=True,
                        sort=True)
                    area = ForeignKey(Area)
                    city = models.CharField(max_length=50)
                    street = models.CharField(max_length=100)


!!!!!!!!!!!!!!!! change app's name !!!!!!!!!!!!


1 add verbose_name = '<Любой>' to app.py


!!!!!!!!!!!!!!!! change app's name end  !!!!!!!!!!!!