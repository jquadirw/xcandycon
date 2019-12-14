from django.db import models
import uuid

class Product(models.Model):
    title = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    image = models.CharField(max_length=255)

class ColorScheme(models.Model):
    name = models.CharField(max_length=40)
    description = models.CharField(max_length=200)

class Function(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    website = models.CharField(max_length=256)
    logo = models.CharField(max_length=80)

class Frame (models.Model):
    def __init__(self, head, *args, **kwargs):
        super(Frame, self).__init__(*args, **kwargs)
        self.id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
        self.head = head
        self.source = ''
        self.sourceSize = 0
        self.info = ''
        self.dtypes = ''
        self.stats = ''
        self.data = ''
        self.alldata = ''
        self.alldatahtml = ''
        self.corr = ''
        self.heatmap = ''
        self.columns = []

    def get_source(self):
        return self.source

    def get_info(self):
        return self.info

class Correlation(models.Model):

    DUMMY_COLUMNS = (
                        ('Column A', 'Column A'),
                        ('Column B', 'Column B'),
                        ('Column C', 'Column C'),
                    )

    xcolumns = models.CharField(max_length=100, choices=DUMMY_COLUMNS)
    ycolumns = models.CharField(max_length=100, choices=DUMMY_COLUMNS)

    def __init__(self, *args, **kwargs):
        super(Correlation, self).__init__(*args, **kwargs)

    def __str__(self):
        return self.xcolumns


