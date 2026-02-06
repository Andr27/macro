from reports.average_gdp import AverageGDPReport



REPORTS = {
    "average-gdp": AverageGDPReport,
}



def get_report(name):
    if name not in REPORTS:
        raise ValueError(f"Unknown report: {name}")
    
    return REPORTS[name]()

