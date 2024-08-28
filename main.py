# %%

import pandas as pd
import numpy as np
from datetime import datetime


def dedup_column(value):
    if pd.isnull(value):
        return np.nan

    try:
        value = value.strip('{}')
        items = value.split(',')
    except Exception as e:
        print(f"Error converting value {value}: {e}")

    return items


def parse_participant(part_attr):
    if pd.isnull(part_attr):
        return []

    try:
        part_attr = part_attr.split('-')
        part_attr = [part.strip().strip('"') for part in part_attr]
        # print(part_attr)
    except Exception as e:
        print(f"Error converting value {part_attr}: {e}")

    return part_attr


def parse_datetime(value):
    if pd.isna(value) or value.strip() == '':
        return pd.NaT
    try:
        return pd.to_datetime(value, format='%Y-%m-%d', errors='coerce')
    except ValueError:
        return pd.NaT


df = pd.read_csv('ucd_census.csv')

df['participant_id'] = df['participant_id'].apply(dedup_column)
df['participant'] = df['participant'].apply(dedup_column)
df = df.explode(['participant_id', 'participant'])

df['participant'] = df['participant'].apply(parse_participant)

columns = ['Names', 'First_LN', 'Second_LN', 'Year', 'Month', 'Day']
participant_df = pd.DataFrame(df['participant'].tolist(), columns=columns)
participant_df['DoB'] = participant_df[[
    'Year', 'Month', 'Day']].astype(str).fillna('').agg('-'.join, axis=1)
participant_df['DoB'] = participant_df['DoB'].apply(parse_datetime)

df = df.reset_index(drop=True)
participant_df = participant_df.reset_index(drop=True)

cleaned_df = pd.merge(left=df, right=participant_df, left_on=df.index, right_on=participant_df.index)
cleaned_df = cleaned_df[['census_id', 'participant_id', 'Names', 'First_LN', 'Second_LN', 'DoB']]

cleaned_df.to_csv('cleaned_ucd_census.csv', index=False)
cleaned_df
