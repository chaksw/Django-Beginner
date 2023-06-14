from django.db import models
# import validators for the model
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

# Base One-Many Relationship: Project -> Certification -> Functionality -> Load


class Project(models.Model):
    project = models.CharField(verbose_name="Project", max_length=50)
    projectID = models.IntegerField(unique=True, primary_key=True)

    def __str__(self) -> str:
        return self.project

# Maybe it's not nessary to have a seperate table for Certification
# class Certification(models.Model):
#     cert = models.CharField(verbose_name="Certification", max_length=50)
#     certID = models.IntegerField(unique=True, primary_key=True)
#     Project = models.ForeignKey(
#         'Project', on_delete=models.CASCADE, db_column='Project')

#     def __str__(self) -> str:
#         return f"{self.cert} in {self.Porject}"


class Functionality(models.Model):
    func = models.CharField(verbose_name="Function", max_length=10)
    funcID = models.IntegerField(unique=True, primary_key=True)
    # Certification = models.ForeignKey(
    #     'Certification', on_delete=models.CASCADE, db_column='Cert')
    Project = models.ForeignKey(
        'Project', on_delete=models.CASCADE, db_column='Project')

    def __str__(self) -> str:
        return f"{self.func} <- {self.Project}"


class Load(models.Model):
    load = models.CharField(verbose_name="Load", max_length=50)
    loadID = models.IntegerField(unique=True, primary_key=True)
    Func = models.ForeignKey(
        'Functionality', on_delete=models.CASCADE, db_column='Functionality')

    def __str__(self) -> str:
        return f"{self.load} <- {self.Func}"
# A Date group of SCGA result of a specific load <- Functionality <- Certification <- Project

# Test Plan of a specific Process <- Load


class TestPlan(models.Model):
    # Process like (GgfPfd Mws...)
    process = models.CharField(verbose_name="Process", max_length=50)
    # File Name(x.cpp)
    fName = models.CharField(verbose_name="File Name", max_length=50)
    # Function in file
    func = models.CharField(verbose_name="Function", max_length=50)
    # Load Number
    swLoad = models.ForeignKey(
        'Load', on_delete=models.CASCADE, db_column='Load')
    # Analyst
    analyst = models.CharField(verbose_name="Analyst", max_length=50)
    # Work Site of Analyst
    site = models.CharField(verbose_name="Site", max_length=50)
    # Date of Test
    startDate = models.DateTimeField(verbose_name="Start Date")
    # Data field that recored the precentage of coverage of test
    PRECENTAGE_VALIDATOR = [MinValueValidator(0.0), MaxValueValidator(100.0)]
    mcdcCoverage = models.DecimalField(
        verbose_name="MC/DC Coverage", max_digits=4, decimal_places=2, validators=PRECENTAGE_VALIDATOR)
    eventCoverage = models.DecimalField(
        verbose_name="Event Coverage", max_digits=4, decimal_places=2, validators=PRECENTAGE_VALIDATOR)
    analysisCoverage = models.DecimalField(
        verbose_name="Analysis Coverage", max_digits=4, decimal_places=2, validators=PRECENTAGE_VALIDATOR)
    totalScCoverage = models.DecimalField(
        verbose_name="Total SC Coverage", max_digits=4, decimal_places=2, validators=PRECENTAGE_VALIDATOR)
    # execution Statue
    branches = models.IntegerField(verbose_name="Branches")
    events = models.IntegerField(verbose_name="Events")
    note = models.CharField(verbose_name="Note", max_length=50)

    # Module Structure Data (Branches and Entries/Exits)
    # Covered Decisions
    coveredDecisions = models.IntegerField(verbose_name="Decisions")
    # Covered Conditions
    coveredConditons = models.IntegerField(verbose_name="Conditions")
    # Covered Cases
    coveredCases = models.IntegerField(verbose_name="Cases")
    # Covered Events
    coveredEvents = models.IntegerField(verbose_name="Events")
    # Total Decisions
    totalDecisions = models.IntegerField(verbose_name="Decisions")
    # Total Conditions
    totalConditions = models.IntegerField(verbose_name="Conditions")
    # Total Cases
    totalCases = models.IntegerField(verbose_name="Cases")
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
    tech = models.CharField(verbose_name="Tech", max_length=50)
    nonTech = models.CharField(verbose_name="Non-Tech", max_length=50)
    processDefect = models.CharField(
        verbose_name="Process Defect", max_length=50)


class TestException(models.Model):
    # create fields with data named as: note_, module_, function_ line_ reqTag_ analyst_ class_
    # analysisSummary_, correctiveAction_, issue_ with 'Y/N' choices, applicable_ with 'PAR/CR'
    note = models.CharField(verbose_name="Note", max_length=50)
    module = models.CharField(verbose_name="Module", max_length=50)
    function = models.CharField(verbose_name="Function", max_length=50)
    line = models.CharField(verbose_name="Line", max_length=100)
    reqTag = models.CharField(verbose_name="Requirement Tag", max_length=50)
    analyst = models.CharField(verbose_name="Analyst", max_length=50)

    CLASS_OPTIONS = (('IT', 'Incomplete Test'),
                     ('RCM', 'Requirement-Code Mismatch'),
                     ('DeactCode', 'Deactivated Code'),
                     ('DefenCode', 'Defensive Code'),
                     ('TEL', 'Test Environment Limitation'),
                     ('PAS', 'Previously Analyzed Software'),
                     ('other', 'Other'),
                     (' ', ' ')
                     )
    # UnCovered Category
    ucClassification = models.CharField(verbose_name="Class",
                                        max_length=50, choices=CLASS_OPTIONS, default=' ')
    analysisSummary = models.CharField(
        verbose_name="Analysis Summary", max_length=50)
    correctiveAction = models.CharField(
        verbose_name="Corrective Action", max_length=50, default='')
    Y_OR_N = (
        ('Y', 'Yes'),
        ('N', 'No'),
        (' ', ' '),
    )
    issue = models.CharField(
        verbose_name="Issue", choices=Y_OR_N, max_length=10, default='No corrective action required.')

    PAR_OR_CR = (
        ('PAR', 'PAR'),
        ('CR', 'CR'),
        (' ', ' '),
    )
    applicable = models.CharField(
        verbose_name="Applicable", max_length=10, choices=PAR_OR_CR, default=' ')
