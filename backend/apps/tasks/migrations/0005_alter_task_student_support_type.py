# Generated by Django 3.2.4 on 2022-07-21 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0004_auto_20220714_1027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='student_support_type',
            field=models.CharField(choices=[('hackerrank', 'Hackerrank'), ('ec', 'EC'), ('cohort', 'Cohort'), ('pair_programming', 'Pair Programming'), ('doubt', 'Doubt'), ('quiz', 'Quiz'), ('group_development', 'Group Development Project'), ('self_development', 'Self Development Project'), ('assignment_check', 'Assignment Check'), ('resume', 'Resume'), ('portfolio', 'Portfolio'), ('job_support_assessment', 'Job Support Assessment'), ('job_support_preperation', 'Job Support Preperation'), ('missing_students', 'Missing Students'), ('review', 'Review'), ('kaggle_project', 'Kaggle Project'), ('content_creation', 'Content creation'), ('internal_hackerrank', 'Hackerrank/LeetCode'), ('internal_quiz', 'Quiz'), ('internal_group_development', 'Group Development'), ('internal_self_development', 'Self Development'), ('training', 'Training'), ('internal_assignment_check', 'Assignment Check'), ('missing_students', 'Missing Students'), ('review', 'Review'), ('client_project', 'Client Project'), ('meeting', 'Meeting'), ('job_support', 'Job Support'), ('brainstorming', 'Brainstorming'), ('beniten_team', 'Beniten Team'), ('internal_task', 'Internal Task'), ('internal_project', 'Internal Project'), ('report', 'Report'), ('self_study', 'Self Study'), ('post_job_support', 'Post Job Support')], max_length=200, verbose_name='Student Support type'),
        ),
    ]