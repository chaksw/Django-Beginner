from django.db import models
# import validators for the model
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.


class executionStatue(models.Model):
    branches_ = models.IntegerField(verbose_name="Branches")
    events_ = models.IntegerField(verbose_name="Events")


class TestPlan(models.Model):

    process_ = models.CharField(verbose_name="Process", max_length=50)
    fName_ = models.CharField(verbose_name="File Name", max_length=50)
    func_ = models.CharField(verbose_name="Function", max_length=50)
    swLoad_ = models.CharField(verbose_name="SW Load", max_length=50)
    analyst_ = models.CharField(verbose_name="Analyst", max_length=50)
    site_ = models.CharField(verbose_name="Site", max_length=50)
    startData = models.DateTimeField(verbose_name="Start Date")
    # a data field that recored the precentage of coverage of test
    PRECENTAGE_VALIDATOR = [MinValueValidator(0.0), MaxValueValidator(100.0)]
    mcdcCoverage_ = models.DecimalField(
        verbose_name="MC/DC Coverage", validators=PRECENTAGE_VALIDATOR)
    eventCoverage_ = models.DecimalField(
        verbose_name="Event Coverage", validators=PRECENTAGE_VALIDATOR)
    analysisCoverage = models.DecimalField(
        verbose_name="Analysis Coverage", validators=PRECENTAGE_VALIDATOR)
    totalScCoverage = models.DecimalField(
        verbose_name="Total SC Coverage", validators=PRECENTAGE_VALIDATOR)
    # execution Statue
    branches_ = models.IntegerField(verbose_name="Branches")
    events_ = models.IntegerField(verbose_name="Events")
    note_ = models.CharField(verbose_name="Note", max_length=50)

    # Module Structure Data (Branches and Entries/Exits)
    # Covered Decisions
    coveredDecisions_ = models.IntegerField(verbose_name="Decisions")
    # Covered Conditions
    coveredConditons_ = models.IntegerField(verbose_name="Conditions")
    # Covered Cases
    coveredCases_ = models.IntegerField(verbose_name="Cases")
    # Covered Events
    coveredEvents = models.IntegerField(verbose_name="Events")
    # Total Decisions
    totalDecisions_ = models.IntegerField(verbose_name="Decisions")
    # Total Conditions
    totalConditions_ = models.IntegerField(verbose_name="Conditions")
    # Total Cases
    totalCases_ = models.IntegerField(verbose_name="Cases")
    # Total Events
    totalEvents = models.IntegerField(verbose_name="Events")

    # OverSight
    YorN = (
        ('Y', 'Yes'),
        ('N', 'No'),
        (' ', ' '),
    )
    overSight = models.CharField(max_length=1, choices=YorN, default=' ')

    # Defect Classification
    tech_ = models.CharField(verbose_name="Tech", max_length=50)
    nonTech_ = models.CharField(verbose_name="Non-Tech", max_length=50)
    processDefect = models.CharField(
        verbose_name="Process Defect", max_length=50)


class TestException(models.Model):
    # create fields with data named as: note_, module_, function_ line_ reqTag_ analyst_ class_
    # analysisSummary_, correctiveAction_, issue_ with 'Y/N' choices, applicable_ with 'PAR/CR'
    note_ = models.CharField(verbose_name="Note", max_length=50)
    module_ = models.CharField(verbose_name="Module", max_length=50)
    function_ = models.CharField(verbose_name="Function", max_length=50)
    line_ = models.CharField(verbose_name="Line", max_length=100)
    reqTag_ = models.CharField(verbose_name="Requirement Tag", max_length=50)
    analyst_ = models.CharField(verbose_name="Analyst", max_length=50)

    CLASS_OPTIONS = (('IT', 'Incomplete Test'),
                     ('RCM', 'Requirement-Code Mismatch'),
                     ('DeactCode', 'Deactivated Code'),
                     ('DefenCode', 'Defensive Code'),
                     ('TEL', 'Test Environment Limitation'),
                     ('PAS', 'Previously Analyzed Software'),
                     ('other', 'Other'),
                     (' ', ' ')
                     )
    class_ = models.CharField(verbose_name="Class",
                              max_length=50, choices=CLASS_OPTIONS, default=' ')
    analysisSummary_ = models.CharField(
        verbose_name="Analysis Summary", max_length=50)
    correctiveAction_ = models.CharField(
        verbose_name="Corrective Action", max_length=50, default='')
    Y_OR_N = (
        ('Y', 'Yes'),
        ('N', 'No'),
        (' ', ' '),
    )
    issue_ = models.CharField(
        verbose_name="Issue", choices=Y_OR_N, default='No corrective action required.')

    PAR_OR_CR = (
        ('PAR', 'PAR'),
        ('CR', 'CR'),
        (' ', ' '),
    )
    applicable_ = models.CharField(
        verbose_name="Applicable", choices=PAR_OR_CR, default=' ')
