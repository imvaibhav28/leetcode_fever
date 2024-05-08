# import pandas as pd


# def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:
#     weather.sort_values(by='recordDate', inplace=True)
#     return weather[
#         (weather.temperature.diff() > 0)
#       & (weather.recordDate.diff().dt.days == 1)
#     ][['id']]


# ORACLE:


SELECT W.ID
FROM Weather W
JOIN Weather X
ON W.recordDate = X.recordDate + INTERVAL '1' DAY
WHERE W.temperature > X.temperature
;
