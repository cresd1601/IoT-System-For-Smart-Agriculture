from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from celery import Celery
import os
from .models.setting_model import SettingModel  # Assuming SettingModel is defined in models.setting_model

# Initialize Celery using the existing Redis setup from environment variables
app = Celery('service_worker', broker=os.getenv('REDIS_URL'))

# Database connection strings from environment variables
cloud_db_url = os.getenv('CLOUD_DATABASE_URL')
local_db_url = os.getenv('LOCAL_DATABASE_URL')

# Set up database engines and sessions
cloud_engine = create_engine(cloud_db_url)
local_engine = create_engine(local_db_url)

CloudSession = sessionmaker(bind=cloud_engine)
LocalSession = sessionmaker(bind=local_engine)

@app.task
def sync_data():
    """Task to sync data from cloud DB to local DB with SettingModel"""
    cloud_session = CloudSession()
    local_session = LocalSession()

    try:
        # Fetch data from the correct cloud 'setting' table
        cloud_data = cloud_session.execute("SELECT * FROM setting").fetchall()

        for row in cloud_data:
            # Check if a setting with the same sensor_id already exists in the local DB
            existing_setting = local_session.query(SettingModel).filter_by(sensor_id=row['sensor_id']).first()

            if existing_setting:
                # Update existing setting
                existing_setting.max_temperature = row['max_temperature']
                existing_setting.min_temperature = row['min_temperature']
                existing_setting.max_humidity = row['max_humidity']
                existing_setting.min_humidity = row['min_humidity']
                existing_setting.max_moisture = row['max_moisture']
                existing_setting.min_moisture = row['min_moisture']
            else:
                # Insert new setting
                new_setting = SettingModel(
                    sensor_id=row['sensor_id'],
                    max_temperature=row['max_temperature'],
                    min_temperature=row['min_temperature'],
                    max_humidity=row['max_humidity'],
                    min_humidity=row['min_humidity'],
                    max_moisture=row['max_moisture'],
                    min_moisture=row['min_moisture']
                )
                local_session.add(new_setting)

        # Commit the transaction
        local_session.commit()
        print("Data synced successfully.")

    except Exception as e:
        local_session.rollback()
        print(f"Error during data sync: {e}")
    finally:
        cloud_session.close()
        local_session.close()
