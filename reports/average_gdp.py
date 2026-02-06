class AverageGDPReport:
    def build(self, rows):
        country_to_gdps = {}

        for row in rows:
            country = row["country"]
            gdp = float(row["gdp"])

            if country not in country_to_gdps:
                country_to_gdps[country] = []

            
            country_to_gdps[country].append(gdp)
        
        result = []


        for country, gdps in country_to_gdps.items():
            avg_gdp = sum(gdps) / len(gdps)
            result.append((country, avg_gdp))

        result.sort(key=lambda x: x[1], reverse=True)
        return result
