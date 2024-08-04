# Generated by Django 4.2.14 on 2024-08-01 10:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("bookalesson", "0002_rename_bookings_booking_rename_lessontype_lesson"),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name="commentonlesson",
            name="unique_user_lesson_comment",
        ),
        migrations.AddField(
            model_name="commentonlesson",
            name="lesson_date",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="comments",
                to="bookalesson.lessondate",
            ),
        ),
        migrations.AddConstraint(
            model_name="commentonlesson",
            constraint=models.UniqueConstraint(
                fields=("author", "lesson_type", "lesson_date"),
                name="unique_user_lesson_date_comment",
            ),
        ),
    ]