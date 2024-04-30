from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Tag(models.Model):
    name = models.CharField(max_length=128, blank=False, verbose_name='Название')
    color_code = models.CharField(max_length=128, blank=False, verbose_name='Цветовой код')
    slug = models.SlugField(blank=False, unique=True, verbose_name='Слаг')

    class Meta:
        verbose_name = 'тег'
        verbose_name_plural = 'теги'

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(max_length=128, blank=False, verbose_name='Название')
    measurement_unit = models.CharField(max_length=128, blank=False, verbose_name='Еденица измерения')

    class Meta:
        verbose_name = 'ингредиент'
        verbose_name_plural = 'ингредиенты'

    def __str__(self):
        return self.name


class Recipe(models.Model):
    name = models.CharField(max_length=128, blank=False, verbose_name='Название')
    autor = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    image = models.ImageField(blank=False, verbose_name='Изображение')
    description = models.TextField(blank=False, verbose_name='Описание')
    cooking_time = models.IntegerField(blank=False, verbose_name='Время приготовления')
    ingredients = models.ManyToManyField(Ingredient, verbose_name='Ингредиенты блюда')
    tags = models.ManyToManyField(Tag, verbose_name='Тэг')
    pub_date = models.DateTimeField(verbose_name="Дата публикации", auto_now_add=True, editable=False)

    class Meta:
        verbose_name = 'рецепт'
        verbose_name_plural = 'рецепты'

    def __str__(self):
        return self.name


class AmountIngredient(models.Model):
    """Количество ингридиентов в блюде.

    Модель связывает Recipe и Ingredient с указанием количества ингридиента.

    Attributes:
        recipe(int):
            Связаный рецепт. Связь через ForeignKey.
        ingredients(int):
            Связаный ингридиент. Связь через ForeignKey.
        amount(int):
            Количиства ингридиента в рецепте. Установлены ограничения
            по минимальному и максимальному значениям.
    """
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, verbose_name="В каких рецептах")
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE, verbose_name="Связанные ингредиенты")
    amount = models.PositiveSmallIntegerField(
        verbose_name="Количество",
        default=0,
        validators=(
            # MinValueValidator(
            #     Limits.MIN_AMOUNT_INGREDIENTS,
            #     "Нужно хоть какое-то количество.",
            # ),
            # MaxValueValidator(
            #     Limits.MAX_AMOUNT_INGREDIENTS,
            #     "Слишком много!",
            # ),
        ),
    )

    # class Meta:
    #     verbose_name = "Ингридиентf"
    #     verbose_name_plural = "Количество ингридиентов"


