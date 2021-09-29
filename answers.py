import pandas as pd
from io import StringIO

data = 'Airline Code;DelayTimes;FlightCodes;To_From\nAir Canada (!);[21, 40];20015.0;WAterLoo_NEWYork\n<Air France> (12);[];;Montreal_TORONTO\n(Porter Airways. );[60, 22, 87];20035.0;CALgary_Ottawa\n12. Air France;[78, 66];;Ottawa_VANcouvER\n""".\\.Lufthansa.\\.""";[12, 33];20055.0;london_MONTreal\n'

TESTDATA = StringIO(data)

df = pd.read_csv(TESTDATA, sep=';', lineterminator='\n')

#### QUESTION 1 ####

rows = df.shape[0]
for i in range(rows):
    if pd.isna(df.iloc[i,2]):
       df.iloc[i,2] = df.iloc[i-1,2] + 10
df['FlightCodes'] = df['FlightCodes'].astype('int32')

#### QUESTION 2 ####

to_from_column = df.iloc[:,3]
to_from_column = to_from_column.str.split("_", expand=True)
to_from_column = to_from_column.rename({0: 'TO', 1: 'FROM'}, axis = 'columns')
to_from_column = to_from_column.apply(lambda x: x.astype(str).str.upper())
df = df.drop(columns=['To_From'])
df = pd.concat([df,to_from_column], axis = 1)

#### QUESTION 3 ####

df["Airline Code"] = df['Airline Code'].str.replace('[^\w\s]','', regex=True)
df["Airline Code"] = df["Airline Code"].str.strip()

print(df)

# SAVING TABLE INTO A CSV
df.to_csv('snapcommerce_codetest.csv', index=False)

#### Question 4 ####

# SELECT "Airline Code" FROM flight_schedule WHERE "FROM" = 'WATERLOO';





#### The following mock SQL query was tested on postgreSQL

## CREATE TABLE flight_schedule (
#           "Airline Code" VARCHAR(255),
#           "DelayTimes" VARCHAR(255),
#           "FlightCodes" integer PRIMARY KEY,
#           "TO" VARCHAR(255)
#           "FROM" VARCHAR(255)
#  );

# COPY flight_schedule FROM "PATH_OF_CSV" DELIMITER DELIMITER ',' CSV HEADER;

#### And then we run the above query

# SELECT "Airline Code" FROM flight_schedule WHERE "FROM" = 'WATERLOO';