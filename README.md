 MB 343 - This module is created to extract default data from S&P yearly report "Default, Transition and Recovery report"

"Default_Data_Extraction.py" -  Steps to extract default data:

 1) Get pages related to default data as PDF example "SnP_2018.pdf".
 2) Get the coordinates for table in the PDF. I used "SumatraPDF" to get columns' coordinates.
 3) There are so many heading and blanks rows are created as after excel conversion. Row/Column number may need to
    be change based on new report from S&P. I copied the extracted file to excel and manually looked before cleaning.
 4) After all the cleanup steps we should be able to comeup with company name and default dates. Please verify it before
    moving to next step.
 5) Once company and default date is there we need to find ticker for those companies:

    Company_Ticker_Map.py: This file compares default file with ticker cusip map

 6) Here fuzzy logic is used to compare company name in both the files and then get the one with ratio greater than
    or equal to 80.
 7) Manual cleanup needed after fuzzy logic output.


