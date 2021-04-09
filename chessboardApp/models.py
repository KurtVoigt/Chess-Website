from django.db import models

# Create your models here.


class Board(models.Model):
    board_name = models.CharField(max_length=30)
    def __str__(self):
        return self.board_name

class Space(models.Model):
    board = models.ForeignKey(Board, related_name="space_list", on_delete=models.CASCADE)
    space_col = models.CharField(max_length=1)
    space_row = models.IntegerField()
    space_piece = models.CharField(max_length=6)
    def __str__(self):
        row = str(self.space_row)
        col = str(self.space_col)
        conc = col + row
        return conc