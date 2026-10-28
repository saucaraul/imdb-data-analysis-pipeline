import os
from pathlib import Path

import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine, text
from sqlalchemy.engine import URL

# Load database credentials from .env
load_dotenv()

# Locate the cleaned CSV relative to the project folder
project_root = Path(__file__).resolve().parent.parent
csv_path = project_root / "data" / "processed" / "final_movies.csv"

# Build the PostgreSQL connection
connection_url = URL.create(
    drivername="postgresql+psycopg",
    username=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    host=os.getenv("DB_HOST"),
    port=int(os.getenv("DB_PORT", "5432")),
    database=os.getenv("DB_NAME"),
)

engine = create_engine(connection_url)

try:
    # Read the cleaned movie data
    df = pd.read_csv(csv_path)
    df.columns = [column.lower() for column in df.columns]

    print(f"CSV loaded successfully: {len(df)} rows")

    # Insert data only if the database table is empty
    with engine.begin() as connection:
        existing_rows = connection.execute(
            text("SELECT COUNT(*) FROM movies")
        ).scalar_one()

        if existing_rows > 0:
            raise RuntimeError(
                f"The movies table already contains {existing_rows} rows. "
                "Import cancelled to prevent duplicate records."
            )

        df.to_sql(
            name="movies",
            con=connection,
            schema="public",
            if_exists="append",
            index=False,
            chunksize=1000
        )

        total_rows = connection.execute(
            text("SELECT COUNT(*) FROM movies")
        ).scalar_one()

    print("Import completed successfully!")
    print(f"Rows in PostgreSQL: {total_rows}")

except Exception as error:
    print("\nIMPORT FAILED")
    print(f"Error type: {type(error).__name__}")
    print(f"Error message: {str(error)[:1000]}")

finally:
    engine.dispose()