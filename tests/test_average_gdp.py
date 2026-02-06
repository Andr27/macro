from reports.average_gdp import AverageGDPReport



def test_average_gdp_single_country():
    rows = [
        {"country": 'A', "gdp":'10'},
        {"country": 'A', "gdp":'20'},
        {"country": 'A', "gdp":'60'},
         
    ]


    report = AverageGDPReport()
    result = report.build(rows)

    assert result == [("A", 30.0)]






def test_average_gdp_multiple_countries():
    rows = [
    {"country": 'A', "gdp":'10'},
    {"country": 'B', "gdp":'20'},
    {"country": 'C', "gdp":'60'}
    ]
    
    report = AverageGDPReport()
    result = report.build(rows)

    assert len(result) == 3





def test_sorted():
    rows = [
    {"country": 'A', "gdp":'10'},
    {"country": 'B', "gdp":'20'}
    ]

    report = AverageGDPReport()
    result = report.build(rows)

    assert result[0][0] == "B"



