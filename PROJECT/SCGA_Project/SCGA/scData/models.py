from django.db import models
# import validators for the model
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

# Base One-Many Relationship: Project -> Certification -> Functionality -> Load


class Project(models.Model):
    project = models.CharField(verbose_name="Project", max_length=50)
    # projectID = models.IntegerField(unique=True, primary_key=True)

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
    # funcID = models.IntegerField(unique=True, primary_key=True)
    # Certification = models.ForeignKey(
    #     'Certification', on_delete=models.CASCADE, db_column='Cert')
    Project = models.ForeignKey(
        'Project', on_delete=models.CASCADE, db_column='Project')

    def __str__(self) -> str:
        return f"{self.func}"


class Load(models.Model):
    load = models.CharField(verbose_name="Load", max_length=50)
    # loadID = models.IntegerField(unique=True, primary_key=True)
    Func = models.ForeignKey(
        'Functionality', on_delete=models.CASCADE, db_column='Functionality')

    def __str__(self) -> str:
        return f"{self.load}"
# A Date group of SCGA result of a specific load <- Functionality <- Certification <- Project

# Test Plan and Test Expection (A|B|C)of a specific Process <- Load


# Each row of Test Plan a coverage of MC/DC and Event of a specific function
# for those functions that are not covered according to SCGA, we can use Test Exception to record the reason

# Test Exception recored the reason why a specific function is not covered according to SCGA
class TestException(models.Model):
    # create fields with data named as: note_, module_, function_ line_ reqTag_ analyst_ class_
    # analysisSummary_, correctiveAction_, issue_ with 'Y/N' choices, applicable_ with 'PAR/CR'
    note = models.CharField(verbose_name="Note", max_length=50)
    module = models.CharField(verbose_name="Module", max_length=50)
    function = models.CharField(verbose_name="Function", max_length=50)
    line = models.CharField(verbose_name="Line", max_length=500)
    reqTag = models.CharField(verbose_name="Requirement Tag", max_length=500)
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
                                        max_length=100, choices=CLASS_OPTIONS, default=' ')
    analysisSummary = models.CharField(
        verbose_name="Analysis Summary", max_length=1000, null=True, blank=True)
    correctiveAction = models.CharField(
        verbose_name="Corrective Action", max_length=300, default='No corrective action required.', null=True, blank=True)
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
        ('N/A', 'N/A'),
    )
    applicable = models.CharField(
        verbose_name="Applicable", max_length=10, choices=PAR_OR_CR, default='N/A')


class TestPlan(models.Model):
    # create choices with A|B|C
    LEVEL_OPT = {
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
    }
    level = models.CharField(verbose_name="Level",
                             max_length=2, choices=LEVEL_OPT, default='A', null=True, blank=True)
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
    testException = models.OneToOneField(
        TestException, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Test Exception")
    # note = models.OneToOneField(TestException, on_delete=models.CASCADE)

    # Module Structure Data (Branches and Entries/Exits)
    # Covered Decisions
    coveredDecisions = models.IntegerField(verbose_name="Covered Decisions")
    # Covered Conditions
    coveredConditons = models.IntegerField(verbose_name="Covered Conditions")
    # Covered Cases
    coveredCases = models.IntegerField(verbose_name="Covered Cases")
    # Covered Events
    coveredEvents = models.IntegerField(verbose_name="Covered Events")
    # Total Decisions
    totalDecisions = models.IntegerField(verbose_name="Total Decisions")
    # Total Conditions
    totalConditions = models.IntegerField(verbose_name="Total Conditions")
    # Total Cases
    totalCases = models.IntegerField(verbose_name="Total Cases")
    # Total Events
    totalEvents = models.IntegerField(verbose_name="Total Events")

    # OverSight
    YorN = (
        ('Y', 'Yes'),
        ('N', 'No'),
        (' ', ' '),
    )
    overSight = models.CharField(max_length=1, choices=YorN, default=' ')

    # Defect Classification
    tech = models.CharField(verbose_name="Tech",
                            max_length=50, null=True, blank=True)
    nonTech = models.CharField(
        verbose_name="Non-Tech", max_length=50, null=True, blank=True)
    processDefect = models.CharField(
        verbose_name="Process Defect", max_length=50, null=True, blank=True)